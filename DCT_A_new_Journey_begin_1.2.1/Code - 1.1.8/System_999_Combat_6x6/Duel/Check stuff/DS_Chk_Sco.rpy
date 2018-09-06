#///////////////////////  ATTACKER SLOT 1 - Return
label DS_A_Chk_Sco:
    if DS_A_Level < DS_D_Level:
        $ DS_Lv_odd = DS_D_Level - DS_A_Level
        $ DS_A_Scores += DS_D_Dmg_Rcv + ((DS_D_Dmg_Rcv * DS_Lv_odd)/ 10)
    else:
        $ DS_A_Scores += DS_D_Dmg_Rcv
    return

   

#///////////////////////  DEFFENDER SLOT 1 - Return
label DS_D_Chk_Sco:
    if DS_D_Level < DS_A_Level:
        $ DS_Lv_odd = DS_A_Level - DS_D_Level
        $ DS_D_Scores += DS_A_Dmg_Rcv + ((DS_A_Dmg_Rcv * DS_Lv_odd)/ 10)
    else:
        $ DS_D_Scores += DS_A_Dmg_Rcv
    return

