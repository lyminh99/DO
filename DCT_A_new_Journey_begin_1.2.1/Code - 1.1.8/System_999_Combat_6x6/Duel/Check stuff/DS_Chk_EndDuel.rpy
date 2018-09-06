label DS_Chk_EndDuel:

#---------------------------------------------------------------------------------
    if DS_A_HP <= 0:
#---------------------------------------------------------------------------------
        if DS_Attacker == "Led_A_S1":
            $ A_S1_HP = 0
            $ Led_A_S1_HP = 0
            $ A_S1_CanDuel = "Loser"
        elif DS_Attacker == "Led_A_S2":
            $ A_S2_HP = 0
            $ Led_A_S2_HP = 0
            $ A_S2_CanDuel = "Loser"
        elif DS_Attacker == "Led_A_S3":
            $ A_S3_HP = 0
            $ Led_A_S3_HP = 0
            $ A_S3_CanDuel = "Loser"
        elif DS_Attacker == "Led_A_S4":
            $ A_S4_HP = 0
            $ Led_A_S4_HP = 0
            $ A_S4_CanDuel = "Loser"
        elif DS_Attacker == "Led_A_S5":
            $ A_S5_HP = 0
            $ Led_A_S5_HP = 0
            $ A_S5_CanDuel = "Loser"
        elif DS_Attacker == "Led_A_S6":
            $ A_S6_HP = 0
            $ Led_A_S6_HP = 0
            $ A_S6_CanDuel = "Loser"
        if DS_Deffender == "Led_D_S1":
            $ D_S1_CanDuel = "Winner"
        elif DS_Deffender == "Led_D_S2":
            $ D_S2_CanDuel = "Winner"
        elif DS_Deffender == "Led_D_S3":
            $ D_S3_CanDuel = "Winner"
        elif DS_Deffender == "Led_D_S4":
            $ D_S4_CanDuel = "Winner"
        elif DS_Deffender == "Led_D_S5":
            $ D_S5_CanDuel = "Winner"
        elif DS_Deffender == "Led_D_S6":
            $ D_S6_CanDuel = "Winner"

#---------------------------------------------------------------------------------
    elif DS_D_HP <= 0:
#---------------------------------------------------------------------------------
        if DS_Deffender == "Led_D_S1":
            $ D_S1_HP = 0
            $ Led_D_S1_HP = 0
            $ D_S1_CanDuel = "Loser"
        elif DS_Deffender == "Led_D_S2":
            $ D_S2_HP = 0
            $ Led_D_S2_HP = 0
            $ D_S2_CanDuel = "Loser"
        elif DS_Deffender == "Led_D_S3":
            $ D_S3_HP = 0
            $ Led_D_S3_HP = 0
            $ D_S3_CanDuel = "Loser"
        elif DS_Deffender == "Led_D_S4":
            $ D_S4_HP = 0
            $ Led_D_S4_HP = 0
            $ D_S4_CanDuel = "Loser"
        elif DS_Deffender == "Led_D_S5":
            $ D_S5_HP = 0
            $ Led_D_S5_HP = 0
            $ D_S5_CanDuel = "Loser"
        elif DS_Deffender == "Led_D_S6":
            $ D_S6_HP = 0
            $ Led_D_S6_HP = 0
            $ D_S6_CanDuel = "Loser"
        if DS_Attacker == "Led_A_S1":
            $ A_S1_CanDuel = "Winner"
        elif DS_Attacker == "Led_A_S2":
            $ A_S2_CanDuel = "Winner"
        elif DS_Attacker == "Led_A_S3":
            $ A_S3_CanDuel = "Winner"
        elif DS_Attacker == "Led_A_S4":
            $ A_S4_CanDuel = "Winner"
        elif DS_Attacker == "Led_A_S5":
            $ A_S5_CanDuel = "Winner"
        elif DS_Attacker == "Led_A_S6":
            $ A_S6_CanDuel = "Winner"

#---------------------------------------------------------------------------------
    elif DS_A_HP > 0 and DS_D_HP > 0:
#---------------------------------------------------------------------------------
        if DS_Attacker == "Led_A_S1":
            $ Led_A_S1_HP = DS_A_HP 
        elif DS_Attacker == "Led_A_S2":
            $ Led_A_S2_HP = DS_A_HP 
        elif DS_Attacker == "Led_A_S3":
            $ Led_A_S3_HP = DS_A_HP 
        elif DS_Attacker == "Led_A_S4":
            $ Led_A_S4_HP = DS_A_HP 
        elif DS_Attacker == "Led_A_S5":
            $ Led_A_S5_HP = DS_A_HP 
        elif DS_Attacker == "Led_A_S6":
            $ Led_A_S6_HP = DS_A_HP 

        if DS_Deffender == "Led_D_S1":
            $ Led_D_S1_HP = DS_D_HP 
        elif DS_Deffender == "Led_D_S2":
            $ Led_D_S2_HP = DS_D_HP 
        elif DS_Deffender == "Led_D_S3":
            $ Led_D_S3_HP = DS_D_HP 
        elif DS_Deffender == "Led_D_S4":
            $ Led_D_S4_HP = DS_D_HP 
        elif DS_Deffender == "Led_D_S5":
            $ Led_D_S5_HP = DS_D_HP 
        elif DS_Deffender == "Led_D_S6":
            $ Led_D_S6_HP = DS_D_HP 

