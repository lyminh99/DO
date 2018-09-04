##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
#######################################################################

screen preferences:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/config_ground.jpg" # We add the image that is shown in the background of the preferences screen.
    use navigation # We include the navigation screen (game menu)

####################################################################### Display windowed/full screen:
    imagebutton auto "gui/config_display_window_%s.png" xpos 560 ypos 346 focus_mask True action Preference('display', 'window') at config_eff hovered [ Play ("test_one", "sfx/click.ogg")]
    imagebutton auto "gui/config_display_fullscreen_%s.png" xpos 720 ypos 346 focus_mask True action Preference('display', 'fullscreen') at config_eff hovered [ Play ("test_two", "sfx/click.ogg")]

####################################################################### Transitions on/off:
    imagebutton auto "gui/config_transitions_none_%s.png" xpos 935 ypos 346 focus_mask True action Preference('transitions', 'none') at config_eff hovered [ Play ("test_four", "sfx/click.ogg")]
    imagebutton auto "gui/config_transitions_all_%s.png" xpos 1105 ypos 346 focus_mask True action Preference('transitions', 'all') at config_eff hovered [ Play ("test_four", "sfx/click.ogg")]

####################################################################### Stop/continue skipping after choices
    imagebutton auto "gui/config_afterchoices_stop_%s.png" xpos 560 ypos 645 focus_mask True action Preference('after choices', 'stop') at config_eff hovered [ Play ("test_one", "sfx/click.ogg")]
    imagebutton auto "gui/config_afterchoices_skip_%s.png" xpos 720 ypos 645 focus_mask True action Preference('after choices', 'skip') at config_eff hovered [ Play ("test_two", "sfx/click.ogg")]

####################################################################### Skip all/seen text
    imagebutton auto "gui/config_skip_seen_%s.png" xpos 935 ypos 645 focus_mask True action Preference('skip', 'seen') at config_eff hovered [ Play ("test_one", "sfx/click.ogg")]
    imagebutton auto "gui/config_skip_all_%s.png" xpos 1105 ypos 645 focus_mask True action Preference('skip', 'all') at config_eff hovered [ Play ("test_two", "sfx/click.ogg")]

####################################################################### Button to begin skipping. Only active/visible if the game is started. Image config_begin_skipping_insensitive.png is used when the button is not active.
    imagebutton auto "gui/config_begin_skipping_%s.png" xpos 590 ypos 217 focus_mask True action Preference('begin skipping') hovered [ Play ("test_one", "sfx/click.ogg")]

####################################################################### bar sliders for volume control, text speed and auto-forward time
    frame xpos 105 ypos 256:
        style_group "pref"
        has vbox
        bar value Preference("music volume")

    frame xpos 105 ypos 382:
        style_group "pref"
        has vbox
        bar value Preference("sound volume")

    frame xpos 105 ypos 508:
        style_group "pref"
        has vbox
        bar value Preference("voice volume")

    frame xpos 105 ypos 664:
        style_group "pref"
        has vbox
        bar value Preference("text speed")

    frame xpos 105 ypos 790:
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time")

init -2 python: 
    # Styling for the bar sliders:
    # Aleema's Customizing Menus tutorial: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
    # Bar style properties documentation: http://www.renpy.org/doc/html/style.html#bar-style-properties
    style.pref_frame.background = None
    style.pref_slider.left_bar = "gui/config_bar_full.png"
    style.pref_slider.right_bar = "gui/config_bar_empty.png"
    style.pref_slider.thumb = None
    style.pref_slider.xmaximum = 406
    style.pref_slider.ymaximum = 67   
