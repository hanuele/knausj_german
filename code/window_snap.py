"""Tools for voice-driven window management.

Originally from dweil/talon_community - modified for newapi by jcaw.

"""

# TODO: Map keyboard shortcuts to this manager once Talon has key hooks on all
#   platforms

import time
from operator import xor
from typing import Optional

from talon import ui, Module, Context,ctrl, actions
from user.knausj_talon.code.window_snap import RelativeScreenPos

mod = Module()
ctx = Context()
ctx.matches = r"""
language: de_DE
"""

_snap_positions = {
    # Halves
    # .---.---.     .-------.
    # |   |   |  &  |-------|
    # '---'---'     '-------'
    "links": RelativeScreenPos(0, 0, 0.5, 1),
    "rechts": RelativeScreenPos(0.5, 0, 1, 1),
    "hoch": RelativeScreenPos(0, 0, 1, 0.5),
    "runter": RelativeScreenPos(0, 0.5, 1, 1),
    # Thirds
    # .--.--.--.
    # |  |  |  |
    # '--'--'--'
    "katze": RelativeScreenPos(1 / 3, 0, 2 / 3, 1),
    "maus": RelativeScreenPos(0, 0, 1 / 3, 1),
    "hund": RelativeScreenPos(2 / 3, 0, 1, 1),
    "fett": RelativeScreenPos(0, 0, 2 / 3, 1),
    "breit": RelativeScreenPos(1 / 3, 0, 1, 1,),
    "teams": RelativeScreenPos(0, 1 / 3, 1, 2 / 3),
    "kätzchen": RelativeScreenPos(0, 1 / 3, 1, 2 / 3),
    "mäuschen": RelativeScreenPos(0, 0, 1, 1 / 3),
    "mail": RelativeScreenPos(0, 2 / 3, 1, 1),
    "hundchen": RelativeScreenPos(0, 2 / 3, 1, 1),
    "dickerchen": RelativeScreenPos(0, 0, 1, 2 / 3),
    "breitchen": RelativeScreenPos(0, 1 / 3, 1, 1,),
    # Forths
    # .-.-.-.-'
    # | | | | |
    # '-'-'-'-'
    "list": RelativeScreenPos(1/4, 0, 1 / 2, 1),

    # Quarters
    # .---.---.
    # |---|---|
    # '---'---'
    "oben links": RelativeScreenPos(0, 0, 0.5, 0.5),
    "oben rechts": RelativeScreenPos(0.5, 0, 1, 0.5),
    "unten links": RelativeScreenPos(0, 0.5, 0.5, 1),
    "unten rechts": RelativeScreenPos(0.5, 0.5, 1, 1),
    # Sixths
    # .--.--.--.
    # |--|--|--|
    # '--'--'--'
    "log": RelativeScreenPos(1/2, 0, 1, 1 / 3),
    "explorer": RelativeScreenPos(0, 0, 1/2, 1 / 3),
    # Special
    "zentrum": RelativeScreenPos(1 / 8, 1 / 6, 7 / 8, 5 / 6),
    "voll": RelativeScreenPos(0, 0, 1, 1),
    "vollschirm": RelativeScreenPos(0, 0, 1, 1),
}


@ctx.capture("user.window_snap_position",rule="{user.window_snap_positions}")
def window_snap_position(m) -> RelativeScreenPos:
    return _snap_positions[m.window_snap_positions]


ctx.lists["user.window_snap_positions"] = _snap_positions.keys()
