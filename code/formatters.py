from talon import Module, Context, actions, ui, imgui, app
from talon.grammar import Phrase
from typing import List, Union
import logging
import re

from user.knausj_talon.code.formatters import ImmuneString

mod = Module()
ctx = Context()
ctx.matches = r"""
language: de_DE
"""

key = actions.key
edit = actions.edit

#German: This needs to be verified as viable/necessary in the end
#https://www.scribbr.de/wissenschaftliches-schreiben/gross-und-kleinschreibung/
words_to_keep_lowercase = "ein eine der die das bei am um für in auf auf unter zu von und als aber oder".split()

# The last phrase spoken, without & with formatting. Used for reformatting.
last_phrase = ""
last_phrase_formatted = ""

# Internally, a formatter is a pair (sep, fn).
#
# - sep: a boolean, true iff the formatter should leave spaces between words.
#   We use SEP & NOSEP for this for clarity.
#
# - fn: a function (i, word, is_end) --> formatted_word, called on each `word`.
#   `i` is the word's index in the list, and `is_end` is True iff it's the
#   last word in the list.
SEP = True
NOSEP = False


def format_phrase(m: Union[str, Phrase], formatters: str):
    global last_phrase, last_phrase_formatted
    last_phrase = m
    words = []
    if isinstance(m, str):
        words = m.split(" ")
    else:
        # FIXME: I believe this is no longer necessary. -rntz, 2022-02-10
        if m.words[-1] == "über":
            m.words = m.words[:-1]
        words = actions.dictate.replace_words(actions.dictate.parse_words(m))

    result = last_phrase_formatted = format_phrase_without_adding_to_history(words, formatters)
    actions.user.add_phrase_to_history(result)
    # Arguably, we shouldn't be dealing with history here, but somewhere later
    # down the line. But we have a bunch of code that relies on doing it this
    # way and I don't feel like rewriting it just now. -rntz, 2020-11-04
    return result


def format_phrase_without_adding_to_history(word_list, formatters: str):
    # A formatter is a pair (keep_spaces, function). We drop spaces if any
    # formatter does; we apply their functions in reverse order.
    formatters = [all_formatters[name] for name in formatters.split(',')]
    separator = ' ' if all(x[0] for x in formatters) else ''
    functions = [x[1] for x in reversed(formatters)]
    words = []
    for i, word in enumerate(word_list):
        for f in functions:
            word = f(i, word, i == len(word_list) - 1)
        words.append(word)
    return separator.join(words)

# Formatter helpers
def surround(by):
    return lambda i, word, last: (by if i == 0 else '') + word + (by if last else '')


def words_with_joiner(joiner):
    """Pass through words unchanged, but add a separator between them."""
    return (NOSEP, lambda i, word, _: ('' if i == 0 else joiner) + word)


def first_vs_rest(first_func, rest_func=lambda w: w):
    """Supply one or two transformer functions for the first and rest of
    words respectively.

    Leave second argument out if you want all but the first word to be passed
    through unchanged.
    Set first argument to None if you want the first word to be passed
    through unchanged.
    """
    first_func = first_func or (lambda w: w)
    return lambda i, word, _: first_func(word) if i == 0 else rest_func(word)


def every_word(word_func):
    """Apply one function to every word."""
    return lambda i, word, _: word_func(word)



