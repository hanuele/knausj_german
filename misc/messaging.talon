language: de_DE
tag: user.messaging
-
# Navigation
<user.term_navigate_left> (workspace | server): user.messaging_workspace_previous()
<user.term_navigate_right> (workspace | server): user.messaging_workspace_next()
kanal: user.messaging_open_channel_picker()
kanal <user.text>:
    user.messaging_open_channel_picker()
    insert(user.formatted_text(user.text, "ALL_LOWERCASE"))
kanal <user.term_navigate_left>: user.messaging_channel_previous()
kanal <user.term_navigate_right>: user.messaging_channel_next()
([kanal] ungelesen <user.term_navigate_left> | <user.term_go> <user.term_navigate_left>): user.messaging_unread_previous()
([kanal] ungelesen <user.term_navigate_right> | <user.term_go> <user.term_navigate_right>): user.messaging_unread_next()
<user.term_go> <user.term_find>: user.messaging_open_search()
markiere (alles | workspace | server) als gelesen: user.messaging_mark_workspace_read()
markiere kanal als gelesen: user.messaging_mark_channel_read()
upload file: user.messaging_upload_file()
