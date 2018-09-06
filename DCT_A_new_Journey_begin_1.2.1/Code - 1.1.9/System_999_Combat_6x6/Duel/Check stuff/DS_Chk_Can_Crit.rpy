
#///////////////////////  ATTACKER SLOT 1
label DS_A_Chk_Can_Crit:

    $ Critical_hit = renpy.random.randint(1, 100)
    if DS_A_CrtChc >= Critical_hit:
        $ DS_A_CanCrt = 1
        $ DS_A_Dmg = DS_A_Dmg * 3
    else:
        $ DS_A_CanCrt = 0
    return



        


#///////////////////////  DEFFENDER SLOT 1
label DS_D_Chk_Can_Crit:

    $ Critical_hit = renpy.random.randint(1, 100)
    if DS_D_CrtChc >= Critical_hit:
        $ DS_D_CanCrt = 1
        $ DS_D_Dmg = DS_D_Dmg * 3
    else:
        $ DS_D_CanCrt = 0
    return

