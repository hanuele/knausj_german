language: de_DE
-
lauter: key(volup)
leiser: key(voldown)
#lautstärke auf <number>: user.media_set_volume(number)

stummstellen: key(mute)
(lied <user.term_navigate_right> | <user.term_navigate_right> lied): key(next)
(lied <user.term_navigate_left>| <user.term_navigate_left> lied): key(prev)
(play|pause): user.play_pause()
