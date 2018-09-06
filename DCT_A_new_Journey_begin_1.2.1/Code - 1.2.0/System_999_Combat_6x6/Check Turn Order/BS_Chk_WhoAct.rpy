label BS_Chk_WhoAct:

    call BS_BeginChk_SpdOrder
    call BS_Chk_WhoTurn
    return

label BS_Chk_WhoTurn:
    while Turn_DislayNo_1 != 0:
        call BS_BeginChk_SpdOrder
        call Update_Scr_Atker_On
#-------------------------------------------------------
        if Turn_DislayNo_1 == "A_S1":
            if A_S1_Ctl_Type == "AI":
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S1"
                call AI_Bhv_A_S1
            elif A_S1_Ctl_Type == "PI":
                call PI_A_S1_Chk_Tgt
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S1"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
        elif Turn_DislayNo_1 == "D_S1":
            if D_S1_Ctl_Type == "AI":
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S1"
                call AI_Bhv_D_S1
            elif D_S1_Ctl_Type == "PI":
                call PI_D_S1_Chk_Tgt
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S1"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
    #-------------------------------------------------------
        elif Turn_DislayNo_1 == "A_S2":
            if A_S2_Ctl_Type == "AI":
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S2"
                call AI_Bhv_A_S2
            elif A_S2_Ctl_Type == "PI":
                call PI_A_S2_Chk_Tgt
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S2"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
            call BS_A_S2_Rst_Tgt
        elif Turn_DislayNo_1 == "D_S2":
            if D_S2_Ctl_Type == "AI":
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S2"
                call AI_Bhv_D_S2
            elif D_S2_Ctl_Type == "PI":
                call PI_D_S2_Chk_Tgt
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S2"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
            call BS_D_S2_Rst_Tgt
    #-------------------------------------------------------
        elif Turn_DislayNo_1 == "A_S3":
            if A_S3_Ctl_Type == "AI":
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S3"
                call AI_Bhv_A_S3
            elif A_S3_Ctl_Type == "PI":
                call PI_A_S3_Chk_Tgt
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S3"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
            call BS_A_S3_Rst_Tgt
        elif Turn_DislayNo_1 == "D_S3":
            if D_S3_Ctl_Type == "AI":
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S3"
                call AI_Bhv_D_S3
            elif D_S3_Ctl_Type == "PI":
                call PI_D_S3_Chk_Tgt
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S3"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
            call BS_D_S3_Rst_Tgt
    #-------------------------------------------------------
        elif Turn_DislayNo_1 == "A_S4":
            if A_S4_Ctl_Type == "AI":
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S4"
                call AI_Bhv_A_S4
            elif A_S4_Ctl_Type == "PI":
                call PI_A_S4_Chk_Tgt
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S4"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
            call BS_A_S4_Rst_Tgt
        elif Turn_DislayNo_1 == "D_S4":
            if D_S4_Ctl_Type == "AI":
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S4"
                call AI_Bhv_D_S4
            elif D_S4_Ctl_Type == "PI":
                call PI_D_S4_Chk_Tgt
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S4"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
            call BS_D_S4_Rst_Tgt
    #-------------------------------------------------------
        elif Turn_DislayNo_1 == "A_S5":
            if A_S5_Ctl_Type == "AI":
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S5"
                call AI_Bhv_A_S5
            elif A_S5_Ctl_Type == "PI":
                call PI_A_S5_Chk_Tgt
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S5"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
            call BS_A_S5_Rst_Tgt
        elif Turn_DislayNo_1 == "D_S5":
            if D_S5_Ctl_Type == "AI":
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S5"
                call AI_Bhv_D_S5
            elif D_S5_Ctl_Type == "PI":
                call PI_D_S5_Chk_Tgt
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S5"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
            call BS_D_S5_Rst_Tgt
    #-------------------------------------------------------
        elif Turn_DislayNo_1 == "A_S6":
            if A_S6_Ctl_Type == "AI":
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S6"
                call AI_Bhv_A_S6
            elif A_S6_Ctl_Type == "PI":
                call PI_A_S6_Chk_Tgt
                $ BS_Which_Side = "Attacker"
                $ BS_Who_Turn = "A_S6"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
            call BS_A_S6_Rst_Tgt
        elif Turn_DislayNo_1 == "D_S6":
            if D_S6_Ctl_Type == "AI":
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S6"
                call AI_Bhv_D_S6
            elif D_S6_Ctl_Type == "PI":
                call PI_D_S6_Chk_Tgt
                $ BS_Which_Side = "Deffender"
                $ BS_Who_Turn = "D_S6"
                show screen Screen_UI_PI_Main
                $ renpy.pause(hard = True)
            call BS_D_S6_Rst_Tgt
#-------------------------------------------------------
        call Update_Scr_Atker_Off
        $ renpy.pause(SecWait_NextUnit, hard = True)
#-------------------------------------------------------
    return