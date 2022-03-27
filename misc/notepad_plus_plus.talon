app: notepad_plus_plus
mode: command
-

tag(): user.find_and_replace

<user.term_find> unique$:
	key(ctrl-f)	
	user.paste('\\b[0-9a-fA-F]{{8}}\\b-[0-9a-fA-F]{{4}}-[0-9a-fA-F]{{4}}-[0-9a-fA-F]{{4}}-\\b[0-9a-fA-F]{{12}}\\b')
	key(enter)
	user.quick_macro_set("key","enter")