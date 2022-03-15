language: de_DE
-

## (2021-03-09) This syntax is experimental and may change. See below for an explanation.
<user.term_navigate> [{user.arrow_key}] [{user.navigation_action}] [{user.navigation_target_name}] [{user.before_or_after}] [<user.ordinals>] <user.navigation_target>:
## If you use this command a lot, you may wish to have a shorter syntax that omits the jump keyword. Note that you then at least have to say either a navigation_action or before_or_after:
#({user.navigation_action} [{user.arrow_key}] [{user.navigation_target_name}] [{user.before_or_after}] | [{user.arrow_key}] {user.before_or_after}) [<user.ordinals>] <user.navigation_target>: 
	user.navigation(navigation_action or "GO", arrow_key or "RIGHT", navigation_target_name or "DEFAULT", before_or_after or "DEFAULT", navigation_target, ordinals or 1)

# The functionality for all these commands is covered in the lines above, but these commands are kept here for convenience. Originally from word_selection.talon.  
#<user.term_word_navigate> <user.term_navigate_right> [<number_small>]: user.navigation_by_name("SELECT", "RIGHT", "DEFAULT", "word", number_small or 1)
#<user.term_word_navigate> <user.term_navigate_left> [<number_small>]: user.navigation_by_name("SELECT", "LEFT", "DEFAULT", "word", number_small or 1)
halb <user.term_word_navigate> <user.term_navigate_right> [<number_small>]: user.navigation_by_name("SELECT", "RIGHT", "DEFAULT", "small", number_small or 1)
halb <user.term_word_navigate> <user.term_navigate_left> [<number_small>]: user.navigation_by_name("SELECT", "LEFT", "DEFAULT", "small", number_small or 1)
voll <user.term_word_navigate> <user.term_navigate_right> [<number_small>]: user.navigation_by_name("SELECT", "RIGHT", "DEFAULT", "big", number_small or 1)
voll <user.term_word_navigate> <user.term_navigate_left> [<number_small>]: user.navigation_by_name("SELECT", "LEFT", "DEFAULT", "big", number_small or 1)
