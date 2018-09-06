
label SQ_Chk_FacedTile:
    python:
        for Chk_NPC in SQ_TileMap:
            if Chk_NPC.X == SQ_Store_Character_X and Chk_NPC.Y == SQ_Store_Character_Y:
                SQ_PredictTile = Chk_NPC.Type
                if Chk_NPC.Type == "NPC":
                    SQ_Char_Meet = "NPC"

    if SQ_Char_Meet == "NPC":
        e "Hello !"
        e "May i help you ?"

    return