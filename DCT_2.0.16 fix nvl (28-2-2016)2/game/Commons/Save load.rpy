##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
## ■██▓▒░ SAVE / LOAD SLOT ░▒▓██████████████████████████████■
## This represents a load/save slot. You should customize this to ensure that the placement of the thumbnail and the slot text are as desired. Positions (x1, y1, x2 and y2) are relative to the x, y parameters, that are passed when the screen is called. To set the screenshot thumbnail size see options.rpy.
init -2 python: #we initialize x and y, so the load_save_slot screen below works at startup
    x=0
    y=0
screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot."), FileSaveName(number))
    $x1=x+790
    $y1=y+25
    add FileScreenshot(number) xpos x1 ypos y1  
    $x2=x+190
    $y2=y+50
    text file_text xpos x2 ypos y2 size 30

## ■██▓▒░ SAVE SCREEN ░▒▓███████████████████████████████████■
screen save:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/file_picker_ground.jpg" # We add the file picker background image. This image is the same for save and load screens.
    add "gui/title_save.png" # We add the save title image on top of the background
    use file_picker # We include the file_picker screen

## ■██▓▒░ LOAD SCREEN ░▒▓███████████████████████████████████■
screen load:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/file_picker_ground.jpg"
    add "gui/title_load.png"
    use file_picker

## ■██▓▒░ SAVE / LOAD FILE PICKER ░▒▓███████████████████████■
## Since saving and loading are so similar, we combine them into a single screen, file_picker. We then use the file_picker screen from simple load and save screens.
screen file_picker:
    use navigation # We include the navigation/game menu screen
    # Buttons for selecting the save/load page:
    imagebutton auto "gui/filepage1_%s.png" xpos 80 ypos 204 focus_mask True action FilePage(1) hover_sound "sfx/click.ogg"
    imagebutton auto "gui/filepage2_%s.png" xpos 80 ypos 428 focus_mask True action FilePage(2) hover_sound "sfx/click.ogg"
    imagebutton auto "gui/filepage3_%s.png" xpos 80 ypos 653 focus_mask True action FilePage(3) hover_sound "sfx/click.ogg"
    $ y=204 # ypos for the first save slot
    for i in range(0, 3): # This repeats the block below 3 times (counts from 0 to 2), for the 3 save slots. We could also copy/paste the block below 3 times, but we are too lazy to do that.
        imagebutton auto "gui/fileslot_%s.png" xpos 365 ypos y focus_mask True action FileAction(i) 
         
        use load_save_slot(number=i, x=195, y=y) # This calls the load_save_slot screen defined above. We pass variable i as the slot number and x, y coordinates.
        $ y+=225 # We increase the y variable so every next save slot is moved 124px lower.