tag: browser
language: de_DE
-
adressleiste | adresse editieren | fokus url: browser.focus_address()
adresse kopieren | url kopieren:
    browser.focus_address()
    sleep(50ms)
    edit.copy()
(nächste [Seite]|vorwärts): browser.go_forward()
(letzte [Seite]|rückwärts): browser.go_back()
auf zu {user.website}: browser.go(website)

bookmark erstellen: browser.bookmark()
bookmark tabs: browser.bookmark_tabs()
neuladen: browser.reload()
durchladen: browser.reload_hard()

bookmarks zeigen: browser.bookmarks()
bookmark leiste [anzeigen]: browser.bookmarks_bar()
downloads anzeigen: browser.show_downloads()
erweiterungen anzeigen: browser.show_extensions()
verlauf anzeigen: browser.show_history()
cache anzeigen: browser.show_clear_cache()
dev tools [anzeigen]: browser.toggle_dev_tools()
