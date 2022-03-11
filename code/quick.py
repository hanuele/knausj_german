import re
from talon import Context, Module, actions
from typing import Any
import logging

mod = Module()
ctx = Context()

# This could be None or a tuple.
# None: unassigned.
# tuple: (actions, *args). Action is the path to an action.
quick_macro = None
quick_chained_macro = None
@mod.action_class
class Actions:
    def quick_macro_clear():
        """Clears the quick macro"""
        global quick_macro
        global quick_chained_macro
        # logging.info("== Quick macro cleared ==")
        quick_macro = None
        quick_chained_macro = None

    def quick_macro_set(action: str, arg: Any = None):
        """Sets the quick macro"""
        global quick_macro
        global quick_chained_macro
        quick_chained_macro = None
        quick_macro = (action, arg) if arg is not None else (action,)


    def quick_macro_set_chained(chainedaction: str):
        """Sets the chained quick macro"""
        global quick_macro
        global quick_chained_macro
        quick_macro = None
        quick_chained_macro = (chainedaction)
        newline = '\n> '

    def quick_macro_run():
        """Runs the quick macro"""
        if quick_macro is not None:
            if isinstance(quick_macro, tuple):
                action, *args = quick_macro
                func = actions
                for pathelt in action.split('.'):
                    func = getattr(func, pathelt)
                func(*args)
            else:
                logging.info(f"== Undefined action in quickmacro ==")
        elif quick_chained_macro is not None:
            if isinstance(quick_chained_macro, str):
                for action in quick_chained_macro.split('#'):
                    result = re.search(r'^key\((.+)\)$', action)
                    if result:
                        shortcut = result.group(1)
                        if len(shortcut) > 0:
                            actions.key(shortcut)
                    else:
                        func = actions
                        for pathelt in action.split('.'):
                            func = getattr(func, pathelt)
                        func()
            else:
                logging.info(f"== Unknown chained macro: {quick_chained_macro} ==")
        else:
            return