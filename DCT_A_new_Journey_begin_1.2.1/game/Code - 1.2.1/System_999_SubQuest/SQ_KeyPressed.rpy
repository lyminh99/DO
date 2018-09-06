
label Key_Pressed:

#-----------------------------------------------------------
    if Key_Pressed == "LEFT":
#-----------------------------------------------------------
        $ SQ_Character.N = 0
        $ SQ_Character.S = 0
        $ SQ_Character.W = 1
        $ SQ_Character.E = 0
        $ SQ_Store_Character_X = SQ_Character.X
        $ SQ_Store_Character_Y = SQ_Character.Y
        $ SQ_Character.X -= SQ_TileSpace
        call SQ_Chk_Char_CurrentPOS
#-----------------------------------------------------------
    elif Key_Pressed == "RIGHT":
#-----------------------------------------------------------
        $ SQ_Character.N = 0
        $ SQ_Character.S = 0
        $ SQ_Character.W = 0
        $ SQ_Character.E = 1
        $ SQ_Store_Character_X = SQ_Character.X
        $ SQ_Store_Character_Y = SQ_Character.Y
        $ SQ_Character.X += SQ_TileSpace
        call SQ_Chk_Char_CurrentPOS
#-----------------------------------------------------------
    elif Key_Pressed == "DOWN":
#-----------------------------------------------------------
        $ SQ_Character.N = 0
        $ SQ_Character.S = 1
        $ SQ_Character.W = 0
        $ SQ_Character.E = 0
        $ SQ_Store_Character_X = SQ_Character.X
        $ SQ_Store_Character_Y = SQ_Character.Y
        $ SQ_Character.Y += SQ_TileSpace
        call SQ_Chk_Char_CurrentPOS
#-----------------------------------------------------------
    elif Key_Pressed == "UP":
#-----------------------------------------------------------
        $ SQ_Character.N = 1
        $ SQ_Character.S = 0
        $ SQ_Character.W = 0
        $ SQ_Character.E = 0
        $ SQ_Store_Character_X = SQ_Character.X
        $ SQ_Store_Character_Y = SQ_Character.Y
        $ SQ_Character.Y -= SQ_TileSpace
        call SQ_Chk_Char_CurrentPOS
#-----------------------------------------------------------
    elif Key_Pressed == "E":
#-----------------------------------------------------------
        $ SQ_Char_Meet = 0
        $ SQ_Store_Character_X = SQ_Character.X
        $ SQ_Store_Character_Y = SQ_Character.Y
        if SQ_Character.W == 1:
            $ SQ_Store_Character_X -= SQ_TileSpace
            call SQ_Chk_FacedTile
        elif SQ_Character.E == 1:
            $ SQ_Store_Character_X += SQ_TileSpace
            call SQ_Chk_FacedTile
        elif SQ_Character.S == 1:
            $ SQ_Store_Character_Y += SQ_TileSpace
            call SQ_Chk_FacedTile
        elif SQ_Character.N == 1:
            $ SQ_Store_Character_Y -= SQ_TileSpace
            call SQ_Chk_FacedTile
#-----------------------------------------------------------
    $ renpy.pause (0.05, hard = True)
    jump SQ_MainLabel

