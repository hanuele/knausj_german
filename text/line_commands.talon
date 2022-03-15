tag: user.line_commands
language: de_DE
-
#this defines some common line commands. More may be defined that are ide-specific.
[zeilen] ende: edit.line_end()
[zeilen] anfang: edit.line_start()
zeile <number>: edit.jump_line(number)
zeilenende <number>: 
    edit.jump_line(number)
    edit.line_end()
zeile <number> auskommentieren:
    user.select_range(number, number)
    code.toggle_comment()
zeilen <number> bis <number> auskommentieren: 
    user.select_range(number_1, number_2)
    code.toggle_comment()
zeile <number> <user.term_delete>:
    edit.jump_line(number)
    user.select_range(number, number)
    edit.delete()
zeile <number> bis <number> <user.term_delete>: 
    user.select_range(number_1, number_2)
    edit.delete()
zeile <number> <user.term_copy>: 
    user.select_range(number, number)
    edit.copy()
zeilen <number> bis <number> <user.term_copy>: 
    user.select_range(number_1, number_2)
    edit.copy()
zeile <number> <user.term_cut>: 
    user.select_range(number, number)
    edit.cut()
zeilen <number> bis <number> <user.term_cut>: 
    user.select_range(number_1, number_2)
    edit.cut()
zeilen <number> bis <number> <user.term_paste>:
    user.select_range(number_1, number_2)
    edit.paste()
zeile <number> <user.term_select>: user.select_range(number, number)
zeilen <number> bis <number> <user.term_select>: user.select_range(number_1, number_2)
einrücken: edit.indent_more()
zeile <number> einrücken:
    edit.jump_line(number)
    edit.indent_more()
zeilen <number> bis <number> einrücken:
    user.select_range(number_1, number_2)
    edit.indent_more()
ausrücken: edit.indent_less()
zeile <number> ausrücken:
    user.select_range(number, number)
    edit.indent_less()
zeilen <number> bis <number> ausrücken:
    user.select_range(number_1, number_2)
    edit.indent_less()
runterziehen: edit.line_swap_down()
hochziehen: edit.line_swap_up()
zeile <number> hoch [ziehen]:
    user.select_range(number, number)
    edit.line_swap_up()
zeilen <number> bis <number> hoch [ziehen]: 
    user.select_range(number_1, number_2)
    edit.line_swap_up()
zeile <number> runter [ziehen]: 
    user.select_range(number, number)
    edit.line_swap_down()
zeilen <number> bis <number> runter [ziehen]: 
    user.select_range(number_1, number_2)
    edit.line_swap_down()
klon zeile: edit.line_clone()

<user.term_select> kamel <user.term_navigate_left>: user.extend_camel_left()
<user.term_select> kamel <user.term_navigate_right>: user.extend_camel_right()
zu kamel <user.term_navigate_left>: user.camel_left()
zu kamel <user.term_navigate_right>: user.camel_right()
