
#///////////////////////  ATTACKER SLOT 1
label DS_A_Chk_Can_Evd:

    $ BS_EvdRate = renpy.random.randint(1, 100)

    if DS_A_EvdRate >= BS_EvdRate:
        $ DS_A_CanEvd = 1
    else:
        $ DS_A_CanEvd = 0
    return
        


#///////////////////////  DEFFENDER SLOT 1
label DS_D_Chk_Can_Evd:

    $ BS_EvdRate = renpy.random.randint(1, 100)

    if DS_D_EvdRate >= BS_EvdRate:
        $ DS_D_CanEvd = 1
    else:
        $ DS_D_CanEvd = 0
    return