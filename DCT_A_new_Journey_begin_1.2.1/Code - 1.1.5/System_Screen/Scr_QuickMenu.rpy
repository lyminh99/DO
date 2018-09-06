##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
#######################################################################

init -2 python:
    #style.quick_button.set_parent('default')
    #style.quick_button.background = None
    style.quick_button.xpadding = 5
    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 36
    style.quick_button_text.idle_color = "#ebe5e5"
    style.quick_button_text.hover_color = "#fffafa"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#fffafa"

        
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False

#/////////////////////////////////////////////////////////////////////////////////////////////////////
init -2:
    #style Style_MainMenu is default
    style Style_Q_Menu is button_text:
        clear
    style Style_Q_Menu is button:
        xpadding 20
        ypadding 0
        #xmargin 0
        #ymargin 0
        xminimum int(160)
        xmaximum int(160)
        yminimum int(60)
        ymaximum int(60)
    style Style_Q_Menu_text:
        size 34
        xalign 0.5
        yalign 0.5
        insensitive_color "#afafaf"
        idle_color "#ffffff"
        hover_color "#ffffff"
        selected_idle_color "#ffb600"
        selected_hover_color "#ffb600"

screen quick_menu:

    hbox:
        xalign 0.98
        yalign 0.96
        if Sys_Langue == "ENG":
            vbox:
                textbutton "Q. Save" action QuickSave() hovered [ Play ("test_one", "sfx/click.ogg")]               style "Style_Q_Menu"
                textbutton "Q. Load"action QuickLoad() hovered [ Play ("test_one", "sfx/click.ogg")]                style "Style_Q_Menu"
                textbutton "S/Load" action Show('save') hovered [ Play ("test_one", "sfx/click.ogg")]             style "Style_Q_Menu"
            vbox:
                textbutton "Skip" action Skip() hovered [ Play ("test_one", "sfx/click.ogg")]                                           style "Style_Q_Menu"
                textbutton "Auto" action Preference("auto-forward", "toggle") hovered [ Play ("test_one", "sfx/click.ogg")]     style "Style_Q_Menu"
                textbutton "Config" action Show('Scr_Setting') hovered [ Play ("test_one", "sfx/click.ogg")]                style "Style_Q_Menu"
        elif Sys_Langue == "VN":
            vbox:
                textbutton "Lưu tạm" action QuickSave() hovered [ Play ("test_one", "sfx/click.ogg")]               style "Style_Q_Menu"
                textbutton "Tải tạm"action QuickLoad() hovered [ Play ("test_one", "sfx/click.ogg")]                style "Style_Q_Menu"
                textbutton "Lưu/Tải" action Show('save') hovered [ Play ("test_one", "sfx/click.ogg")]             style "Style_Q_Menu"
            vbox:
                textbutton "Tua" action Skip() hovered [ Play ("test_one", "sfx/click.ogg")]                                           style "Style_Q_Menu"
                textbutton "Tự đọc" action Preference("auto-forward", "toggle") hovered [ Play ("test_one", "sfx/click.ogg")]     style "Style_Q_Menu"
                textbutton "Sửa" action Show('Scr_Setting') hovered [ Play ("test_one", "sfx/click.ogg")]                style "Style_Q_Menu"
