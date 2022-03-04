not mode: sleep
language: de_DE
-

^diktier modus$:
    mode.disable("sleep")
    mode.disable("command")
    mode.disable("user.screenshare")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")

^Kommando modus$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.disable("user.screenshare")
    mode.enable("command")

^gemischter modus$:
    mode.disable("sleep")
    mode.disable("user.screenshare")
    mode.enable("dictation")
    mode.enable("command")

^bildschirm teilen modus$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.disable("command")
    mode.enable("user.screenshare")