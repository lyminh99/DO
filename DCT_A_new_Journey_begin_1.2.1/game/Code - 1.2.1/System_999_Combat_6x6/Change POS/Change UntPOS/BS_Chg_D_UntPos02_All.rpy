﻿
#=====================================================
label BS_Chg_D_UntPos02_01:
#=====================================================
#-------------------------------
    call BS_Update_D_S2_UntStorePOS
    call BS_Update_D_S1_UntStorePOS
#-------------------------------
    $ D_S2_Ctl_Type = D_S1_UntStorePOS [0]
    $ D_S2_Reg_No = D_S1_UntStorePOS [1]
    $ D_S2_Name = D_S1_UntStorePOS [2]
    $ D_S2_Level = D_S1_UntStorePOS [3]
    $ D_S2_Exp = D_S1_UntStorePOS [4]
    $ D_S2_MHP = D_S1_UntStorePOS [5]
    $ D_S2_HP = D_S1_UntStorePOS [6]
    $ D_S2_Atk = D_S1_UntStorePOS [7]
    $ D_S2_Mag = D_S1_UntStorePOS [8]
    $ D_S2_Def = D_S1_UntStorePOS [9]
    $ D_S2_Res = D_S1_UntStorePOS [10]
    $ D_S2_Spd = D_S1_UntStorePOS [11] 
    $ D_S2_Cls = D_S1_UntStorePOS [12]
    $ D_S2_Ttc = D_S1_UntStorePOS [13]
    $ D_S2_Ocu = D_S1_UntStorePOS [14]
    $ D_S2_CanAct = D_S1_UntStorePOS [15]
    $ D_S2_Mor = D_S1_UntStorePOS [16]
    $ D_S2_Fgt = D_S1_UntStorePOS [17]
    $ D_S2_Stn = D_S1_UntStorePOS [18]
    $ D_S2_AtkType = D_S1_UntStorePOS [19]
    $ D_S2_DefType = D_S1_UntStorePOS [20]
    $ D_S2_CrtChc = D_S1_UntStorePOS [21]
    $ D_S2_EvdChc = D_S1_UntStorePOS [22]
    $ D_S2_DuelChc = D_S1_UntStorePOS [23]
    $ D_S2_DuelEvd = D_S1_UntStorePOS [24]
    $ D_S2_AtkIcr = D_S1_UntStorePOS [25]
    $ D_S2_AtkDcr = D_S1_UntStorePOS [26]
    $ D_S2_AtkChg = D_S1_UntStorePOS [27]
    $ D_S2_DefIcr = D_S1_UntStorePOS [28]
    $ D_S2_DefDcr = D_S1_UntStorePOS [29]
    $ D_S2_DefChg = D_S1_UntStorePOS [30]
    $ D_S2_MorIcr = D_S1_UntStorePOS [31]
    $ D_S2_MorDcr = D_S1_UntStorePOS [32]
    $ D_S2_MorChg = D_S1_UntStorePOS [33]
    $ D_S2_Kill = D_S1_UntStorePOS [34]
    $ D_S2_Killed = D_S1_UntStorePOS [35]
    $ D_S2_ChgTtc_Count = D_S1_UntStorePOS [36]
    $ D_S2_ChgPos_Count = D_S1_UntStorePOS [37]
