
label Topic05:

    if CS_Emo_01 == "X":
        $ CS_Emo_01 = "Love"
    elif CS_Emo_02 == "X":
        $ CS_Emo_02 = "Love"
    elif CS_Emo_03 == "X":
        $ CS_Emo_03 = "Love"
    elif CS_Emo_04 == "X":
        $ CS_Emo_04 = "Love"

    e "Thật thế sao ? Còn gì nữa ? Cậu kể tiếp đi"
    jump CS_Start_Conversation