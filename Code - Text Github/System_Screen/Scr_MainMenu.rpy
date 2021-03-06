﻿init -2:

#----------------------------------------------------------

    transform Top_to_Bottom:
        yalign 0.0
        xalign 0.0
        linear 20.0 yalign 1.0
    
    transform Left_to_Right:
        yalign 0.0
        xalign 0.8
        alpha 0.0
        linear 2.0 xalign 0.9 alpha 1.0
    #style Style_MainMenu is default

#----------------------------------------------------------

    style Style_MainMenu is button_text:
        clear
    style Style_MainMenu is button:
        xpadding 0
        ypadding 0
        #xmargin 0
        #ymargin 0
        xminimum int(300)
        xmaximum int(300)
        yminimum int(60)
        ymaximum int(60)
    style Style_MainMenu_text:
        size 40
        xalign 0.5
        yalign 0.5
        insensitive_color "#afafaf"
        idle_color "#ffffff"
        hover_color "#ffffff"
        selected_idle_color "#ffb600"
        selected_hover_color "#ffb600"

init:

    $ Sys_Mmenu_But01 = ShowMenu('load')
    $ Sys_Mmenu_But02 = ShowMenu('Scr_Setting')    
    $ Sys_Mmenu_But03 = Hide('main_menu'), Show('Sys_MainMenu2')
    $ Sys_Mmenu_But04 = Hide("Sys_MainMenu2"), Show("cg_gallery")
    $ Sys_Mmenu_But05 = Hide('Sys_MainMenu2'), Show("music_room")
    $ Sys_Mmenu_But06 = Hide('Sys_MainMenu2'), Show("databaseAzu")
    $ Sys_Mmenu_But07 = Hide('Sys_MainMenu2'), Show("main_menu")    
    $ Sys_Mmenu_But08 = SetVariable ("Sys_Current_Game", "DCT")
    $ Sys_Mmenu_But09 = SetVariable ("Sys_Current_Game", "SMM")
    
#, Play("Soundtracks/001 - SMM/001 - Summer Melody.mp3")
#, Play("Soundtracks/004 - Lovely Bubbles.ogg") 

    transform Eft_MM_BG:
        xalign 0.0
        yalign 0.0
        alpha 0.0

        linear 3.0 xalign 0.1 alpha 1.0
        linear 30.0 xalign 0.9
        linear 3.0 xalign 1.0 alpha 0.0
        repeat
        #easein 10 align(1,0)

screen main_menu:

    tag menu
    if Sys_Current_Game == "DCT":
        use Sys_DCT_MainMenu_BG
    elif Sys_Current_Game == "SMM":
        use Sys_SMM_MainMenu_BG
        
    frame:
        xalign .98
        yalign .98
        vbox:

            if Sys_Langue == "ENG":
                if Sys_Current_Game == "DCT":
                    textbutton _("Summer Melody") action Sys_Mmenu_But09, mr.Play("Soundtracks/001 - SMM/001 - Summer Melody.mp3") style "Style_MainMenu"
                elif Sys_Current_Game == "SMM":
                    textbutton _("At the Horizon") action Sys_Mmenu_But08, mr.Play("Soundtracks/004 - Lovely Bubbles.ogg") style "Style_MainMenu"

                textbutton _("Start Game") action Start() style "Style_MainMenu"
                textbutton _("Load Game") action Sys_Mmenu_But01 style "Style_MainMenu"
                textbutton _("Config") action Sys_Mmenu_But02 style "Style_MainMenu"
                textbutton _("Extras") action Sys_Mmenu_But03 style "Style_MainMenu"
                textbutton _("")
                textbutton _("Quit") action Quit(confirm=False) style "Style_MainMenu"

            elif Sys_Langue == "VN":
                if Sys_Current_Game == "DCT":
                    textbutton _("Giai điệu mùa hè") action Sys_Mmenu_But09, mr.Play("Soundtracks/001 - SMM/001 - Summer Melody.mp3") style "Style_MainMenu"
                elif Sys_Current_Game == "SMM":
                    textbutton _("Đường chân trời") action Sys_Mmenu_But08, mr.Play("Soundtracks/004 - Lovely Bubbles.ogg") style "Style_MainMenu"

                textbutton _("Bắt đầu") action Start() style "Style_MainMenu"
                textbutton _("Nhật kí") action Sys_Mmenu_But01 style "Style_MainMenu"
                textbutton _("Nhà bếp") action Sys_Mmenu_But02 style "Style_MainMenu"
                textbutton _("Thư viện") action Sys_Mmenu_But03 style "Style_MainMenu"
                textbutton _("")
                textbutton _("Thoát") action Quit(confirm=False) style "Style_MainMenu"

screen Sys_MainMenu2:

    tag menu
    if Sys_Current_Game == "DCT":
        use Sys_DCT_MainMenu_BG
    elif Sys_Current_Game == "SMM":
        use Sys_SMM_MainMenu_BG

    frame:
        xalign .98
        yalign .98
        vbox:

            if Sys_Langue == "ENG":
                textbutton _("Gallery")      action Sys_Mmenu_But04 style "Style_MainMenu"
                textbutton _("Music room")   action Sys_Mmenu_But05 style "Style_MainMenu"
                textbutton _("Profiles")     action Sys_Mmenu_But06 style "Style_MainMenu"
                textbutton _("")
                textbutton _("Return")       action Sys_Mmenu_But07 style "Style_MainMenu"

            elif Sys_Langue == "VN":
                textbutton _("Phòng tranh")  action Sys_Mmenu_But04 style "Style_MainMenu"
                textbutton _("Phòng nhạc")   action Sys_Mmenu_But05 style "Style_MainMenu"
                textbutton _("Sổ tay")       action Sys_Mmenu_But06 style "Style_MainMenu"
                textbutton _("")
                textbutton _("Quay lại")     action Sys_Mmenu_But07 style "Style_MainMenu"

screen Sys_DCT_MainMenu_BG:

    on "show":
        if renpy.music.get_playing("music") is None:
            if Sys_Current_Game == "DCT":
                action mr.Play("Soundtracks/004 - Lovely Bubbles.ogg")
            elif Sys_Current_Game == "SMM":
                action mr.Play("Soundtracks/001 - SMM/001 - Summer Melody.mp3")
    add "DCT_Screen_title"
    add "DCT_tittle" at Left_to_Right

screen Sys_SMM_MainMenu_BG:

    on "show":
        if renpy.music.get_playing("music") is None:
            if Sys_Current_Game == "DCT":
                action mr.Play("Soundtracks/004 - Lovely Bubbles.ogg")
            elif Sys_Current_Game == "SMM":
                action mr.Play("Soundtracks/001 - SMM/001 - Summer Melody.mp3")

    add "SMM_Screen_title" at Top_to_Bottom
    add "SMM_tittle" at Left_to_Right