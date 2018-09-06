##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

init python:
# text
    #style.nvl_dialogue.size = 0
    style.nvl_vbox.box_spacing = 0
    style.nvl_dialogue.font = "fonts/Roboto-Condensed.ttf"
    #style.nvl_dialogue.drop_shadow = [(1, 1)] 
    #style.nvl_dialogue.drop_shadow_color = "#330000"

# Size of the box
    style.nvl_window.top_margin = 0
    style.nvl_window.bottom_margin = 0
    style.nvl_window.left_margin = 0
    style.nvl_window.right_margin = 0

# Size of the textbox
    style.nvl_window.top_padding = 170
    style.nvl_window.bottom_padding = 150
    style.nvl_window.left_padding = 190
    style.nvl_window.right_padding = 300
    style.nvl_window.background = "images/DCT/Interface/NVL_mode.png"

screen nvl:
    window:
        style "nvl_window"
    frame:
        background None
        xpos 150 ypos 120
        top_padding 20 
        bottom_padding 20 
        left_padding 20
        right_padding 20
            #vbar value YScrollValue("vp") bar_invert True
        has side "c r":
            area (0, 0, 1700, 740)
            viewport id "vp":
                
                mousewheel True
                yadjustment ui.adjustment (value=99999, range=99999)   # err... works, but...

                vbox:
                    style "nvl_vbox"
                
                    # Display dialogue.
                    for who, what, who_id, what_id, window_id in dialogue:
                        window:
                            id window_id

                            has hbox:
                                spacing 10

                            if who is not None:
                                text who id who_id

                            text what id what_id
            #vbar value YScrollValue("vp") bar_invert True
    vbar value YScrollValue("vp") bar_invert True:
                xalign 0.99 yalign 0.4
                xmaximum 15 
                ymaximum 750
                #left_bar Frame("gui/config_bar_full.png", 10, 0) 
                #right_bar Frame("gui/config_bar_empty.png", 10, 0)

        # Display a menu, if given.
    if items:
        frame:
            xpos 90 ypos 400
            top_padding 10 
            bottom_padding 10 
            left_padding 10 
            right_padding 10
            has side "c r":
                area (0, 0, 200, 150)
                viewport id "menu_vp":
                    
                    vbox:
                        id "menu"

                        for caption, action, chosen in items:

                            if action:

                                button:
                                    style "nvl_menu_choice_button"
                                    action action

                                    text caption style "nvl_menu_choice"

                            else:

                                text caption style "nvl_dialogue"
                vbar value YScrollValue("menu_vp")
