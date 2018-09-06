
label Sys_SMM_Start_Check:

    call Sys_SMM_Home_Start

    return
    
label Sys_SMM_Home_Start:

    hide screen SMM_Home_Scr_MySchedule
    hide screen SMM_Home_Scr_GoOut_Map
    hide screen SMM_Home_Scr_GirlsStatus
    show screen SMM_Home_Scr_HomeMenu
    $ renpy.pause (hard = True)

    return