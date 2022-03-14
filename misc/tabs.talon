tag: user.tabs
language: de_DE
-

neuer reiter: 
	app.tab_open()

reiter <user.term_navigate_left>: 
	app.tab_previous()
    user.quick_macro_set("app.tab_previous")

reiter <user.term_navigate_right>: 
	app.tab_next()
    user.quick_macro_set("app.tab_next")

reiter schliessen: 
	app.tab_close()
    user.quick_macro_set("app.tab_close")

reiter wiederherstellen: app.tab_reopen()

[zu] reiter <number>: user.tab_jump(number)
[zu] letztem reiter: user.tab_final()
reiter duplizieren: user.tab_duplicate()
