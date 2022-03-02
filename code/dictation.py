# Descended from https://github.com/dwiel/talon_community/blob/master/misc/dictation.py
#German: As we have to change some methods originating from knausj, a bunch of auxiliry methods are copy pasted yet.


from talon import Module, Context, ui, actions, clip, app, grammar
from typing import Optional, Tuple, Literal, Callable
import re
import os

from user.knausj_talon.code.dictation import DictationFormat

# dictionary for capitalization

path = os.path.dirname(os.path.abspath(__file__))
with open(path + "/Resources/dictionary/german.dic", encoding='ISO-8859-1') as f:
	list_of_words = f.read().split("\n")

dict_of_words = {}
for word in list_of_words:
	if word.lower() in dict_of_words:
		# multiple entries, use lower
		dict_of_words[word.lower()] = word.lower()
	else:
		dict_of_words[word.lower()] = word

mod = Module()
ctx = Context()
ctx.matches = r"""
language: de_DE
"""
setting_context_sensitive_dictation = mod.setting(
    "context_sensitive_dictation",
    type=bool,
    default=True,
    desc="Look at surrounding text to improve auto-capitalization/spacing in dictation mode. By default, this works by selecting that text & copying it to the clipboard, so it may be slow or fail in some applications.",
)

mod.list("prose_modifiers", desc="Modifiers that can be used within prose")
mod.list("prose_snippets", desc="Snippets that can be used within prose")

# Maps spoken forms to DictationFormat method names (see DictationFormat below).
ctx.lists["user.prose_modifiers"] = {
    "großschreibung": "cap",
    "kleinschreibung": "no_cap",
    "kleinschreibung dragon": "no_cap", # "no caps" variant for Dragon
    "ohne leerzeichen": "no_space",
}
ctx.lists["user.prose_snippets"] = {
    "leerzeichen": " ",
    "einzug": "\n",
    "neuer paragraph": "\n\n",
    # Curly quotes are used to obtain proper spacing for left and right quotes, but will later be straightened.
    "zitat": "“",
    "zitat ende": "”",
    "smiley": ":-)",
    "winky": ";-)",
    "frowny": ":-(",
}

@ctx.capture("user.prose_modifier", rule="{user.prose_modifiers}")
def prose_modifier(m) -> Callable:
    return getattr(DictationFormat, m.prose_modifiers)


@ctx.capture("user.prose_simple_number", rule="numeral <user.number_string>")
def prose_simple_number(m) -> str:
    return m.number_string


@ctx.capture("user.prose_number_with_dot", rule="numeral <user.number_string> punkt <digit_string>")
def prose_number_with_dot(m) -> str:
    return m.number_string + "." + m.digit_string


@ctx.capture("user.prose_number_with_colon",rule="numeral <user.number_string> (komma|beistrich) <user.number_string>")
def prose_number_with_colon(m) -> str:
    return m.number_string_1 + ":" + m.number_string_2

@ctx.capture("user.prose_number", rule="<user.prose_simple_number> | <user.prose_number_with_dot> | <user.prose_number_with_colon>")
def prose_number(m) -> str:
    return str(m)

@ctx.capture("user.word", rule="({user.vocabulary} | <word>)")
def word(m) -> str:
    try:
        return m.vocabulary
    except AttributeError:
        #German: The word replacement for german is different to the origin knausj code as we use a dictionary to identify upper case words.
        temp_word = str(m)
        key = temp_word.replace(" ", "").lower()
        if key in dict_of_words:
            return " "+dict_of_words[key]
        else:
            return " ".join(actions.dictate.replace_words(actions.dictate.parse_words(m.word)))

@ctx.capture("user.text",rule="({user.vocabulary} | <phrase>)+")
def text(m) -> str:
    return format_phrase(m)

@ctx.capture("user.prose", rule="({user.vocabulary} | {user.punctuation} | {user.prose_snippets} | <phrase> | <user.prose_number> | <user.prose_modifier>)+")
def prose(m) -> str:
    # Straighten curly quotes that were introduced to obtain proper spacing.
    return apply_formatting(m).replace("“", "\"").replace("”", "\"")

@ctx.capture("user.raw_prose", rule="({user.vocabulary} | {user.punctuation} | {user.prose_snippets} | <phrase> | <user.prose_number>)+")
def raw_prose(m) -> str:
    return apply_formatting(m)


# ---------- FORMATTING ---------- #
def format_phrase(m):
    words = capture_to_words(m)
    result = ""
    for i, word in enumerate(words):
        if i > 0 and needs_space_between(words[i-1], word):
            result += " "
        result += word
    return result

