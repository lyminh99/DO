﻿screen Scr_Cls_All_Phase_04:

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if BS_AniPhase == 4:
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#///////////////////////  ATTACKER SLOT 1
            if A_S1_Cls == 1:
                if A_S1_CanEvd == "Evade_Rtn":
                    add "A_Cls01_Evd_Rtn" at A_S1_Eft_Cls_001
                elif A_S1_CanAct == "Return":
                    if A_S1_DmgType == "Melee":
                        add "A_Cls01_Atk_Melee_Return" at A_S1_Eft_Cls_001
                    elif A_S1_DmgType == "Range":
                        add "A_Cls01_Atk_Range_Return" at A_S1_Eft_Cls_001
                elif A_S1_CanAct == 0:
                    add "A_Cls01_Idl" at A_S1_Eft_Cls_001
                elif A_S1_CanAct == 1:
                    add "A_Cls01_Rdy" at A_S1_Eft_Cls_001
#--------------------------
            elif A_S1_Cls == 2:
                if A_S1_CanEvd == "Evade_Rtn":
                    add "A_Cls02_Evd_Rtn" at A_S1_Eft_Cls_002
                elif A_S1_CanAct == "Return":
                    if A_S1_DmgType == "Melee":
                        add "A_Cls02_Atk_Melee_Return" at A_S1_Eft_Cls_002
                    elif A_S1_DmgType == "Range":
                        add "A_Cls02_Atk_Range_Return" at A_S1_Eft_Cls_002
                elif A_S1_CanAct == 0:
                    add "A_Cls02_Idl" at A_S1_Eft_Cls_002
                elif A_S1_CanAct == 1:
                    add "A_Cls02_Rdy" at A_S1_Eft_Cls_002
#--------------------------
            elif A_S1_Cls == 3:
                if A_S1_CanEvd == "Evade_Rtn":
                    add "A_Cls03_Evd_Rtn" at A_S1_Eft_Cls_003
                elif A_S1_CanAct == "Return":
                    if A_S1_DmgType == "Melee":
                        add "A_Cls03_Atk_Melee_Return" at A_S1_Eft_Cls_003
                    elif A_S1_DmgType == "Range":
                        add "A_Cls03_Atk_Range_Return" at A_S1_Eft_Cls_003
                elif A_S1_CanAct == 0:
                    add "A_Cls03_Idl" at A_S1_Eft_Cls_003
                elif A_S1_CanAct == 1:
                    add "A_Cls03_Rdy" at A_S1_Eft_Cls_003
#--------------------------
            elif A_S1_Cls == 4:
                if A_S1_CanEvd == "Evade_Rtn":
                    add "A_Cls04_Evd_Rtn" at A_S1_Eft_Cls_004
                elif A_S1_CanAct == "Return":
                    if A_S1_DmgType == "Skill":
                        add "A_Cls04_Heal_Return" at A_S1_Eft_Cls_004
                elif A_S1_CanAct == 0:
                    add "A_Cls04_Idl" at A_S1_Eft_Cls_004
                elif A_S1_CanAct == 1:
                    add "A_Cls04_Rdy" at A_S1_Eft_Cls_004

#///////////////////////  ATTACKER SLOT 1
            if A_S2_Cls == 1:
                if A_S2_CanEvd == "Evade_Rtn":
                    add "A_Cls01_Evd_Rtn" at A_S2_Eft_Cls_001
                elif A_S2_CanAct == "Return":
                    if A_S2_DmgType == "Melee":
                        add "A_Cls01_Atk_Melee_Return" at A_S2_Eft_Cls_001
                    elif A_S2_DmgType == "Range":
                        add "A_Cls01_Atk_Range_Return" at A_S2_Eft_Cls_001
                elif A_S2_CanAct == 0:
                    add "A_Cls01_Idl" at A_S2_Eft_Cls_001
                elif A_S2_CanAct == 1:
                    add "A_Cls01_Rdy" at A_S2_Eft_Cls_001
#--------------------------
            elif A_S2_Cls == 2:
                if A_S2_CanEvd == "Evade_Rtn":
                    add "A_Cls02_Evd_Rtn" at A_S2_Eft_Cls_002
                elif A_S2_CanAct == "Return":
                    if A_S2_DmgType == "Melee":
                        add "A_Cls02_Atk_Melee_Return" at A_S2_Eft_Cls_002
                    elif A_S2_DmgType == "Range":
                        add "A_Cls02_Atk_Range_Return" at A_S2_Eft_Cls_002
                elif A_S2_CanAct == 0:
                    add "A_Cls02_Idl" at A_S2_Eft_Cls_002
                elif A_S2_CanAct == 1:
                    add "A_Cls02_Rdy" at A_S2_Eft_Cls_002
