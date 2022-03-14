language: de_DE
mode: command
mode: mixed
-

^<user.term_select> <user.term_desktop>$:                       user.screenshot()
^<user.term_select> <user.term_desktop> <number_small>$:        user.screenshot(number_small)
^<user.term_select> fenster$:                       user.screenshot_window()
^<user.term_select> (auswahl|selektion)$:                    user.screenshot_selection()
^<user.term_select> einstellungen$:                     user.screenshot_settings()
^<user.term_select> <user.term_desktop> klip$:                  user.screenshot_clipboard()
^<user.term_select> <user.term_desktop> <number_small> klip$:   user.screenshot_clipboard(number_small)
^<user.term_select> fenster klip$:                  user.screenshot_window_clipboard()