#-------------------------------
#-------------------------------
    $ D_S1_Ctl_Type = D_S2_UntStorePOS [0]
    $ D_S1_Reg_No = D_S2_UntStorePOS [1]
    $ D_S1_Name = D_S2_UntStorePOS [2]
    $ D_S1_Level = D_S2_UntStorePOS [3]
    $ D_S1_Exp = D_S2_UntStorePOS [4]
    $ D_S1_MHP = D_S2_UntStorePOS [5]
    $ D_S1_HP = D_S2_UntStorePOS [6]
    $ D_S1_Atk = D_S2_UntStorePOS [7]
    $ D_S1_Mag = D_S2_UntStorePOS [8]
    $ D_S1_Def = D_S2_UntStorePOS [9]
    $ D_S1_Res = D_S2_UntStorePOS [10]
    $ D_S1_Spd = D_S2_UntStorePOS [11] 
    $ D_S1_Cls = D_S2_UntStorePOS [12]
    $ D_S1_Ttc = D_S2_UntStorePOS [13]
    $ D_S1_Ocu = D_S2_UntStorePOS [14]
    $ D_S1_CanAct = D_S2_UntStorePOS [15]
    $ D_S1_Mor = D_S2_UntStorePOS [16]
    $ D_S1_Fgt = D_S2_UntStorePOS [17]
    $ D_S1_Stn = D_S2_UntStorePOS [18]
    $ D_S1_AtkType = D_S2_UntStorePOS [19]
    $ D_S1_DefType = D_S2_UntStorePOS [20]
    $ D_S1_CrtChc = D_S2_UntStorePOS [21]
    $ D_S1_EvdChc = D_S2_UntStorePOS [22]
    $ D_S1_DuelChc = D_S2_UntStorePOS [23]
    $ D_S1_DuelEvd = D_S2_UntStorePOS [24]
    $ D_S1_AtkIcr = D_S2_UntStorePOS [25]
    $ D_S1_AtkDcr = D_S2_UntStorePOS [26]
    $ D_S1_AtkChg = D_S2_UntStorePOS [27]
    $ D_S1_DefIcr = D_S2_UntStorePOS [28]
    $ D_S1_DefDcr = D_S2_UntStorePOS [29]
    $ D_S1_DefChg = D_S2_UntStorePOS [30]
    $ D_S1_MorIcr = D_S2_UntStorePOS [31]
    $ D_S1_MorDcr = D_S2_UntStorePOS [32]
    $ D_S1_MorChg = D_S2_UntStorePOS [33]
    $ D_S1_Kill = D_S2_UntStorePOS [34]
    $ D_S1_Killed = D_S2_UntStorePOS [35]
    $ D_S1_ChgTtc_Count = D_S2_UntStorePOS [36]
    $ D_S1_ChgPos_Count = D_S2_UntStorePOS [37]
#-------------------------------
    return

#=====================================================
label BS_Chg_D_UntPos02_03:
#=====================================================
#-------------------------------
    call BS_Update_D_S2_UntStorePOS
    call BS_Update_D_S3_UntStorePOS
#-------------------------------
    $ D_S2_Ctl_Type = D_S3_UntStorePOS [0]
    $ D_S2_Reg_No = D_S3_UntStorePOS [1]
    $ D_S2_Name = D_S3_UntStorePOS [2]
    $ D_S2_Level = D_S3_UntStorePOS [3]
    $ D_S2_Exp = D_S3_UntStorePOS [4]
    $ D_S2_MHP = D_S3_UntStorePOS [5]
    $ D_S2_HP = D_S3_UntStorePOS [6]
    $ D_S2_Atk = D_S3_UntStorePOS [7]
    $ D_S2_Mag = D_S3_UntStorePOS [8]
    $ D_S2_Def = D_S3_UntStorePOS [9]
    $ D_S2_Res = D_S3_UntStorePOS [10]
    $ D_S2_Spd = D_S3_UntStorePOS [11] 
    $ D_S2_Cls = D_S3_UntStorePOS [12]
    $ D_S2_Ttc = D_S3_UntStorePOS [13]
    $ D_S2_Ocu = D_S3_UntStorePOS [14]
    $ D_S2_CanAct = D_S3_UntStorePOS [15]
    $ D_S2_Mor = D_S3_UntStorePOS [16]
    $ D_S2_Fgt = D_S3_UntStorePOS [17]
    $ D_S2_Stn = D_S3_UntStorePOS [18]
    $ D_S2_AtkType = D_S3_UntStorePOS [19]
    $ D_S2_DefType = D_S3_UntStorePOS [20]
    $ D_S2_CrtChc = D_S3_UntStorePOS [21]
    $ D_S2_EvdChc = D_S3_UntStorePOS [22]
    $ D_S2_DuelChc = D_S3_UntStorePOS [23]
    $ D_S2_DuelEvd = D_S3_UntStorePOS [24]
    $ D_S2_AtkIcr = D_S3_UntStorePOS [25]
    $ D_S2_AtkDcr = D_S3_UntStorePOS [26]
    $ D_S2_AtkChg = D_S3_UntStorePOS [27]
    $ D_S2_DefIcr = D_S3_UntStorePOS [28]
    $ D_S2_DefDcr = D_S3_UntStorePOS [29]
    $ D_S2_DefChg = D_S3_UntStorePOS [30]
    $ D_S2_MorIcr = D_S3_UntStorePOS [31]
    $ D_S2_MorDcr = D_S3_UntStorePOS [32]
    $ D_S2_MorChg = D_S3_UntStorePOS [33]
    $ D_S2_Kill = D_S3_UntStorePOS [34]
    $ D_S2_Killed = D_S3_UntStorePOS [35]
    $ D_S2_ChgTtc_Count = D_S3_UntStorePOS [36]
    $ D_S2_ChgPos_Count = D_S3_UntStorePOS [37]
