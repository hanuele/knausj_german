from talon import Context, Module
from glob import glob



#from user.knausj_talon.code.switcher import RelativeScreenPos

mod = Module()
ctx = Context()
ctx.matches = r"""
language: de_DE
"""


@ctx.capture("user.running_applications", rule="{self.running}")  # | <user.text>)")
def running_applications(m) -> str:
    "Returns a single application name"
    try:
        return m.running
    except AttributeError:
        return m.text

@ctx.capture("user.visible_windows", rule="{self.visible}")  # | <user.text>)")
def visible_windows(m) -> str:
    "Returns a single window name"
    try:
        return m.visible
    except AttributeError:
        return m.text


@ctx.capture("user.launch_applications", rule="{self.launch}")
def launch_applications(m) -> str:
    "Returns a single application name"
    return m.launch

