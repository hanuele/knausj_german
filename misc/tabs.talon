tag: user.tabs
language: de_DE
-

neuer tab: 
	app.tab_open()

letzter tab: 
	app.tab_previous()
    user.quick_macro_set("app.tab_previous")

nächster tab: 
	app.tab_next()
    user.quick_macro_set("app.tab_next")

tab schliessen: 
	app.tab_close()
    user.quick_macro_set("app.tab_close")

tab wiederherstellen: app.tab_reopen()

[zu] tab <number>: user.tab_jump(number)
[zu] letztem tab: user.tab_final()
tab duplizieren: user.tab_duplicate()
