language: en_US
-
settings(): 
	speech.record_all = 1
	speech.record_labels = 1

^activate german: 
    mode.disable("user.english")
    mode.enable("user.german")