#-------------------------------
#-------------------------------
    $ D_S3_Ctl_Type = D_S2_UntStorePOS [0]
    $ D_S3_Reg_No = D_S2_UntStorePOS [1]
    $ D_S3_Name = D_S2_UntStorePOS [2]
    $ D_S3_Level = D_S2_UntStorePOS [3]
    $ D_S3_Exp = D_S2_UntStorePOS [4]
    $ D_S3_MHP = D_S2_UntStorePOS [5]
    $ D_S3_HP = D_S2_UntStorePOS [6]
    $ D_S3_Atk = D_S2_UntStorePOS [7]
    $ D_S3_Mag = D_S2_UntStorePOS [8]
    $ D_S3_Def = D_S2_UntStorePOS [9]
    $ D_S3_Res = D_S2_UntStorePOS [10]
    $ D_S3_Spd = D_S2_UntStorePOS [11] 
    $ D_S3_Cls = D_S2_UntStorePOS [12]
    $ D_S3_Ttc = D_S2_UntStorePOS [13]
    $ D_S3_Ocu = D_S2_UntStorePOS [14]
    $ D_S3_CanAct = D_S2_UntStorePOS [15]
    $ D_S3_Mor = D_S2_UntStorePOS [16]
    $ D_S3_Fgt = D_S2_UntStorePOS [17]
    $ D_S3_Stn = D_S2_UntStorePOS [18]
    $ D_S3_AtkType = D_S2_UntStorePOS [19]
    $ D_S3_DefType = D_S2_UntStorePOS [20]
    $ D_S3_CrtChc = D_S2_UntStorePOS [21]
    $ D_S3_EvdChc = D_S2_UntStorePOS [22]
    $ D_S3_DuelChc = D_S2_UntStorePOS [23]
    $ D_S3_DuelEvd = D_S2_UntStorePOS [24]
    $ D_S3_AtkIcr = D_S2_UntStorePOS [25]
    $ D_S3_AtkDcr = D_S2_UntStorePOS [26]
    $ D_S3_AtkChg = D_S2_UntStorePOS [27]
    $ D_S3_DefIcr = D_S2_UntStorePOS [28]
    $ D_S3_DefDcr = D_S2_UntStorePOS [29]
    $ D_S3_DefChg = D_S2_UntStorePOS [30]
    $ D_S3_MorIcr = D_S2_UntStorePOS [31]
    $ D_S3_MorDcr = D_S2_UntStorePOS [32]
    $ D_S3_MorChg = D_S2_UntStorePOS [33]
    $ D_S3_Kill = D_S2_UntStorePOS [34]
    $ D_S3_Killed = D_S2_UntStorePOS [35]
    $ D_S3_ChgTtc_Count = D_S2_UntStorePOS [36]
    $ D_S3_ChgPos_Count = D_S2_UntStorePOS [37]
#-------------------------------
    return

#=====================================================
label BS_Chg_D_UntPos02_04:
#=====================================================
#-------------------------------
    call BS_Update_D_S2_UntStorePOS
    call BS_Update_D_S4_UntStorePOS
