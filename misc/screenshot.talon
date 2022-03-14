language: de_DE
mode: command
mode: mixed
-

^<user.term_select> [bild] schirm$:                       user.screenshot()
^<user.term_select> [bild] schirm <number_small>$:        user.screenshot(number_small)
^<user.term_select> fenster$:                       user.screenshot_window()
^<user.term_select> (auswahl|selektion)$:                    user.screenshot_selection()
^<user.term_select> einstellungen$:                     user.screenshot_settings()
^<user.term_select> [bild] schirm klip$:                  user.screenshot_clipboard()
^<user.term_select> [bild] schirm <number_small> kclip$:   user.screenshot_clipboard(number_small)
^<user.term_select> fenster klip$:                  user.screenshot_window_clipboard()