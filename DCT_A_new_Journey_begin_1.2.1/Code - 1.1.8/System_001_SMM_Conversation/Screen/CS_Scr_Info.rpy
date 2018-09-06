
screen CS_Scr_Info:

    frame:
        align (0.1,0.1)
        hbox:
            text "{size=30} [CS_Emo_01] {/size}"
            text "{size=30} [CS_Emo_02] {/size}"
            text "{size=30} [CS_Emo_03] {/size}"
            text "{size=30} [CS_Emo_04] {/size}"


    frame:
        align (0.9,0.1)
        vbox:
            text "{size=20} Turn: [CS_Turn]/[CS_MaxTurn] {/size}"
            text "{size=20} Status: [CS_Staus] {/size}"
            text "{size=20} Char: [CS_Char] {/size}"
            text "{size=20} Place: [CS_Place] {/size}"
            text "{size=20} Level: [CS_Level] {/size}"
            text "{size=20} AtkLevel: [CS_AtkLevel] {/size}"

    frame:
        align (0.1,0.2)
        vbox:
            text "{size=20} Normal: [CS_Count_Normal] {/size}"
            text "{size=20} Love: [CS_Count_Love] {/size}"
            text "{size=20} Hate: [CS_Count_Hate] {/size}"
            text "{size=20} Respect: [CS_Count_Respect] {/size}"
            text "{size=20} --------- {/size}"
            text "{size=20} Love Point: [CS_Char_Point_Love] {/size}"
            text "{size=20} Hate Point: [CS_Char_Point_Hate] {/size}"
            text "{size=20} Respect Point: [CS_Char_Point_Respect] {/size}"