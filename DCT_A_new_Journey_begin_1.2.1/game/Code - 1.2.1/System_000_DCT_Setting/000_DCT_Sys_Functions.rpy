﻿label Sys_Chk_Ending:

    if (Force_end_7c == 0) and (
    Hopeless_Dream_End == 0) and (
    WAR_END_DEATH_OF_A_SPY == 0) and (
    WAR_END_REVOLUTION == 0) and (
    A_Rich_Happy_Family == 0):
        menu:
            "Sys_Check Routes and Ending (Skip all)":
                pass
            "Sys_Red all":
                $ Sys_SkipAll = 1
        menu:
            "Routes Maping ON":
                show screen Scr_Status
            "Routes Maping OFF":
                hide screen Scr_Status
        call Storyline 

    $ Force_end_7c = 0
    $ True_end = 0
    $ Hopeless_Dream_End = 0
    $ WAR_END_DEATH_OF_A_SPY = 0
    $ WAR_END_REVOLUTION = 0
    $ A_Rich_Happy_Family = 0
    hide screen Scr_Status
    return

label Sys_Chk_Lines:

    menu:
        "Stop":
            return
#------------------------------------------------------
        "prologue2":
            call prologue2
        "GC 1-4 (+)":
            menu:
                "gc_chuong1":
                    call gc_chuong1
                "gc_chuong2":
                    call gc_chuong2
                "gc_chuong3":
                    call gc_chuong3
                "gc_chuong4":
                    call gc_chuong4
#------------------------------------------------------
        "gc2":
            call gc2
#------------------------------------------------------                 
        "gc3":
            call gc3
#------------------------------------------------------
        "Chapter 1 (+)":
            menu:
                "Chapter 1 - p1 (+)":
                    menu:
                        "Ch1P1":
                            call Ch1P1
                        "Ch1P1_C2":
                            call Ch1P1_C2
                        "Ch1P1_C3":
                            call Ch1P1_C3
                        "Ch1P1_C3C1":
                            call Ch1P1_C3C1
                        "Ch1P1_C3C2":
                            call Ch1P1_C3C2
                "Chapter 1 - p2 (+)":
                    menu:
                        "Ch1P2":
                            call Ch1P2
                        "Ch1P2B1_C1":
                            call Ch1P2B1_C1
                        "Ch1P2B1_C2":
                            call Ch1P2B1_C2
                        "Ch1P2B1_C3":
                            call Ch1P2B1_C3
                        "Ch1P2B1_C4":
                            call Ch1P2B1_C4
                "Chapter 1 - p3 (+)":
                    menu:
                        "Ch1P3":
                            call Ch1P3
                        "Ch1P3B2_C1":
                            call Ch1P3B2_C1
                        "Ch1P3B2_C2":
                            call Ch1P3B2_C2
                        "Ch1P3B2_C3":
                            call Ch1P3B2_C3
                "Chapter 1 - p4 (+)":
                    menu:
                        "Ch1P4":
                            call Ch1P4
                        "Ch1P4_B1":
                            call Ch1P4_B1
                        "Ch1P4_B2":
                            call Ch1P4_B2
                        "Ch1P4_B3":
                            call Ch1P4_B3
                "Chapter 1 - p5 (+)":
                    menu:
                        "Ch1P5":
                            call Ch1P5
                        "Ch1P5_C1":
                            call Ch1P5_C1
                        "Ch1P5_C2":
                            call Ch1P5_C2
                        "Ch1P5_C2C1":
                            call Ch1P5_C2C1
                        "Ch1P5_C2C3":
                            call Ch1P5_C2C3
                "Ch1P6":
                    call Ch1P6
#------------------------------------------------------
        "Chapter 2 (+)":
            menu:
                "Ch2P1":
                    call Ch2P1
                "Ch2P1_C1":
                    call Ch2P1_C1
                "Ch2P1_C2":
                    call Ch2P1_C2
                "Ch2P2_C1":
                    call Ch2P2_C1
                "Ch2P2_C2":
                    call Ch2P2_C2
                "Ch2P2_C3":
                    call Ch2P2_C3
                "Ch2P2":
                    call Ch2P2
                "Ch2P3":
                    call Ch2P3
#------------------------------------------------------
        "Chapter 3 (+)":
            menu:
                "Ch3P1":
                    call Ch3P1
                "Ch3P1_C1":
                    call Ch3P1_C1
                "Ch3P1_C2":
                    call Ch3P1_C2
                "Ch3P2":
                    call Ch3P2
#------------------------------------------------------
        "Chapter 4 (+)":
            menu:
                "Ch4P1":
                    call Ch4P1
                "Ch4P1_C1":
                    call Ch4P1_C1
                "Ch4P1_C2":
                    call Ch4P1_C2
                "Ch4P1_C3":
                    call Ch4P1_C3
                "Ch4P2":
                    call Ch4P2
                "Ch4P3":
                    call Ch4P3
                "Ch4P3B1_C1":
                    call Ch4P3B1_C1
                "Ch4P3B1_C2":
                    call Ch4P3B1_C2
                "Ch4P3B1_C3":
                    call Ch4P3B1_C3
                "Ch4P4":
                    call Ch4P4
#------------------------------------------------------         
        "Chapter 5 (+)":
            menu:
                "Ch5 ":
                    call Ch5
                "Ch5_C1 ":
                    call Ch5_C1
                "Ch5_C2 ":
                    call Ch5_C2
                "Ch5_C3 ":
                    call Ch5_C3
                "Ch5_C1C1 ":
                    call Ch5_C1C1
                "Ch5_C1C2 ":
                    call Ch5_C1C2
                "Ch5_C1C3 ":
                    call Ch5_C1C3
