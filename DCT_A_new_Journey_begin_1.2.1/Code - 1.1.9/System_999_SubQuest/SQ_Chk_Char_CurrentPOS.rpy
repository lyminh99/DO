label SQ_Chk_Char_CurrentPOS:

    python:
        SQ_PredictTile = 0
        SQ_Move = 0
        for Chk_Map in SQ_TileMap:
            if Chk_Map.X == SQ_Character.X and Chk_Map.Y == SQ_Character.Y:
                SQ_PredictTile = Chk_Map.Type
                if Chk_Map.Type == "Exit":
                    SQ_Move = "Exit"
                elif Chk_Map.Type == "...":
                    SQ_Move = "Move"
                elif Chk_Map.Type == "X":
                    SQ_Move = "X"
                elif Chk_Map.Type != "...":
                    SQ_Move = "Notmove"

    if SQ_Move == "Exit":
        $ SQ_Exit = True
        hide screen Sys_SQ_CharPOS
        show screen Sys_SQ_CharMoving
        $ renpy.pause (SQ_Moving_Time, hard = True)
        hide screen Sys_SQ_CharMoving
        show screen Sys_SQ_CharPOS
    elif SQ_Move == "Move":
        hide screen Sys_SQ_CharPOS
        show screen Sys_SQ_CharMoving
        $ renpy.pause (SQ_Moving_Time, hard = True)
        hide screen Sys_SQ_CharMoving
        show screen Sys_SQ_CharPOS
    elif SQ_Move == "X":
        hide screen Sys_SQ_CharPOS
        show screen Sys_SQ_CharMoving
        $ renpy.pause (SQ_Moving_Time, hard = True)
        hide screen Sys_SQ_CharMoving
        show screen Sys_SQ_CharPOS
        e "Quai vat kia"
        e "Chay mau khong chet"
    elif SQ_Move == "Notmove":
        $ SQ_Character.X = SQ_Store_Character_X
        $ SQ_Character.Y = SQ_Store_Character_Y
    else:
        $ SQ_Character.X = SQ_Store_Character_X
        $ SQ_Character.Y = SQ_Store_Character_Y

    return
