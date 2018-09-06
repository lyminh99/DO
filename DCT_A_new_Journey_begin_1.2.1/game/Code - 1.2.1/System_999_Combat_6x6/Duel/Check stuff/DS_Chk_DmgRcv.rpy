
#///////////////////////  ATTACKER SLOT 1
label DS_A_Chk_DmgRcv:
    $ DS_A_Dmg_Rcv = DS_D_Dmg

    if DS_A_CanEvd == 1:
        $ DS_A_Dmg_Rcv = 0
    elif DS_A_Dmg_Rcv >= DS_A_HP and DS_A_CanEvd == 0:
        $ DS_A_Dmg_Rcv =  DS_A_HP
    return
        
        
        

        


#///////////////////////  DEFFENDER SLOT 1
label DS_D_Chk_DmgRcv:
    $ DS_D_Dmg_Rcv = DS_A_Dmg

    if DS_D_CanEvd == 1:
        $ DS_D_Dmg_Rcv = 0
    elif DS_D_Dmg_Rcv >= DS_D_HP and DS_D_CanEvd == 0:
        $ DS_D_Dmg_Rcv =  DS_D_HP
    return