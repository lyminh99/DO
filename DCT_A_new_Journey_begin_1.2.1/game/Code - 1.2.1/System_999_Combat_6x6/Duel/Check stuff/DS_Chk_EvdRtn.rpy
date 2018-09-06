
#///////////////////////  ATTACKER SLOT 1
label DS_A_Chk_EvdRtn:
    hide screen Scr_Duel
    show screen Scr_Duel

    if DS_A_AntAct == "Evade_Idle":
        $ DS_A_AntAct = "Evade_Return"
    else:
        $ DS_A_AntAct = "Idle"
    return
        



#///////////////////////  DEFFENDER SLOT 1
label DS_D_Chk_EvdRtn:
    hide screen Scr_Duel
    show screen Scr_Duel

    if DS_D_AntAct == "Evade_Idle":
        $ DS_D_AntAct = "Evade_Return"
    else:
        $ DS_D_AntAct = "Idle"
    return