language: de_DE
-

# -1 because we are repeating, so the initial command counts as one
<user.ordinals>: core.repeat_command(ordinals-1)
<number_small> mal: core.repeat_command(number_small-1)
(wiederholen|doppelt|repetieren): core.repeat_command(1)
(wiederhole|repetiere) <number_small> [mal]: core.repeat_command(number_small)
