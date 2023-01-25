mode: command
mode: mixed
language: de_DE
-
#TODO


Fenster öffnen: app.window_open()
nächstes Fenster: app.window_next()
vorheriges Fenster: app.window_previous()
Fenster schliessen: app.window_close()

minimieren: 
    key(alt-space)
    sleep(0.1)
    key(n)

    #app.window_hide()
maximieren: 
    key(alt-space)
    sleep(0.1)
    key(x)    
    #user.maximize()

normal:
    key(alt-space)
    sleep(0.1)
    key(r)

fokus <user.running_applications> [<phrase>]$:
    user.switcher_focus(running_applications)
    sleep(200ms)
    user.parse_phrase(phrase or "")

# following only works on windows. Can't figure out how to make it work for mac. No idea what the equivalent for linux would be.
fokus$: user.switcher_menu()
laufende liste: user.switcher_toggle_running()
sichtbare liste: user.switcher_toggle_visible()
laufende schliessen: user.switcher_hide_running()
sichtbare schliessen: user.switcher_hide_visible()
starte <user.launch_applications>: user.switcher_launch(launch_applications)

schnapp <user.window_snap_position>: user.snap_window(window_snap_position)
schnapp <user.term_navigate_right> [schirm]: user.move_window_next_screen()
schnapp <user.term_navigate_left> [schirm]: user.move_window_move_window_previous_screen()
schnapp schirm <number>: user.move_window_to_screen(number)
schnapp <user.running_applications> <user.window_snap_position>:
    user.snap_app(running_applications, window_snap_position)
schnapp <user.running_applications> [schirm] <number>:
    user.move_app_to_screen(running_applications, number)

schnapp <number> <user.window_snap_position>: 
    user.move_window_to_screen(number)
    sleep(0.5)
    user.snap_window(window_snap_position)

ziel <number> <user.window_snap_position>: 
    user.move_cursor_to_snap_position_center(number, window_snap_position)
    mouse_click(0)

osten:
    key(super-right)
    user.quick_macro_set("key","super-right")

westen:
    key(super-left)
    user.quick_macro_set("key","super-left")

norden:
    key(super-up)
    user.quick_macro_set("key","super-up")

sueden:
    key(super-down)
    user.quick_macro_set("key","super-down")

