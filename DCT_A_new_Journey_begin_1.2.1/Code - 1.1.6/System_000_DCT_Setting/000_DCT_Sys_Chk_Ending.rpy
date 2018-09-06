label Sys_DCT_Chk_Ending:

    if (Force_end_7c == 0) and (
    True_end == 0) and (
    Hopeless_Dream_End == 0) and (
    WAR_END_DEATH_OF_A_SPY == 0) and (
    WAR_END_REVOLUTION == 0) and (
    A_Rich_Happy_Family == 0):

        if persistent.Sys_Langue == "VN":
            call Sys_DCT_Storyline_VN
        elif persistent.Sys_Langue == "ENG":
            call Sys_DCT_Storyline_ENG

    $ Force_end_7c = 0
    $ True_end = 0
    $ Hopeless_Dream_End = 0
    $ WAR_END_DEATH_OF_A_SPY = 0
    $ WAR_END_REVOLUTION = 0
    $ A_Rich_Happy_Family = 0
    #hide screen Scr_Status
    return
