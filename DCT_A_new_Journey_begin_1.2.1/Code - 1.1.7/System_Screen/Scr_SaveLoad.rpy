##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
# ■██▓▒░ SAVE / LOAD SLOT ░▒▓██████████████████████████████■

init -2 python: #we initialize x and y, so the load_save_slot screen below works at startup
    x=0
    y=0

screen load_save_slot:

    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot."), FileSaveName(number))
    add FileScreenshot(number)
    text file_text size 30

screen save:

    add ('black') alpha 0.8
    modal True
    use file_picker

    frame:
        xalign 0.5
        yalign 0.1
        text "{size=50}Save{/size}"


    vbox:
        xalign .01
        yalign .96
        if persistent.Sys_Langue == "ENG":
            textbutton "Save" action Hide ('load'), Show('save') hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_SettingMenu"
            textbutton "Load" action Hide ('save'), Show ('load') hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_SettingMenu"
            textbutton "Return" action Hide ('save'), Hide ('load'), Return() hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_SettingMenu"
        elif persistent.Sys_Langue == "VN":
            textbutton "Lưu" action Hide ('load'), Show('save') hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_SettingMenu"
            textbutton "Tải" action Hide ('save'), Show ('load') hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_SettingMenu"
            textbutton "Trở về" action Hide ('save'), Hide ('load'), Return() hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_SettingMenu"


screen load:

    add ('black') alpha 0.8
    modal True
    use file_picker

    frame:
        xalign 0.5
        yalign 0.1
        text "{size=50}Load{/size}"

    vbox:
        xalign .01
        yalign .96
        if persistent.Sys_Langue == "ENG":
            textbutton "Save" action Hide ('load'), Show('save') hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_SettingMenu"
            textbutton "Load" action Hide ('save'), Show ('load') hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_SettingMenu"
            textbutton "Return" action Hide ('save'), Hide ('load'), Return() hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_SettingMenu"
        elif persistent.Sys_Langue == "VN":
            textbutton "Lưu" action Hide ('load'), Show('save') hovered [ Play ("test_one", "sfx/click.ogg")] style "Style_SettingMenu"
            textbutton "Tải" action Hide ('save'), Show ('load') hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_SettingMenu"
            textbutton "Trở về" action Hide ('save'), Hide ('load'), Return() hovered [ Play ("test_two", "sfx/click.ogg")] style "Style_SettingMenu"

screen file_picker():

    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.5
        vbox:
            vbox:
                for i in range(0, 3): # This repeats the block below 3 times (counts from 0 to 2), for the 3 save slots. We could also copy/paste the block below 3 times, but we are too lazy to do that.
                    hbox:
                        textbutton "Save data" action FileAction(i) style "Style_SettingMenu"
                        use load_save_slot(number=i) # This calls the load_save_slot screen defined above. We pass variable i as the slot number and x, y coordinates.

            hbox:
                if persistent.Sys_Langue == "ENG":
                    textbutton "Page 001" action FilePage(1) hover_sound "sfx/click.ogg" style "Style_SettingMenu"
                    textbutton "Page 002" action FilePage(2) hover_sound "sfx/click.ogg" style "Style_SettingMenu"
                    textbutton "Page 003" action FilePage(3) hover_sound "sfx/click.ogg" style "Style_SettingMenu"
                elif persistent.Sys_Langue == "VN":
                    textbutton "Trang 001" action FilePage(1) hover_sound "sfx/click.ogg" style "Style_SettingMenu"
                    textbutton "Trang 002" action FilePage(2) hover_sound "sfx/click.ogg" style "Style_SettingMenu"
                    textbutton "Trang 003" action FilePage(3) hover_sound "sfx/click.ogg" style "Style_SettingMenu"

                #$ y=204 # ypos for the first save slot