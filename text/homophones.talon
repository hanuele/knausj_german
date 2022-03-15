language: de_DE
-

homofon <user.homophones_canonical>: user.homophones_show(homophones_canonical)
homofon auswahl: user.homophones_show_selection()
homofon <user.homophones_canonical> erwirken: user.homophones_force_show(homophones_canonical)
homofon erwirken: user.homophones_force_show_selection()
homofone ausblenden: user.homophones_hide()
homofon <user.term_word_navigate>:
  edit.select_word()
  user.homophones_show_selection()
homofon [<user.ordinals>] <user.term_word_navigate> <user.term_navigate_left>:
  n = ordinals or 1
  user.words_left(n - 1)
  edit.extend_word_left()
  user.homophones_show_selection()
homofon [<user.ordinals>] <user.term_word_navigate> <user.term_navigate_right>:
  n = ordinals or 1
  user.words_right(n - 1)
  edit.extend_word_right()
  user.homophones_show_selection()