#--------------------------
            elif A_S2_Cls == 3:
                if A_S2_CanEvd == "Evade_Rtn":
                    add "A_Cls03_Evd_Rtn" at A_S2_Eft_Cls_003
                elif A_S2_CanAct == "Return":
                    if A_S2_DmgType == "Melee":
                        add "A_Cls03_Atk_Melee_Return" at A_S2_Eft_Cls_003
                    elif A_S2_DmgType == "Range":
                        add "A_Cls03_Atk_Range_Return" at A_S2_Eft_Cls_003
                elif A_S2_CanAct == 0:
                    add "A_Cls03_Idl" at A_S2_Eft_Cls_003
                elif A_S2_CanAct == 1:
                    add "A_Cls03_Rdy" at A_S2_Eft_Cls_003
#--------------------------
            elif A_S2_Cls == 4:
                if A_S2_CanEvd == "Evade_Rtn":
                    add "A_Cls04_Evd_Rtn" at A_S2_Eft_Cls_004
                elif A_S2_CanAct == "Return":
                    if A_S2_DmgType == "Skill":
                        add "A_Cls04_Heal_Return" at A_S2_Eft_Cls_004
                elif A_S2_CanAct == 0:
                    add "A_Cls04_Idl" at A_S2_Eft_Cls_004
                elif A_S2_CanAct == 1:
                    add "A_Cls04_Rdy" at A_S2_Eft_Cls_004

#///////////////////////  ATTACKER SLOT 1
            if A_S3_Cls == 1:
                if A_S3_CanEvd == "Evade_Rtn":
                    add "A_Cls01_Evd_Rtn" at A_S3_Eft_Cls_001
                elif A_S3_CanAct == "Return":
                    if A_S3_DmgType == "Melee":
                        add "A_Cls01_Atk_Melee_Return" at A_S3_Eft_Cls_001
                    elif A_S3_DmgType == "Range":
                        add "A_Cls01_Atk_Range_Return" at A_S3_Eft_Cls_001
                elif A_S3_CanAct == 0:
                    add "A_Cls01_Idl" at A_S3_Eft_Cls_001
                elif A_S3_CanAct == 1:
                    add "A_Cls01_Rdy" at A_S3_Eft_Cls_001
#--------------------------
            elif A_S3_Cls == 2:
                if A_S3_CanEvd == "Evade_Rtn":
                    add "A_Cls02_Evd_Rtn" at A_S3_Eft_Cls_002
                elif A_S3_CanAct == "Return":
                    if A_S3_DmgType == "Melee":
                        add "A_Cls02_Atk_Melee_Return" at A_S3_Eft_Cls_002
                    elif A_S3_DmgType == "Range":
                        add "A_Cls02_Atk_Range_Return" at A_S3_Eft_Cls_002
                elif A_S3_CanAct == 0:
                    add "A_Cls02_Idl" at A_S3_Eft_Cls_002
                elif A_S3_CanAct == 1:
                    add "A_Cls02_Rdy" at A_S3_Eft_Cls_002
#--------------------------
            elif A_S3_Cls == 3:
                if A_S3_CanEvd == "Evade_Rtn":
                    add "A_Cls03_Evd_Rtn" at A_S3_Eft_Cls_003
                elif A_S3_CanAct == "Return":
                    if A_S3_DmgType == "Melee":
                        add "A_Cls03_Atk_Melee_Return" at A_S3_Eft_Cls_003
                    elif A_S3_DmgType == "Range":
                        add "A_Cls03_Atk_Range_Return" at A_S3_Eft_Cls_003
                elif A_S3_CanAct == 0:
                    add "A_Cls03_Idl" at A_S3_Eft_Cls_003
                elif A_S3_CanAct == 1:
                    add "A_Cls03_Rdy" at A_S3_Eft_Cls_003
#--------------------------
            elif A_S3_Cls == 4:
                if A_S3_CanEvd == "Evade_Rtn":
                    add "A_Cls04_Evd_Rtn" at A_S3_Eft_Cls_004
                elif A_S3_CanAct == "Return":
                    if A_S3_DmgType == "Skill":
                        add "A_Cls04_Heal_Return" at A_S3_Eft_Cls_004
                elif A_S3_CanAct == 0:
                    add "A_Cls04_Idl" at A_S3_Eft_Cls_004
                elif A_S3_CanAct == 1:
                    add "A_Cls04_Rdy" at A_S3_Eft_Cls_004

