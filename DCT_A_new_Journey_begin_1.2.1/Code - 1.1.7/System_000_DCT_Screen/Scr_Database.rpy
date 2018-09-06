
screen databaseEle:

    add "images/DCT/Database/BG.png" # We add the image that is shown in the background of the preferences screen.
    add "images/DCT/Database/Elenatext.png" at Azuicon
    add "images/DCT/Database/ElenaPose2.png"
    add "images/DCT/Database/TextdesEle.png" at Azuicon
    
     # We include the navigation screen (game menu)
    # Display windowed/full screen:
    imagebutton auto "images/DCT/Database/Azu_Icon_%s.png" xpos 660 ypos 16 focus_mask True action Hide ('databaseEle'), Show('databaseAzu') at config_eff
    imagebutton auto "images/DCT/Database/Ele_Icon_%s.png" xpos 500 ypos 16 focus_mask True action NullAction() at config_eff
    imagebutton auto "images/DCT/Database/ElenaPose_%s.png" focus_mask True action NullAction() at Eleicon

    if persistent.Sys_Langue == "ENG":
        textbutton "Return" action Hide ('databaseEle'), Show ('Sys_MainMenu2') xalign 0.98 yalign 0.96 style "Style_MainMenu"
    elif persistent.Sys_Langue == "VN":
        textbutton "Trở lại" action Hide ('databaseEle'), Show ('Sys_MainMenu2') xalign 0.98 yalign 0.96 style "Style_MainMenu"

########################################################################

screen databaseAzu:

    add "images/DCT/Database/BG.png" # We add the image that is shown in the background of the preferences screen.
    add "images/DCT/Database/Azutext.png" at Azuicon
    add "images/DCT/Database/AzuPose2.png" 
    add "images/DCT/Database/TextdesAzu.png" at Azuicon
    
     # We include the navigation screen (game menu)
    # Display windowed/full screen:
    imagebutton auto "images/DCT/Database/Azu2_Icon_%s.png" xpos 660 ypos 16 focus_mask True action NullAction() at config_eff
    imagebutton auto "images/DCT/Database/Ele2_Icon_%s.png" xpos 500 ypos 16 focus_mask True action Hide ('databaseAzu'), ShowMenu('databaseEle') at config_eff
    imagebutton auto "images/DCT/Database/AzuPose_%s.png" focus_mask True action NullAction() at Eleicon

    if persistent.Sys_Langue == "ENG":
        textbutton "Return" action Hide ('databaseAzu'), Show ('Sys_MainMenu2') xalign 0.98 yalign 0.96 style "Style_MainMenu"
    elif persistent.Sys_Langue == "VN":
        textbutton "Trở lại" action Hide ('databaseAzu'), Show ('Sys_MainMenu2') xalign 0.98 yalign 0.96 style "Style_MainMenu"
    


