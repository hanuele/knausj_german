language: de_DE
-

<user.term_find> es:
    edit.find()
    user.quick_macro_set("edit.find_next")

<user.term_find> das:
    edit.find(edit.selected_text())
    user.quick_macro_set("edit.find_next")

<user.term_find> <user.term_navigate_right>:
    edit.find_next()
    user.quick_macro_set("edit.find_next")

<user.term_find> <user.term_navigate_left>:
    edit.find_previous()
    user.quick_macro_set("edit.find_previous")

spring <user.term_word_navigate> <user.term_navigate_left>:
    edit.word_left()
    user.quick_macro_set("edit.word_left")

spring <user.term_word_navigate> [<user.term_navigate_right>]:
    edit.word_right()
    user.quick_macro_set("edit.word_right")

tick <user.term_navigate_left>:
    edit.left()
    user.quick_macro_set("edit.left")

tick [<user.term_navigate_right>]:
    edit.right()
    user.quick_macro_set("edit.right")

norden:
    edit.up()
    user.quick_macro_set("edit.up")

süden:
    edit.down()
    user.quick_macro_set("edit.down")

<user.term_start>:
    edit.line_start()
    user.quick_macro_set("edit.line_end")

<user.term_end>:
    edit.line_end()
    user.quick_macro_set("edit.line_insert_down")

zeile <user.term_start>:
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
<user.term_select> zeile:
    edit.select_line()
    user.quick_macro_set("edit.copy")

<user.term_select> alles:
    edit.select_all()
    user.quick_macro_set("edit.copy")

<user.term_select> <user.term_navigate_left>:
    edit.extend_left()
    user.quick_macro_set("edit.extend_left")

<user.term_select> [<user.term_navigate_right>]:
    edit.extend_right()
    user.quick_macro_set("edit.extend_right")

<user.term_select> hoch:
    edit.extend_line_up()
    user.quick_macro_set("edit.extend_line_up")

<user.term_select> runter:
    edit.extend_line_down()
    user.quick_macro_set("edit.extend_line_down")

<user.term_select> hier:
    edit.select_word()
    user.quick_macro_set("edit.copy")

<user.term_select> <user.term_word_navigate> <user.term_navigate_left>:
    edit.extend_word_left()
    user.quick_macro_set("edit.extend_word_left")

<user.term_select> <user.term_word_navigate> [<user.term_navigate_right>]:
    edit.extend_word_right()
    user.quick_macro_set("edit.extend_word_right")

<user.term_select> <user.term_start>:
    edit.extend_line_start()
    user.quick_macro_set("edit.copy")

<user.term_select> <user.term_end>:
    edit.extend_line_end()
    user.quick_macro_set("edit.copy")

<user.term_select> decke:
    edit.extend_file_start()
    user.quick_macro_set("edit.copy")

<user.term_select> keller:
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
<user.term_delete> zeile:
    edit.delete_line()
    user.quick_macro_set("edit.delete_line")

<user.term_delete> <user.term_navigate_left>:
    key(backspace)
    user.quick_macro_set("edit.delete_line")

<user.term_delete> [<user.term_navigate_right>]:
    key(delete)
    user.quick_macro_set("key","delete")


<user.term_delete> hoch:
    edit.extend_line_up()
    edit.delete()
    user.quick_macro_set_chained("edit.extend_line_up#edit.delete")

<user.term_delete> runter:
    edit.extend_line_down()
    edit.delete()
    user.quick_macro_set_chained("edit.extend_line_down#edit.delete")

<user.term_delete> hier:
    edit.delete_word()
    user.quick_macro_set("edit.undo")

<user.term_delete> <user.term_word_navigate> <user.term_navigate_left>:
    edit.extend_word_left()
    edit.delete()
    user.quick_macro_set_chained("edit.extend_word_left#edit.delete")

<user.term_delete> <user.term_word_navigate> [<user.term_navigate_right>]:
    edit.extend_word_right()
    edit.delete()
    user.quick_macro_set_chained("edit.extend_word_right#edit.delete")

<user.term_delete> <user.term_start>:
    edit.extend_line_start()
    edit.delete()
    user.quick_macro_set("edit.undo")

<user.term_delete> <user.term_end>:
    edit.extend_line_end()
    edit.delete()
    user.quick_macro_set("edit.undo")

<user.term_delete> decke:
    edit.extend_file_start()
    edit.delete()
    user.quick_macro_set("edit.undo")

<user.term_delete> keller:
    edit.extend_file_end()
    edit.delete()
    user.quick_macro_set("edit.undo")

<user.term_delete> alles:
    edit.select_all()
    edit.delete()
    user.quick_macro_set("edit.undo")

#<user.term_copy> commands
<user.term_copy> alles:
    edit.select_all()
    edit.copy()
    user.quick_macro_set("edit.paste")

<user.term_copy> hier:
    edit.select_word()
    edit.copy()
    user.quick_macro_set("edit.paste")

<user.term_copy> <user.term_word_navigate> <user.term_navigate_left>:
    edit.extend_word_left()
    edit.copy()
    user.quick_macro_set("edit.paste")

<user.term_copy> <user.term_word_navigate> [<user.term_navigate_right>]:
    edit.extend_word_right()
    edit.copy()
    user.quick_macro_set("edit.paste")

<user.term_copy> zeile:
    edit.select_line()
    edit.copy()
    user.quick_macro_set("edit.paste")

<user.term_copy> <user.term_end>:
	edit.extend_line_end()
	edit.copy()
	user.quick_macro_set("edit.paste")

<user.term_copy> <user.term_start>:
	edit.extend_line_start()
	edit.copy()
	user.quick_macro_set("edit.paste")
    
#cut commands
<user.term_cut> alles [aus]:
    edit.select_all()
    edit.cut()
    user.quick_macro_set("edit.paste")

<user.term_cut> hier:
    edit.select_word()
    edit.cut()
    user.quick_macro_set("edit.paste")

<user.term_cut> <user.term_word_navigate> <user.term_navigate_left>:
    edit.extend_word_left()
    edit.cut()
    user.quick_macro_set("edit.paste")

<user.term_cut> <user.term_word_navigate> [<user.term_navigate_right>]:
    edit.extend_word_right()
    edit.cut()
    user.quick_macro_set("edit.paste")

<user.term_cut> zeile:
    edit.select_line()
    edit.cut()
    user.quick_macro_set("edit.paste")
