
screen databaseEle:
    tag menu # This ensures that any other menu screen is replaced.
    add "Database/BG.png" # We add the image that is shown in the background of the preferences screen.
    add "Database/Elenatext.png" at Azuicon
    add "Database/ElenaPose2.png"
    add "Database/TextdesEle.png" at Azuicon
    
     # We include the navigation screen (game menu)
    # Display windowed/full screen:
    imagebutton auto "Database/Azu_Icon_%s.png" xpos 660 ypos 16 focus_mask True action ShowMenu('databaseAzu') hovered [ Play ("test_two", "sfx/click.ogg")] at config_eff
    imagebutton auto "Database/Ele_Icon_%s.png" xpos 500 ypos 16 focus_mask True action NullAction() hovered [ Play ("test_two", "sfx/click.ogg")] at config_eff
    imagebutton auto "Database/Return_%s.png" xpos 1750 ypos 946 focus_mask True action Hide ('databaseEle'), Hide ('databaseAzu'), ShowMenu("main_menu2") hovered [ Play ("test_two", "sfx/click.ogg")]
    imagebutton auto "Database/ElenaPose_%s.png" focus_mask True action NullAction() at Eleicon

########################################################################

screen databaseAzu:
    tag menu # This ensures that any other menu screen is replaced.
    add "Database/BG.png" # We add the image that is shown in the background of the preferences screen.
    add "Database/Azutext.png" at Azuicon
    add "Database/AzuPose2.png" 
    add "Database/TextdesAzu.png" at Azuicon
    
     # We include the navigation screen (game menu)
    # Display windowed/full screen:
    imagebutton auto "Database/Azu2_Icon_%s.png" xpos 660 ypos 16 focus_mask True action NullAction() hovered [ Play ("test_two", "sfx/click.ogg")] at config_eff
    imagebutton auto "Database/Ele2_Icon_%s.png" xpos 500 ypos 16 focus_mask True action ShowMenu('databaseEle') hovered [ Play ("test_two", "sfx/click.ogg")] at config_eff
    imagebutton auto "Database/Return_%s.png" xpos 1750 ypos 946 focus_mask True action Hide ('databaseEle'), Hide ('databaseAzu'), ShowMenu("main_menu2") hovered [ Play ("test_two", "sfx/click.ogg")]
    imagebutton auto "Database/AzuPose_%s.png" focus_mask True action NullAction() at Eleicon

    


