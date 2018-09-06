
label Topic03:

    if CS_Emo_01 == "X":
        $ CS_Emo_01 = "Hate"
    elif CS_Emo_02 == "X":
        $ CS_Emo_02 = "Hate"
    elif CS_Emo_03 == "X":
        $ CS_Emo_03 = "Hate"
    elif CS_Emo_04 == "X":
        $ CS_Emo_04 = "Hate"

    e "Ừm, mình nghĩ là nó không hay cho lắm"
    jump CS_Start_Conversation