language: de_DE
-
settings(): 
	speech.record_all = 1
	speech.record_labels = 1

^(aktiviere englisch|sprache englisch)$:
	mode.disable("user.german")
	mode.enable("user.english")