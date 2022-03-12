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
    "FIND" : "such",
    "SHOW_LIST" : "liste",
    "COPY" : "lade",
    "CUT" : "schneide",
    "PASTE" : "falle",
    "END" : "ende",
    "START" : "start",
}
ctx.lists["self.terms"] = terms_dict

@ctx.capture("user.select",rule=terms_dict["SELECT"])
def select(m) -> str:
    """Term for select"""
    return str(m)


@ctx.capture("user.teleport",rule=terms_dict["TELEPORT"])
def teleport(m) -> str:
    """Verb to use for commands that teleport the cursor to another place"""
    return str(m)


@ctx.capture("user.operator",rule=terms_dict["OPERATOR"])
def operator(m) -> str:
    """Prefix for operators"""
    return str(m)


@ctx.capture("user.delete",rule=terms_dict["DELETE"])
def delete(m) -> str:
    """Verb to use for commands that delete things"""
    return str(m)


@ctx.capture("user.find",rule=terms_dict["FIND"])
def find(m) -> str:
    """Verb to use for commands that find things"""
    return str(m)


@ctx.capture("user.show_list",rule=terms_dict["SHOW_LIST"])
def show_list(m) -> str:
    """Verb to use for commands that show lists"""
    return str(m)

@ctx.capture("user.copy",rule=terms_dict["COPY"])
def copy(m) -> str:
    """Verb to use for copy commands"""
    return str(m)

@ctx.capture("user.cut",rule=terms_dict["CUT"])
def cut(m) -> str:
    """Verb to use for cut commands"""
    return str(m)

@ctx.capture("user.paste",rule=terms_dict["PASTE"])
def paste(m) -> str:
    """Verb to use for pasting"""
    return str(m)

@ctx.capture("user.end",rule=terms_dict["END"])
def end(m) -> str:
    """Word to use for position end"""
    return str(m)

@ctx.capture("user.start",rule=terms_dict["START"])
def start(m) -> str:
    """Word to use for position start"""
    return str(m)