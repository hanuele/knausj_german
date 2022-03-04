from talon import Context, Module, actions, app, ui

mod = Module()
ctx = Context()
ctx.matches = r"""
language: de_DE
"""


# The primitive ordinal words in German below a hundred.
ordinal_words = {
    0: "nullte",
    1: "erste",
    2: "zweite",
    3: "dritte",
    4: "vierte",
    5: "fünfte",
    6: "sechste",
    7: "siebte",
    8: "achte",
    9: "neunte",
    10: "zehnte",
    11: "elfte",
    12: "zwölfte",
    13: "dreizehnte",
    14: "vierzehnte",
    15: "fünfzehnte",
    16: "sechzehnte",
    17: "siebzehnte",
    18: "achtzehnte",
    19: "neunzehnte",
    20: "zwanzigste",
    30: "dreißigste",
    40: "vierzigste",
    50: "fünfzigste",
    60: "sechzigste",
    70: "siebzigste",
    80: "achtzigste",
    90: "neunzigste",
}
# The primitive ordinal words in German for below 1.
ordinal_words_prefix = {
    1: "ein",
    2: "zwei",
    3: "drei",
    4: "vier",
    5: "fünf",
    6: "sechs",
    7: "sieben",
    8: "acht",
    9: "neun",
}
tens_words = "null zehn zwanzig dreißig vierzig fünfzig sechzig siebzig achtzig neunzig".split()

# ordinal_numbers maps ordinal words into their corresponding numbers.
ordinal_numbers = {}
ordinal_small = {}
for n in range(1, 100):
    if n in ordinal_words:
        word = ordinal_words[n]
    else:
        (tens, units) = divmod(n, 10)
        assert 1 < tens < 10, "we have already handled all ordinals < 20"
        assert 0 < units, "we have already handled all ordinals divisible by ten"
        word = f"{ordinal_words_prefix[units]}und{tens_words[tens]} "

    if n <= 20:
        ordinal_small[word] = n
    ordinal_numbers[word] = n

ctx.lists["self.ordinals"] = ordinal_numbers.keys()
ctx.lists["self.ordinals_small"] = ordinal_small.keys()

    
@ctx.capture("user.ordinals", rule="{self.ordinals}")
def ordinals(m) -> int:
    """Returns a single ordinal as a digit"""
    return int(ordinal_numbers[m[0]])

@ctx.capture("user.ordinals_small", rule="{self.ordinals_small}")
def ordinals_small(m) -> int:
    """Returns a single ordinal as a digit"""
    return int(ordinal_numbers[m[0]])