#------------------------------------------------------
        "Chapter 6 (+)":
            menu:
                "Chapter 6 - p1 (+)":
                    menu:   
                        "Ch6P1 ":
                            call Ch6P1
                        "Ch6P1B1 ":
                            call Ch6P1B1
                        "Ch6P1B2 (+)":
                            menu:   
                                "Ch6P1B2 ":
                                    call Ch6P1B2
                                "Ch6P1B2_C1 ":
                                    call Ch6P1B2_C1
                                "Ch6P1B2_C1C1 ":
                                    call Ch6P1B2_C1C1
                                "Ch6P1B2_C1C1_B1 ":
                                    call Ch6P1B2_C1C1_B1
                                "Ch6P1B2_C2 ":
                                    call Ch6P1B2_C2
                                "Ch6P2_C1 ":
                                    call Ch6P2_C1
                                "Ch6P2_C2 ":
                                    call Ch6P2_C2
                                "Ch6P2_C2C1 ":
                                    call Ch6P2_C2C1
                                "Ch6P2_C2C2 ":
                                    call Ch6P2_C2C2
                                "Ch6P2_C3 ":
                                    call Ch6P2_C3
                                "Ch6P2_C4 ":
                                    call Ch6P2_C4
                                "Ch6P2_C4C1 ":
                                    call Ch6P2_C4C1
                                "Ch6P2_C4C2 ":
                                    call Ch6P2_C4C2
                                "Ch6P2_C4C3 ":
                                    call Ch6P2_C4C3
                        "Ch6P1B3 ":
                            call Ch6P1B3
                        "Ch6P1B3a ":
                            call Ch6P1B3a
                        "Ch6P1B4 ":
                            call Ch6P1B4
#------------------------------------------------------  
                "Ch6P2 ":
                    call Ch6P2
#------------------------------------------------------
                "Ch6P2_Fes_Hanes_B ":
                    call Ch6P2_Fes_Hanes_B
                "Ch6P2_Fes_Hanes_G ":
                    call Ch6P2_Fes_Hanes_G
#------------------------------------------------------  
                "Chapter 6 - p3 (+)":
                    menu:   
                        "Ch6P3 ":
                            call Ch6P3
                        "Ch6P3B5 ":
                            call Ch6P3B5
                        "Ch6P3B5_C1 ":
                            call Ch6P3B5_C1
                        "Ch6P3B5_C2 ":
                            call Ch6P3B5_C2
                        "Ch6P3B5_C3 ":
                            call Ch6P3B5_C3
                        "Ch6P3B5_C3a ":
                            call Ch6P3B5_C3a
                        "Ch6P3B5_C3b ":
                            call Ch6P3B5_C3b
#------------------------------------------------------  
                "Chapter 6 - p4 (+)":
                    menu:   
                        "Ch6P4 ":
                            call Ch6P4
                        "Ch6P1B1_C1 ":
                            call Ch6P1B1_C1
                        "Ch6P1B1_C1_E1 ":
                            call Ch6P1B1_C1_E1
                        "Ch6P1B1_C1_E2 ":
                            call Ch6P1B1_C1_E2
                        "Ch6P1B1_C2 ":
                            call Ch6P1B1_C2
#------------------------------------------------------
        "SchallendorfHouse (+)":
            menu:
                "SchallendorfHouse ":
                    call SchallendorfHouse
                "SchallendorfHouse_choice_001 ":
                    call SchallendorfHouse_choice_001
                "SchallendorfHouse_choice_002 ":
                    call SchallendorfHouse_choice_002
                "SchallendorfHouse_choice_003 ":
                    call SchallendorfHouse_choice_003
#------------------------------------------------------
        "Azzurra_Corridor (+)":
            menu:
                "Azzurra_Corridor ":
                    call Azzurra_Corridor
                "Azzurra_Corridor_choice_001 ":
                    call Azzurra_Corridor_choice_001
                "Azzurra_Corridor_choice_002a ":
                    call Azzurra_Corridor_choice_002a
                "Azzurra_Corridor_choice_002b ":
                    call Azzurra_Corridor_choice_002b
                "Azzurra_Corridor_choice_003 ":
                    call Azzurra_Corridor_choice_003
#------------------------------------------------------
        "Escape (+)":
            menu:
                "Escape_Choice_001 ":
                    call Escape_Choice_001
                "Escape_Choice_002 ":
                    call Escape_Choice_002
                "Escape_p1 ":
                    call Escape_p1
                "Escape_Choice_001_E001 ":
                    call Escape_Choice_001_E001
                "Escape_Choice_001_E002 ":
                    call Escape_Choice_001_E002
                "Escape_E001 ":
                    call Escape_E001
                "Escape_E002 ":
                    call Escape_E002
                "Escape_p2 ":
                    call Escape_p2
                "Escape_E002_E001 ":
                    call Escape_E002_E001
                "Escape_E002_E001_Choice_001 ":
                    call Escape_E002_E001_Choice_001
                "Escape_E002_E001_Choice_002 ":
                    call Escape_E002_E001_Choice_002
                "Escape_E002_E001_Choice_002_E001 ":
                    call Escape_E002_E001_Choice_002_E001
                "Escape_E002_E001_C002_E001_E001 ":
                    call Escape_E002_E001_C002_E001_E001
                "Escape_E002_E001_Choice_002_E002 ":
                    call Escape_E002_E001_Choice_002_E002
                "OutIf_ElenaRescue_1 ":
                    call OutIf_ElenaRescue_1
#------------------------------------------------------
    jump Sys_Chk_Lines