formatters_dict = {
    "NOOP": (SEP, lambda i, word, _: word),
    "DOUBLE_UNDERSCORE": (NOSEP, first_vs_rest(lambda w: "__%s__" % w)),
    "PRIVATE_CAMEL_CASE": (NOSEP, first_vs_rest(lambda w: w.lower(), lambda w: w.capitalize())),
    "PROTECTED_CAMEL_CASE": (NOSEP, first_vs_rest(lambda w: w.lower(), lambda w: w.capitalize())),
    "PUBLIC_CAMEL_CASE": (NOSEP, every_word(lambda w: w.capitalize())),
    "SNAKE_CASE": (
        NOSEP,
        first_vs_rest(lambda w: w.lower(), lambda w: "_" + w.lower()),
    ),
    "NO_SPACES": (NOSEP, every_word(lambda w: w)),
    "DASH_SEPARATED": words_with_joiner("-"),
    "TERMINAL_DASH_SEPARATED": (
        NOSEP,
        first_vs_rest(lambda w: " --" + w.lower(), lambda w: "-" + w.lower()),
    ),
    "DOUBLE_COLON_SEPARATED": words_with_joiner("::"),
    "ALL_CAPS": (SEP, every_word(lambda w: w.upper())),
    "ALL_LOWERCASE": (SEP, every_word(lambda w: w.lower())),
    "DOUBLE_QUOTED_STRING": (SEP, surround('"')),
    "SINGLE_QUOTED_STRING": (SEP, surround("'")),
    "SPACE_SURROUNDED_STRING": (SEP, surround(" ")),
    "DOT_SEPARATED": words_with_joiner("."),
    "DOT_SNAKE": (NOSEP, lambda i, word, _: "." + word if i == 0 else "_" + word),
    "SLASH_SEPARATED": (NOSEP, every_word(lambda w: "/" + w)),
    "CAPITALIZE_FIRST_WORD": (SEP, first_vs_rest(lambda w: w.capitalize())),
    "CAPITALIZE_ALL_WORDS": (
        SEP,
        lambda i, word, _: word.capitalize()
        if i == 0 or word not in words_to_keep_lowercase
        else word,
    ),
}
# German: This is just a first version to even have german terms
# This is the mapping from spoken phrases to formatters
formatters_words = {
    "allesgroß": formatters_dict["ALL_CAPS"],
    "allesklein": formatters_dict["ALL_LOWERCASE"],
    "kamel": formatters_dict["PRIVATE_CAMEL_CASE"],
    "gepunktet": formatters_dict["DOT_SEPARATED"],
    "text": formatters_dict["DOUBLE_QUOTED_STRING"],
    "doppelunterstrichen": formatters_dict["DOUBLE_UNDERSCORE"],
    "hammer": formatters_dict["PUBLIC_CAMEL_CASE"],
    "kebap": formatters_dict["DASH_SEPARATED"],
    "gepackt": formatters_dict["DOUBLE_COLON_SEPARATED"],
    "freiraum": formatters_dict["SPACE_SURROUNDED_STRING"],
    "kippen": formatters_dict["SLASH_SEPARATED"],
    "quetschen": formatters_dict["NO_SPACES"],
    "verbinden": formatters_dict["SNAKE_CASE"],
    "zeichen": formatters_dict["SINGLE_QUOTED_STRING"],
    "titel": formatters_dict["CAPITALIZE_ALL_WORDS"],
    "satz": formatters_dict["CAPITALIZE_FIRST_WORD"],
}

all_formatters = {}
all_formatters.update(formatters_dict)
all_formatters.update(formatters_words)


@ctx.capture("user.formatters",rule="{self.formatters}+")
def formatters(m) -> str:
    """Returns a comma-separated string of formatters e.g. 'SNAKE,DUBSTRING'"""
    return ",".join(m.formatters_list)


@ctx.capture(
    # Note that if the user speaks something like "snake dot", it will
    # insert "dot" - otherwise, they wouldn't be able to insert punctuation
    # words directly.
    "user.format_text", rule="<self.formatters> <user.text> (<user.text> | <user.formatter_immune>)*"
)
def format_text(m) -> str:
    """Formats the text and returns a string"""
    out = ""
    formatters = m[0]
    for chunk in m[1:]:
        if isinstance(chunk, ImmuneString):
            out += chunk.string
        else:
            out += format_phrase(chunk, formatters)
    return out


@ctx.capture(
    # Add anything else into this that you want to be able to speak during a
    # formatter.
    "user.formatter_immune", rule="(<user.symbol_key> | nummer <number>)"
)
def formatter_immune(m) -> ImmuneString:
    """Text that can be interspersed into a formatter, e.g. characters.
       It will be inserted directly, without being formatted.
    """
    if hasattr(m, "number"):
        value = m.number
    else:
        value = m[0]
    return ImmuneString(str(value))

ctx.lists["self.formatters"] = formatters_words.keys()

ctx.lists["self.prose_formatter"] = {
    "say": "NOOP",
    "speak": "NOOP",
    "sentence": "CAPITALIZE_FIRST_WORD",
}