#///////////////////////  ATTACKER SLOT 1
            if A_S4_Cls == 1:
                if A_S4_CanEvd == "Evade_Rtn":
                    add "A_Cls01_Evd_Rtn" at A_S4_Eft_Cls_001
                elif A_S4_CanAct == "Return":
                    if A_S4_DmgType == "Melee":
                        add "A_Cls01_Atk_Melee_Return" at A_S4_Eft_Cls_001
                    elif A_S4_DmgType == "Range":
                        add "A_Cls01_Atk_Range_Return" at A_S4_Eft_Cls_001
                elif A_S4_CanAct == 0:
                    add "A_Cls01_Idl" at A_S4_Eft_Cls_001
                elif A_S4_CanAct == 1:
                    add "A_Cls01_Rdy" at A_S4_Eft_Cls_001
#--------------------------
            elif A_S4_Cls == 2:
                if A_S4_CanEvd == "Evade_Rtn":
                    add "A_Cls02_Evd_Rtn" at A_S4_Eft_Cls_002
                elif A_S4_CanAct == "Return":
                    if A_S4_DmgType == "Melee":
                        add "A_Cls02_Atk_Melee_Return" at A_S4_Eft_Cls_002
                    elif A_S4_DmgType == "Range":
                        add "A_Cls02_Atk_Range_Return" at A_S4_Eft_Cls_002
                elif A_S4_CanAct == 0:
                    add "A_Cls02_Idl" at A_S4_Eft_Cls_002
                elif A_S4_CanAct == 1:
                    add "A_Cls02_Rdy" at A_S4_Eft_Cls_002
#--------------------------
            elif A_S4_Cls == 3:
                if A_S4_CanEvd == "Evade_Rtn":
                    add "A_Cls03_Evd_Rtn" at A_S4_Eft_Cls_003
                elif A_S4_CanAct == "Return":
                    if A_S4_DmgType == "Melee":
                        add "A_Cls03_Atk_Melee_Return" at A_S4_Eft_Cls_003
                    elif A_S4_DmgType == "Range":
                        add "A_Cls03_Atk_Range_Return" at A_S4_Eft_Cls_003
                elif A_S4_CanAct == 0:
                    add "A_Cls03_Idl" at A_S4_Eft_Cls_003
                elif A_S4_CanAct == 1:
                    add "A_Cls03_Rdy" at A_S4_Eft_Cls_003
#--------------------------
            elif A_S4_Cls == 4:
                if A_S4_CanEvd == "Evade_Rtn":
                    add "A_Cls04_Evd_Rtn" at A_S4_Eft_Cls_004
                elif A_S4_CanAct == "Return":
                    if A_S4_DmgType == "Skill":
                        add "A_Cls04_Heal_Return" at A_S4_Eft_Cls_004
                elif A_S4_CanAct == 0:
                    add "A_Cls04_Idl" at A_S4_Eft_Cls_004
                elif A_S4_CanAct == 1:
                    add "A_Cls04_Rdy" at A_S4_Eft_Cls_004

#///////////////////////  ATTACKER SLOT 1
            if A_S5_Cls == 1:
                if A_S5_CanEvd == "Evade_Rtn":
                    add "A_Cls01_Evd_Rtn" at A_S5_Eft_Cls_001
                elif A_S5_CanAct == "Return":
                    if A_S5_DmgType == "Melee":
                        add "A_Cls01_Atk_Melee_Return" at A_S5_Eft_Cls_001
                    elif A_S5_DmgType == "Range":
                        add "A_Cls01_Atk_Range_Return" at A_S5_Eft_Cls_001
                elif A_S5_CanAct == 0:
                    add "A_Cls01_Idl" at A_S5_Eft_Cls_001
                elif A_S5_CanAct == 1:
                    add "A_Cls01_Rdy" at A_S5_Eft_Cls_001
#--------------------------
            elif A_S5_Cls == 2:
                if A_S5_CanEvd == "Evade_Rtn":
                    add "A_Cls02_Evd_Rtn" at A_S5_Eft_Cls_002
                elif A_S5_CanAct == "Return":
                    if A_S5_DmgType == "Melee":
                        add "A_Cls02_Atk_Melee_Return" at A_S5_Eft_Cls_002
                    elif A_S5_DmgType == "Range":
                        add "A_Cls02_Atk_Range_Return" at A_S5_Eft_Cls_002
                elif A_S5_CanAct == 0:
                    add "A_Cls02_Idl" at A_S5_Eft_Cls_002
                elif A_S5_CanAct == 1:
                    add "A_Cls02_Rdy" at A_S5_Eft_Cls_002
