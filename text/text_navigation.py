import re
from talon import Module, Context, actions
import itertools

ctx = Context()
ctx = Context()
ctx.matches = r"""
language: de_DE
"""
mod = Module()


text_navigation_max_line_search = mod.setting(
    "text_navigation_max_line_search",
    type=int,
    default=10,
    desc="the maximum number of rows that will be included in the search for the keywords above and below in <user direction>",
)

ctx.lists["self.navigation_action"] = {
    "bewegen": "GO",
    "erweitern": "EXTEND",
    "nimm": "SELECT",
    "(wisch|müll|löschen)": "DELETE",
    "schneide": "CUT",
    "(merke|lade)": "COPY",
}
ctx.lists["self.before_or_after"] = {
    "bevor": "BEFORE",
    "nach": "AFTER",
    # DEFAULT is also a valid option as input for this capture, but is not directly accessible for the user.
}
navigation_target_names = {
    "ding": r"\w+",
    "halb": r"[A-Z]?[a-z0-9]+",
    "voll": r"[\S]+",
    "klammern": r'\((.*?)\)',
    "block": r'\[(.*?)\]',
    "schweif": r'\{(.*?)\}',
    "text": r'\"(.*?)\"',
    "winkel": r'\<(.*?)\>',
    "einfach text": r'\'(.*?)\'',
    "alle": r'(.+)',
    "funktion": r'\w+\((.*?)\)',
    "konstante": r'[A-Z_][A-Z_]+',
    "eindeutig": r'\b[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-\b[0-9a-fA-F]{12}\b'
}
ctx.lists["self.navigation_target_name"] = navigation_target_names

@ctx.capture("user.navigation_target",rule="<user.any_alphanumeric_key> | {user.navigation_target_name} | <user.term_sentence> <user.text>")
def navigation_target(m) -> re.Pattern:
    """A target to navigate to. Returns a regular expression."""
    if hasattr(m, 'any_alphanumeric_key'):
        return re.compile(re.escape(m.any_alphanumeric_key), re.IGNORECASE)
    if hasattr(m, 'navigation_target_name'):
        return re.compile(m.navigation_target_name)
    return re.compile(re.escape(m.text), re.IGNORECASE)
