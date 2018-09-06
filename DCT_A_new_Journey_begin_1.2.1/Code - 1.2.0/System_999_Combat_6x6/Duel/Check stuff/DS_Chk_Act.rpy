
#///////////////////////  ATTACKER SLOT 1
label DS_A_Chk_Act:

    if DS_A_Type == "Solider":
        if DS_A_CanCrt == 1:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_A_AntAct = "CritHit"
            if DS_A_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls001_MeleeCrit, hard=True)
            elif DS_A_DmgType == "Range":
                $ renpy.pause(AntSec_Cls001_RangeCrit, hard=True)
        else:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_A_AntAct = "Hit"
            if DS_A_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls001_MeleeNormal, hard=True)
            elif DS_A_DmgType == "Range":
                $ renpy.pause(AntSec_Cls001_RangeNormal, hard=True)
    elif DS_A_Type == "Archer":
        if DS_A_CanCrt == 1:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_A_AntAct = "CritHit"
            if DS_A_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls002_MeleeCrit, hard=True)
            elif DS_A_DmgType == "Range":
                $ renpy.pause(AntSec_Cls002_RangeCrit, hard=True)
        else:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_A_AntAct = "Hit"
            if DS_A_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls002_MeleeNormal, hard=True)
            elif DS_A_DmgType == "Range":
                $ renpy.pause(AntSec_Cls002_RangeNormal, hard=True)
    elif DS_A_Type == "Horse_Rider":
        if DS_A_CanCrt == 1:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_A_AntAct = "CritHit"
            if DS_A_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
            elif DS_A_DmgType == "Range":
                $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
        else:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_A_AntAct = "Hit"
            if DS_A_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
            elif DS_A_DmgType == "Range":
                $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)
    elif DS_A_Type == "Healer":
        pass

    $ DS_A_AntAct = "Hit_Idle"

    return


    


#///////////////////////  DEFFENDER SLOT 1
label DS_D_Chk_Act:

    if DS_D_Type == "Solider":
        if DS_D_CanCrt == 1:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_D_AntAct = "CritHit"
            if DS_D_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls001_MeleeCrit, hard=True)
            elif DS_D_DmgType == "Range":
                $ renpy.pause(AntSec_Cls001_RangeCrit, hard=True)
        else:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_D_AntAct = "Hit"
            if DS_D_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls001_MeleeNormal, hard=True)
            elif DS_D_DmgType == "Range":
                $ renpy.pause(AntSec_Cls001_RangeNormal, hard=True)
    elif DS_D_Type == "Archer":
        if DS_D_CanCrt == 1:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_D_AntAct = "CritHit"
            if DS_D_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls002_MeleeCrit, hard=True)
            elif DS_D_DmgType == "Range":
                $ renpy.pause(AntSec_Cls002_RangeCrit, hard=True)
        else:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_D_AntAct = "Hit"
            if DS_D_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls002_MeleeNormal, hard=True)
            elif DS_D_DmgType == "Range":
                $ renpy.pause(AntSec_Cls002_RangeNormal, hard=True)
    elif DS_D_Type == "Horse_Rider":
        if DS_D_CanCrt == 1:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_D_AntAct = "CritHit"
            if DS_D_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
            elif DS_D_DmgType == "Range":
                $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
        else:
            $ renpy.pause(SecWait_Act, hard=True)
            call Call_Show_Scr_Duel
            $ DS_D_AntAct = "Hit"
            if DS_D_DmgType == "Melee":
                $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
            elif DS_D_DmgType == "Range":
                $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)
    elif DS_D_Type == "Healer":
        pass

    $ DS_D_AntAct = "Hit_Idle"

    return

