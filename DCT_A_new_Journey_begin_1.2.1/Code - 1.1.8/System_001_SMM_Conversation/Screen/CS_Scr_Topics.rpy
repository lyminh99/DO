init:
    $ CS_Topic01_Picked = Hide ("CS_Scr_Topics"), Jump ("Topic01")
    $ CS_Topic02_Picked = Hide ("CS_Scr_Topics"), Jump ("Topic02")
    $ CS_Topic03_Picked = Hide ("CS_Scr_Topics"), Jump ("Topic03")
    $ CS_Topic04_Picked = Hide ("CS_Scr_Topics"), Jump ("Topic04")
    $ CS_Topic05_Picked = Hide ("CS_Scr_Topics"), Jump ("Topic05")
    $ CS_Attack_Picked = Hide ("CS_Scr_Topics"), Jump ("CS_Attack")

screen CS_Scr_Topics:
    tag menu
    modal True

    frame:
        align (0.5,0.9)
        hbox:
            textbutton "{size=20} Topic_01 {/size}" action CS_Topic01_Picked
            textbutton "{size=20} Topic_02 {/size}" action CS_Topic02_Picked
            textbutton "{size=20} Topic_03 {/size}" action CS_Topic03_Picked
            textbutton "{size=20} Topic_04 {/size}" action CS_Topic04_Picked
            textbutton "{size=20} Topic_05 {/size}" action CS_Topic05_Picked
            if CS_AtkLevel > 0:
                textbutton "{size=20} Attack [CS_AtkLevel] {/size}" action CS_Attack_Picked