language: en_US
-
settings(): 
	speech.record_all = 1
	speech.record_labels = 1

^(activate german|language german)$: 
    mode.disable("user.english")
    mode.enable("user.german")

^german [<phrase>]$:
    user.german_recognize(phrase) 