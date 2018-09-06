
screen SMM_Home_Scr_GirlsStatus:
    
    tag menu
    modal True
    add "SMM_Home_BG_000"

    frame:
        align (0.2, 0.2)
        hbox:
            frame:
                vbox:
                    text "{size=24} Họ tên          : [Sys_Character_001.Name] {/size}"
                    text "{size=24} Độ thân thiết : [Sys_Character_001.Level] {/size}"
                    text "{size=24} Quý mến       : [Sys_Character_001.Love] {/size}"
                    text "{size=24} Ghét            : [Sys_Character_001.Hate] {/size}"
                    text "{size=24} Khâm phục    : [Sys_Character_001.Respect] {/size}"
                    text "{size=24} {/size}"
                    text "{size=24} {/size}"
                    add "images/SMM/Characters/Char_001.png"

#-------------------------------
            text "{size=24} {/size}"
#-------------------------------

            frame:
                vbox:
                    text "{size=24} Họ tên          : [Sys_Character_002.Name] {/size}"
                    text "{size=24} Độ thân thiết : [Sys_Character_002.Level] {/size}"
                    text "{size=24} Quý mến       : [Sys_Character_002.Love] {/size}"
                    text "{size=24} Ghét            : [Sys_Character_002.Hate] {/size}"
                    text "{size=24} Khâm phục    : [Sys_Character_002.Respect] {/size}"
                    text "{size=24} {/size}"
                    text "{size=24} {/size}"
                    add "images/SMM/Characters/Char_002.png"

#-------------------------------
            text "{size=24} {/size}"
#-------------------------------

            frame:
                vbox:
                    text "{size=24} Họ tên          : [Sys_Character_003.Name] {/size}"
                    text "{size=24} Độ thân thiết : [Sys_Character_003.Level] {/size}"
                    text "{size=24} Quý mến       : [Sys_Character_003.Love] {/size}"
                    text "{size=24} Ghét            : [Sys_Character_003.Hate] {/size}"
                    text "{size=24} Khâm phục    : [Sys_Character_003.Respect] {/size}"
                    text "{size=24} {/size}"
                    text "{size=24} {/size}"
                    add "images/SMM/Characters/Char_003.png"

#-------------------------------
            text "{size=24} {/size}"
#-------------------------------

            frame:
                vbox:
                    text "{size=24} Họ tên          : [Sys_Character_004.Name] {/size}"
                    text "{size=24} Độ thân thiết : [Sys_Character_004.Level] {/size}"
                    text "{size=24} Quý mến       : [Sys_Character_004.Love] {/size}"
                    text "{size=24} Ghét            : [Sys_Character_004.Hate] {/size}"
                    text "{size=24} Khâm phục    : [Sys_Character_004.Respect] {/size}"
                    text "{size=24} {/size}"
                    text "{size=24} {/size}"
                    add "images/SMM/Characters/Char_004.png"

    frame:
        align (0.9, 0.9)
        textbutton "{size=24} Trở lại {/size}" action Hide ("SMM_Home_Scr_GirlsStatus"), Jump("Sys_SMM_Home_Start")