#-------------------------------
    $ D_S2_Ctl_Type = D_S4_UntStorePOS [0]
    $ D_S2_Reg_No = D_S4_UntStorePOS [1]
    $ D_S2_Name = D_S4_UntStorePOS [2]
    $ D_S2_Level = D_S4_UntStorePOS [3]
    $ D_S2_Exp = D_S4_UntStorePOS [4]
    $ D_S2_MHP = D_S4_UntStorePOS [5]
    $ D_S2_HP = D_S4_UntStorePOS [6]
    $ D_S2_Atk = D_S4_UntStorePOS [7]
    $ D_S2_Mag = D_S4_UntStorePOS [8]
    $ D_S2_Def = D_S4_UntStorePOS [9]
    $ D_S2_Res = D_S4_UntStorePOS [10]
    $ D_S2_Spd = D_S4_UntStorePOS [11] 
    $ D_S2_Cls = D_S4_UntStorePOS [12]
    $ D_S2_Ttc = D_S4_UntStorePOS [13]
    $ D_S2_Ocu = D_S4_UntStorePOS [14]
    $ D_S2_CanAct = D_S4_UntStorePOS [15]
    $ D_S2_Mor = D_S4_UntStorePOS [16]
    $ D_S2_Fgt = D_S4_UntStorePOS [17]
    $ D_S2_Stn = D_S4_UntStorePOS [18]
    $ D_S2_AtkType = D_S4_UntStorePOS [19]
    $ D_S2_DefType = D_S4_UntStorePOS [20]
    $ D_S2_CrtChc = D_S4_UntStorePOS [21]
    $ D_S2_EvdChc = D_S4_UntStorePOS [22]
    $ D_S2_DuelChc = D_S4_UntStorePOS [23]
    $ D_S2_DuelEvd = D_S4_UntStorePOS [24]
    $ D_S2_AtkIcr = D_S4_UntStorePOS [25]
    $ D_S2_AtkDcr = D_S4_UntStorePOS [26]
    $ D_S2_AtkChg = D_S4_UntStorePOS [27]
    $ D_S2_DefIcr = D_S4_UntStorePOS [28]
    $ D_S2_DefDcr = D_S4_UntStorePOS [29]
    $ D_S2_DefChg = D_S4_UntStorePOS [30]
    $ D_S2_MorIcr = D_S4_UntStorePOS [31]
    $ D_S2_MorDcr = D_S4_UntStorePOS [32]
    $ D_S2_MorChg = D_S4_UntStorePOS [33]
    $ D_S2_Kill = D_S4_UntStorePOS [34]
    $ D_S2_Killed = D_S4_UntStorePOS [35]
    $ D_S2_ChgTtc_Count = D_S4_UntStorePOS [36]
    $ D_S2_ChgPos_Count = D_S4_UntStorePOS [37]
#-------------------------------
#-------------------------------
    $ D_S4_Ctl_Type = D_S2_UntStorePOS [0]
    $ D_S4_Reg_No = D_S2_UntStorePOS [1]
    $ D_S4_Name = D_S2_UntStorePOS [2]
    $ D_S4_Level = D_S2_UntStorePOS [3]
    $ D_S4_Exp = D_S2_UntStorePOS [4]
    $ D_S4_MHP = D_S2_UntStorePOS [5]
    $ D_S4_HP = D_S2_UntStorePOS [6]
    $ D_S4_Atk = D_S2_UntStorePOS [7]
    $ D_S4_Mag = D_S2_UntStorePOS [8]
    $ D_S4_Def = D_S2_UntStorePOS [9]
    $ D_S4_Res = D_S2_UntStorePOS [10]
    $ D_S4_Spd = D_S2_UntStorePOS [11] 
    $ D_S4_Cls = D_S2_UntStorePOS [12]
    $ D_S4_Ttc = D_S2_UntStorePOS [13]
    $ D_S4_Ocu = D_S2_UntStorePOS [14]
    $ D_S4_CanAct = D_S2_UntStorePOS [15]
    $ D_S4_Mor = D_S2_UntStorePOS [16]
    $ D_S4_Fgt = D_S2_UntStorePOS [17]
    $ D_S4_Stn = D_S2_UntStorePOS [18]
    $ D_S4_AtkType = D_S2_UntStorePOS [19]
    $ D_S4_DefType = D_S2_UntStorePOS [20]
    $ D_S4_CrtChc = D_S2_UntStorePOS [21]
    $ D_S4_EvdChc = D_S2_UntStorePOS [22]
    $ D_S4_DuelChc = D_S2_UntStorePOS [23]
    $ D_S4_DuelEvd = D_S2_UntStorePOS [24]
    $ D_S4_AtkIcr = D_S2_UntStorePOS [25]
    $ D_S4_AtkDcr = D_S2_UntStorePOS [26]
    $ D_S4_AtkChg = D_S2_UntStorePOS [27]
    $ D_S4_DefIcr = D_S2_UntStorePOS [28]
    $ D_S4_DefDcr = D_S2_UntStorePOS [29]
    $ D_S4_DefChg = D_S2_UntStorePOS [30]
    $ D_S4_MorIcr = D_S2_UntStorePOS [31]
    $ D_S4_MorDcr = D_S2_UntStorePOS [32]
    $ D_S4_MorChg = D_S2_UntStorePOS [33]
    $ D_S4_Kill = D_S2_UntStorePOS [34]
    $ D_S4_Killed = D_S2_UntStorePOS [35]
    $ D_S4_ChgTtc_Count = D_S2_UntStorePOS [36]
    $ D_S4_ChgPos_Count = D_S2_UntStorePOS [37]
