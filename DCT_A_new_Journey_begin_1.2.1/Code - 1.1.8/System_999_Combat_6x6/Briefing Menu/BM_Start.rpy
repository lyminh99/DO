
#=====================================================
label BS_BM_Start:
#=====================================================
#---------------------------------------------
    if BS_Ctl_PlayerSide == 1:
        call BM_Load_A_ListArmy_Rdm
    elif BS_Ctl_PlayerSide == 2:
        call BM_Load_D_ListArmy_Rdm
    elif BS_Ctl_PlayerSide == 3:
        call BM_Load_A_ListArmy_Rdm
        call BM_Load_D_ListArmy_Rdm
#---------------------------------------------
    $ renpy.pause(BS_SysSpd, hard = True)
    call Update_Scr_Loading_Off
#---------------------------------------------
    call BM_Start
#---------------------------------------------
    if BS_Ctl_PlayerSide == 0 or (
    BS_Ctl_PlayerSide == 1) or (
    BS_Ctl_PlayerSide == 2) :
        call BM_Load_SlotsRdm
#---------------------------------------------
    hide screen Scr_PI_PosPicked
    hide screen Scr_PI_PickPos
    hide screen Scr_Test_BM_SlotsInfo
    hide screen Scr_PI_PosPicked
    hide screen Scr_PI_ChgPos
    hide screen Scr_PI_ListArmy
#---------------------------------------------
    call Update_Scr_Loading_On
#---------------------------------------------
    return

#=====================================================
label BM_Load_SlotsRdm:
#=====================================================
    #call BS_Stages_Slt_Stp
    call BS_Stages_Slt_Stp_AllClsRdm
    call BS_Army_Led_SltStp
    call BS_Army_Led_StsRdm
    #call BS_Stages_Slt_Stp_Test01
    #call BS_Stages_Slt_Stp_Test02
    #call BS_Stages_Slt_Stp_Test03
    #call BS_Stages_Stg001_Stp
    return

#=====================================================
label BM_Start:
#=====================================================
    if BS_Ctl_PlayerSide > 0:
        $ BS_WhatKindOfChgPOS = "BM_PI_ChgPOS"

        if CC_Progress == "Done":
            show screen Scr_PI_PosPicked
            show screen Scr_PI_PickPos
            e "Pick your spot"
            $ renpy.pause(hard = True)
        elif BS_Progress == 1:
            e "Are you sure ?"
            $ renpy.pause(hard = True)
        elif BS_Progress == 2:
            #call BM_Load_SlotsRdm
            show screen Scr_Test_BM_SlotsInfo
            show screen Scr_PI_PosPicked
            show screen Scr_PI_ChgPos
            show screen Scr_PI_ListArmy
            $ renpy.pause(hard = True)
        elif BS_Progress == 3:
            #call BM_Load_SlotsRdm
            $ renpy.pause(hard = True)
        elif BS_Progress == 99:
            $ BS_Progress = 0
            $ CC_Progress = 0

        $ BS_WhatKindOfChgPOS = 0 
        $ BM_WhoPickedToChgPOS = 0

    return
