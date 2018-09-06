
#///////////////////////  ATTACKER SLOT 1
label DS_A_Chk_DmgHit:

    $ DS_A_Dmg = DS_A_Dmg - DS_D_Def

    if DS_A_Dmg <= 0:
        $ DS_A_Dmg = 0

    return


        


#///////////////////////  DEFFENDER SLOT 1
label DS_D_Chk_DmgHit:

    $ DS_D_Dmg = DS_D_Dmg - DS_A_Def

    if DS_D_Dmg <= 0:
        $ DS_D_Dmg = 0

    return