#-------------------------------
    return

#=====================================================
label BS_Chg_D_UntPos02_05:
#=====================================================
#-------------------------------
    call BS_Update_D_S2_UntStorePOS
    call BS_Update_D_S5_UntStorePOS
#-------------------------------
    $ D_S2_Ctl_Type = D_S5_UntStorePOS [0]
    $ D_S2_Reg_No = D_S5_UntStorePOS [1]
    $ D_S2_Name = D_S5_UntStorePOS [2]
    $ D_S2_Level = D_S5_UntStorePOS [3]
    $ D_S2_Exp = D_S5_UntStorePOS [4]
    $ D_S2_MHP = D_S5_UntStorePOS [5]
    $ D_S2_HP = D_S5_UntStorePOS [6]
    $ D_S2_Atk = D_S5_UntStorePOS [7]
    $ D_S2_Mag = D_S5_UntStorePOS [8]
    $ D_S2_Def = D_S5_UntStorePOS [9]
    $ D_S2_Res = D_S5_UntStorePOS [10]
    $ D_S2_Spd = D_S5_UntStorePOS [11] 
    $ D_S2_Cls = D_S5_UntStorePOS [12]
    $ D_S2_Ttc = D_S5_UntStorePOS [13]
    $ D_S2_Ocu = D_S5_UntStorePOS [14]
    $ D_S2_CanAct = D_S5_UntStorePOS [15]
    $ D_S2_Mor = D_S5_UntStorePOS [16]
    $ D_S2_Fgt = D_S5_UntStorePOS [17]
    $ D_S2_Stn = D_S5_UntStorePOS [18]
    $ D_S2_AtkType = D_S5_UntStorePOS [19]
    $ D_S2_DefType = D_S5_UntStorePOS [20]
    $ D_S2_CrtChc = D_S5_UntStorePOS [21]
    $ D_S2_EvdChc = D_S5_UntStorePOS [22]
    $ D_S2_DuelChc = D_S5_UntStorePOS [23]
    $ D_S2_DuelEvd = D_S5_UntStorePOS [24]
    $ D_S2_AtkIcr = D_S5_UntStorePOS [25]
    $ D_S2_AtkDcr = D_S5_UntStorePOS [26]
    $ D_S2_AtkChg = D_S5_UntStorePOS [27]
    $ D_S2_DefIcr = D_S5_UntStorePOS [28]
    $ D_S2_DefDcr = D_S5_UntStorePOS [29]
    $ D_S2_DefChg = D_S5_UntStorePOS [30]
    $ D_S2_MorIcr = D_S5_UntStorePOS [31]
    $ D_S2_MorDcr = D_S5_UntStorePOS [32]
    $ D_S2_MorChg = D_S5_UntStorePOS [33]
    $ D_S2_Kill = D_S5_UntStorePOS [34]
    $ D_S2_Killed = D_S5_UntStorePOS [35]
    $ D_S2_ChgTtc_Count = D_S5_UntStorePOS [36]
    $ D_S2_ChgPos_Count = D_S5_UntStorePOS [37]
