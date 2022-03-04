from typing import Set
from talon import Module, Context, actions, app
import sys

mod = Module()
ctx = Context()
ctx.matches = r"""
language: de_DE
"""

#German: Just trying to find my way here ;-)
default_alphabet = "alf ära bett cello din edi edach fell grunz horst ida jass kilo lidl mett nova oskar öko papa quer rom satt tes tango ulk büsi vik wolf kena yak zoll".split(
    " "
)
letters_string = "aäbcdeéfghijklmnoöpqrsß11tuüvwxyz"

default_digits = "null eins zwei drei vier fünf sechs sieben acht neun zehn elf zwölf".split(" ")
numbers = [str(i) for i in range(10)]
# I like to use up to f24
default_f_digits = "eins zwei drei vier fünf sechs sieben acht neun zehn elf zwölf dreizehn vierzehn fünfzehn sechzehn siebzehn achtzehn neunzehn zwanzig einundzwanzig zweiundzwanzig dreiundzwanzig vierundzwanzig".split(
    " "
)


modifier_keys = {
    # If you find 'alt' is often misrecognized, try using 'alter'.
    "alt": "alt",  #'alter': 'alt',
    "control": "ctrl",  #'troll':   'ctrl',
    "shift": "shift",  #'sky':     'shift',
    "super": "super",
}
if app.platform  == "mac":
    modifier_keys["command"] = "cmd"
    modifier_keys["option"] = "alt"
ctx.lists["self.modifier_key"] = modifier_keys

alphabet = dict(zip(default_alphabet, letters_string))
ctx.lists["self.letter"] = alphabet

# `punctuation_words` is for words you want available BOTH in dictation and as key names in command mode.
# `symbol_key_words` is for key names that should be available in command mode, but NOT during dictation.
punctuation_words = {
    # TODO: I'm not sure why we need these, I think it has something to do with
    # Dragon. Possibly it has been fixed by later improvements to talon? -rntz
    "`": 				"`",
    ",": 				",",  # <== these things
    "graf": 			"`",
    "leerzeichen":      " ",
	"komma":            ",",  # komma is often confused with komme
    "punkt":            ".",
    "doppelpunkt":      ":",
    "semikolon":        ";",
	"schrägstrich":     "/",
    "fragezeichen":     "?",
    "ausrufezeichen":   "!",
    "sternchen":		"*",
    "gartenhag": 		"#",
    "raute":	 		"#",
    "prozent":		 	"%",
 	"klammer affe":     "@",
    "schund":	   		"&",
    "schwebe strich":   "-",
    "gedanken strich":   "–",
    "lieg strich":      "_",
    "pflug":       		"\\",
    "zitat":            '„',
	"zitat ende":       '“',
	"halbes zitat":     '‚',
	"halbes zitat ende":'‘',
	"apostroph":        "’",
	"klammer auf":      "(",
	"klammer zu":       ")",
    # Currencies
    "dollar zeichen":	"$",
    "pfund zeichen": 	"£",
	"euro zeichen": 	"€",
}
symbol_key_words = {
    
    "einfaches anführungszeichen": "'",
    "minus": 				"-",
    "plus": 				"+",
    "prozent":		 		"%",
    "pipe": 				"|",
    "anführungszeichen":	'"',
	"leerzeichen":          " ", 
	"blank":                " ",
	"punkt":                ".",
	"beistrich":            ",",  # komma is often confused with komme
	"komma":                ",",  # komma is often confused with komme
	"fragezeichen":         "?",
	"ausrufezeichen":       "!",
	"doppelpunkt":          ":",
	"semikolon":            ";",
	"bindestrich": 			"-",
	"gedankenstrich": 		"–",
	"unterstrich": 			"_",
	"schrägstrich": 		"/",
	"backslash": 			"\\",
	"pipe": 				"|",
	"zitat": 				'„',
	"zitat ende": 			'“',
	"halbes zitat": 		'‚',
	"halbes zitat ende": 	'‘',
	"apostroph": 			"’",
	"klammer auf": 			"(",
	"klammer zu": 			")",
	"eckig auf": 			"[",
	"eckig zu": 			"]",
	"geschweift auf":		"{",
	"geschweift zu": 		"}",
	"klammeraffe": 			"@",
    "undzeichen":	   		"&",
	"sternchen": 			"*",
	"kleiner zeichen": 		"<",
	"größer zeichen": 		">",
	"gleich zeichen": 		"=",
	"raute": 				"#",
	"tilde": 				"~",
	"zirkumflex": 			"^",
    "hausdach": 			"^",

    # Currencies
    "dollar zeichen":		"$",
    "pfund zeichen": 		"£",
	"euro zeichen": 		"€",
}

