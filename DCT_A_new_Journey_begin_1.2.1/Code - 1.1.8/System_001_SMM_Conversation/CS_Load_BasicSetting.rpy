
label CS_Load_BasicSetting:

    python:
        class CS_Topics:
            def __init__(self, a1, a2):
                self.CS_Tpc_Repeat = a1
                self.CS_Tpc_Plot = a2

        CS_Topic01 = CS_Topics (0,0)
        CS_Topic02 = CS_Topics (0,0)
        CS_Topic03 = CS_Topics (0,0)
        CS_Topic04 = CS_Topics (0,0)
        CS_Topic05 = CS_Topics (0,0)

    define CS_Turn = 0
    define CS_MaxTurn = 5

    define CS_Place = 0
    define CS_Char = 0
    define CS_Staus = 0
    define CS_Level = 0
    define CS_AtkLevel = 0

    define CS_Emo_01 = "X"
    define CS_Emo_02 = "X"
    define CS_Emo_03 = "X"
    define CS_Emo_04 = "X"

    define CS_Count_Normal = 0
    define CS_Count_Love = 0
    define CS_Count_Hate = 0
    define CS_Count_Respect = 0

    define CS_Char_level = 0
    define CS_Char_Point_Hate = 0
    define CS_Char_Point_Love = 0
    define CS_Char_Point_Respect = 0

    return