#--------------------------
            elif A_S5_Cls == 3:
                if A_S5_CanEvd == "Evade_Rtn":
                    add "A_Cls03_Evd_Rtn" at A_S5_Eft_Cls_003
                elif A_S5_CanAct == "Return":
                    if A_S5_DmgType == "Melee":
                        add "A_Cls03_Atk_Melee_Return" at A_S5_Eft_Cls_003
                    elif A_S5_DmgType == "Range":
                        add "A_Cls03_Atk_Range_Return" at A_S5_Eft_Cls_003
                elif A_S5_CanAct == 0:
                    add "A_Cls03_Idl" at A_S5_Eft_Cls_003
                elif A_S5_CanAct == 1:
                    add "A_Cls03_Rdy" at A_S5_Eft_Cls_003
#--------------------------
            elif A_S5_Cls == 4:
                if A_S5_CanEvd == "Evade_Rtn":
                    add "A_Cls04_Evd_Rtn" at A_S5_Eft_Cls_004
                elif A_S5_CanAct == "Return":
                    if A_S5_DmgType == "Skill":
                        add "A_Cls04_Heal_Return" at A_S5_Eft_Cls_004
                elif A_S5_CanAct == 0:
                    add "A_Cls04_Idl" at A_S5_Eft_Cls_004
                elif A_S5_CanAct == 1:
                    add "A_Cls04_Rdy" at A_S5_Eft_Cls_004

#///////////////////////  ATTACKER SLOT 1
            if A_S6_Cls == 1:
                if A_S6_CanEvd == "Evade_Rtn":
                    add "A_Cls01_Evd_Rtn" at A_S6_Eft_Cls_001
                elif A_S6_CanAct == "Return":
                    if A_S6_DmgType == "Melee":
                        add "A_Cls01_Atk_Melee_Return" at A_S6_Eft_Cls_001
                    elif A_S6_DmgType == "Range":
                        add "A_Cls01_Atk_Range_Return" at A_S6_Eft_Cls_001
                elif A_S6_CanAct == 0:
                    add "A_Cls01_Idl" at A_S6_Eft_Cls_001
                elif A_S6_CanAct == 1:
                    add "A_Cls01_Rdy" at A_S6_Eft_Cls_001
#--------------------------
            elif A_S6_Cls == 2:
                if A_S6_CanEvd == "Evade_Rtn":
                    add "A_Cls02_Evd_Rtn" at A_S6_Eft_Cls_002
                elif A_S6_CanAct == "Return":
                    if A_S6_DmgType == "Melee":
                        add "A_Cls02_Atk_Melee_Return" at A_S6_Eft_Cls_002
                    elif A_S6_DmgType == "Range":
                        add "A_Cls02_Atk_Range_Return" at A_S6_Eft_Cls_002
                elif A_S6_CanAct == 0:
                    add "A_Cls02_Idl" at A_S6_Eft_Cls_002
                elif A_S6_CanAct == 1:
                    add "A_Cls02_Rdy" at A_S6_Eft_Cls_002
#--------------------------
            elif A_S6_Cls == 3:
                if A_S6_CanEvd == "Evade_Rtn":
                    add "A_Cls03_Evd_Rtn" at A_S6_Eft_Cls_003
                elif A_S6_CanAct == "Return":
                    if A_S6_DmgType == "Melee":
                        add "A_Cls03_Atk_Melee_Return" at A_S6_Eft_Cls_003
                    elif A_S6_DmgType == "Range":
                        add "A_Cls03_Atk_Range_Return" at A_S6_Eft_Cls_003
                elif A_S6_CanAct == 0:
                    add "A_Cls03_Idl" at A_S6_Eft_Cls_003
                elif A_S6_CanAct == 1:
                    add "A_Cls03_Rdy" at A_S6_Eft_Cls_003
