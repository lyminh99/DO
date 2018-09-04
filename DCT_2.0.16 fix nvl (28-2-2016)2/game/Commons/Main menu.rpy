init:
    $ Main_menu_001 = Hide('main_menu'), ShowMenu('load')
    $ Main_menu_002 = Hide('main_menu'), ShowMenu('preferences')
    $ Main_menu_003 = Hide('main_menu'), ShowMenu('main_menu2')
    $ Main_menu_004 = Hide("main_menu2"), ShowMenu("cg_gallery")
    $ Main_menu_005 = Hide('main_menu2'), ShowMenu("music_room")
    $ Main_menu_006 = Hide('main_menu2'), ShowMenu("databaseAzu")
    $ Main_menu_007 = Hide('main_menu2'), ShowMenu("main_menu")
    $ Main_menu_001 = Hide('main_menu'), ShowMenu('load')
    $ Main_menu_001 = Hide('main_menu'), ShowMenu('load')


screen main_menu:
    tag menu # This ensures that any other menu screen is replaced.

    add "Images/Themes/Screen_title.jpg"
    add "Images/Themes/DCT_tittle.png" at left_to_right

    $ y=370 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start_%s.png" xpos 1473 ypos y focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.ogg")] at main_eff1
    
    $ y+=101 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185

    imagebutton auto "gui/main_load_%s.png" xpos 1473 ypos y focus_mask True  action Main_menu_001 hovered [ Play ("test_two", "sfx/click.ogg")] at main_eff2
    $ y+=101

    imagebutton auto "gui/main_config_%s.png" xpos 1473 ypos y focus_mask True action Main_menu_002 hovered [ Play ("test_three", "sfx/click.ogg")] at main_eff3
    $ y+=101

    imagebutton auto "gui/main_extras_%s.png" xpos 1473 ypos y focus_mask True action Main_menu_003 hovered [ Play ("test_four", "sfx/click.ogg")] at main_eff4

    $ y+=101
    imagebutton auto "gui/main_quit_%s.png" xpos 1473 ypos y focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.ogg") ] at main_eff5


screen main_menu2:
    tag menu # This ensures that any other menu screen is replaced.


    add "Images/Themes/Screen_title.jpg"
    add "Images/Themes/DCT_tittle.png" at left_to_right

    $ y=370 # 
    
    imagebutton auto "gui/main_gallery_%s.png" xpos 1473 ypos y focus_mask True action Main_menu_004 hovered [ Play ("test_four", "sfx/click.ogg")] at main_eff4
    $ y+=101
    imagebutton auto "gui/main_music_room_%s.png" xpos 1473 ypos y focus_mask True action Main_menu_005 hovered [ Play ("test_four", "sfx/click.ogg")] at main_eff4
    $ y+=101
    imagebutton auto "gui/Menu_Extra_Profile/Main_Extras_Profiles_%s.png" xpos 1473 ypos y focus_mask True action Main_menu_006 hovered [ Play ("test_four", "sfx/click.ogg")] at main_eff4
    $ y+=201
    imagebutton auto "gui/main_quit_%s.png" xpos 1473 ypos y focus_mask True action Main_menu_007 hovered [ Play ("test_five", "sfx/click.ogg") ] at main_eff5
