language: de_DE
-

datum <user.term_paste>:
    insert(user.time_format("%Y-%m-%d"))
UTC datum <user.term_paste>:
    insert(user.time_format_utc("%Y-%m-%d"))
zeitstempel <user.term_paste>:
    insert(user.time_format("%Y-%m-%d %H:%M:%S"))
hochaufgelösten zeitstempel <user.term_paste>:
    insert(user.time_format("%Y-%m-%d %H:%M:%S.%f"))
UTC zeitstempel <user.term_paste>:
    insert(user.time_format_utc("%Y-%m-%d %H:%M:%S"))
hochaufgelösten UTC zeitstempel <user.term_paste>:
    insert(user.time_format_utc("%Y-%m-%d %H:%M:%S.%f"))
