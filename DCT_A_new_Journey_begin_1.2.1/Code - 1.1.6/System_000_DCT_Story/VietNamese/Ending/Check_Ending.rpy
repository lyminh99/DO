﻿label Check_Ending:

    if Force_end_7c == 1:
        $ Sys_GameProgress = "MYSTERY_END"
        if Sys_SkipAll == 0:
            call MYSTERY_END
    elif True_end == 1:
        $ Sys_GameProgress = "True_End"
        if Sys_SkipAll == 0:
            call True_End
    elif Hopeless_Dream_End == 1:
        $ Sys_GameProgress = "Hopeless_Dream_End"
        if Sys_SkipAll == 0:
            call Hopeless_Dream_End
    elif WAR_END_DEATH_OF_A_SPY == 1:
        $ Sys_GameProgress = "WAR_END_DEATH_OF_A_SPY"
        if Sys_SkipAll == 0:
            call WAR_END_DEATH_OF_A_SPY
    elif WAR_END_REVOLUTION == 1:
        $ Sys_GameProgress = "WAR_END_REVOLUTION"
        if Sys_SkipAll == 0:
            call WAR_END_REVOLUTION
    elif A_Rich_Happy_Family == 1:
        $ Sys_GameProgress = "A_Rich_Happy_Family"
        if Sys_SkipAll == 0:
            call A_Rich_Happy_Family

    jump Sys_DCT_Chk_Ending