
screen music_room:      
    tag menu
    add "images/Themes/Music_room_Gallery.png"
    add "Gui/Music_room/Music Box.png" at Azuicon
    imagebutton auto "Gui/Music_room/back_%s.png" xpos 43 ypos 895 focus_mask True action mr.Previous() hovered [ Play ("test_one", "sfx/click.ogg")] 
    imagebutton auto "Gui/Music_room/Play_%s.png" xpos 199 ypos 889 focus_mask True action mr.TogglePlay() hovered [ Play ("test_one", "sfx/click.ogg")] 
    imagebutton auto "Gui/Music_room/Forward_%s.png" xpos 297 ypos 896 focus_mask True action mr.Next() hovered [ Play ("test_one", "sfx/click.ogg")] 
    imagebutton auto "Gui/Music_room/Stopm_%s.png" xpos 116 ypos 896 focus_mask True action [mr.Stop(), Show("gui_tooltip", my_picture="gui/Stop.png", my_tt_xpos=46, my_tt_ypos=968)] hovered [ Play ("test_one", "sfx/click.ogg")] 
    imagebutton auto "Gui/Music_room/Random_%s.png" xpos 600 ypos 884 focus_mask True action mr.RandomPlay() hovered [ Play ("test_one", "sfx/click.ogg")] 
    imagebutton auto "Gui/Music_room/Loop_%s.png" xpos 700 ypos 882 focus_mask True action mr.ToggleLoop() hovered [ Play ("test_one", "sfx/click.ogg")] 
    imagebutton auto "Gui/Music_room/Shuffle_%s.png" xpos 800 ypos 886 focus_mask True action mr.ToggleShuffle() hovered [ Play ("test_one", "sfx/click.ogg")] 
    imagebutton auto "Gui/Music_room/Return_%s.png" xpos 1765 ypos 817 focus_mask True action Hide ('music_room'),Return() hovered [ Play ("test_one", "sfx/click.ogg")] 
    
    if renpy.music.get_playing("music") is not None:
        add ("%s.png" %(renpy.music.get_playing("music")[:-4])) xpos 50 ypos 58
    $ y=344 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    
    
####################################################################### Column 1

   # frame: #these positioning changes depending on your layout
    #    style_group "mm"
    #    xpos 50
    #    ypos 180
    #    background None
    #    has vbox:
    #        xalign 0.0 
    #        yalign 0.0

        # The buttons that play each track.  MUST CORRESPOND TO THE TRACK LIST ABOVE
        #textbutton "000 - Joy" action mr.Play("Soundtracks/000 - Joy.ogg")
        #textbutton "000 - Opening song theme" action mr.Play("Soundtracks/000 - Opening song theme.ogg")

####################################################################### Column 2

    frame: #these positioning changes depending on your layout
        style_group "mm"
        xpos 180
        ypos 180
        background None
        has side "c r":
            area (0, 0, 1000, 550)
            viewport id "vp":
                draggable True
                mousewheel True
                #yadjustment ui.adjustment (value=99999, range=99999)
                has vbox:
                    xalign 0.0 
                    yalign 0.0

        # The buttons that play each track.  MUST CORRESPOND TO THE TRACK LIST ABOVE
                    textbutton "000 - Joy" action mr.Play("Soundtracks/000 - Joy.ogg")
                    textbutton "001 - Stela Stellina" action mr.Play("Soundtracks/001 - Dark Piano.ogg")
                    textbutton "002 - Finding" action mr.Play("Soundtracks/002 - Finding.ogg")
                    textbutton "003 - Sincere" action mr.Play("Soundtracks/003 - Sincere.ogg")
                    textbutton "004 - Lovely Bubbles" action mr.Play("Soundtracks/004 - Lovely Bubbles.ogg")
                    textbutton "005 - Father and mother" action mr.Play("Soundtracks/005 - Father and mother.ogg")
                    textbutton "006 - Flower blomming" action mr.Play("Soundtracks/11 2 2014 - 2_2.mp3")
                    textbutton "007 - Memories - Composed" action mr.Play("Soundtracks/007 - Memories - Composed.ogg")
                    textbutton "008 - Stream f life" action mr.Play("Soundtracks/008 - Stream f life.ogg")
                    textbutton "009 - AUTUMN" action mr.Play("Soundtracks/AUTUMN.mp3")
                    textbutton "010 - My love like winter" action mr.Play("Soundtracks/010 - My love like winter.mp3")
                    textbutton "011 - My childhood" action mr.Play("Soundtracks/011 - My childhood.ogg")
                    textbutton "012 - Confused" action mr.Play("Soundtracks/012 - 11 2 2013_2.mp3")
                    textbutton "013 - Question?" action mr.Play("Soundtracks/013 - 11 2 2013_3.mp3")                    
                    textbutton "014 - Flyin_" action mr.Play("Soundtracks/014 - Flyin_.mp3")                    
                    textbutton "015 - Dying World" action mr.Play("Soundtracks/015 - Dying World.mp3")                    
                    textbutton "016 - Winter when i can_t see you" action mr.Play("Soundtracks/016 - Winter when i can_t see you.mp3")                    
                    textbutton "017 - The sun" action mr.Play("Soundtracks/017 - untitled.mp3")                    
                    textbutton "018 - Azzura theme - Slowed" action mr.Play("Soundtracks/018 - Azzura theme - Slowed.mp3")                    
                    textbutton "019 - Azzura theme" action mr.Play("Soundtracks/019 - Azzura theme.mp3")                    
                    textbutton "020 - Night sky" action mr.Play("Soundtracks/Demo2_3.mp3") 
                    textbutton "021 - No way out" action mr.Play("Soundtracks/021 - 2 6 2014_2.mp3")
                    textbutton "022 - Skipping" action mr.Play("Soundtracks/022 - Skipping.mp3")                    


        vbar value YScrollValue("vp") bar_invert True

####################################################################### Column 3    

    frame: #these positioning changes depending on your layout
        style_group "mm"
        xpos 910
        ypos 180
        background None
        has vbox:
            xalign 0.0 
            yalign 0.0

        # The buttons that play each track.  MUST CORRESPOND TO THE TRACK LIST ABOVE
        #textbutton "END - Farewell" action mr.Play("Soundtracks/END - Farewell.ogg")

####################################################################### Button

        
    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "Soundtracks/000 - Joy.ogg")

####################################################################### Starting music

    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "Soundtracks/000 - Joy.ogg")