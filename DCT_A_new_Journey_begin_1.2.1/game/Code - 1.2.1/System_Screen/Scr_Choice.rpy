
##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu_choice_button"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice_button" at Sys_Eff_Appear

                else:
                    text caption style "menu_choice_button"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xpadding 20
        ypadding 0
        xminimum int(1000)
        xmaximum int(1800)
    style menu_choice_button:
        size 50
        xalign 0.5
        yalign 0.5
        insensitive_color "#afafaf"
        idle_color "#ffffff"
        hover_color "#ffffff"
        selected_idle_color "#ffb600"
        selected_hover_color "#ffb600"

    #style.menu_choice_button.background = Frame("gui/Choice menu/Choice_menu.png",0,0)
    #style.menu_choice_button.hover_background = Frame("gui/Choice menu/Choice_menu_hover.png",0,0)
