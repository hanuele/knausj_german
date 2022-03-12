language: de_DE
mode: command
mode: mixed
-

^<user.select> [bild] schirm$:                       user.screenshot()
^<user.select> [bild] schirm <number_small>$:        user.screenshot(number_small)
^<user.select> fenster$:                       user.screenshot_window()
^<user.select> (auswahl|selektion)$:                    user.screenshot_selection()
^<user.select> einstellungen$:                     user.screenshot_settings()
^<user.select> [bild] schirm klip$:                  user.screenshot_clipboard()
^<user.select> [bild] schirm <number_small> kclip$:   user.screenshot_clipboard(number_small)
^<user.select> fenster klip$:                  user.screenshot_window_clipboard()