def capture_to_words(m):
    words = []
    for item in m:
        words.extend(
            actions.dictate.replace_words(actions.dictate.parse_words(item))
            if isinstance(item, grammar.vm.Phrase)
            else [item])
    return words

def format_phrase(m):
    words = capture_to_words(m)
    result = ""
    for i, word in enumerate(words):
        if i > 0 and needs_space_between(words[i-1], word):
            result += " "
        #German: The word replacement for german is different to the origin knausj code as we use a dictionary to identify upper case words.
        temp_word = str(word)
        key = temp_word.replace(" ", "").lower()
        if key in dict_of_words:
            result += dict_of_words[key]
        else:
            result += word
    return result

def apply_formatting(m):
    formatter = DictationFormat()
    formatter.state = None
    result = ""
    for item in m:
        # prose modifiers (cap/no cap/no space) produce formatter callbacks.
        if isinstance(item, Callable):
            item(formatter)
        else:
            words = (actions.dictate.replace_words(actions.dictate.parse_words(item))
                     if isinstance(item, grammar.vm.Phrase)
                     else [item])
            for word in words:
                 #German: The word replacement for german is different to the origin knausj code as we use a dictionary to identify upper case words.
                temp_word = str(word)
                key = temp_word.replace(" ", "").lower()
                if key in dict_of_words:
                    temp_word = dict_of_words[key]
                result += formatter.format(temp_word)
    return result

# There must be a simpler way to do this, but I don't see it right now.
no_space_after = re.compile(r"""
  (?:
    [\s\-_/#@([{‘“]     # characters that never need space after them
  | (?<!\w)[$£€¥₩₽₹]    # currency symbols not preceded by a word character
  # quotes preceded by beginning of string, space, opening braces, dash, or other quotes
  | (?: ^ | [\s([{\-'"] ) ['"]
  )$""", re.VERBOSE)
no_space_before = re.compile(r"""
  ^(?:
    [\s\-_.,!?/%)\]}’”]   # characters that never need space before them
  | [$£€¥₩₽₹](?!\w)        # currency symbols not followed by a word character
  | [;:](?!-\)|-\()        # colon or semicolon except for smiley faces
  # quotes followed by end of string, space, closing braces, dash, other quotes, or some punctuation.
  | ['"] (?: $ | [\s)\]}\-'".,!?;:/] )
  # apostrophe s
  | 's(?!\w)
  )""", re.VERBOSE)

def omit_space_before(text: str) -> bool:
    return not text or no_space_before.search(text)
def omit_space_after(text: str) -> bool:
    return not text or no_space_after.search(text)
def needs_space_between(before: str, after: str) -> bool:
    return not (omit_space_after(before) or omit_space_before(after))


def auto_capitalize(text, state = None):
    """
    Auto-capitalizes text. `state` argument means:

    - None: Don't capitalize initial word.
    - "sentence start": Capitalize initial word.
    - "after newline": Don't capitalize initial word, but we're after a newline.
      Used for double-newline detection.

    Returns (capitalized text, updated state).
    """
    output = ""
    # Imagine a metaphorical "capitalization charge" travelling through the
    # string left-to-right.
    charge = state == "sentence start"
    newline = state == "after newline"
    for c in text:
        # Sentence endings & double newlines create a charge.
        if c in ".!?" or (newline and c == "\n"):
            charge = True
        # Alphanumeric characters and commas/colons absorb charge & try to
        # capitalize (for numbers & punctuation this does nothing, which is what
        # we want).
        elif charge and (c.isalnum() or c in ",:"):
            charge = False
            c = c.capitalize()
        # Otherwise the charge just passes through.
        output += c
        newline = c == "\n"
    return output, ("sentence start" if charge else
                    "after newline" if newline else None)


def format_first_letter(text, formatter):
    i = -1
    for i, c in enumerate(text):
        if c.isalpha():
            break
    if i >= 0 and i < len(text):
        text = text[:i] + formatter(text[i]) + text[i+1:]
    return text

dictation_formatter = DictationFormat()
ui.register("app_deactivate", lambda app: dictation_formatter.reset())
ui.register("win_focus", lambda win: dictation_formatter.reset())

def reformat_last_utterance(formatter):
    text = actions.user.get_last_phrase()
    actions.user.clear_last_phrase()
    text = formatter(text)
    actions.user.add_phrase_to_history(text)
    actions.insert(text)