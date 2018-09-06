
#///////////////////////  ATTACKER SLOT 1 - Attack
label DS_A_Atk:
    if DS_D_HP > 0:
        call DS_A_Chk_DmgOrg
        call DS_A_Chk_Can_Crit
        call DS_A_Chk_DmgHit
        call DS_D_Chk_Can_Evd
        call DS_D_Chk_DmgRcv
        call DS_A_Chk_Act
        call DS_A_Chk_Sco
        call DS_D_Chg_HP
        call DS_D_Chk_Evd
        call DS_D_Chk_EvdRtn
        call DS_A_Chk_Rtn
        call DS_D_Chk_Evt
        $ DS_A_AntAct = "Idle"
        $ DS_D_AntAct = "Idle"

    return


#///////////////////////  DEFFENDER SLOT 1 - Attack
label DS_D_Atk:
    if DS_A_HP > 0:
        call DS_D_Chk_DmgOrg
        call DS_D_Chk_Can_Crit
        call DS_D_Chk_DmgHit
        call DS_A_Chk_Can_Evd
        call DS_A_Chk_DmgRcv
        call DS_D_Chk_Act
        call DS_D_Chk_Sco
        call DS_A_Chg_HP
        call DS_A_Chk_Evd
        call DS_A_Chk_EvdRtn
        call DS_D_Chk_Rtn
        call DS_A_Chk_Evt
        $ DS_A_AntAct = "Idle"
        $ DS_D_AntAct = "Idle"

    return
