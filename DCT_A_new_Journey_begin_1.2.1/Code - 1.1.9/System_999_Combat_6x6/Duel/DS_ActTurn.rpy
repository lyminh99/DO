
#///////////////////////  ATTACKER SLOT 1 - Attack
label DS_A_ActTurn:

    hide screen Scr_Duel
    show screen Scr_Duel

    if DS_StrikeFirst_Side == "Attacker":
        if DS_A_Type != "Healer" and DS_A_Type != "Archer":
            call DS_A_Atk
        $ DS_Which_Side = "Deffender"
        $ DS_StrikeFirst_Side = 0
    elif DS_A_Strike == "Double":
        if DS_A_Type != "Healer" and DS_A_Type != "Archer":
            call DS_A_Atk
            call DS_A_Atk
        $ DS_Which_Side = "Deffender"
    elif DS_A_Strike == "Single":
        if DS_A_Type != "Healer" and DS_A_Type != "Archer":
            call DS_A_Atk
        $ DS_Which_Side = "Deffender"

    $ DuelTurn -= 1
    return


#///////////////////////  DEFFENDER SLOT 1 - Attack
label DS_D_ActTurn:

    hide screen Scr_Duel
    show screen Scr_Duel

    if DS_StrikeFirst_Side == "Deffender":
        if DS_D_Type != "Healer" and DS_D_Type != "Archer":
            call DS_D_Atk
        $ DS_Which_Side = "Attacker"
        $ DS_StrikeFirst_Side = 0
    elif DS_D_Strike == "Double":
        if DS_D_Type != "Healer" and DS_D_Type != "Archer":
            call DS_D_Atk
            call DS_D_Atk
        $ DS_Which_Side = "Attacker"
    elif DS_D_Strike == "Single":
        if DS_D_Type != "Healer" and DS_D_Type != "Archer":
            call DS_D_Atk
        $ DS_Which_Side = "Attacker"
    $ DuelTurn -= 1
    return
