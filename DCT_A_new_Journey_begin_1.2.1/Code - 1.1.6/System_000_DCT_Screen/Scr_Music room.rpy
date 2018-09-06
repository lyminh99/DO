
screen music_room:   
 
    on "show" action mr.Stop()

    tag menu

    add "images/DCT/Music_room/Music_room_Gallery.png"
    add "images/DCT/Music_room/Music Box.png" at Azuicon

    imagebutton auto "images/DCT/Music_room/back_%s.png" xpos 43 ypos 895 focus_mask True action mr.Previous()
    imagebutton auto "images/DCT/Music_room/Play_%s.png" xpos 199 ypos 889 focus_mask True action mr.TogglePlay()
    imagebutton auto "images/DCT/Music_room/Forward_%s.png" xpos 297 ypos 896 focus_mask True action mr.Next()
    imagebutton auto "images/DCT/Music_room/Stopm_%s.png" xpos 116 ypos 896 focus_mask True action mr.Stop()
    imagebutton auto "images/DCT/Music_room/Random_%s.png" xpos 600 ypos 884 focus_mask True action mr.RandomPlay()
    imagebutton auto "images/DCT/Music_room/Loop_%s.png" xpos 700 ypos 882 focus_mask True action mr.ToggleLoop()
    imagebutton auto "images/DCT/Music_room/Shuffle_%s.png" xpos 800 ypos 886 focus_mask True action mr.ToggleShuffle()

    if renpy.music.get_playing("music") is not None:
        add ("%s.png" %(renpy.music.get_playing("music")[:-4])) xalign 0.05 yalign 0.05
    $ y=172 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
   
    imagebutton auto "images/DCT/Music_room/Return_%s.png" xpos 1765 ypos 817 focus_mask True action Hide ('music_room'),Show ('Sys_MainMenu2'), mr.Stop()

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
                    textbutton "000 - Joy"                          action mr.Play("Soundtracks/000 - Joy.ogg")
                    textbutton "001 - Stela Stellina"               action mr.Play("Soundtracks/001 - Dark Piano.ogg")
                    textbutton "002 - Finding"                      action mr.Play("Soundtracks/002 - Finding.ogg")
                    textbutton "003 - Sincere"                      action mr.Play("Soundtracks/003 - Sincere.ogg")
                    textbutton "004 - Lovely Bubbles"               action mr.Play("Soundtracks/004 - Lovely Bubbles.ogg")
                    textbutton "005 - Father and mother"            action mr.Play("Soundtracks/005 - Father and mother.ogg")
                    textbutton "006 - Flower blomming"              action mr.Play("Soundtracks/11 2 2014 - 2_2.mp3")
                    textbutton "007 - Memories - Composed"          action mr.Play("Soundtracks/007 - Memories - Composed.ogg")
                    textbutton "008 - Stream f life"                action mr.Play("Soundtracks/008 - Stream f life.ogg")
                    textbutton "009 - AUTUMN"                       action mr.Play("Soundtracks/AUTUMN.mp3")
                    textbutton "010 - My love like winter"          action mr.Play("Soundtracks/010 - My love like winter.ogg")
                    textbutton "011 - My childhood"                 action mr.Play("Soundtracks/011 - My childhood.ogg")
                    textbutton "012 - Confused"                     action mr.Play("Soundtracks/012 - 11 2 2013_2.mp3")
                    textbutton "013 - Question?"                    action mr.Play("Soundtracks/013 - 11 2 2013_3.mp3")                    
                    textbutton "014 - Flyin_"                       action mr.Play("Soundtracks/014 - Flyin_.mp3")                    
                    textbutton "015 - Dying World"                  action mr.Play("Soundtracks/015 - Dying World.mp3")                    
                    textbutton "016 - Winter when i can_t see you"  action mr.Play("Soundtracks/016 - Winter when i can_t see you.mp3")                    
                    textbutton "017 - The sun"                      action mr.Play("Soundtracks/017 - untitled.mp3")                    
                    textbutton "018 - Azzura theme - Slowed"        action mr.Play("Soundtracks/018 - Azzura theme - Slowed.mp3")                    
                    textbutton "019 - Azzura theme"                 action mr.Play("Soundtracks/019 - Azzura theme.mp3")                    
                    textbutton "020 - Night sky"                    action mr.Play("Soundtracks/Demo2_3.mp3") 
                    textbutton "021 - No way out"                   action mr.Play("Soundtracks/021 - 2 6 2014_2.mp3")
                    textbutton "022 - Skipping"                     action mr.Play("Soundtracks/022 - Skipping.mp3")                    

        vbar value YScrollValue("vp") bar_invert True
