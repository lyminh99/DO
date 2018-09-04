##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
#######################################################################

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 10
    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 30
    style.quick_button_text.idle_color = "#ebe5e5"
    style.quick_button_text.hover_color = "#fffafa"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#fffafa"

        
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False

screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xalign 1.0
        yalign 1.0

        imagebutton auto "gui/Ingame_quick_save/Ingame_quick_save_%s.png" xpos 510 ypos -165 focus_mask True action QuickSave() hovered [ Play ("test_one", "sfx/click.ogg")]
        imagebutton auto "gui/Ingame_quick_load/Ingame_quick_load_%s.png" xpos 375 ypos -105 focus_mask True action QuickLoad() hovered [ Play ("test_one", "sfx/click.ogg")]
        imagebutton auto "gui/Ingame_save/Ingame_save_%s.png" xpos 240 ypos -45 focus_mask True action ShowMenu('save') hovered [ Play ("test_one", "sfx/click.ogg")]
        imagebutton auto "gui/Ingame_skip/Ingame_skip_%s.png" xpos 250 ypos -165 focus_mask True action Skip() hovered [ Play ("test_one", "sfx/click.ogg")]
        imagebutton auto "gui/Ingame_Auto/Ingame_Auto_%s.png" xpos 115 ypos -105 focus_mask True action Preference("auto-forward", "toggle") hovered [ Play ("test_one", "sfx/click.ogg")]
        imagebutton auto "gui/Ingame_Prefs/Ingame_Prefs_%s.png" xpos -20 ypos -45 focus_mask True action ShowMenu('preferences') hovered [ Play ("test_one", "sfx/click.ogg")]

screen quick_menu1:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xalign 0.915
        yalign 0.875
        imagebutton auto "gui/Ingame_quick_save/Ingame_quick_save_%s.png" xpos 0 ypos 0 focus_mask True action QuickSave() hovered [ Play ("test_one", "sfx/click.ogg")]
        imagebutton auto "gui/Ingame_quick_load/Ingame_quick_load_%s.png" xpos 15 ypos 0 focus_mask True action QuickLoad() hovered [ Play ("test_one", "sfx/click.ogg")]
        imagebutton auto "gui/Ingame_save/Ingame_save_%s.png" xpos 30 ypos 0 focus_mask True action ShowMenu('save') hovered [ Play ("test_one", "sfx/click.ogg")]
        imagebutton auto "gui/Ingame_skip/Ingame_skip_%s.png" xpos 45 ypos 0 focus_mask True action Skip() hovered [ Play ("test_one", "sfx/click.ogg")]
        imagebutton auto "gui/Ingame_Auto/Ingame_Auto_%s.png" xpos 60 ypos 0 focus_mask True action Preference("auto-forward", "toggle") hovered [ Play ("test_one", "sfx/click.ogg")]
        imagebutton auto "gui/Ingame_Prefs/Ingame_Prefs_%s.png" xpos 75 ypos 0 focus_mask True action ShowMenu('preferences') hovered [ Play ("test_one", "sfx/click.ogg")]