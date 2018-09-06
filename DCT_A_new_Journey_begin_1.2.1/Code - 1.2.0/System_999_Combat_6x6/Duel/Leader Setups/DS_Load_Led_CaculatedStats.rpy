
#/////////////////////// LEADER ATTACKER SLOT 1
label DS_Load_Led_CaculatedStats:

    if DS_A_Spd - DS_D_Spd >= 4:
        $ DS_A_Strike = "Double"
    else: 
        $ DS_A_Strike = "Single"

    if DS_D_Spd - DS_A_Spd >= 4:
        $ DS_D_Strike = "Double"
    else: 
        $ DS_D_Strike = "Single"

    $ DS_A_CrtChc = (DS_A_Skl + DS_A_Int)/ 2
    $ DS_A_EvdRate = DS_A_Spd

    $ DS_D_CrtChc = (DS_D_Skl + DS_D_Int)/ 2
    $ DS_D_EvdRate = DS_D_Spd

    return