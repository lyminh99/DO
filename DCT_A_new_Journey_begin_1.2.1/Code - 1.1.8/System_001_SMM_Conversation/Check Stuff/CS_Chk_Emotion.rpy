
label CS_Chk_Emotion:

    $ CS_Count_Normal = 0
    $ CS_Count_Love = 0
    $ CS_Count_Hate = 0
    $ CS_Count_Respect = 0
    $ CS_Group_Emotion = [CS_Emo_01, CS_Emo_02, CS_Emo_03, CS_Emo_04]

    python:    
        for Check in CS_Group_Emotion:
            if Check == "Normal":
                CS_Count_Normal += 1
            elif Check == "Love":
                CS_Count_Love += 1
            elif Check == "Hate":
                CS_Count_Hate += 1
            elif Check == "Respect":
                CS_Count_Respect += 1

    return