#--------------------------
            elif A_S6_Cls == 4:
                if A_S6_CanEvd == "Evade_Rtn":
                    add "A_Cls04_Evd_Rtn" at A_S6_Eft_Cls_004
                elif A_S6_CanAct == "Return":
                    if A_S6_DmgType == "Skill":
                        add "A_Cls04_Heal_Return" at A_S6_Eft_Cls_004
                elif A_S6_CanAct == 0:
                    add "A_Cls04_Idl" at A_S6_Eft_Cls_004
                elif A_S6_CanAct == 1:
                    add "A_Cls04_Rdy" at A_S6_Eft_Cls_004

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
            if D_S1_Cls == 1:
                if D_S1_CanEvd == "Evade_Rtn":
                    add "D_Cls01_Evd_Rtn" at D_S1_Eft_Cls_001
                elif D_S1_CanAct == "Return":
                    if D_S1_DmgType == "Melee":
                        add "D_Cls01_Atk_Melee_Return" at D_S1_Eft_Cls_001
                    elif D_S1_DmgType == "Range":
                        add "D_Cls01_Atk_Range_Return" at D_S1_Eft_Cls_001
                elif D_S1_CanAct == 0:
                    add "D_Cls01_Idl" at D_S1_Eft_Cls_001
                elif D_S1_CanAct == 1:
                    add "D_Cls01_Rdy" at D_S1_Eft_Cls_001
#--------------------------
            elif D_S1_Cls == 2:
                if D_S1_CanEvd == "Evade_Rtn":
                    add "D_Cls02_Evd_Rtn" at D_S1_Eft_Cls_002
                elif D_S1_CanAct == "Return":
                    if D_S1_DmgType == "Melee":
                        add "D_Cls02_Atk_Melee_Return" at D_S1_Eft_Cls_002
                    elif D_S1_DmgType == "Range":
                        add "D_Cls02_Atk_Range_Return" at D_S1_Eft_Cls_002
                elif D_S1_CanAct == 0:
                    add "D_Cls02_Idl" at D_S1_Eft_Cls_002
                elif D_S1_CanAct == 1:
                    add "D_Cls02_Rdy" at D_S1_Eft_Cls_002
#--------------------------
            elif D_S1_Cls == 3:
                if D_S1_CanEvd == "Evade_Rtn":
                    add "D_Cls03_Evd_Rtn" at D_S1_Eft_Cls_003
                elif D_S1_CanAct == "Return":
                    if D_S1_DmgType == "Melee":
                        add "D_Cls03_Atk_Melee_Return" at D_S1_Eft_Cls_003
                    elif D_S1_DmgType == "Range":
                        add "D_Cls03_Atk_Range_Return" at D_S1_Eft_Cls_003
                elif D_S1_CanAct == 0:
                    add "D_Cls03_Idl" at D_S1_Eft_Cls_003
                elif D_S1_CanAct == 1:
                    add "D_Cls03_Rdy" at D_S1_Eft_Cls_003
#--------------------------
            elif D_S1_Cls == 4:
                if D_S1_CanEvd == "Evade_Rtn":
                    add "D_Cls04_Evd_Rtn" at D_S1_Eft_Cls_004
                elif D_S1_CanAct == "Return":
                    if D_S1_DmgType == "Skill":
                        add "D_Cls04_Heal_Return" at D_S1_Eft_Cls_004
                elif D_S1_CanAct == 0:
                    add "D_Cls04_Idl" at D_S1_Eft_Cls_004
                elif D_S1_CanAct == 1:
                    add "D_Cls04_Rdy" at D_S1_Eft_Cls_004

#///////////////////////  DEFFENDER SLOT 1
            if D_S2_Cls == 1:
                if D_S2_CanEvd == "Evade_Rtn":
                    add "D_Cls01_Evd_Rtn" at D_S2_Eft_Cls_001
                elif D_S2_CanAct == "Return":
                    if D_S2_DmgType == "Melee":
                        add "D_Cls01_Atk_Melee_Return" at D_S2_Eft_Cls_001
                    elif D_S2_DmgType == "Range":
                        add "D_Cls01_Atk_Range_Return" at D_S2_Eft_Cls_001
                elif D_S2_CanAct == 0:
                    add "D_Cls01_Idl" at D_S2_Eft_Cls_001
                elif D_S2_CanAct == 1:
                    add "D_Cls01_Rdy" at D_S2_Eft_Cls_001
#--------------------------
            elif D_S2_Cls == 2:
                if D_S2_CanEvd == "Evade_Rtn":
                    add "D_Cls02_Evd_Rtn" at D_S2_Eft_Cls_002
                elif D_S2_CanAct == "Return":
                    if D_S2_DmgType == "Melee":
                        add "D_Cls02_Atk_Melee_Return" at D_S2_Eft_Cls_002
                    elif D_S2_DmgType == "Range":
                        add "D_Cls02_Atk_Range_Return" at D_S2_Eft_Cls_002
                elif D_S2_CanAct == 0:
                    add "D_Cls02_Idl" at D_S2_Eft_Cls_002
                elif D_S2_CanAct == 1:
                    add "D_Cls02_Rdy" at D_S2_Eft_Cls_002
