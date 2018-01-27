screen Scr_Status:

    frame:
        xalign 0.15
        yalign 0.1
        vbox:
            text "{size=18} [Elena_Point]{/size}"
            text "{size=18} [Azzurra_Point]{/size}"
            text "{size=18} [Azzurra_Persuasion]{/size}"
            text "{size=18} [Church]{/size}"
            text "{size=18} [Global_ParentPoint]{/size}"
            text "{size=18} [RescueTime]{/size}"
            text "{size=18} [Lohengramm]{/size}"
            text "{size=18} [Azzurra_Stays_With_Fredo]{/size}"
            text "{size=18} [Hanes_Truth]{/size}"
            text "{size=18} [Anatolio_Defies_Hanes]{/size}"
            text "{size=18} [Coin_Toss]{/size}"
            text "{size=18} [A_Rich_Happy_Family]{/size}"
            text "{size=18} [ElenaRescue]{/size}"
            text "{size=18} [QuantumPhysics]{/size}"

            text "{size=18} {/size}"

            text "{size=18} [Force_end_7c]{/size}"
            text "{size=18} [Hopeless_Dream_End]{/size}"
            text "{size=18} [True_end]{/size}"
            text "{size=18} [WAR_END_DEATH_OF_A_SPY]{/size}"
            text "{size=18} [WAR_END_REVOLUTION]{/size}"
            text "{size=18} [A_Rich_Happy_Family_end]{/size}"

    frame:
        xalign 0.02
        yalign 0.1
        vbox:
            text "{size=18} Elena_Point{/size}"
            text "{size=18} Azzurra_Point{/size}"
            text "{size=18} Azzurra_Persuasion{/size}"
            text "{size=18} Church{/size}"
            text "{size=18} Global_ParentPoint{/size}"
            text "{size=18} RescueTime {/size}"
            text "{size=18} Lohengramm {/size}"
            text "{size=18} Azu_Stays_With_Fre {/size}"
            text "{size=18} Hanes_Truth{/size}"
            text "{size=18} Ana_Defies_Han{/size}"
            text "{size=18} Coin_Toss {/size}"
            text "{size=18} A_Rich_Happy_Family{/size}"
            text "{size=18} ElenaRescue {/size}"
            text "{size=18} Quantum Physics {/size}"

            text "{size=18} {/size}"

            text "{size=18} Force_end_7c  {/size}"
            text "{size=18} Hopeless_Dream_End {/size}"
            text "{size=18} True_end           {/size}"
            text "{size=18} WAR_END_DEATH_OF_A_SPY {/size}"
            text "{size=18} WAR_END_REVOLUTION {/size}"
            text "{size=18} A_Rich_Happy_Family_end  {/size}"
    frame:
        xalign 0.95
        yalign 0.1
        vbox:
            if Sys_DCT_Progress >= 1:
                text "{size=15} prologue {/size}"
            if Sys_DCT_Progress >= 2:
                text "{size=15} Noted Ch 1 {/size}"
            if Sys_DCT_Progress >= 3:
                text "{size=15} Noted Ch 2 {/size}"
            if Sys_DCT_Progress >= 4:
                text "{size=15} Noted Ch 3 {/size}"
            if Sys_DCT_Progress >= 5:
                text "{size=15} Noted Ch 4 {/size}"
            if Sys_DCT_Progress >= 6:
                text "{size=15} Chapter 1 p1{/size}"
                hbox:
                    if Ch1P1_C1_played == 1:
                        text "{size=18}<>Ch1P1_C1_played{/size}"
                    if Ch1P1_C2_played == 1:
                        text "{size=18}<>Ch1P1_C2_played{/size}"
                    if Ch1P1_C3_played == 1:
                        text "{size=18}<>Ch1P1_C3_played{/size}"
                        if Ch1P1_C3C1 == 1:
                            text "{size=18}<>Ch1P1_C3C1{/size}"
                        if Ch1P1_C3C2 == 1:
                            text "{size=18}<>Ch1P1_C3C2{/size}"
            if Sys_DCT_Progress >= 7:
                text "{size=15} Chapter 1 p2 {/size}"
                hbox:
                    if Ch1P2B1_C1_played == 1:
                        text "{size=18}<>Ch1P2B1_C1_played{/size}"
                    if Ch1P2B1_C2_played == 1:
                        text "{size=18}<>Ch1P2B1_C2_played{/size}"
                    if Ch1P2B1_C3_played == 1:
                        text "{size=18}<>Ch1P2B1_C3_played{/size}"
                    if Ch1P2B1_C4_played == 1:
                        text "{size=18}<>Ch1P2B1_C4_played{/size}"
            if Sys_DCT_Progress >= 8:
                text "{size=15} Chapter 1 p3 {/size}"
                hbox:
                    if Ch1P3B2_C1_played == 1:
                        text "{size=18}<>Ch1P3B2_C1_played{/size}"
                    if Ch1P3B2_C2_played == 1:
                        text "{size=18}<>Ch1P3B2_C2_played{/size}"
                    if Ch1P3B2_C3_played == 1:
                        text "{size=18}<>Ch1P3B2_C3_played{/size}"
            if Sys_DCT_Progress >= 9:
                text "{size=15} Chapter 1 p4 {/size}"
            if Sys_DCT_Progress >= 10:
                text "{size=15} Chapter 1 p5 {/size}"
            if Sys_DCT_Progress >= 11:
                text "{size=15} Chapter 1 p6 {/size}"
            if Sys_DCT_Progress >= 12:
                text "{size=15} Chapter 2 p1 {/size}"
                hbox:
                    if Ch2P1_C1_played == 1:
                        text "{size=18}<>Ch2P1_C1_played{/size}"
                    if Ch2P1_C2_played == 1:
                        text "{size=18}<>Ch2P1_C2_played{/size}"
            if Sys_DCT_Progress >= 13:
                text "{size=15} Chapter 2 p2 {/size}"
            if Sys_DCT_Progress >= 14:
                text "{size=15} Chapter 2 p3 {/size}"
            if Sys_DCT_Progress >= 15:
                text "{size=15} Noted 2 {/size}"
            if Sys_DCT_Progress >= 16:
                text "{size=15} Chapter 3 p1 {/size}"
            if Sys_DCT_Progress >= 17:
                text "{size=15} Chapter 3 p2 {/size}"
            if Sys_DCT_Progress >= 18:
                text "{size=15} Chapter 4 p1 {/size}"
                hbox:
                    if Ch4P1_Choice1 == 1:
                        text "{size=18}<>Ch4p1c1_pld{/size}"
                    if Ch4P1_Choice1 == 2:
                        text "{size=18}<>Ch4p1c2_pld{/size}"
                    if Ch4P1_Choice1 == 3:
                        text "{size=18}<>Ch4p1c3_pld{/size}"
            if Sys_DCT_Progress >= 19:
                text "{size=15} Chapter 4 p2 {/size}"
            if Sys_DCT_Progress >= 20:
                text "{size=15} Chapter 4 p3 {/size}"
            if Sys_DCT_Progress >= 21:
                text "{size=15} Chapter 4 p4 {/size}"
            if Sys_DCT_Progress >= 22:
                text "{size=15} Noted 3 {/size}"
            if Sys_DCT_Progress >= 23:
                text "{size=15} Chapter 5 {/size}"
                hbox:
                    if Ch5_Choice1 == 1:
                        text "{size=18}<>Ch5C1c1_pld{/size}"
                    if Ch5_Choice1 == 2:
                        text "{size=18}<>Ch5C1c2_pld{/size}"
                    if Ch5_Choice1 == 3:
                        text "{size=18}<>Ch5C1c3_pld{/size}"
                    if Ch5_Choice2 == 1:
                        text "{size=18}<>Ch5C2c1_pld{/size}"
                    if Ch5_Choice2 == 2:
                        text "{size=18}<>Ch5C2c2_pld{/size}"
                    if Ch5_Choice2 == 3:
                        text "{size=18}<>Ch5C2c3_pld{/size}"
            if Sys_DCT_Progress >= 24:
                text "{size=15} Oth_House {/size}"
                hbox:
                    if Oth_House_Choice == 1:
                        text "{size=18}<>Oth_House_C1_pld{/size}"
                    if Oth_House_Choice == 2:
                        text "{size=18}<>Oth_House_C2_pld{/size}"
                    if Oth_House_Choice == 3:
                        text "{size=18}<>Oth_House_C3_pld{/size}"
            if Sys_DCT_Progress >= 25:
                text "{size=15} Azzurracorridor {/size}"
                hbox:
                    if Oth_AzuCor_Choice1 == 1:
                        text "{size=18}<>Oth_AzuCor_C1_Pld{/size}"
                    if Oth_AzuCor_Choice1 == 2:
                        text "{size=18}<>Oth_AzuCor_C2_Pld{/size}"
                    if Oth_AzuCor_Choice1 == 3:
                        text "{size=18}<>Oth_AzuCor_C3_Pld{/size}"
                    if Oth_AzuCor_Choice1 == 4:
                        text "{size=18}<>Oth_AzuCor_C4_Pld{/size}"
            if Sys_DCT_Progress >= 26:
                text "{size=15} Escape_p1 {/size}"
            if Sys_DCT_Progress >= 27:
                text "{size=15} Escape_p2 {/size}"
            if Sys_DCT_Progress >= 28:
                text "{size=15} EscapeB2B1 {/size}"
            if Sys_DCT_Progress >= 29:
                text "{size=15} Chapter 6 p1 {/size}"
                hbox:
                    if Ch6P2_Choice1 == 1:
                        text "{size=18}<>Ch6P2_Choice1 = 1{/size}"
                    if Ch6P2_Choice1 == 2:
                        text "{size=18}<>Ch6P2_Choice1 = 2{/size}"
                    if Ch6P2_Choice1 == 3:
                        text "{size=18}<>Ch6P2_Choice1 = 3{/size}"
            if Sys_DCT_Progress >= 30:
                text "{size=15} Chapter 6 p2 {/size}"
            if Sys_DCT_Progress >= 31:
                text "{size=15} Chapter 6 p3 {/size}"
                hbox:
                    if Ch6P3_Choice1 == 1:
                        text "{size=18}<>Ch6P3_Choice1 = 1{/size}"
                    if Ch6P3_Choice1 == 2:
                        text "{size=18}<>Ch6P3_Choice1 = 2{/size}"
                    if Ch6P3_Choice1 == 3:
                        text "{size=18}<>Ch6P3_Choice1 = 3{/size}"
            if Sys_DCT_Progress >= 32:
                text "{size=15} Chapter 6 p4 {/size}"