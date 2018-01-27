##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    on "show" action Play("sound", "sfx/alert.ogg")
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.

    #add "gui/yesno_ground.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        vbox:
            if Sys_Langue == "ENG":
                if message == layout.ARE_YOU_SURE:
                    text "{size=50}Are you sure{/size}":
                        xalign 0.5
                elif message == layout.DELETE_SAVE:
                    text "{size=50}Delete save{/size}":
                        xalign 0.5
                elif message == layout.OVERWRITE_SAVE:
                    text "{size=50}Overwrite save{/size}":
                        xalign 0.5
                elif message == layout.LOADING:
                    text "{size=50}Loading{/size}":
                        xalign 0.5
                elif message == layout.QUIT:
                    text "{size=50}Do you want to quit{/size}":
                        xalign 0.5
                elif message == layout.MAIN_MENU:
                    text "{size=50}Return Main menu{/size}":
                        xalign 0.5

                text ""

                textbutton "Yes" action yes_action hover_sound "sfx/click.ogg" style "Style_MainMenu":
                    xalign 0.5
                textbutton "No" action no_action hover_sound "sfx/click.ogg" style "Style_MainMenu":
                    xalign 0.5

            elif Sys_Langue == "VN":
                if message == layout.ARE_YOU_SURE:
                    text "{size=50}Bạn chắc chứ{/size}":
                        xalign 0.5
                elif message == layout.DELETE_SAVE:
                    text "{size=50}Xóa dữ liệu lưu{/size}":
                        xalign 0.5
                elif message == layout.OVERWRITE_SAVE:
                    text "{size=50}Ghi đè dữ liệu lưu{/size}":
                        xalign 0.5
                elif message == layout.LOADING:
                    text "{size=50}Bạn muốn tải chứ{/size}":
                        xalign 0.5
                elif message == layout.QUIT:
                    text "{size=50}Bạn có muốn thoát không{/size}":
                        xalign 0.5
                elif message == layout.MAIN_MENU:
                    text "{size=50}Trở về Trang chính{/size}":
                        xalign 0.5

                text ""

                textbutton "Có" action yes_action hover_sound "sfx/click.ogg" style "Style_MainMenu":
                    xalign 0.5
                textbutton "Không" action no_action hover_sound "sfx/click.ogg" style "Style_MainMenu":
                    xalign 0.5