#---------------------------------------------------------------------------------
        if DS_A_Scores > DS_D_Scores:
#---------------------------------------------------------------------------------
            if DS_Attacker == "Led_A_S1":
                $ A_S1_CanDuel = "Winner"
            elif DS_Attacker == "Led_A_S2":
                $ A_S2_CanDuel = "Winner"
            elif DS_Attacker == "Led_A_S3":
                $ A_S3_CanDuel = "Winner"
            elif DS_Attacker == "Led_A_S4":
                $ A_S4_CanDuel = "Winner"
            elif DS_Attacker == "Led_A_S5":
                $ A_S5_CanDuel = "Winner"
            elif DS_Attacker == "Led_A_S6":
                $ A_S6_CanDuel = "Winner"

            if DS_Deffender == "Led_D_S1":
                $ D_S1_CanDuel = "Loser"
            elif DS_Deffender == "Led_D_S2":
                $ D_S2_CanDuel = "Loser"
            elif DS_Deffender == "Led_D_S3":
                $ D_S3_CanDuel = "Loser"
            elif DS_Deffender == "Led_D_S4":
                $ D_S4_CanDuel = "Loser"
            elif DS_Deffender == "Led_D_S5":
                $ D_S5_CanDuel = "Loser"
            elif DS_Deffender == "Led_D_S6":
                $ D_S6_CanDuel = "Loser"

#---------------------------------------------------------------------------------
        elif DS_D_Scores > DS_A_Scores:
#---------------------------------------------------------------------------------
            if DS_Deffender == "Led_D_S1":
                $ D_S1_CanDuel = "Winner"
            elif DS_Deffender == "Led_D_S2":
                $ D_S2_CanDuel = "Winner"
            elif DS_Deffender == "Led_D_S3":
                $ D_S3_CanDuel = "Winner"
            elif DS_Deffender == "Led_D_S4":
                $ D_S4_CanDuel = "Winner"
            elif DS_Deffender == "Led_D_S5":
                $ D_S5_CanDuel = "Winner"
            elif DS_Deffender == "Led_D_S6":
                $ D_S6_CanDuel = "Winner"

            if DS_Attacker == "Led_A_S1":
                $ A_S1_CanDuel = "Loser"
            elif DS_Attacker == "Led_A_S2":
                $ A_S2_CanDuel = "Loser"
            elif DS_Attacker == "Led_A_S3":
                $ A_S3_CanDuel = "Loser"
            elif DS_Attacker == "Led_A_S4":
                $ A_S4_CanDuel = "Loser"
            elif DS_Attacker == "Led_A_S5":
                $ A_S5_CanDuel = "Loser"
            elif DS_Attacker == "Led_A_S6":
                $ A_S6_CanDuel = "Loser"

#---------------------------------------------------------------------------------
        elif DS_D_Scores == DS_A_Scores:
#---------------------------------------------------------------------------------
            if DS_Deffender == "Led_D_S1":
                $ D_S1_CanDuel = "Draw"
            elif DS_Deffender == "Led_D_S2":
                $ D_S2_CanDuel = "Draw"
            elif DS_Deffender == "Led_D_S3":
                $ D_S3_CanDuel = "Draw"
            elif DS_Deffender == "Led_D_S4":
                $ D_S4_CanDuel = "Draw"
            elif DS_Deffender == "Led_D_S5":
                $ D_S5_CanDuel = "Draw"
            elif DS_Deffender == "Led_D_S6":
                $ D_S6_CanDuel = "Draw"

            if DS_Attacker == "Led_A_S1":
                $ A_S1_CanDuel = "Draw"
            elif DS_Attacker == "Led_A_S2":
                $ A_S2_CanDuel = "Draw"
            elif DS_Attacker == "Led_A_S3":
                $ A_S3_CanDuel = "Draw"
            elif DS_Attacker == "Led_A_S4":
                $ A_S4_CanDuel = "Draw"
            elif DS_Attacker == "Led_A_S5":
                $ A_S5_CanDuel = "Draw"
            elif DS_Attacker == "Led_A_S6":
                $ A_S6_CanDuel = "Draw"
    return