
label Topic01:

    if CS_Emo_01 == "X":
        $ CS_Emo_01 = "Normal"
    elif CS_Emo_02 == "X":
        $ CS_Emo_02 = "Normal"
    elif CS_Emo_03 == "X":
        $ CS_Emo_03 = "Normal"
    elif CS_Emo_04 == "X":
        $ CS_Emo_04 = "Normal"

    e "Cũng thú vị đó"
    jump CS_Start_Conversation