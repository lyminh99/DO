screen Scr_PI_PickPos:
    
    modal True

    if CC_Progress == "Done":
    
        if BS_Ctl_PlayerSide == 3 or BS_Ctl_PlayerSide == 1:
        
            if A_S1_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_A_S1_Slot at A_S1_Eft_EmptySlots
            if A_S2_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_A_S2_Slot at A_S2_Eft_EmptySlots
            if A_S3_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_A_S3_Slot at A_S3_Eft_EmptySlots
            if A_S4_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_A_S4_Slot at A_S4_Eft_EmptySlots
            if A_S5_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_A_S5_Slot at A_S5_Eft_EmptySlots
            if A_S6_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_A_S6_Slot at A_S6_Eft_EmptySlots
    
        if BS_Ctl_PlayerSide == 3 or BS_Ctl_PlayerSide == 2:

            if D_S1_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_D_S1_Slot at D_S1_Eft_EmptySlots
            if D_S2_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_D_S2_Slot at D_S2_Eft_EmptySlots
            if D_S3_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_D_S3_Slot at D_S3_Eft_EmptySlots
            if D_S4_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_D_S4_Slot at D_S4_Eft_EmptySlots
            if D_S5_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_D_S5_Slot at D_S5_Eft_EmptySlots
            if D_S6_Ocu == 0:
                imagebutton auto "Images/Combat System/Icons/Slot_Empty_%s.png" focus_mask True action BS_Pick_D_S6_Slot at D_S6_Eft_EmptySlots

    if BS_Progress == 1:
    
        if BS_Ctl_PlayerSide == 3 or BS_Ctl_PlayerSide == 1:
        
            if A_S1_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at A_S1_Eft_EmptySlots
            if A_S2_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at A_S2_Eft_EmptySlots
            if A_S3_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at A_S3_Eft_EmptySlots
            if A_S4_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at A_S4_Eft_EmptySlots
            if A_S5_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at A_S5_Eft_EmptySlots
            if A_S6_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at A_S6_Eft_EmptySlots
    
        if BS_Ctl_PlayerSide == 3 or BS_Ctl_PlayerSide == 2:

            if D_S1_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at D_S1_Eft_EmptySlots
            if D_S2_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at D_S2_Eft_EmptySlots
            if D_S3_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at D_S3_Eft_EmptySlots
            if D_S4_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at D_S4_Eft_EmptySlots
            if D_S5_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at D_S5_Eft_EmptySlots
            if D_S6_Ocu == 0:
                add "Images/Combat System/Icons/Slot_Empty_idle.png" at D_S6_Eft_EmptySlots

        textbutton "Yes" action BS_ChooseYes anchor (0.5,0.5) align (0.47,0.75)
        textbutton "No" action BS_ChooseNo anchor (0.5,0.5) align (0.53,0.75)
