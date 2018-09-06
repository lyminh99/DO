label DS_A_Chk_Evt:

#///////////////////////  ATTACKER SLOT 1

    if DS_A_HP <= 0:
        $ DS_A_AntAct = "Died"
        $ renpy.pause(AntSec_Wait_To_Die, hard=True)
        $ DS_A_Name = "..."
        $ DS_A_Level = 0
        $ DS_A_Type = 0
        $ DS_A_HP = 0
        $ DS_A_MHP = 0
        $ DS_A_AvlAct = 0
    return

label DS_D_Chk_Evt:

#///////////////////////  DEFFENDER SLOT 1

    if DS_D_HP <= 0:
        $ DS_D_AntAct = "Died"
        $ renpy.pause(AntSec_Wait_To_Die, hard=True)
        $ DS_D_Name = "..."
        $ DS_D_Level = 0
        $ DS_D_Type = 0
        $ DS_D_HP = 0
        $ DS_D_MHP = 0
        $ DS_D_AvlAct = 0
    return