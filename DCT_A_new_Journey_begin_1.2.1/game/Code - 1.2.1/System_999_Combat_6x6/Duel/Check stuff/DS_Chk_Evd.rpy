
#///////////////////////  ATTACKER SLOT 1
label DS_A_Chk_Evd:
    hide screen Scr_Duel
    show screen Scr_Duel

    if DS_A_CanEvd == 1:
        $ DS_A_AntAct = "Evade_Idle"
    elif DS_A_CanEvd == 0:
        $ DS_A_AntAct = "Damged"

    $ renpy.pause(0.9, hard=True)
    return
        



#///////////////////////  DEFFENDER SLOT 1
label DS_D_Chk_Evd:
    hide screen Scr_Duel
    show screen Scr_Duel

    if DS_D_CanEvd == 1:
        $ DS_D_AntAct = "Evade_Idle"
    elif DS_D_CanEvd == 0:
        $ DS_D_AntAct = "Damged"

    $ renpy.pause(0.9, hard=True)
    return