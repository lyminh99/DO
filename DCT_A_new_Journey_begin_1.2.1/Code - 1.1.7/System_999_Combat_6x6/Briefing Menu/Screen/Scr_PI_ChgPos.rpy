screen Scr_PI_ChgPos:

    if BS_Ctl_PlayerSide == 3 or BS_Ctl_PlayerSide == 1:

#---------------------------------------------
        if A_S1_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_A_S1_ChgPOSClicked at BM_A_S1_Eft_ChgPOSButton
        elif A_S1_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_A_S1_Picked at BM_A_S1_Eft_ArmyPicked
#---------------------------------------------
        if A_S2_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_A_S2_ChgPOSClicked at BM_A_S2_Eft_ChgPOSButton
        elif A_S2_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_A_S2_Picked at BM_A_S2_Eft_ArmyPicked
#---------------------------------------------
        if A_S3_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_A_S3_ChgPOSClicked at BM_A_S3_Eft_ChgPOSButton
        elif A_S3_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_A_S3_Picked at BM_A_S3_Eft_ArmyPicked
#---------------------------------------------
        if A_S4_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_A_S4_ChgPOSClicked at BM_A_S4_Eft_ChgPOSButton
        elif A_S4_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_A_S4_Picked at BM_A_S4_Eft_ArmyPicked
#---------------------------------------------
        if A_S5_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_A_S5_ChgPOSClicked at BM_A_S5_Eft_ChgPOSButton
        elif A_S5_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_A_S5_Picked at BM_A_S5_Eft_ArmyPicked
#---------------------------------------------
        if A_S6_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_A_S6_ChgPOSClicked at BM_A_S6_Eft_ChgPOSButton
        elif A_S6_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_A_S6_Picked at BM_A_S6_Eft_ArmyPicked
#---------------------------------------------

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

    if BS_Ctl_PlayerSide == 3 or BS_Ctl_PlayerSide == 2:

#---------------------------------------------
        if D_S1_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_D_S1_ChgPOSClicked at BM_D_S1_Eft_ChgPOSButton
        elif D_S1_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_D_S1_Picked at BM_D_S1_Eft_ArmyPicked
#---------------------------------------------
        if D_S2_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_D_S2_ChgPOSClicked at BM_D_S2_Eft_ChgPOSButton
        elif D_S2_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_D_S2_Picked at BM_D_S2_Eft_ArmyPicked
#---------------------------------------------
        if D_S3_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_D_S3_ChgPOSClicked at BM_D_S3_Eft_ChgPOSButton
        elif D_S3_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_D_S3_Picked at BM_D_S3_Eft_ArmyPicked
#---------------------------------------------
        if D_S4_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_D_S4_ChgPOSClicked at BM_D_S4_Eft_ChgPOSButton
        elif D_S4_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_D_S4_Picked at BM_D_S4_Eft_ArmyPicked
#---------------------------------------------
        if D_S5_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_D_S5_ChgPOSClicked at BM_D_S5_Eft_ChgPOSButton
        elif D_S5_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_D_S5_Picked at BM_D_S5_Eft_ArmyPicked
#---------------------------------------------
        if D_S6_Ocu == 1:
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action BM_D_S6_ChgPOSClicked at BM_D_S6_Eft_ChgPOSButton
        elif D_S6_Ocu == 0:
            imagebutton auto "Images/Briefing Menu/Army_Icon_%s.png" focus_mask True action BM_Army_D_S6_Picked at BM_D_S6_Eft_ArmyPicked
#---------------------------------------------

    textbutton "Done" action BS_ChooseDone anchor (0.5,0.5) align (0.5,0.75)