#--------------------------
            elif D_S2_Cls == 3:
                if D_S2_CanEvd == "Evade_Rtn":
                    add "D_Cls03_Evd_Rtn" at D_S2_Eft_Cls_003
                elif D_S2_CanAct == "Return":
                    if D_S2_DmgType == "Melee":
                        add "D_Cls03_Atk_Melee_Return" at D_S2_Eft_Cls_003
                    elif D_S2_DmgType == "Range":
                        add "D_Cls03_Atk_Range_Return" at D_S2_Eft_Cls_003
                elif D_S2_CanAct == 0:
                    add "D_Cls03_Idl" at D_S2_Eft_Cls_003
                elif D_S2_CanAct == 1:
                    add "D_Cls03_Rdy" at D_S2_Eft_Cls_003
#--------------------------
            elif D_S2_Cls == 4:
                if D_S2_CanEvd == "Evade_Rtn":
                    add "D_Cls04_Evd_Rtn" at D_S2_Eft_Cls_004
                elif D_S2_CanAct == "Return":
                    if D_S2_DmgType == "Skill":
                        add "D_Cls04_Heal_Return" at D_S2_Eft_Cls_004
                elif D_S2_CanAct == 0:
                    add "D_Cls04_Idl" at D_S2_Eft_Cls_004
                elif D_S2_CanAct == 1:
                    add "D_Cls04_Rdy" at D_S2_Eft_Cls_004

#///////////////////////  DEFFENDER SLOT 1
            if D_S3_Cls == 1:
                if D_S3_CanEvd == "Evade_Rtn":
                    add "D_Cls01_Evd_Rtn" at D_S3_Eft_Cls_001
                elif D_S3_CanAct == "Return":
                    if D_S3_DmgType == "Melee":
                        add "D_Cls01_Atk_Melee_Return" at D_S3_Eft_Cls_001
                    elif D_S3_DmgType == "Range":
                        add "D_Cls01_Atk_Range_Return" at D_S3_Eft_Cls_001
                elif D_S3_CanAct == 0:
                    add "D_Cls01_Idl" at D_S3_Eft_Cls_001
                elif D_S3_CanAct == 1:
                    add "D_Cls01_Rdy" at D_S3_Eft_Cls_001
#--------------------------
            elif D_S3_Cls == 2:
                if D_S3_CanEvd == "Evade_Rtn":
                    add "D_Cls02_Evd_Rtn" at D_S3_Eft_Cls_002
                elif D_S3_CanAct == "Return":
                    if D_S3_DmgType == "Melee":
                        add "D_Cls02_Atk_Melee_Return" at D_S3_Eft_Cls_002
                    elif D_S3_DmgType == "Range":
                        add "D_Cls02_Atk_Range_Return" at D_S3_Eft_Cls_002
                elif D_S3_CanAct == 0:
                    add "D_Cls02_Idl" at D_S3_Eft_Cls_002
                elif D_S3_CanAct == 1:
                    add "D_Cls02_Rdy" at D_S3_Eft_Cls_002
#--------------------------
            elif D_S3_Cls == 3:
                if D_S3_CanEvd == "Evade_Rtn":
                    add "D_Cls03_Evd_Rtn" at D_S3_Eft_Cls_003
                elif D_S3_CanAct == "Return":
                    if D_S3_DmgType == "Melee":
                        add "D_Cls03_Atk_Melee_Return" at D_S3_Eft_Cls_003
                    elif D_S3_DmgType == "Range":
                        add "D_Cls03_Atk_Range_Return" at D_S3_Eft_Cls_003
                elif D_S3_CanAct == 0:
                    add "D_Cls03_Idl" at D_S3_Eft_Cls_003
                elif D_S3_CanAct == 1:
                    add "D_Cls03_Rdy" at D_S3_Eft_Cls_003
#--------------------------
            elif D_S3_Cls == 4:
                if D_S3_CanEvd == "Evade_Rtn":
                    add "D_Cls04_Evd_Rtn" at D_S3_Eft_Cls_004
                elif D_S3_CanAct == "Return":
                    if D_S3_DmgType == "Skill":
                        add "D_Cls04_Heal_Return" at D_S3_Eft_Cls_004
                elif D_S3_CanAct == 0:
                    add "D_Cls04_Idl" at D_S3_Eft_Cls_004
                elif D_S3_CanAct == 1:
                    add "D_Cls04_Rdy" at D_S3_Eft_Cls_004