# make punctuation words also included in {user.symbol_keys}
symbol_key_words.update(punctuation_words)
ctx.lists["self.punctuation"] = punctuation_words
ctx.lists["self.symbol_key"] = symbol_key_words
ctx.lists["self.number_key"] = dict(zip(default_digits, numbers))
ctx.lists["self.arrow_key"] = {
	"runter": "down",
    "links": "left",
    "rechts": "right",
    "hoch": "up",
}

simple_keys =  {
    "tabulator":	"tab",
    "menü":			"menu",
	"einzug":		"enter",
	"anfang":		"home",
	"ende":			"end",
	"einfügen":		"insert",
	"abbrechen": 	"escape",
    "caps lock":    "capslock",
    "num lock":     "numlock",
}

alternate_keys = {
    "löschen":			"backspace",
    "forwärts löschen": "delete",
    "Seite hoch":   	"pageup",
    "Seite runter": 	"pagedown",
}

# mac apparently doesn't have the menu key.
if app.platform in ("windows", "linux"):
    alternate_keys["menu key"] = "menu"
    alternate_keys["print screen"] = "printscr"

special_keys = simple_keys
special_keys.update(alternate_keys)
ctx.lists["self.special_key"] = special_keys
ctx.lists["self.function_key"] = {
    f"F {default_f_digits[i]}": f"f{i + 1}" for i in range(24)
}

@ctx.capture("user.modifiers", rule="{user.modifier_key}+")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m.modifier_key_list)

@ctx.capture("user.arrow_key", rule="{self.arrow_key}")
def arrow_key(m) -> str:
    "One directional arrow key"
    return m.arrow_key


@ctx.capture("user.arrow_keys", rule="<self.arrow_key>+")
def arrow_keys(m) -> str:
    "One or more arrow keys separated by a space"
    return str(m)


@ctx.capture("user.number_key",rule="{self.number_key}")
def number_key(m) -> str:
    "One number key"
    return m.number_key


@ctx.capture("user.letter",rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter

@ctx.capture("user.special_key",rule="{self.special_key}")
def special_key(m) -> str:
    "One special key"
    return m.special_key

@ctx.capture("user.symbol_key",rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key


@ctx.capture("user.function_key",rule="{self.function_key}")
def function_key(m) -> str:
    "One function key"
    return m.function_key


@ctx.capture("user.any_alphanumeric_key",rule="( <self.letter> | <self.number_key> | <self.symbol_key> )")
def any_alphanumeric_key(m) -> str:
    "any alphanumeric key"
    return str(m)


@ctx.capture("user.unmodified_key",
    rule="( <self.letter> | <self.number_key> | <self.symbol_key> "
    "| <self.arrow_key> | <self.function_key> | <self.special_key> )"
)
def unmodified_key(m) -> str:
    "A single key with no modifiers"
    return str(m)

@ctx.capture("user.key",rule="{self.modifier_key}* <self.unmodified_key>")
def key(m) -> str:
    "A single key with optional modifiers"
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return "-".join(mods + [m.unmodified_key])


@ctx.capture("user.keys",rule="<self.key>+")
def keys(m) -> str:
    "A sequence of one or more keys with optional modifiers"
    return " ".join(m.key_list)


@ctx.capture("user.letters",rule="{self.letter}+")
def letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.letter_list)