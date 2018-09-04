# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        
        vbox:
            style "menu"
            spacing 2
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)
    style.menu_choice_button.background = Frame("gui/Choice menu/Choice_menu.png",0,0)
    style.menu_choice_button.hover_background = Frame("gui/Choice menu/Choice_menu_hover.png",0,0)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

    use quick_menu

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:
    on "show" action Play("sound", "sfx/alert.ogg")
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.

    add "gui/yesno_ground.png"
    imagebutton auto "gui/yesno_yes_%s.png" xpos 467 ypos 669 action yes_action hover_sound "sfx/click.ogg"
    imagebutton auto "gui/yesno_no_%s.png" xpos 926 ypos 669 action no_action hover_sound "sfx/click.ogg"
    
    if message == layout.ARE_YOU_SURE:
        add "gui/yesno_are_you_sure.png"
    elif message == layout.DELETE_SAVE:
        add "gui/yesno_delete_save.png"
    elif message == layout.OVERWRITE_SAVE:
        add "gui/yesno_overwrite_save.png"
    elif message == layout.LOADING:
        add "gui/yesno_loading.png"
    elif message == layout.QUIT:
        add "gui/yesno_quit.png"
    elif message == layout.MAIN_MENU:
        add "gui/yesno_main_menu.png"

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
#######################################################################

screen navigation:
    imagebutton auto "gui/game_menu_save_%s.png" xpos 1510 ypos 160 focus_mask True action ShowMenu('save') hovered [ Play ("test_one", "sfx/click.ogg")] at nav_eff
    imagebutton auto "gui/game_menu_load_%s.png" xpos 1510 ypos 280 focus_mask True action ShowMenu('load') hovered [ Play ("test_two", "sfx/click.ogg")] at nav_eff
    imagebutton auto "gui/game_menu_config_%s.png" xpos 1510 ypos 400 focus_mask True action ShowMenu('preferences') hovered [ Play ("test_three", "sfx/click.ogg")] at nav_eff
    imagebutton auto "gui/game_menu_main_%s.png" xpos 1510 ypos 520 focus_mask True action MainMenu() hovered [ Play ("test_one", "sfx/click.ogg")] at nav_eff
    imagebutton auto "gui/game_menu_return_%s.png" xpos 1510 ypos 640 focus_mask True action Return() hovered [ Play ("test_two", "sfx/click.ogg")] at nav_eff
    imagebutton auto "gui/game_menu_quit_%s.png" xpos 1510 ypos 760 focus_mask True action Quit() hovered [ Play ("test_three", "sfx/click.ogg")] at nav_eff