#///////////////////////  DEFFENDER SLOT 1
            if D_S4_Cls == 1:
                if D_S4_CanEvd == "Evade_Rtn":
                    add "D_Cls01_Evd_Rtn" at D_S4_Eft_Cls_001
                elif D_S4_CanAct == "Return":
                    if D_S4_DmgType == "Melee":
                        add "D_Cls01_Atk_Melee_Return" at D_S4_Eft_Cls_001
                    elif D_S4_DmgType == "Range":
                        add "D_Cls01_Atk_Range_Return" at D_S4_Eft_Cls_001
                elif D_S4_CanAct == 0:
                    add "D_Cls01_Idl" at D_S4_Eft_Cls_001
                elif D_S4_CanAct == 1:
                    add "D_Cls01_Rdy" at D_S4_Eft_Cls_001
#--------------------------
            elif D_S4_Cls == 2:
                if D_S4_CanEvd == "Evade_Rtn":
                    add "D_Cls02_Evd_Rtn" at D_S4_Eft_Cls_002
                elif D_S4_CanAct == "Return":
                    if D_S4_DmgType == "Melee":
                        add "D_Cls02_Atk_Melee_Return" at D_S4_Eft_Cls_002
                    elif D_S4_DmgType == "Range":
                        add "D_Cls02_Atk_Range_Return" at D_S4_Eft_Cls_002
                elif D_S4_CanAct == 0:
                    add "D_Cls02_Idl" at D_S4_Eft_Cls_002
                elif D_S4_CanAct == 1:
                    add "D_Cls02_Rdy" at D_S4_Eft_Cls_002
#--------------------------
            elif D_S4_Cls == 3:
                if D_S4_CanEvd == "Evade_Rtn":
                    add "D_Cls03_Evd_Rtn" at D_S4_Eft_Cls_003
                elif D_S4_CanAct == "Return":
                    if D_S4_DmgType == "Melee":
                        add "D_Cls03_Atk_Melee_Return" at D_S4_Eft_Cls_003
                    elif D_S4_DmgType == "Range":
                        add "D_Cls03_Atk_Range_Return" at D_S4_Eft_Cls_003
                elif D_S4_CanAct == 0:
                    add "D_Cls03_Idl" at D_S4_Eft_Cls_003
                elif D_S4_CanAct == 1:
                    add "D_Cls03_Rdy" at D_S4_Eft_Cls_003
#--------------------------
            elif D_S4_Cls == 4:
                if D_S4_CanEvd == "Evade_Rtn":
                    add "D_Cls04_Evd_Rtn" at D_S4_Eft_Cls_004
                elif D_S4_CanAct == "Return":
                    if D_S4_DmgType == "Skill":
                        add "D_Cls04_Heal_Return" at D_S4_Eft_Cls_004
                elif D_S4_CanAct == 0:
                    add "D_Cls04_Idl" at D_S4_Eft_Cls_004
                elif D_S4_CanAct == 1:
                    add "D_Cls04_Rdy" at D_S4_Eft_Cls_004

#///////////////////////  DEFFENDER SLOT 1
            if D_S5_Cls == 1:
                if D_S5_CanEvd == "Evade_Rtn":
                    add "D_Cls01_Evd_Rtn" at D_S5_Eft_Cls_001
                elif D_S5_CanAct == "Return":
                    if D_S5_DmgType == "Melee":
                        add "D_Cls01_Atk_Melee_Return" at D_S5_Eft_Cls_001
                    elif D_S5_DmgType == "Range":
                        add "D_Cls01_Atk_Range_Return" at D_S5_Eft_Cls_001
                elif D_S5_CanAct == 0:
                    add "D_Cls01_Idl" at D_S5_Eft_Cls_001
                elif D_S5_CanAct == 1:
                    add "D_Cls01_Rdy" at D_S5_Eft_Cls_001
#--------------------------
            elif D_S5_Cls == 2:
                if D_S5_CanEvd == "Evade_Rtn":
                    add "D_Cls02_Evd_Rtn" at D_S5_Eft_Cls_002
                elif D_S5_CanAct == "Return":
                    if D_S5_DmgType == "Melee":
                        add "D_Cls02_Atk_Melee_Return" at D_S5_Eft_Cls_002
                    elif D_S5_DmgType == "Range":
                        add "D_Cls02_Atk_Range_Return" at D_S5_Eft_Cls_002
                elif D_S5_CanAct == 0:
                    add "D_Cls02_Idl" at D_S5_Eft_Cls_002
                elif D_S5_CanAct == 1:
                    add "D_Cls02_Rdy" at D_S5_Eft_Cls_002
