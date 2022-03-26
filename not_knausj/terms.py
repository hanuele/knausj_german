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
    "FIND" : "(suche|suchen)",
    "SHOW_LIST" : "liste",
    "COPY" : "(merke|lade|merken|laden)",
    "CUT" : "(schneide|ausschneiden)",
    "PASTE" : "(einfügen|füge|ersetzen)",
    "END" : "ende",
    "START" : "start",
    "NAVIGATE" : "(flieg|spähe)",
    "WORD_NAVIGATE" : "(ding|wort)",
    "NAVIGATE_LEFT" : "(letztes|zurück)",
    "NAVIGATE_RIGHT" : "(nächstes|vor)",
    "SENTENCE" : "(satz|sag)",
    "DESKTOP" : "(tisch|[bild] schirm)",
    "GO" : "(gehe [zu]|[auf] zu|[auf] zum|[auf] zur)",
    "CLIPBOARD" : "klipp",
    "SAVE" : "(speichern|platte)",
    "LEFTMOST" : "(anfang|alfa)", 
}
ctx.lists["self.terms"] = terms_dict

@mod.capture
def term_select() -> str:
    """Term for select"""

@ctx.capture("user.term_select",rule=terms_dict["SELECT"])
def term_select(m) -> str:
    return str(m)

@mod.capture
def term_teleport() -> str:
    """Term for select"""

@ctx.capture("user.term_teleport",rule=terms_dict["TELEPORT"])
def term_teleport(m) -> str:
    """Verb to use for commands that teleport the cursor to another place"""
    return str(m)

@mod.capture
def term_operator() -> str:
    """Prefix for operators"""
@ctx.capture("user.term_operator",rule=terms_dict["OPERATOR"])
def term_operator(m) -> str:
    return str(m)

@mod.capture
def term_delete() -> str:
    """Verb to use for commands that delete things"""
@ctx.capture("user.term_delete",rule=terms_dict["DELETE"])
def term_delete(m) -> str:
    return str(m)

@mod.capture
def term_find() -> str:
    """Verb to use for commands that find things"""
@ctx.capture("user.term_find",rule=terms_dict["FIND"])
def term_find(m) -> str:
    return str(m)

@mod.capture
def term_show_list() -> str:
    """Verb to use for commands that show lists"""
@ctx.capture("user.term_show_list",rule=terms_dict["SHOW_LIST"])
def term_show_list(m) -> str:
    return str(m)

@mod.capture
def term_copy() -> str:
    """Verb to use for copy commands"""
@ctx.capture("user.term_copy",rule=terms_dict["COPY"])
def term_copy(m) -> str:
    return str(m)

@mod.capture
def term_cut() -> str:
    """Verb to use for cut commands"""
@ctx.capture("user.term_cut",rule=terms_dict["CUT"])
def term_cut(m) -> str:
    return str(m)

@mod.capture
def term_paste() -> str:
    """Verb to use for pasting"""
@ctx.capture("user.term_paste",rule=terms_dict["PASTE"])
def term_paste(m) -> str:
    return str(m)

@mod.capture
def term_end() -> str:
    """Word to use for position end"""
@ctx.capture("user.term_end",rule=terms_dict["END"])
def term_end(m) -> str:
    return str(m)

@mod.capture
def term_start() -> str:
    """Word to use for position start"""
@ctx.capture("user.term_start",rule=terms_dict["START"])
def term_start(m) -> str:
    return str(m)

@mod.capture
def term_navigate() -> str:
    """Verb to use for navigating"""
@ctx.capture("user.term_navigate",rule=terms_dict["NAVIGATE"])
def term_navigate(m) -> str:
    return str(m)

@mod.capture
def term_word_navigate() -> str:
    """Verb to use for word navigating"""
@ctx.capture("user.term_word_navigate",rule=terms_dict["WORD_NAVIGATE"])
def term_word_navigate(m) -> str:
    return str(m)

@mod.capture
def term_navigate_left() -> str:
    """Verb to use for navigating left"""
@ctx.capture("user.term_navigate_left",rule=terms_dict["NAVIGATE_LEFT"])
def term_navigate_left(m) -> str:
    """Verb to use for navigating left"""
    return str(m)

@mod.capture
def term_navigate_right() -> str:
    """Verb to use for navigating right"""
@ctx.capture("user.term_navigate_right",rule=terms_dict["NAVIGATE_RIGHT"])
def term_navigate_right(m) -> str:
    return str(m)

@mod.capture
def term_sentence() -> str:
    """Word to use to dictate sentence"""
@ctx.capture("user.term_sentence",rule=terms_dict["SENTENCE"])
def term_sentence(m) -> str:
    return str(m)

@mod.capture
def term_desktop() -> str:
    """Word to use to for desktop"""
@ctx.capture("user.term_desktop",rule=terms_dict["DESKTOP"])
def term_desktop(m) -> str:
    return str(m)

@mod.capture
def term_go() -> str:
    """Verb to use for go to"""
@ctx.capture("user.term_go",rule=terms_dict["GO"])
def term_go(m) -> str:
    return str(m)


@mod.capture
def term_clipboard() -> str:
    """Word to use to for clipboard"""   
@ctx.capture("user.term_clipboard",rule=terms_dict["CLIPBOARD"])
def term_clipboard(m) -> str: 
    return str(m)

@mod.capture
def term_save() -> str:
    """Verb to use for saving"""
@ctx.capture("user.term_save",rule=terms_dict["SAVE"])
def term_save(m) -> str:
    return str(m)

@mod.capture
def term_leftmost() -> str:
    """Word to use for leftmost position"""
@ctx.capture("user.term_leftmost",rule=terms_dict["LEFTMOST"])
def term_leftmost(m) -> str:
    return str(m)