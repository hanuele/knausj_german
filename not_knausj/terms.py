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
    "DELETE" : "(wisch|müll|löschen)",
    "FIND" : "suche",
    "SHOW_LIST" : "liste",
    "COPY" : "(merke|lade)",
    "CUT" : "schneide",
    "PASTE" : "(einfügen|füge)",
    "END" : "ende",
    "START" : "start",
    "NAVIGATE" : "lotse",
    "WORD_NAVIGATE" : "ding",
    "NAVIGATE_LEFT" : "zurück",
    "NAVIGATE_RIGHT" : "vor",
    "SENTENCE" : "satz",
    "DESKTOP" : "(tisch|[bild] schirm)",
}
ctx.lists["self.terms"] = terms_dict


@mod.capture(rule=terms_dict["SELECT"])
def term_select(m) -> str:
    """Term for select"""
    return str(m)

@mod.capture(rule=terms_dict["TELEPORT"])
def term_teleport(m) -> str:
    """Verb to use for commands that teleport the cursor to another place"""
    return str(m)

@mod.capture(rule=terms_dict["OPERATOR"])
def term_operator(m) -> str:
    """Prefix for operators"""
    return str(m)

@mod.capture(rule=terms_dict["DELETE"])
def term_delete(m) -> str:
    """Verb to use for commands that delete things"""
    return str(m)

@mod.capture(rule=terms_dict["FIND"])
def term_find(m) -> str:
    """Verb to use for commands that find things"""
    return str(m)

@mod.capture(rule=terms_dict["SHOW_LIST"])
def term_show_list(m) -> str:
    """Verb to use for commands that show lists"""
    return str(m)

@mod.capture(rule=terms_dict["COPY"])
def term_copy(m) -> str:
    """Verb to use for copy commands"""
    return str(m)

@mod.capture(rule=terms_dict["CUT"])
def term_cut(m) -> str:
    """Verb to use for cut commands"""
    return str(m)

@mod.capture(rule=terms_dict["PASTE"])
def term_paste(m) -> str:
    """Verb to use for pasting"""
    return str(m)

@mod.capture(rule=terms_dict["END"])
def term_end(m) -> str:
    """Word to use for position end"""
    return str(m)

@mod.capture(rule=terms_dict["START"])
def term_start(m) -> str:
    """Word to use for position start"""
    return str(m)

@mod.capture(rule=terms_dict["NAVIGATE"])
def term_navigate(m) -> str:
    """Verb to use for navigation"""
    return str(m)

@mod.capture(rule=terms_dict["WORD_NAVIGATE"])
def term_word_navigate(m) -> str:
    """Verb to use for word navigating"""
    return str(m)

@mod.capture(rule=terms_dict["NAVIGATE_LEFT"])
def term_navigate_left(m) -> str:
    """Verb to use for navigating left"""
    return str(m)

@mod.capture(rule=terms_dict["NAVIGATE_RIGHT"])
def term_navigate_right(m) -> str:
    """Verb to use for navigating right"""
    return str(m)

@mod.capture(rule=terms_dict["SENTENCE"])
def term_sentence(m) -> str:
    """Word to use to dictate sentence"""
    return str(m)

@mod.capture(rule=terms_dict["DESKTOP"])
def term_desktop(m) -> str:
    """Word for term desktop"""
    return str(m)