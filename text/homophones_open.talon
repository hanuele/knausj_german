mode: user.homophones
language: de_DE
-
wähle <number_small> [aus]:
    result = user.homophones_select(number_small)
    insert(result)
    user.homophones_hide()
wähle <user.formatters> <number_small> [aus]:
    result = user.homophones_select(number_small)
    insert(user.formatted_text(result, formatters))
    user.homophones_hide()