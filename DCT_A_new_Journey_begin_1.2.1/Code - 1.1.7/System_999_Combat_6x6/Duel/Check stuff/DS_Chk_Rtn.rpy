#///////////////////////  ATTACKER SLOT 1 - Return
label DS_A_Chk_Rtn:

    hide screen Scr_Duel
    show screen Scr_Duel

    $ DS_A_AntAct = "Return"

    if DS_A_Type == "Solider":
        if DS_A_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif DS_A_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif DS_A_Type == "Archer":
        if DS_A_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif DS_A_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif DS_A_Type == "Horse_Rider":
        if DS_A_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif DS_A_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
    elif DS_A_Type == "Healer":
        if DS_A_DmgType == "Heal":
            $ renpy.pause(AntSec_Cls004_HealReturn, hard=True)

    $ DS_A_AntAct = "Idle"
    return

    
    
    
    

#///////////////////////  DEFFENDER SLOT 1 - Return
label DS_D_Chk_Rtn:

    hide screen Scr_Duel
    show screen Scr_Duel

    $ DS_D_AntAct = "Return"

    if DS_D_Type == "Solider":
        if DS_D_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif DS_D_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif DS_D_Type == "Archer":
        if DS_D_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif DS_D_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif DS_D_Type == "Horse_Rider":
        if DS_D_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif DS_D_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
    elif DS_D_Type == "Healer":
        if DS_D_DmgType == "Heal":
            $ renpy.pause(AntSec_Cls004_HealReturn, hard=True)

    $ DS_D_AntAct = "Idle"
    return

