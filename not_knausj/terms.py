"""
Stores terms that are used in many different places
"""
from talon import Module, Context

mod = Module()
ctx = Context()
ctx.matches = r"""
language: de_DE
"""

mod.list("terms", desc="Terms that can be easily replaced.")
terms_dict = {
    "SELECT" : "nimm",
    "TELEPORT" : "pop",
    "OPERATOR" : "mach",
    "DELETE" : "kratz",
    "FIND" : "suche",
    "SHOW_LIST" : "liste",
    "COPY" : "lade",
    "CUT" : "schneide",
    "PASTE" : "falle",
    "END" : "ende",
    "START" : "start",
    "NAVIGATE" : "lotse",
    "WORD_NAVIGATE" : "ding",
    "NAVIGATE_LEFT" : "zurück",
    "NAVIGATE_RIGHT" : "vor",
    "SENTENCE" : "satz",
}
ctx.lists["self.terms"] = terms_dict

@ctx.capture("user.term_select",rule=terms_dict["SELECT"])
def term_select(m) -> str:
    """Term for select"""
    return str(m)


@ctx.capture("user.term_teleport",rule=terms_dict["TELEPORT"])
def term_teleport(m) -> str:
    """Verb to use for commands that teleport the cursor to another place"""
    return str(m)


@ctx.capture("user.term_operator",rule=terms_dict["OPERATOR"])
def term_operator(m) -> str:
    """Prefix for operators"""
    return str(m)


@ctx.capture("user.term_delete",rule=terms_dict["DELETE"])
def term_delete(m) -> str:
    """Verb to use for commands that delete things"""
    return str(m)


@ctx.capture("user.term_find",rule=terms_dict["FIND"])
def term_find(m) -> str:
    """Verb to use for commands that find things"""
    return str(m)


@ctx.capture("user.term_show_list",rule=terms_dict["SHOW_LIST"])
def term_show_list(m) -> str:
    """Verb to use for commands that show lists"""
    return str(m)

@ctx.capture("user.term_copy",rule=terms_dict["COPY"])
def term_copy(m) -> str:
    """Verb to use for copy commands"""
    return str(m)

@ctx.capture("user.term_cut",rule=terms_dict["CUT"])
def term_cut(m) -> str:
    """Verb to use for cut commands"""
    return str(m)

@ctx.capture("user.term_paste",rule=terms_dict["PASTE"])
def term_paste(m) -> str:
    """Verb to use for pasting"""
    return str(m)

@ctx.capture("user.term_end",rule=terms_dict["END"])
def term_end(m) -> str:
    """Word to use for position end"""
    return str(m)

@ctx.capture("user.term_start",rule=terms_dict["START"])
def term_start(m) -> str:
    """Word to use for position start"""
    return str(m)

@ctx.capture("user.term_navigate",rule=terms_dict["NAVIGATE"])
def term_navigate(m) -> str:
    """Verb to use for navigating"""
    return str(m)

@ctx.capture("user.term_word_navigate",rule=terms_dict["WORD_NAVIGATE"])
def term_word_navigate(m) -> str:
    """Verb to use for word navigating"""
    return str(m)

@ctx.capture("user.term_navigate_left",rule=terms_dict["NAVIGATE_LEFT"])
def term_navigate_left(m) -> str:
    """Verb to use for navigating left"""
    return str(m)

@ctx.capture("user.term_navigate_right",rule=terms_dict["NAVIGATE_RIGHT"])
def term_navigate_right(m) -> str:
    """Verb to use for navigating right"""
    return str(m)

@ctx.capture("user.term_sentence",rule=terms_dict["SENTENCE"])
def term_sentence(m) -> str:
    """Word to use to dictate sentence"""
    return str(m)