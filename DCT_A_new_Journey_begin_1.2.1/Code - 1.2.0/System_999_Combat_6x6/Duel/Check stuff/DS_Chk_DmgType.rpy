
#///////////////////////  ATTACKER
label DS_A_Chk_DmgType:
    if DS_A_Type == "Solider":
        $ DS_A_DmgType = "Melee"
    if DS_A_Type == "Archer":
        $ DS_A_DmgType = "Range"
    if DS_A_Type == "Horse_Rider":
        $ DS_A_DmgType = "Melee"
    if DS_A_Type == "Healer":
        $ DS_A_DmgType = "None"
    return

#================================================================
#================================================================
#================================================================    
#================================================================  
#================================================================
#================================================================
#================================================================    
#================================================================  

#///////////////////////  DEFFENDER
label DS_D_Chk_DmgType:
    if DS_D_Type == "Solider":
        $ DS_D_DmgType = "Melee"
    if DS_D_Type == "Archer":
        $ DS_D_DmgType = "Range"
    if DS_D_Type == "Horse_Rider":
        $ DS_D_DmgType = "Melee"
    if DS_D_Type == "Healer":
        $ DS_D_DmgType = "None"
    return
