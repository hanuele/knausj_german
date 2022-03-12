language: de_DE
-

<user.find> es:
    edit.find()
    user.quick_macro_set("edit.find_next")

<user.find> das:
    edit.find(edit.selected_text())
    user.quick_macro_set("edit.find_next")

<user.find> nächste:
    edit.find_next()
    user.quick_macro_set("edit.find_next")

spring wort links:
    edit.word_left()
    user.quick_macro_set("edit.word_left")

spring wort [rechts]:
    edit.word_right()
    user.quick_macro_set("edit.word_right")

tick links:
    edit.left()
    user.quick_macro_set("edit.left")

tick [rechts]:
    edit.right()
    user.quick_macro_set("edit.right")

norden:
    edit.up()
    user.quick_macro_set("edit.up")

süden:
    edit.down()
    user.quick_macro_set("edit.down")

<user.start>:
    edit.line_start()
    user.quick_macro_set("edit.line_end")

<user.end>:
    edit.line_end()
    user.quick_macro_set("edit.line_insert_down")

zeile <user.start>:
    edit.line_start()
    edit.line_start()
    user.quick_macro_set("edit.line_end")

[(zu|zum|zur)] keller:
    edit.file_end()
    user.quick_macro_set("edit.file_start")
    
[(zu|zum|zur)] decke:
    edit.file_start()
    user.quick_macro_set("edit.file_end")

[(zu|zum|zur)] seite runter:
    edit.page_down()
    user.quick_macro_set("edit.page_down")


[(zu|zum|zur)] seite hoch:
    edit.page_up()
    user.quick_macro_set("edit.page_up")

# selecting
<user.select> zeile:
    edit.select_line()
    user.quick_macro_set("edit.copy")

<user.select> alles:
    edit.select_all()
    user.quick_macro_set("edit.copy")

<user.select> links:
    edit.extend_left()
    user.quick_macro_set("edit.extend_left")

<user.select> [rechts]:
    edit.extend_right()
    user.quick_macro_set("edit.extend_right")

<user.select> hoch:
    edit.extend_line_up()
    user.quick_macro_set("edit.extend_line_up")

<user.select> runter:
    edit.extend_line_down()
    user.quick_macro_set("edit.extend_line_down")

<user.select> hier:
    edit.select_word()
    user.quick_macro_set("edit.copy")

<user.select> wort links:
    edit.extend_word_left()
    user.quick_macro_set("edit.extend_word_left")

<user.select> wort [rechts]:
    edit.extend_word_right()
    user.quick_macro_set("edit.extend_word_right")

<user.select> <user.start>:
    edit.extend_line_start()
    user.quick_macro_set("edit.copy")

<user.select> <user.end>:
    edit.extend_line_end()
    user.quick_macro_set("edit.copy")

<user.select> decke:
    edit.extend_file_start()
    user.quick_macro_set("edit.copy")

<user.select> keller:
    edit.extend_file_end()
    user.quick_macro_set("edit.copy")

# editing
einrücken:
    edit.indent_more()
    user.quick_macro_set("edit.indent_more")

ausrücken:
    edit.indent_less()
    user.quick_macro_set("edit.indent_less")

# deleting
<user.delete> zeile:
    edit.delete_line()
    user.quick_macro_set("edit.delete_line")

<user.delete> links:
    key(backspace)
    user.quick_macro_set("edit.delete_line")

<user.delete> [rechts]:
    key(delete)
    user.quick_macro_set("key","delete")


<user.delete> hoch:
    edit.extend_line_up()
    edit.delete()
    user.quick_macro_set_chained("edit.extend_line_up#edit.delete")

<user.delete> runter:
    edit.extend_line_down()
    edit.delete()
    user.quick_macro_set_chained("edit.extend_line_down#edit.delete")

<user.delete> hier:
    edit.delete_word()
    user.quick_macro_set("edit.undo")

<user.delete> wort links:
    edit.extend_word_left()
    edit.delete()
    user.quick_macro_set_chained("edit.extend_word_left#edit.delete")

<user.delete> wort [rechts]:
    edit.extend_word_right()
    edit.delete()
    user.quick_macro_set_chained("edit.extend_word_right#edit.delete")

<user.delete> <user.start>:
    edit.extend_line_start()
    edit.delete()
    user.quick_macro_set("edit.undo")

<user.delete> <user.end>:
    edit.extend_line_end()
    edit.delete()
    user.quick_macro_set("edit.undo")

<user.delete> decke:
    edit.extend_file_start()
    edit.delete()
    user.quick_macro_set("edit.undo")

<user.delete> keller:
    edit.extend_file_end()
    edit.delete()
    user.quick_macro_set("edit.undo")

<user.delete> alles:
    edit.select_all()
    edit.delete()
    user.quick_macro_set("edit.undo")

#<user.copy> commands
<user.copy> alles:
    edit.select_all()
    edit.copy()
    user.quick_macro_set("edit.paste")

<user.copy> hier:
    edit.select_word()
    edit.copy()
    user.quick_macro_set("edit.paste")

<user.copy> wort links:
    edit.extend_word_left()
    edit.copy()
    user.quick_macro_set("edit.paste")

<user.copy> wort [rechts]:
    edit.extend_word_right()
    edit.copy()
    user.quick_macro_set("edit.paste")

<user.copy> zeile:
    edit.select_line()
    edit.copy()
    user.quick_macro_set("edit.paste")

<user.copy> <user.end>:
	edit.extend_line_end()
	edit.copy()
	user.quick_macro_set("edit.paste")

<user.copy> <user.start>:
	edit.extend_line_start()
	edit.copy()
	user.quick_macro_set("edit.paste")
    
#cut commands
<user.cut> alles:
    edit.select_all()
    edit.cut()
    user.quick_macro_set("edit.paste")

<user.cut> hier:
    edit.select_word()
    edit.cut()
    user.quick_macro_set("edit.paste")

<user.cut> wort links:
    edit.extend_word_left()
    edit.cut()
    user.quick_macro_set("edit.paste")

<user.cut> wort [rechts]:
    edit.extend_word_right()
    edit.cut()
    user.quick_macro_set("edit.paste")

<user.cut> zeile:
    edit.select_line()
    edit.cut()
    user.quick_macro_set("edit.paste")
