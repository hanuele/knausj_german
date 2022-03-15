language: de_DE
-

frage [zeichen]: "?"
unterstrich: "_"
doppel strich: "--"
(schweif [auf] | geschweift [auf]| locke): "{"
(schweif zu | geschweift zu | locke zu): "}"
dreifach strich: "'''"
dreifach graf:
    insert("```")
punkt punkt: ".."
ellipse: "..."
(komma und | kohl): ", "
plus: "+"
pfeil: "->"
doppel pfeil: "=>"
neue zeile: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
leer text:
    '""'
    key(left)
leer flucht text:
    '\\"\\"'
    key(left)
    key(left)
leer einfach [text]:
    "''"
    key(left)
leer flucht einfach [text]:
    "\\'\\'"
    key(left)
    key(left)
(in klammern | parameter):
	insert("()")
	key(left)
in (block [auf] | liste):
	insert("[]")
	key(left)
in (schweif | locken):
	insert("{}")
	key(left)
in prozent:
	insert("%%")
	key(left)
in einfach [text]:
	insert("''")
	key(left)
in text:
    insert('""')
	key(left)
in graf:
	insert("``")
	key(left)
einecken:
    text = edit.selected_text()
    user.paste("<{text}>")
einblocken:
    text = edit.selected_text()
    user.paste("[{text}]")
einlocken:
    text = edit.selected_text()
    user.paste("{{{text}}}")
einklammern:
    text = edit.selected_text()
    user.paste("({text})")
prozentual:
    text = edit.selected_text()
    user.paste("%{text}%")
einzeichen:
    text = edit.selected_text()
    user.paste("'{text}'")
eintexten:
    text = edit.selected_text()
    user.paste('"{text}"')
eingrafen:
    text = edit.selected_text()
    user.paste('`{text}`')
