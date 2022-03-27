language: de_DE
-

<user.term_go> {user.website}: user.open_url(website)
{user.search_engine} <user.term_find> <user.text>$: user.search_with_search_engine(search_engine, user.text)
{user.search_engine} (das|dies):
    text = edit.selected_text()
    user.search_with_search_engine(search_engine, text)