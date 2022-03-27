language: de_DE
-

talon [überprüfe] updates: menu.check_for_updates()
talon öffne log: menu.open_log()
talon öffne rebel: menu.open_repl()
talon home: menu.open_talon_home()
talon <user.term_copy> kontext python: user.talon_add_context_clipboard_python()
talon <user.term_copy> kontext: user.talon_add_context_clipboard()
talon <user.term_copy> applikationsname:
    name = app.name()
    clip.set_text(name)  
talon <user.term_copy> echse:
    executable = app.executable()
    clip.set_text(executable)
talon <user.term_copy> bandel:
    bundle = app.bundle()
    clip.set_text(bundle)
talon <user.term_copy> [fenster] titel: 
    title = win.title()
    clip.set_text(title)
talon drucke version: 
    result = user.talon_version_info()
    print(result)
talon <user.term_paste> version: 
    result = user.talon_version_info()
    user.paste(result)
talon <user.term_paste> kontext: 
    result = user.talon_get_active_context()
    print(result)
^talon test <user.term_navigate_left>$:
    phrase = user.history_get(1)
    user.talon_sim_phrase(phrase)
^talon test nummer <number_small>$:
    phrase = user.history_get(number_small)
    user.talon_sim_phrase(phrase)
^talon test <phrase>$:
    user.talon_sim_phrase(phrase)
^talon debugge aktion {user.talon_actions}$: 
    user.talon_action_find("{user.talon_actions}")
^talon debugge liste {user.talon_lists}$:
    user.talon_debug_list(talon_lists)
^talon <user.term_copy> list {user.talon_lists}$:
    user.talon_copy_list(talon_lists)
^talon debugge tags$:
    user.talon_debug_tags()
^talon debugge modi$:
    user.talon_debug_modes()
^talon debugge bereich {user.talon_scopes}$:
    user.talon_debug_scope(talon_scopes)
^talon debug einestellung {user.talon_settings}$:
    user.talon_debug_setting(talon_settings)
^talon debugge alle einstellungen$: 
    user.talon_debug_all_settings()
^talon debugge aktive applikation$: 
    result = user.talon_get_active_application_info()
    print("**** Dumping active application **** ")
    print(result)
    print("***********************")
^talon <user.term_copy> aktive applikation$:
    result = user.talon_get_active_application_info()
    clip.set_text(result)
