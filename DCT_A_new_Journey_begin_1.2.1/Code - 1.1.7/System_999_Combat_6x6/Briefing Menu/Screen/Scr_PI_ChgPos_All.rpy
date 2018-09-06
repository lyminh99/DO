screen Scr_PI_ChgPos_All:
    
    modal True

    if BS_Ctl_PlayerSide == 3 or BS_Ctl_PlayerSide == 1:
    
        if A_S1_Ocu == 1 and BM_WhoPickedToChgPOS == "A_S1":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS02_Icon_%s.png" focus_mask True action BM_A_S1_ChgPOS02Clicked at BM_A_Eft_ChgPOS02Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS03_Icon_%s.png" focus_mask True action BM_A_S1_ChgPOS03Clicked at BM_A_Eft_ChgPOS03Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS04_Icon_%s.png" focus_mask True action BM_A_S1_ChgPOS04Clicked at BM_A_Eft_ChgPOS04Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS05_Icon_%s.png" focus_mask True action BM_A_S1_ChgPOS05Clicked at BM_A_Eft_ChgPOS05Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS06_Icon_%s.png" focus_mask True action BM_A_S1_ChgPOS06Clicked at BM_A_Eft_ChgPOS06Button

        if A_S2_Ocu == 1 and BM_WhoPickedToChgPOS == "A_S2":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS01_Icon_%s.png" focus_mask True action BM_A_S2_ChgPOS01Clicked at BM_A_Eft_ChgPOS01Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS03_Icon_%s.png" focus_mask True action BM_A_S2_ChgPOS03Clicked at BM_A_Eft_ChgPOS03Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS04_Icon_%s.png" focus_mask True action BM_A_S2_ChgPOS04Clicked at BM_A_Eft_ChgPOS04Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS05_Icon_%s.png" focus_mask True action BM_A_S2_ChgPOS05Clicked at BM_A_Eft_ChgPOS05Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS06_Icon_%s.png" focus_mask True action BM_A_S2_ChgPOS06Clicked at BM_A_Eft_ChgPOS06Button

        if A_S3_Ocu == 1 and BM_WhoPickedToChgPOS == "A_S3":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS01_Icon_%s.png" focus_mask True action BM_A_S3_ChgPOS01Clicked at BM_A_Eft_ChgPOS01Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS02_Icon_%s.png" focus_mask True action BM_A_S3_ChgPOS02Clicked at BM_A_Eft_ChgPOS02Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS04_Icon_%s.png" focus_mask True action BM_A_S3_ChgPOS04Clicked at BM_A_Eft_ChgPOS04Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS05_Icon_%s.png" focus_mask True action BM_A_S3_ChgPOS05Clicked at BM_A_Eft_ChgPOS05Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS06_Icon_%s.png" focus_mask True action BM_A_S3_ChgPOS06Clicked at BM_A_Eft_ChgPOS06Button

        if A_S4_Ocu == 1 and BM_WhoPickedToChgPOS == "A_S4":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS01_Icon_%s.png" focus_mask True action BM_A_S4_ChgPOS01Clicked at BM_A_Eft_ChgPOS01Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS02_Icon_%s.png" focus_mask True action BM_A_S4_ChgPOS02Clicked at BM_A_Eft_ChgPOS02Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS03_Icon_%s.png" focus_mask True action BM_A_S4_ChgPOS03Clicked at BM_A_Eft_ChgPOS03Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS05_Icon_%s.png" focus_mask True action BM_A_S4_ChgPOS05Clicked at BM_A_Eft_ChgPOS05Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS06_Icon_%s.png" focus_mask True action BM_A_S4_ChgPOS06Clicked at BM_A_Eft_ChgPOS06Button

        if A_S5_Ocu == 1 and BM_WhoPickedToChgPOS == "A_S5":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS01_Icon_%s.png" focus_mask True action BM_A_S5_ChgPOS01Clicked at BM_A_Eft_ChgPOS01Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS02_Icon_%s.png" focus_mask True action BM_A_S5_ChgPOS02Clicked at BM_A_Eft_ChgPOS02Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS03_Icon_%s.png" focus_mask True action BM_A_S5_ChgPOS03Clicked at BM_A_Eft_ChgPOS03Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS04_Icon_%s.png" focus_mask True action BM_A_S5_ChgPOS04Clicked at BM_A_Eft_ChgPOS04Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS06_Icon_%s.png" focus_mask True action BM_A_S5_ChgPOS06Clicked at BM_A_Eft_ChgPOS06Button

        if A_S6_Ocu == 1 and BM_WhoPickedToChgPOS == "A_S6":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS01_Icon_%s.png" focus_mask True action BM_A_S6_ChgPOS01Clicked at BM_A_Eft_ChgPOS01Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS02_Icon_%s.png" focus_mask True action BM_A_S6_ChgPOS02Clicked at BM_A_Eft_ChgPOS02Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS03_Icon_%s.png" focus_mask True action BM_A_S6_ChgPOS03Clicked at BM_A_Eft_ChgPOS03Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS04_Icon_%s.png" focus_mask True action BM_A_S6_ChgPOS04Clicked at BM_A_Eft_ChgPOS04Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS05_Icon_%s.png" focus_mask True action BM_A_S6_ChgPOS05Clicked at BM_A_Eft_ChgPOS05Button

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

    if BS_Ctl_PlayerSide == 3 or BS_Ctl_PlayerSide == 2:
    
        if D_S1_Ocu == 1 and BM_WhoPickedToChgPOS == "D_S1":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS02_Icon_%s.png" focus_mask True action BM_D_S1_ChgPOS02Clicked at BM_D_Eft_ChgPOS02Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS03_Icon_%s.png" focus_mask True action BM_D_S1_ChgPOS03Clicked at BM_D_Eft_ChgPOS03Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS04_Icon_%s.png" focus_mask True action BM_D_S1_ChgPOS04Clicked at BM_D_Eft_ChgPOS04Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS05_Icon_%s.png" focus_mask True action BM_D_S1_ChgPOS05Clicked at BM_D_Eft_ChgPOS05Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS06_Icon_%s.png" focus_mask True action BM_D_S1_ChgPOS06Clicked at BM_D_Eft_ChgPOS06Button

        if D_S2_Ocu == 1 and BM_WhoPickedToChgPOS == "D_S2":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS01_Icon_%s.png" focus_mask True action BM_D_S2_ChgPOS01Clicked at BM_D_Eft_ChgPOS01Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS03_Icon_%s.png" focus_mask True action BM_D_S2_ChgPOS03Clicked at BM_D_Eft_ChgPOS03Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS04_Icon_%s.png" focus_mask True action BM_D_S2_ChgPOS04Clicked at BM_D_Eft_ChgPOS04Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS05_Icon_%s.png" focus_mask True action BM_D_S2_ChgPOS05Clicked at BM_D_Eft_ChgPOS05Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS06_Icon_%s.png" focus_mask True action BM_D_S2_ChgPOS06Clicked at BM_D_Eft_ChgPOS06Button

        if D_S3_Ocu == 1 and BM_WhoPickedToChgPOS == "D_S3":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS01_Icon_%s.png" focus_mask True action BM_D_S3_ChgPOS01Clicked at BM_D_Eft_ChgPOS01Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS02_Icon_%s.png" focus_mask True action BM_D_S3_ChgPOS02Clicked at BM_D_Eft_ChgPOS02Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS04_Icon_%s.png" focus_mask True action BM_D_S3_ChgPOS04Clicked at BM_D_Eft_ChgPOS04Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS05_Icon_%s.png" focus_mask True action BM_D_S3_ChgPOS05Clicked at BM_D_Eft_ChgPOS05Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS06_Icon_%s.png" focus_mask True action BM_D_S3_ChgPOS06Clicked at BM_D_Eft_ChgPOS06Button

        if D_S4_Ocu == 1 and BM_WhoPickedToChgPOS == "D_S4":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS01_Icon_%s.png" focus_mask True action BM_D_S4_ChgPOS01Clicked at BM_D_Eft_ChgPOS01Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS02_Icon_%s.png" focus_mask True action BM_D_S4_ChgPOS02Clicked at BM_D_Eft_ChgPOS02Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS03_Icon_%s.png" focus_mask True action BM_D_S4_ChgPOS03Clicked at BM_D_Eft_ChgPOS03Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS05_Icon_%s.png" focus_mask True action BM_D_S4_ChgPOS05Clicked at BM_D_Eft_ChgPOS05Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS06_Icon_%s.png" focus_mask True action BM_D_S4_ChgPOS06Clicked at BM_D_Eft_ChgPOS06Button

        if D_S5_Ocu == 1 and BM_WhoPickedToChgPOS == "D_S5":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS01_Icon_%s.png" focus_mask True action BM_D_S5_ChgPOS01Clicked at BM_D_Eft_ChgPOS01Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS02_Icon_%s.png" focus_mask True action BM_D_S5_ChgPOS02Clicked at BM_D_Eft_ChgPOS02Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS03_Icon_%s.png" focus_mask True action BM_D_S5_ChgPOS03Clicked at BM_D_Eft_ChgPOS03Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS04_Icon_%s.png" focus_mask True action BM_D_S5_ChgPOS04Clicked at BM_D_Eft_ChgPOS04Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS06_Icon_%s.png" focus_mask True action BM_D_S5_ChgPOS06Clicked at BM_D_Eft_ChgPOS06Button

        if D_S6_Ocu == 1 and BM_WhoPickedToChgPOS == "D_S6":
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS01_Icon_%s.png" focus_mask True action BM_D_S6_ChgPOS01Clicked at BM_D_Eft_ChgPOS01Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS02_Icon_%s.png" focus_mask True action BM_D_S6_ChgPOS02Clicked at BM_D_Eft_ChgPOS02Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS03_Icon_%s.png" focus_mask True action BM_D_S6_ChgPOS03Clicked at BM_D_Eft_ChgPOS03Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS04_Icon_%s.png" focus_mask True action BM_D_S6_ChgPOS04Clicked at BM_D_Eft_ChgPOS04Button
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS05_Icon_%s.png" focus_mask True action BM_D_S6_ChgPOS05Clicked at BM_D_Eft_ChgPOS05Button

    textbutton "Cancel" action BS_BM_ChgPOSCancel anchor (0.5,0.5) align (0.5,0.75)