label BS_Player_ResetChoice:

    if BS_PickedSlot == "A_S1":
        $ A_S1_Ocu = 0
        $ A_S1_Ctl_Type = "AI"
        $ Led_A_S1_Ocu = 0
        $ A_S1_Cls = 0
    elif BS_PickedSlot == "A_S2":
        $ A_S2_Ocu = 0
        $ A_S2_Ctl_Type = "AI"
        $ Led_A_S2_Ocu = 0
        $ A_S2_Cls = 0
    elif BS_PickedSlot == "A_S3":
        $ A_S3_Ocu = 0
        $ A_S3_Ctl_Type = "AI"
        $ Led_A_S3_Ocu = 0
        $ A_S3_Cls = 0
    elif BS_PickedSlot == "A_S4":
        $ A_S4_Ocu = 0
        $ A_S4_Ctl_Type = "AI"
        $ Led_A_S4_Ocu = 0
        $ A_S4_Cls = 0
    elif BS_PickedSlot == "A_S5":
        $ A_S5_Ocu = 0
        $ A_S5_Ctl_Type = "AI"
        $ Led_A_S5_Ocu = 0
        $ A_S5_Cls = 0
    elif BS_PickedSlot == "A_S6":
        $ A_S6_Ocu = 0
        $ A_S6_Ctl_Type = "AI"
        $ Led_A_S6_Ocu = 0
        $ A_S6_Cls = 0

    elif BS_PickedSlot == "D_S1":
        $ D_S1_Ocu = 0
        $ D_S1_Ctl_Type = "AI"
        $ Led_D_S1_Ocu = 0
        $ D_S1_Cls = 0
    elif BS_PickedSlot == "D_S2":
        $ D_S2_Ocu = 0
        $ D_S2_Ctl_Type = "AI"
        $ Led_D_S2_Ocu = 0
        $ D_S2_Cls = 0
    elif BS_PickedSlot == "D_S3":
        $ D_S3_Ocu = 0
        $ D_S3_Ctl_Type = "AI"
        $ Led_D_S3_Ocu = 0
        $ D_S3_Cls = 0
    elif BS_PickedSlot == "D_S4":
        $ D_S4_Ocu = 0
        $ D_S4_Ctl_Type = "AI"
        $ Led_D_S4_Ocu = 0
        $ D_S4_Cls = 0
    elif BS_PickedSlot == "D_S5":
        $ D_S5_Ocu = 0
        $ D_S5_Ctl_Type = "AI"
        $ Led_D_S5_Ocu = 0
        $ D_S5_Cls = 0
    elif BS_PickedSlot == "D_S6":
        $ D_S6_Ocu = 0
        $ D_S6_Ctl_Type = "AI"
        $ Led_D_S6_Ocu = 0
        $ D_S6_Cls = 0

    $ BS_PickedSlot = 0
    $ CC_Progress = "Done"

    jump BM_Start