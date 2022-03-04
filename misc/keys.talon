language: de_DE
-

gehe <user.arrow_keys>: user.move_cursor(arrow_keys)
<user.letter>: key(letter)
(steige | großschrift) <user.letters> [(kleinschrift | sinke)]: 
        user.insert_formatted(letters, "ALL_CAPS")
<user.symbol_key>: key(symbol_key)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
# for key combos consisting only of modifiers, eg. `press super`.
drücke <user.modifiers>: key(modifiers)
# for consistency with dictation mode and explicit arrow keys if you need them.
drücke <user.keys>: key(keys)

# Add symbol at end of line and then insert line below
abschliessend {user.symbol_key}:
    edit.line_end()
    "{symbol_key}"
    edit.line_insert_down()

# Special symbols
neue zeile symbol:      "\\n"
tab symbol:             "\\t"