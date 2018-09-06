
##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
#######################################################################
init -2:

    style Style_SettingMenu is button:
        xpadding 20
        ypadding 0
        #xmargin 0
        #ymargin 0
        xminimum int(300)
        xmaximum int(300)

screen navigation:

    vbox:
        xalign .01
        yalign .96
        if persistent.Sys_Langue == "ENG":
            textbutton "Main Menu" action MainMenu() hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_SettingMenu" at Sys_Eff_Appear
            textbutton "Return" action Hide('navigation'), Hide('Scr_Setting') hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_SettingMenu" at Sys_Eff_Appear
        elif persistent.Sys_Langue == "VN":
            textbutton "Trang chính" action MainMenu() hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_SettingMenu" at Sys_Eff_Appear
            textbutton "Trở lại" action Hide('navigation'), Hide('Scr_Setting') hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_SettingMenu" at Sys_Eff_Appear
