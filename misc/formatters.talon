language: de_DE
-
#provide both anchored and unachored commands via 'over'
satz <user.text>$: user.insert_formatted(text, "NOOP")
satz <user.text> über: user.insert_formatted(text, "NOOP")
{user.prose_formatter} <user.prose>$: user.insert_formatted(prose, prose_formatter)
{user.prose_formatter} <user.prose> über: user.insert_formatted(prose, prose_formatter)
<user.format_text>+$: user.insert_many(format_text_list)
<user.format_text>+ über: user.insert_many(format_text_list)
<user.formatters> das: user.formatters_reformat_selection(user.formatters)
word <user.word>: user.insert_formatted(user.word, "NOOP")
gerade eben liste: user.toggle_phrase_history()
gerade eben schliessen: user.phrase_history_hide()
gerade eben wiederholen <number_small>: insert(user.get_recent_phrase(number_small))
gerade eben kopieren <number_small>: clip.set_text(user.get_recent_phrase(number_small))
selektiere das: user.select_last_phrase()
vor dem: user.before_last_phrase()
nein das | weg damit: user.clear_last_phrase()
nein das war <user.formatters>: user.formatters_reformat_last(formatters)