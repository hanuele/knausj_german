mode: dictation
language: de_DE
experiment: anchor-file
-

settings(): 
    speech.record_all = 1
    speech.record_labels = 1

^drück <user.modifiers>$: key(modifiers)
^drück <user.keys>$: key(keys)

# Everything here should call `auto_insert()` (instead of `insert()`), to preserve the state to correctly auto-capitalize/auto-space.
# (Talonscript string literals implicitly call `auto_insert`, so there's no need to wrap those)
<user.raw_prose>: auto_insert(raw_prose)
grossbuchstaben: user.dictation_format_cap()
# Hyphenated variants are for Dragon.
kleinbuchstaben: user.dictation_format_no_cap()
keine leerzeichen: user.dictation_format_no_space()
#TODO replace terms

# Navigations
geh <number_small> (zeilen|zeile) hoch:
    edit.up()
    repeat(number_small - 1)
geh <number_small> (zeilen|zeile) runter:
    edit.down()
    repeat(number_small - 1)
geh <number_small> (wörter|wort) links:
    edit.word_left()
    repeat(number_small - 1)
geh <number_small> (wörter|wort) rechts:
        edit.word_right()
    repeat(number_small - 1)
zeilen anfang : edit.line_start()
zeilen ende: edit.line_end()

# Selection
selektiere <number_small> (wörter|wort) links:
    edit.extend_word_left()
    repeat(number_small - 1)
selektiere <number_small> (wörter|wort) rechts:
    edit.extend_word_right()
    repeat(number_small - 1)
selektiere <number_small> (buchstsabe|buchstaben) links:
    edit.extend_left()
    repeat(number_small - 1)
selektiere <number_small> (buchstsabe|buchstaben) rechts:
    edit.extend_right()
    repeat(number_small - 1)
lösche <number_small> (wörter|wort) links:
    edit.extend_word_left()
    repeat(number_small - 1)
    edit.delete()
lösche <number_small> (wörter|wort) rechts:
    edit.extend_word_right()
    repeat(number_small - 1)
    edit.delete()
lösche <number_small> (buchstsabe|buchstaben) links:
    edit.extend_left()
    repeat(number_small - 1)
    edit.delete()
lösche <number_small> (buchstsabe|buchstaben) rechts:
    edit.extend_right()
    repeat(number_small - 1)
    edit.delete()

# Formatting
formatiere <user.format_text>:
    user.dictation_insert_raw(format_text)
^format auswahl <user.formatters>$:
    user.formatters_reformat_selection(formatters)

# Corrections
nope: user.clear_last_phrase()
nope das: edit.delete()
selektier das: user.select_last_phrase()
buchstabier das <user.letters>: auto_insert(letters)
buchstabier das <user.formatters> <user.letters>:
    result = user.formatted_text(letters, formatters)
    user.dictation_insert_raw(result)

# Escape, type things that would otherwise be commands
^aether <user.text>$:
    auto_insert(user.text)

#Additions not in official knausj
nummer <user.number_string>: "{number_string}"
nummer <user.number_string> punkt <digit_string>: "{number_string}.{digit_string}"
nummer <user.number_string> komma <digit_string>: "{number_string}.{digit_string}"

halt [<phrase>]$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
    user.parse_phrase(phrase or "")