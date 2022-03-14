mode: command
mode: mixed
language: de_DE
-

(jay son | jason ): "json"
(http | htp): "http"
word regex: "regex"
word queue: "queue"
word no: "NULL"

vergrößern: 
	edit.zoom_in()
	user.quick_macro_set("edit.zoom_in")

verkleinern: 
	edit.zoom_out()
	user.quick_macro_set("edit.zoom_out")

seite hoch: 
	key(pgup)
	user.quick_macro_set("key","pgup")

seite runter: 
	key(pgdown)
	user.quick_macro_set("key","pgdown")

<user.term_copy> <user.term_end>:
	edit.extend_line_end()
	edit.copy()
	user.quick_macro_set("edit.paste")

<user.term_copy> <user.term_start>:
	edit.extend_line_start()
	edit.copy()
	user.quick_macro_set("edit.paste")
		
<user.term_copy>: 
	edit.copy()
	user.quick_macro_set("edit.paste")

<user.term_copy> alles:
    edit.select_all()
    edit.copy()
    user.quick_macro_set("edit.paste")

<user.term_cut>: 
	edit.cut()
	user.quick_macro_set("edit.paste")

<user.term_paste>: 
	edit.paste()
	user.quick_macro_set("edit.paste")

<user.term_paste> formattiert: 
	edit.paste_match_style()
	user.quick_macro_set("edit.paste_match_style")

speichern: edit.save()
alles speichern: edit.save_all()

(nein|rückgängig): 
	edit.undo()
	user.quick_macro_set("edit.undo")

(nochmal|wiederholen): 
	edit.redo()
	user.quick_macro_set("edit.redo")

(weg|müll): 
	key(backspace)
	user.quick_macro_set("key","backspace")

(schub|einschub): 
	insert("  ") 
	key(left)

(zeilenwechsel|einzug): edit.line_insert_down()