#-------------------------------
#-------------------------------
    $ D_S5_Ctl_Type = D_S2_UntStorePOS [0]
    $ D_S5_Reg_No = D_S2_UntStorePOS [1]
    $ D_S5_Name = D_S2_UntStorePOS [2]
    $ D_S5_Level = D_S2_UntStorePOS [3]
    $ D_S5_Exp = D_S2_UntStorePOS [4]
    $ D_S5_MHP = D_S2_UntStorePOS [5]
    $ D_S5_HP = D_S2_UntStorePOS [6]
    $ D_S5_Atk = D_S2_UntStorePOS [7]
    $ D_S5_Mag = D_S2_UntStorePOS [8]
    $ D_S5_Def = D_S2_UntStorePOS [9]
    $ D_S5_Res = D_S2_UntStorePOS [10]
    $ D_S5_Spd = D_S2_UntStorePOS [11] 
    $ D_S5_Cls = D_S2_UntStorePOS [12]
    $ D_S5_Ttc = D_S2_UntStorePOS [13]
    $ D_S5_Ocu = D_S2_UntStorePOS [14]
    $ D_S5_CanAct = D_S2_UntStorePOS [15]
    $ D_S5_Mor = D_S2_UntStorePOS [16]
    $ D_S5_Fgt = D_S2_UntStorePOS [17]
    $ D_S5_Stn = D_S2_UntStorePOS [18]
    $ D_S5_AtkType = D_S2_UntStorePOS [19]
    $ D_S5_DefType = D_S2_UntStorePOS [20]
    $ D_S5_CrtChc = D_S2_UntStorePOS [21]
    $ D_S5_EvdChc = D_S2_UntStorePOS [22]
    $ D_S5_DuelChc = D_S2_UntStorePOS [23]
    $ D_S5_DuelEvd = D_S2_UntStorePOS [24]
    $ D_S5_AtkIcr = D_S2_UntStorePOS [25]
    $ D_S5_AtkDcr = D_S2_UntStorePOS [26]
    $ D_S5_AtkChg = D_S2_UntStorePOS [27]
    $ D_S5_DefIcr = D_S2_UntStorePOS [28]
    $ D_S5_DefDcr = D_S2_UntStorePOS [29]
    $ D_S5_DefChg = D_S2_UntStorePOS [30]
    $ D_S5_MorIcr = D_S2_UntStorePOS [31]
    $ D_S5_MorDcr = D_S2_UntStorePOS [32]
    $ D_S5_MorChg = D_S2_UntStorePOS [33]
    $ D_S5_Kill = D_S2_UntStorePOS [34]
    $ D_S5_Killed = D_S2_UntStorePOS [35]
    $ D_S5_ChgTtc_Count = D_S2_UntStorePOS [36]
    $ D_S5_ChgPos_Count = D_S2_UntStorePOS [37]
#-------------------------------
    return

#=====================================================
label BS_Chg_D_UntPos02_06:
#=====================================================
#-------------------------------
    call BS_Update_D_S2_UntStorePOS
    call BS_Update_D_S6_UntStorePOS
#-------------------------------
    $ D_S2_Ctl_Type = D_S6_UntStorePOS [0]
    $ D_S2_Reg_No = D_S6_UntStorePOS [1]
    $ D_S2_Name = D_S6_UntStorePOS [2]
    $ D_S2_Level = D_S6_UntStorePOS [3]
    $ D_S2_Exp = D_S6_UntStorePOS [4]
    $ D_S2_MHP = D_S6_UntStorePOS [5]
    $ D_S2_HP = D_S6_UntStorePOS [6]
    $ D_S2_Atk = D_S6_UntStorePOS [7]
    $ D_S2_Mag = D_S6_UntStorePOS [8]
    $ D_S2_Def = D_S6_UntStorePOS [9]
    $ D_S2_Res = D_S6_UntStorePOS [10]
    $ D_S2_Spd = D_S6_UntStorePOS [11] 
    $ D_S2_Cls = D_S6_UntStorePOS [12]
    $ D_S2_Ttc = D_S6_UntStorePOS [13]
    $ D_S2_Ocu = D_S6_UntStorePOS [14]
    $ D_S2_CanAct = D_S6_UntStorePOS [15]
    $ D_S2_Mor = D_S6_UntStorePOS [16]
    $ D_S2_Fgt = D_S6_UntStorePOS [17]
    $ D_S2_Stn = D_S6_UntStorePOS [18]
    $ D_S2_AtkType = D_S6_UntStorePOS [19]
    $ D_S2_DefType = D_S6_UntStorePOS [20]
    $ D_S2_CrtChc = D_S6_UntStorePOS [21]
    $ D_S2_EvdChc = D_S6_UntStorePOS [22]
    $ D_S2_DuelChc = D_S6_UntStorePOS [23]
    $ D_S2_DuelEvd = D_S6_UntStorePOS [24]
    $ D_S2_AtkIcr = D_S6_UntStorePOS [25]
    $ D_S2_AtkDcr = D_S6_UntStorePOS [26]
    $ D_S2_AtkChg = D_S6_UntStorePOS [27]
    $ D_S2_DefIcr = D_S6_UntStorePOS [28]
    $ D_S2_DefDcr = D_S6_UntStorePOS [29]
    $ D_S2_DefChg = D_S6_UntStorePOS [30]
    $ D_S2_MorIcr = D_S6_UntStorePOS [31]
    $ D_S2_MorDcr = D_S6_UntStorePOS [32]
    $ D_S2_MorChg = D_S6_UntStorePOS [33]
    $ D_S2_Kill = D_S6_UntStorePOS [34]
    $ D_S2_Killed = D_S6_UntStorePOS [35]
    $ D_S2_ChgTtc_Count = D_S6_UntStorePOS [36]
    $ D_S2_ChgPos_Count = D_S6_UntStorePOS [37]
