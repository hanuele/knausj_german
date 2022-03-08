
language: de_DE
-

Maus kontroll modus: user.mouse_toggle_control_mouse()
Maus zoom modus: user.mouse_toggle_zoom_mouse()
Kamera überblendung: user.mouse_toggle_camera_overlay()
Maus kalibrieren: user.mouse_calibrate()	
(Picke|Auswahl): 
	mouse_click(0)
	# close the mouse grid if open
	user.grid_close()
    # End any open drags
	# Touch automatically ends left drags so this is for right drags specifically
	user.mouse_drag_end()

Rechtsklick:
	mouse_click(1)
	# close the mouse grid if open
	user.grid_close()
	user.quick_macro_set("mouse_click",0)
Mittelklick: 
	mouse_click(2)
	# close the mouse grid
	user.grid_close()
	user.quick_macro_set("mouse_click",2)

#see keys.py for modifiers.
#defaults
#command
#control
#option = alt
#shift
#super = windows key
<user.modifiers> (Picke|Auswahl): 
	key("{modifiers}:down")
	mouse_click(0)
	key("{modifiers}:up")
	# close the mouse grid
	user.grid_close()
<user.modifiers> Rechtsklick: 
	key("{modifiers}:down")
	mouse_click(1)
	key("{modifiers}:up")
	# close the mouse grid
	user.grid_close()
Doppelklick: 
	mouse_click()
	mouse_click()
	# close the mouse grid
	user.grid_close()
Dreifachklick: 
	mouse_click()
	mouse_click()
	mouse_click()
	# close the mouse grid
	user.grid_close()
ziehen:
	user.mouse_drag(0)
	# close the mouse grid
	user.grid_close()
rad runter: 
	user.mouse_scroll_down()
	user.quick_macro_set("user.mouse_scroll_down",3)

rechts ziehen:
	user.mouse_drag(1)
	# close the mouse grid
	user.grid_close()
loslassen:
    user.mouse_drag_end()

rad hier runter:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down()
ein bisschen runter: user.mouse_scroll_down(0.2)
hier ein bisschen runter:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down(0.2)
Rad tiefer: user.mouse_scroll_down_continuous()
Rad hier tiefer:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down_continuous()
Rad hoch: 
	user.mouse_scroll_up()
	user.quick_macro_set("user.mouse_scroll_up",3)

Rad hier hoch:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up()
ein bisschen hoch: user.mouse_scroll_up(0.2)
hier ein bisschen hoch:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up(0.2)
Rad höher: user.mouse_scroll_up_continuous()
Rad hier höher:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up_continuous()
Radstarre: user.mouse_gaze_scroll()
hier Radstarre:
    user.mouse_move_center_active_window()
    user.mouse_gaze_scroll()
Rad stop: user.mouse_scroll_stop()
Rad stop hier:
    user.mouse_move_center_active_window()
    user.mouse_scroll_stop()
Rad links: user.mouse_scroll_left()
Rad hier links:
    user.mouse_move_center_active_window()
    user.mouse_scroll_left()
ein bisschen links: user.mouse_scroll_left(0.5)
hier ein bisschen links:
    user.mouse_move_center_active_window()
    user.mouse_scroll_left(0.5)
Rad rechts: user.mouse_scroll_right()
Rad hier rechts:
    user.mouse_move_center_active_window()
    user.mouse_scroll_right()
ein bisschen rechts: user.mouse_scroll_right(0.5)
hier ein bisschen rechts:
    user.mouse_move_center_active_window()
    user.mouse_scroll_right(0.5)
merke Mausposition: user.copy_mouse_position()

Maus mittig: user.mouse_move_center_active_window()