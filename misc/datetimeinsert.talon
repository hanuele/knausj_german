language: de_DE
-

datum einfügen:
    insert(user.time_format("%Y-%m-%d"))
UTC datum einfügen:
    insert(user.time_format_utc("%Y-%m-%d"))
zeitstempel einfügen:
    insert(user.time_format("%Y-%m-%d %H:%M:%S"))
hochaufgelösten zeitstempel einfügen:
    insert(user.time_format("%Y-%m-%d %H:%M:%S.%f"))
UTC zeitstempel einfügen:
    insert(user.time_format_utc("%Y-%m-%d %H:%M:%S"))
hochaufgelösten UTC zeitstempel einfügen:
    insert(user.time_format_utc("%Y-%m-%d %H:%M:%S.%f"))