#-------------------------------
#-------------------------------
    $ D_S6_Ctl_Type = D_S2_UntStorePOS [0]
    $ D_S6_Reg_No = D_S2_UntStorePOS [1]
    $ D_S6_Name = D_S2_UntStorePOS [2]
    $ D_S6_Level = D_S2_UntStorePOS [3]
    $ D_S6_Exp = D_S2_UntStorePOS [4]
    $ D_S6_MHP = D_S2_UntStorePOS [5]
    $ D_S6_HP = D_S2_UntStorePOS [6]
    $ D_S6_Atk = D_S2_UntStorePOS [7]
    $ D_S6_Mag = D_S2_UntStorePOS [8]
    $ D_S6_Def = D_S2_UntStorePOS [9]
    $ D_S6_Res = D_S2_UntStorePOS [10]
    $ D_S6_Spd = D_S2_UntStorePOS [11] 
    $ D_S6_Cls = D_S2_UntStorePOS [12]
    $ D_S6_Ttc = D_S2_UntStorePOS [13]
    $ D_S6_Ocu = D_S2_UntStorePOS [14]
    $ D_S6_CanAct = D_S2_UntStorePOS [15]
    $ D_S6_Mor = D_S2_UntStorePOS [16]
    $ D_S6_Fgt = D_S2_UntStorePOS [17]
    $ D_S6_Stn = D_S2_UntStorePOS [18]
    $ D_S6_AtkType = D_S2_UntStorePOS [19]
    $ D_S6_DefType = D_S2_UntStorePOS [20]
    $ D_S6_CrtChc = D_S2_UntStorePOS [21]
    $ D_S6_EvdChc = D_S2_UntStorePOS [22]
    $ D_S6_DuelChc = D_S2_UntStorePOS [23]
    $ D_S6_DuelEvd = D_S2_UntStorePOS [24]
    $ D_S6_AtkIcr = D_S2_UntStorePOS [25]
    $ D_S6_AtkDcr = D_S2_UntStorePOS [26]
    $ D_S6_AtkChg = D_S2_UntStorePOS [27]
    $ D_S6_DefIcr = D_S2_UntStorePOS [28]
    $ D_S6_DefDcr = D_S2_UntStorePOS [29]
    $ D_S6_DefChg = D_S2_UntStorePOS [30]
    $ D_S6_MorIcr = D_S2_UntStorePOS [31]
    $ D_S6_MorDcr = D_S2_UntStorePOS [32]
    $ D_S6_MorChg = D_S2_UntStorePOS [33]
    $ D_S6_Kill = D_S2_UntStorePOS [34]
    $ D_S6_Killed = D_S2_UntStorePOS [35]
    $ D_S6_ChgTtc_Count = D_S2_UntStorePOS [36]
    $ D_S6_ChgPos_Count = D_S2_UntStorePOS [37]
#-------------------------------
    return
