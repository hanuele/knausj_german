from talon import Context, Module, actions
from typing import List, Optional, Union, Iterator

mod = Module()
ctx = Context()
ctx.matches = r"""
language: de_DE
"""

#German: Getting numbers right in german is not easy and I did not a way to do the same as in english.
# As professionals in offices spell e.g. phone number by only using single or double digit numbers, I do the same for now.
# If there is an idea, I am glad to hear from it.
digits = "null eins zwei drei vier fünf sechs sieben acht neun".split()
#"zehn" does not work the same (e.g. in function "scan_small_numbers") as "ten" so I do not declare it in "teens" but in "tens". 
teens = "elf zwölf dreizehn vierzehn fünfzehn sechzehn siebzehn achtzehn neunzehn".split()
tens = "zehn zwanzig dreissig vierzig fünfzig sechzig siebzig achtzig neunzig".split()
scales = "hundert tausend".split()
#German: currently scales don't work because of the counting system in german. 
# You can however adapt the way you count ;-)
scales_einzahl = "hundert tausend"
digits_map = {n: i for i, n in enumerate(digits)}
digits_map["nullen"] = 0
teens_map = {n: i + 11 for i, n in enumerate(teens)}
tens_map = {n: 10 * (i + 1) for i, n in enumerate(tens)}
scales_map = {n: 10 ** (3 * (i+1)) for i, n in enumerate(scales[1:])}
scales_map["hundert"] = 100

numbers_map = digits_map.copy()
numbers_map.update(teens_map)
numbers_map.update(tens_map)
numbers_map.update(scales_map)

def parse_number(l: List[str]) -> str:
    """Parses a list of words into a number/digit string."""
    l = list(scan_small_numbers(l))
    for scale in scales:
        l = parse_scale(scale, l)
    return "".join(str(n) for n in l)

def scan_small_numbers(l: List[str]) -> Iterator[Union[str,int]]:
    """
    Takes a list of number words, yields a generator of mixed numbers & strings.
    Translates small number terms (<100) into corresponding numbers.
    Drops all occurrences of "und".
    Smashes digits onto tens words, eg. ["eins", "zwanzig"] -> [21].
    But note that "null" is excluded, ie:
      ["fünfzig", "null"] -> [50, 0]
    Does nothing to scale words ("hundert", "tausend", "millionen", etc).
    """
    # reversed so that repeated pop() visits in left-to-right order
    l = [x for x in reversed(l) if x != "und"]
    while l:
        n = l.pop()
        # fuse tens onto digits, eg. "ein", "zwanzig" -> 21
        if n in tens_map and l and digits_map.get(l[-1], 0) != 0:
            d = l.pop()
            yield numbers_map[n] + numbers_map[d]
        # turn small number terms into corresponding numbers
        elif n not in scales_map:
            yield numbers_map[n]
        else:
            yield n

def parse_scale(scale: str, l: List[Union[str,int]]) -> List[Union[str,int]]:
    """Parses a list of mixed numbers & strings for occurrences of the following
    pattern:

        <multiplier> <scale> <remainder>

    where <scale> is a scale word like "hundert", "tausend", "millionen" "million", etc and
    multiplier and remainder are numbers or strings of numbers of the
    appropriate size. For example:

        parse_scale("hundred", [1, "hundert", 2]) -> [102]
        parse_scale("thousand", [12, "tausend", 3, 45]) -> [12345]

    We assume that all scales of lower magnitude have already been parsed; don't
    call parse_scale("tausend") until you've called parse_scale("hundert").
    """
    scale_value = scales_map[scale]
    scale_digits = len(str(scale_value))

    # Split the list on the desired scale word, then parse from left to right.
    left, *splits = split_list(scale, l)
    for right in splits:
        # (1) Figure out the multiplier by looking to the left of the scale
        # word. We ignore non-integers because they are scale words that we
        # haven't processed yet; this strategy means that "tausend hundert"
        # gets parsed as 1,100 instead of 100,000, but "hundert tausend" is
        # parsed correctly as 100,000.
        before = 1 # default multiplier
        if left and isinstance(left[-1], int) and left[-1] != 0:
            before = left.pop()

        # (2) Absorb numbers to the right, eg. in [1, "tausend", 1, 26], "1
        # tausend" absorbs ["1", "26"] to make 1,126. We pull numbers off
        # `right` until we fill up the desired number of digits.
        after = ""
        while right and isinstance(right[0], int):
            next = after + str(right[0])
            if len(next) >= scale_digits: break
            after = next
            right.pop(0)
        after = int(after) if after else 0

        # (3) Push the parsed number into place, append whatever was left
        # unparsed, and continue.
        left.append(before * scale_value + after)
        left.extend(right)

    return left

def split_list(value, l: list) -> Iterator:
    """Splits a list by occurrences of a given value."""
    start = 0
    while True:
        try: i = l.index(value, start)
        except ValueError: break
        yield l[start:i]
        start = i+1
    yield l[start:]


# ---------- CAPTURES ----------
alt_digits = "(" + ("|".join(digits_map.keys())) + ")"
alt_teens = "(" + ("|".join(teens_map.keys())) + ")"
alt_tens = "(" + ("|".join(tens_map.keys())) + ")"
alt_scales = "(" + ("|".join(scales_map.keys())) + ")"
number_word = "(" + "|".join(numbers_map.keys()) + ")"
# don't allow numbers to start with scale words like "hundred", "thousand", etc
leading_words = numbers_map.keys() - scales_map.keys()
leading_words -= {'oh', 'o'} # comment out to enable bare/initial "oh"
number_word_leading = f"({'|'.join(leading_words)})"

# TODO: allow things like "double eight" for 88
@ctx.capture("digit_string", rule=f"({alt_digits} | {alt_teens} | {alt_tens})+")
def digit_string(m) -> str: return parse_number(list(m))


@ctx.capture("digits", rule="<digit_string>")
def digits(m) -> int:
    """Parses a phrase representing a digit sequence, returning it as an integer."""
    return int(m.digit_string)


@ctx.capture("user.number_string", rule=f"{number_word_leading} ([und] {number_word})*")
def number_string(m) -> str:
    """Parses a number phrase, returning that number as a string."""
    return parse_number(list(m))


@ctx.capture("number", rule="<user.number_string>")
def number(m) -> int:
    """Parses a number phrase, returning it as an integer."""
    return int(m.number_string)


@ctx.capture("number_signed", rule=f"[negativ|minus] <number>")
def number_signed(m):
    """Parses a number phrase, returning it as an integer."""
    number = m[-1]
    return -number if (m[0] in ["negativ", "minus"]) else number


@ctx.capture(
    "number_small", rule=f"({alt_digits} | {alt_teens} | {alt_tens} [{alt_digits}])"
)
def number_small(m): 
    """Parses a number phrase, returning it as a small number."""
    return int(parse_number(list(m)))