#--------------------------
            elif D_S5_Cls == 3:
                if D_S5_CanEvd == "Evade_Rtn":
                    add "D_Cls03_Evd_Rtn" at D_S5_Eft_Cls_003
                elif D_S5_CanAct == "Return":
                    if D_S5_DmgType == "Melee":
                        add "D_Cls03_Atk_Melee_Return" at D_S5_Eft_Cls_003
                    elif D_S5_DmgType == "Range":
                        add "D_Cls03_Atk_Range_Return" at D_S5_Eft_Cls_003
                elif D_S5_CanAct == 0:
                    add "D_Cls03_Idl" at D_S5_Eft_Cls_003
                elif D_S5_CanAct == 1:
                    add "D_Cls03_Rdy" at D_S5_Eft_Cls_003
#--------------------------
            elif D_S5_Cls == 4:
                if D_S5_CanEvd == "Evade_Rtn":
                    add "D_Cls04_Evd_Rtn" at D_S5_Eft_Cls_004
                elif D_S5_CanAct == "Return":
                    if D_S5_DmgType == "Skill":
                        add "D_Cls04_Heal_Return" at D_S5_Eft_Cls_004
                elif D_S5_CanAct == 0:
                    add "D_Cls04_Idl" at D_S5_Eft_Cls_004
                elif D_S5_CanAct == 1:
                    add "D_Cls04_Rdy" at D_S5_Eft_Cls_004

#///////////////////////  DEFFENDER SLOT 1
            if D_S6_Cls == 1:
                if D_S6_CanEvd == "Evade_Rtn":
                    add "D_Cls01_Evd_Rtn" at D_S6_Eft_Cls_001
                elif D_S6_CanAct == "Return":
                    if D_S6_DmgType == "Melee":
                        add "D_Cls01_Atk_Melee_Return" at D_S6_Eft_Cls_001
                    elif D_S6_DmgType == "Range":
                        add "D_Cls01_Atk_Range_Return" at D_S6_Eft_Cls_001
                elif D_S6_CanAct == 0:
                    add "D_Cls01_Idl" at D_S6_Eft_Cls_001
                elif D_S6_CanAct == 1:
                    add "D_Cls01_Rdy" at D_S6_Eft_Cls_001
#--------------------------
            elif D_S6_Cls == 2:
                if D_S6_CanEvd == "Evade_Rtn":
                    add "D_Cls02_Evd_Rtn" at D_S6_Eft_Cls_002
                elif D_S6_CanAct == "Return":
                    if D_S6_DmgType == "Melee":
                        add "D_Cls02_Atk_Melee_Return" at D_S6_Eft_Cls_002
                    elif D_S6_DmgType == "Range":
                        add "D_Cls02_Atk_Range_Return" at D_S6_Eft_Cls_002
                elif D_S6_CanAct == 0:
                    add "D_Cls02_Idl" at D_S6_Eft_Cls_002
                elif D_S6_CanAct == 1:
                    add "D_Cls02_Rdy" at D_S6_Eft_Cls_002
#--------------------------
            elif D_S6_Cls == 3:
                if D_S6_CanEvd == "Evade_Rtn":
                    add "D_Cls03_Evd_Rtn" at D_S6_Eft_Cls_003
                elif D_S6_CanAct == "Return":
                    if D_S6_DmgType == "Melee":
                        add "D_Cls03_Atk_Melee_Return" at D_S6_Eft_Cls_003
                    elif D_S6_DmgType == "Range":
                        add "D_Cls03_Atk_Range_Return" at D_S6_Eft_Cls_003
                elif D_S6_CanAct == 0:
                    add "D_Cls03_Idl" at D_S6_Eft_Cls_003
                elif D_S6_CanAct == 1:
                    add "D_Cls03_Rdy" at D_S6_Eft_Cls_003
#--------------------------
            elif D_S6_Cls == 4:
                if D_S6_CanEvd == "Evade_Rtn":
                    add "D_Cls04_Evd_Rtn" at D_S6_Eft_Cls_004
                elif D_S6_CanAct == "Return":
                    if D_S6_DmgType == "Skill":
                        add "D_Cls04_Heal_Return" at D_S6_Eft_Cls_004
                elif D_S6_CanAct == 0:
                    add "D_Cls04_Idl" at D_S6_Eft_Cls_004
                elif D_S6_CanAct == 1:
                    add "D_Cls04_Rdy" at D_S6_Eft_Cls_004
