
label SMM_Home_Pick_Rest:

    hide screen SMM_Home_Scr_HomeMenu
    hide screen SMM_Home_Scr_Home
    with Dissolve (1.0)

    e "Đi ngủ thôi"

    if HS_Day == 30:
        $ HS_Day = 1
        $ HS_Month += 1
    elif HS_Day >= 1 and HS_Day <= 29:
        $ HS_Day += 1

    if HS_Date == 7:
        $ HS_Date = 1
    elif HS_Date >= 1 and HS_Date < 7:
        $ HS_Date += 1

    if HS_Month == 13:
        $ HS_Month = 1
    
    $ HS_Weather = renpy.random.choice (["Mưa", "Nắng", "Bão", "Râm"])

    $ HS_MyStrength += HS_Growth_Strength
    $ HS_MyStamina += HS_Growth_Stamina
    $ HS_MyIntelligence += HS_Growth_Intelligence
    $ HS_MyCharm += HS_Growth_Charm
    $ HS_MyWisdom += HS_Growth_Wisdom

    jump Sys_SMM_Home_Start

#-----------------------------------
label SMM_Home_Place_Park:

    show screen SMM_Home_Scr_GoOut_Map
    $ renpy.pause (hard = True)

#-----------------------------------
label SMM_Home_Place_CoffeBar:

    show screen SMM_Home_Scr_GoOut_Map
    $ renpy.pause (hard = True)

#-----------------------------------
label SMM_Home_Place_Lake:

    show screen SMM_Home_Scr_GoOut_Map
    $ renpy.pause (hard = True)

#-----------------------------------
label SMM_Home_Place_School:

    show screen SMM_Home_Scr_GoOut_Map
    $ renpy.pause (hard = True)

#-----------------------------------
label SMM_Home_Place_Supermarket:

    show screen SMM_Home_Scr_GoOut_Map
    $ renpy.pause (hard = True)

#-----------------------------------
label SMM_Home_Place_BackHome:

    hide screen SMM_Home_Scr_GoOut_Map

    jump Sys_SMM_Home_Start