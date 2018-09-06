##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

init -2:

    #style Style_Setting is default
    style Style_Setting is button_text:
        clear
    style Style_Setting is button:
        xpadding 20
        ypadding 0
        #xmargin 0
        #ymargin 0
        xminimum int(200)
        xmaximum int(200)
    style Style_Setting_text:
        size 50
        xalign 0.5
        yalign 0.5
        idle_color "#ffffff"
        hover_color "#ffffff"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#fffafa"
    style Style_Text_Label:
        size 50
init -2 python: 
    # Styling for the bar sliders:
    # Aleema's Customizing Menus tutorial: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
    # Bar style properties documentation: http://www.renpy.org/doc/html/style.html#bar-style-properties
    style.pref_frame.background = None
    #style.pref_slider.left_bar = "gui/config_bar_full.png"
    #style.pref_slider.hover_left_bar = "gui/config_bar_Background.png"
    #style.pref_slider.right_bar = "GUI/config_bar_empty.png"
    #style.pref_slider.thumb = "GUI/Config_Menu/config_bar_thumb.png"
    style.pref_slider.thumb_shadow = None
    style.pref_slider.thumb_offset = 10
    style.pref_slider.xmaximum = 500
    style.pref_slider.ymaximum = 50

screen Scr_Setting:

    add ('black') alpha 0.8
    modal True
    use navigation

    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.5

        hbox:
            vbox:
                if persistent.Sys_Langue == "ENG":
                    text "Langue" style "Style_Text_Label"
                    text "Display" style "Style_Text_Label"
                    text "Transitions" style "Style_Text_Label"
                    text "Skip after choice" style "Style_Text_Label"
                    text "Skip reading" style "Style_Text_Label"
                    text "" 
                    text "Music volume" style "Style_Text_Label"
                    text "Sound volume" style "Style_Text_Label"
                    text "Voice volume" style "Style_Text_Label"
                    text "Text Speed" style "Style_Text_Label"
                    text "Auto-Forward" style "Style_Text_Label"
                elif persistent.Sys_Langue == "VN":
                    text "Ngôn ngữ" style "Style_Text_Label"
                    text "Hiển thị" style "Style_Text_Label"
                    text "Hiệu ứng" style "Style_Text_Label"
                    text "Bỏ sau chọn" style "Style_Text_Label"
                    text "Bỏ sau đọc" style "Style_Text_Label"
                    text "" 
                    text "Nhạc nền" style "Style_Text_Label"
                    text "Tiếng động" style "Style_Text_Label"
                    text "Giọng nói" style "Style_Text_Label"
                    text "Tốc độ chữ" style "Style_Text_Label"
                    text "Tự động đọc" style "Style_Text_Label"

            text ""
            text ""
            text ""
            text ""

            vbox:
                if persistent.Sys_Langue == "ENG":
                    textbutton "VN" action SetField(persistent, "Sys_Langue", "VN") hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_Setting"
                    hbox:
                        textbutton "Window" action Preference('display', 'window') hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_Setting"
                        textbutton "Full" action Preference('display', 'fullscreen') hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_Setting"
                    hbox:
                        textbutton "All" action Preference('transitions', 'all') hovered [ Play ("test_four", "sfx/click.ogg")] style "Style_Setting"
                        textbutton "None" action Preference('transitions', 'none') hovered [ Play ("test_four", "sfx/click.ogg")] style "Style_Setting"
                    hbox:
                        textbutton "Skip" action Preference('after choices', 'skip')  hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_Setting"
                        textbutton "Stop" action Preference('after choices', 'stop')  hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_Setting"
                    hbox:
                        textbutton "All" action Preference('skip', 'all')  hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_Setting"
                        textbutton "Seen" action Preference('skip', 'seen')  hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_Setting"

                elif persistent.Sys_Langue == "VN":
                    textbutton "ENG" action SetField(persistent, "Sys_Langue", "ENG") hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_Setting"
                    hbox:
                        textbutton "Cửa sổ" action Preference('display', 'window') hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_Setting"
                        textbutton "Toàn bộ" action Preference('display', 'fullscreen') hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_Setting"
                    hbox:
                        textbutton "Tất cả" action Preference('transitions', 'all') hovered [ Play ("test_four", "sfx/click.ogg")] style "Style_Setting"
                        textbutton "Không" action Preference('transitions', 'none') hovered [ Play ("test_four", "sfx/click.ogg")] style "Style_Setting"
                    hbox:
                        textbutton "Có" action Preference('after choices', 'skip')  hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_Setting"
                        textbutton "Không" action Preference('after choices', 'stop')  hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_Setting"
                    hbox:
                        textbutton "Có" action Preference('skip', 'all')  hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_Setting"
                        textbutton "Không" action Preference('skip', 'seen')  hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_Setting"
                text ""

                vbox:
                    frame:
                        style_group "pref"
                        has vbox
                        bar value Preference("music volume")
                    frame:
                        style_group "pref"
                        has vbox
                        bar value Preference("sound volume")
                    frame:
                        style_group "pref"
                        has vbox
                        bar value Preference("voice volume")
                    frame:
                        style_group "pref"
                        has vbox
                        bar value Preference("text speed")
                    frame:
                        style_group "pref"
                        has vbox
                        bar value Preference("auto-forward time")