
#=====================================================
label BS_Chg_A_UntStoreSklSlt03_01:
#=====================================================
#-------------------------------
    call BS_Update_A_S3_UntStoreSklSlt
    call BS_Update_A_S1_UntStoreSklSlt
#-------------------------------
    $ A_S3_EftSlt01 = A_S1_UntStoreSklSlt [0]
    $ A_S3_EftSlt02 = A_S1_UntStoreSklSlt [1]
    $ A_S3_EftSlt03 = A_S1_UntStoreSklSlt [2]
    $ A_S3_EftSlt04 = A_S1_UntStoreSklSlt [3]
    $ A_S3_EftSlt05 = A_S1_UntStoreSklSlt [4]
    $ A_S3_EftSlt06 = A_S1_UntStoreSklSlt [5]
    $ A_S3_EftSlt01_No = A_S1_UntStoreSklSlt [6]
    $ A_S3_EftSlt02_No = A_S1_UntStoreSklSlt [7]
    $ A_S3_EftSlt03_No = A_S1_UntStoreSklSlt [8]
    $ A_S3_EftSlt04_No = A_S1_UntStoreSklSlt [9]
    $ A_S3_EftSlt05_No = A_S1_UntStoreSklSlt [10]
    $ A_S3_EftSlt06_No = A_S1_UntStoreSklSlt [11]
    $ A_S3_EftSlt01_Type = A_S1_UntStoreSklSlt [12]
    $ A_S3_EftSlt02_Type = A_S1_UntStoreSklSlt [13]
    $ A_S3_EftSlt03_Type = A_S1_UntStoreSklSlt [14]
    $ A_S3_EftSlt04_Type = A_S1_UntStoreSklSlt [15]
    $ A_S3_EftSlt05_Type = A_S1_UntStoreSklSlt [16]
    $ A_S3_EftSlt06_Type = A_S1_UntStoreSklSlt [17]
    $ A_S3_EftSlt01_Used = A_S1_UntStoreSklSlt [18]
    $ A_S3_EftSlt02_Used = A_S1_UntStoreSklSlt [19]
    $ A_S3_EftSlt03_Used = A_S1_UntStoreSklSlt [20]
    $ A_S3_EftSlt04_Used = A_S1_UntStoreSklSlt [21]
    $ A_S3_EftSlt05_Used = A_S1_UntStoreSklSlt [22]
    $ A_S3_EftSlt06_Used = A_S1_UntStoreSklSlt [23]
#-------------------------------
#-------------------------------
    $ A_S1_EftSlt01 = A_S3_UntStoreSklSlt [0]
    $ A_S1_EftSlt02 = A_S3_UntStoreSklSlt [1]
    $ A_S1_EftSlt03 = A_S3_UntStoreSklSlt [2]
    $ A_S1_EftSlt04 = A_S3_UntStoreSklSlt [3]
    $ A_S1_EftSlt05 = A_S3_UntStoreSklSlt [4]
    $ A_S1_EftSlt06 = A_S3_UntStoreSklSlt [5]
    $ A_S1_EftSlt01_No = A_S3_UntStoreSklSlt [6]
    $ A_S1_EftSlt02_No = A_S3_UntStoreSklSlt [7]
    $ A_S1_EftSlt03_No = A_S3_UntStoreSklSlt [8]
    $ A_S1_EftSlt04_No = A_S3_UntStoreSklSlt [9]
    $ A_S1_EftSlt05_No = A_S3_UntStoreSklSlt [10]
    $ A_S1_EftSlt06_No = A_S3_UntStoreSklSlt [11]
    $ A_S1_EftSlt01_Type = A_S3_UntStoreSklSlt [12]
    $ A_S1_EftSlt02_Type = A_S3_UntStoreSklSlt [13]
    $ A_S1_EftSlt03_Type = A_S3_UntStoreSklSlt [14]
    $ A_S1_EftSlt04_Type = A_S3_UntStoreSklSlt [15]
    $ A_S1_EftSlt05_Type = A_S3_UntStoreSklSlt [16]
    $ A_S1_EftSlt06_Type = A_S3_UntStoreSklSlt [17]
    $ A_S1_EftSlt01_Used = A_S3_UntStoreSklSlt [18]
    $ A_S1_EftSlt02_Used = A_S3_UntStoreSklSlt [19]
    $ A_S1_EftSlt03_Used = A_S3_UntStoreSklSlt [20]
    $ A_S1_EftSlt04_Used = A_S3_UntStoreSklSlt [21]
    $ A_S1_EftSlt05_Used = A_S3_UntStoreSklSlt [22]
    $ A_S1_EftSlt06_Used = A_S3_UntStoreSklSlt [23]
#-------------------------------
    return

#=====================================================
label BS_Chg_A_UntStoreSklSlt03_02:
#=====================================================
#-------------------------------
    call BS_Update_A_S3_UntStoreSklSlt
    call BS_Update_A_S2_UntStoreSklSlt
#-------------------------------
    $ A_S3_EftSlt01 = A_S2_UntStoreSklSlt [0]
    $ A_S3_EftSlt02 = A_S2_UntStoreSklSlt [1]
    $ A_S3_EftSlt03 = A_S2_UntStoreSklSlt [2]
    $ A_S3_EftSlt04 = A_S2_UntStoreSklSlt [3]
    $ A_S3_EftSlt05 = A_S2_UntStoreSklSlt [4]
    $ A_S3_EftSlt06 = A_S2_UntStoreSklSlt [5]
    $ A_S3_EftSlt01_No = A_S2_UntStoreSklSlt [6]
    $ A_S3_EftSlt02_No = A_S2_UntStoreSklSlt [7]
    $ A_S3_EftSlt03_No = A_S2_UntStoreSklSlt [8]
    $ A_S3_EftSlt04_No = A_S2_UntStoreSklSlt [9]
    $ A_S3_EftSlt05_No = A_S2_UntStoreSklSlt [10]
    $ A_S3_EftSlt06_No = A_S2_UntStoreSklSlt [11]
    $ A_S3_EftSlt01_Type = A_S2_UntStoreSklSlt [12]
    $ A_S3_EftSlt02_Type = A_S2_UntStoreSklSlt [13]
    $ A_S3_EftSlt03_Type = A_S2_UntStoreSklSlt [14]
    $ A_S3_EftSlt04_Type = A_S2_UntStoreSklSlt [15]
    $ A_S3_EftSlt05_Type = A_S2_UntStoreSklSlt [16]
    $ A_S3_EftSlt06_Type = A_S2_UntStoreSklSlt [17]
    $ A_S3_EftSlt01_Used = A_S2_UntStoreSklSlt [18]
    $ A_S3_EftSlt02_Used = A_S2_UntStoreSklSlt [19]
    $ A_S3_EftSlt03_Used = A_S2_UntStoreSklSlt [20]
    $ A_S3_EftSlt04_Used = A_S2_UntStoreSklSlt [21]
    $ A_S3_EftSlt05_Used = A_S2_UntStoreSklSlt [22]
    $ A_S3_EftSlt06_Used = A_S2_UntStoreSklSlt [23]
#-------------------------------
#-------------------------------
    $ A_S2_EftSlt01 = A_S3_UntStoreSklSlt [0]
    $ A_S2_EftSlt02 = A_S3_UntStoreSklSlt [1]
    $ A_S2_EftSlt03 = A_S3_UntStoreSklSlt [2]
    $ A_S2_EftSlt04 = A_S3_UntStoreSklSlt [3]
    $ A_S2_EftSlt05 = A_S3_UntStoreSklSlt [4]
    $ A_S2_EftSlt06 = A_S3_UntStoreSklSlt [5]
    $ A_S2_EftSlt01_No = A_S3_UntStoreSklSlt [6]
    $ A_S2_EftSlt02_No = A_S3_UntStoreSklSlt [7]
    $ A_S2_EftSlt03_No = A_S3_UntStoreSklSlt [8]
    $ A_S2_EftSlt04_No = A_S3_UntStoreSklSlt [9]
    $ A_S2_EftSlt05_No = A_S3_UntStoreSklSlt [10]
    $ A_S2_EftSlt06_No = A_S3_UntStoreSklSlt [11]
    $ A_S2_EftSlt01_Type = A_S3_UntStoreSklSlt [12]
    $ A_S2_EftSlt02_Type = A_S3_UntStoreSklSlt [13]
    $ A_S2_EftSlt03_Type = A_S3_UntStoreSklSlt [14]
    $ A_S2_EftSlt04_Type = A_S3_UntStoreSklSlt [15]
    $ A_S2_EftSlt05_Type = A_S3_UntStoreSklSlt [16]
    $ A_S2_EftSlt06_Type = A_S3_UntStoreSklSlt [17]
    $ A_S2_EftSlt01_Used = A_S3_UntStoreSklSlt [18]
    $ A_S2_EftSlt02_Used = A_S3_UntStoreSklSlt [19]
    $ A_S2_EftSlt03_Used = A_S3_UntStoreSklSlt [20]
    $ A_S2_EftSlt04_Used = A_S3_UntStoreSklSlt [21]
    $ A_S2_EftSlt05_Used = A_S3_UntStoreSklSlt [22]
    $ A_S2_EftSlt06_Used = A_S3_UntStoreSklSlt [23]
#-------------------------------
    return

#=====================================================
label BS_Chg_A_UntStoreSklSlt03_04:
#=====================================================
#-------------------------------
    call BS_Update_A_S3_UntStoreSklSlt
    call BS_Update_A_S4_UntStoreSklSlt
#-------------------------------
    $ A_S3_EftSlt01 = A_S4_UntStoreSklSlt [0]
    $ A_S3_EftSlt02 = A_S4_UntStoreSklSlt [1]
    $ A_S3_EftSlt03 = A_S4_UntStoreSklSlt [2]
    $ A_S3_EftSlt04 = A_S4_UntStoreSklSlt [3]
    $ A_S3_EftSlt05 = A_S4_UntStoreSklSlt [4]
    $ A_S3_EftSlt06 = A_S4_UntStoreSklSlt [5]
    $ A_S3_EftSlt01_No = A_S4_UntStoreSklSlt [6]
    $ A_S3_EftSlt02_No = A_S4_UntStoreSklSlt [7]
    $ A_S3_EftSlt03_No = A_S4_UntStoreSklSlt [8]
    $ A_S3_EftSlt04_No = A_S4_UntStoreSklSlt [9]
    $ A_S3_EftSlt05_No = A_S4_UntStoreSklSlt [10]
    $ A_S3_EftSlt06_No = A_S4_UntStoreSklSlt [11]
    $ A_S3_EftSlt01_Type = A_S4_UntStoreSklSlt [12]
    $ A_S3_EftSlt02_Type = A_S4_UntStoreSklSlt [13]
    $ A_S3_EftSlt03_Type = A_S4_UntStoreSklSlt [14]
    $ A_S3_EftSlt04_Type = A_S4_UntStoreSklSlt [15]
    $ A_S3_EftSlt05_Type = A_S4_UntStoreSklSlt [16]
    $ A_S3_EftSlt06_Type = A_S4_UntStoreSklSlt [17]
    $ A_S3_EftSlt01_Used = A_S4_UntStoreSklSlt [18]
    $ A_S3_EftSlt02_Used = A_S4_UntStoreSklSlt [19]
    $ A_S3_EftSlt03_Used = A_S4_UntStoreSklSlt [20]
    $ A_S3_EftSlt04_Used = A_S4_UntStoreSklSlt [21]
    $ A_S3_EftSlt05_Used = A_S4_UntStoreSklSlt [22]
    $ A_S3_EftSlt06_Used = A_S4_UntStoreSklSlt [23]
#-------------------------------
#-------------------------------
    $ A_S4_EftSlt01 = A_S3_UntStoreSklSlt [0]
    $ A_S4_EftSlt02 = A_S3_UntStoreSklSlt [1]
    $ A_S4_EftSlt03 = A_S3_UntStoreSklSlt [2]
    $ A_S4_EftSlt04 = A_S3_UntStoreSklSlt [3]
    $ A_S4_EftSlt05 = A_S3_UntStoreSklSlt [4]
    $ A_S4_EftSlt06 = A_S3_UntStoreSklSlt [5]
    $ A_S4_EftSlt01_No = A_S3_UntStoreSklSlt [6]
    $ A_S4_EftSlt02_No = A_S3_UntStoreSklSlt [7]
    $ A_S4_EftSlt03_No = A_S3_UntStoreSklSlt [8]
    $ A_S4_EftSlt04_No = A_S3_UntStoreSklSlt [9]
    $ A_S4_EftSlt05_No = A_S3_UntStoreSklSlt [10]
    $ A_S4_EftSlt06_No = A_S3_UntStoreSklSlt [11]
    $ A_S4_EftSlt01_Type = A_S3_UntStoreSklSlt [12]
    $ A_S4_EftSlt02_Type = A_S3_UntStoreSklSlt [13]
    $ A_S4_EftSlt03_Type = A_S3_UntStoreSklSlt [14]
    $ A_S4_EftSlt04_Type = A_S3_UntStoreSklSlt [15]
    $ A_S4_EftSlt05_Type = A_S3_UntStoreSklSlt [16]
    $ A_S4_EftSlt06_Type = A_S3_UntStoreSklSlt [17]
    $ A_S4_EftSlt01_Used = A_S3_UntStoreSklSlt [18]
    $ A_S4_EftSlt02_Used = A_S3_UntStoreSklSlt [19]
    $ A_S4_EftSlt03_Used = A_S3_UntStoreSklSlt [20]
    $ A_S4_EftSlt04_Used = A_S3_UntStoreSklSlt [21]
    $ A_S4_EftSlt05_Used = A_S3_UntStoreSklSlt [22]
    $ A_S4_EftSlt06_Used = A_S3_UntStoreSklSlt [23]
#-------------------------------
    return

#=====================================================
label BS_Chg_A_UntStoreSklSlt03_05:
#=====================================================
#-------------------------------
    call BS_Update_A_S3_UntStoreSklSlt
    call BS_Update_A_S5_UntStoreSklSlt
#-------------------------------
    $ A_S3_EftSlt01 = A_S5_UntStoreSklSlt [0]
    $ A_S3_EftSlt02 = A_S5_UntStoreSklSlt [1]
    $ A_S3_EftSlt03 = A_S5_UntStoreSklSlt [2]
    $ A_S3_EftSlt04 = A_S5_UntStoreSklSlt [3]
    $ A_S3_EftSlt05 = A_S5_UntStoreSklSlt [4]
    $ A_S3_EftSlt06 = A_S5_UntStoreSklSlt [5]
    $ A_S3_EftSlt01_No = A_S5_UntStoreSklSlt [6]
    $ A_S3_EftSlt02_No = A_S5_UntStoreSklSlt [7]
    $ A_S3_EftSlt03_No = A_S5_UntStoreSklSlt [8]
    $ A_S3_EftSlt04_No = A_S5_UntStoreSklSlt [9]
    $ A_S3_EftSlt05_No = A_S5_UntStoreSklSlt [10]
    $ A_S3_EftSlt06_No = A_S5_UntStoreSklSlt [11]
    $ A_S3_EftSlt01_Type = A_S5_UntStoreSklSlt [12]
    $ A_S3_EftSlt02_Type = A_S5_UntStoreSklSlt [13]
    $ A_S3_EftSlt03_Type = A_S5_UntStoreSklSlt [14]
    $ A_S3_EftSlt04_Type = A_S5_UntStoreSklSlt [15]
    $ A_S3_EftSlt05_Type = A_S5_UntStoreSklSlt [16]
    $ A_S3_EftSlt06_Type = A_S5_UntStoreSklSlt [17]
    $ A_S3_EftSlt01_Used = A_S5_UntStoreSklSlt [18]
    $ A_S3_EftSlt02_Used = A_S5_UntStoreSklSlt [19]
    $ A_S3_EftSlt03_Used = A_S5_UntStoreSklSlt [20]
    $ A_S3_EftSlt04_Used = A_S5_UntStoreSklSlt [21]
    $ A_S3_EftSlt05_Used = A_S5_UntStoreSklSlt [22]
    $ A_S3_EftSlt06_Used = A_S5_UntStoreSklSlt [23]
#-------------------------------
#-------------------------------
    $ A_S5_EftSlt01 = A_S3_UntStoreSklSlt [0]
    $ A_S5_EftSlt02 = A_S3_UntStoreSklSlt [1]
    $ A_S5_EftSlt03 = A_S3_UntStoreSklSlt [2]
    $ A_S5_EftSlt04 = A_S3_UntStoreSklSlt [3]
    $ A_S5_EftSlt05 = A_S3_UntStoreSklSlt [4]
    $ A_S5_EftSlt06 = A_S3_UntStoreSklSlt [5]
    $ A_S5_EftSlt01_No = A_S3_UntStoreSklSlt [6]
    $ A_S5_EftSlt02_No = A_S3_UntStoreSklSlt [7]
    $ A_S5_EftSlt03_No = A_S3_UntStoreSklSlt [8]
    $ A_S5_EftSlt04_No = A_S3_UntStoreSklSlt [9]
    $ A_S5_EftSlt05_No = A_S3_UntStoreSklSlt [10]
    $ A_S5_EftSlt06_No = A_S3_UntStoreSklSlt [11]
    $ A_S5_EftSlt01_Type = A_S3_UntStoreSklSlt [12]
    $ A_S5_EftSlt02_Type = A_S3_UntStoreSklSlt [13]
    $ A_S5_EftSlt03_Type = A_S3_UntStoreSklSlt [14]
    $ A_S5_EftSlt04_Type = A_S3_UntStoreSklSlt [15]
    $ A_S5_EftSlt05_Type = A_S3_UntStoreSklSlt [16]
    $ A_S5_EftSlt06_Type = A_S3_UntStoreSklSlt [17]
    $ A_S5_EftSlt01_Used = A_S3_UntStoreSklSlt [18]
    $ A_S5_EftSlt02_Used = A_S3_UntStoreSklSlt [19]
    $ A_S5_EftSlt03_Used = A_S3_UntStoreSklSlt [20]
    $ A_S5_EftSlt04_Used = A_S3_UntStoreSklSlt [21]
    $ A_S5_EftSlt05_Used = A_S3_UntStoreSklSlt [22]
    $ A_S5_EftSlt06_Used = A_S3_UntStoreSklSlt [23]
#-------------------------------
    return

#=====================================================
label BS_Chg_A_UntStoreSklSlt03_06:
#=====================================================
#-------------------------------
    call BS_Update_A_S3_UntStoreSklSlt
    call BS_Update_A_S6_UntStoreSklSlt
#-------------------------------
    $ A_S3_EftSlt01 = A_S6_UntStoreSklSlt [0]
    $ A_S3_EftSlt02 = A_S6_UntStoreSklSlt [1]
    $ A_S3_EftSlt03 = A_S6_UntStoreSklSlt [2]
    $ A_S3_EftSlt04 = A_S6_UntStoreSklSlt [3]
    $ A_S3_EftSlt05 = A_S6_UntStoreSklSlt [4]
    $ A_S3_EftSlt06 = A_S6_UntStoreSklSlt [5]
    $ A_S3_EftSlt01_No = A_S6_UntStoreSklSlt [6]
    $ A_S3_EftSlt02_No = A_S6_UntStoreSklSlt [7]
    $ A_S3_EftSlt03_No = A_S6_UntStoreSklSlt [8]
    $ A_S3_EftSlt04_No = A_S6_UntStoreSklSlt [9]
    $ A_S3_EftSlt05_No = A_S6_UntStoreSklSlt [10]
    $ A_S3_EftSlt06_No = A_S6_UntStoreSklSlt [11]
    $ A_S3_EftSlt01_Type = A_S6_UntStoreSklSlt [12]
    $ A_S3_EftSlt02_Type = A_S6_UntStoreSklSlt [13]
    $ A_S3_EftSlt03_Type = A_S6_UntStoreSklSlt [14]
    $ A_S3_EftSlt04_Type = A_S6_UntStoreSklSlt [15]
    $ A_S3_EftSlt05_Type = A_S6_UntStoreSklSlt [16]
    $ A_S3_EftSlt06_Type = A_S6_UntStoreSklSlt [17]
    $ A_S3_EftSlt01_Used = A_S6_UntStoreSklSlt [18]
    $ A_S3_EftSlt02_Used = A_S6_UntStoreSklSlt [19]
    $ A_S3_EftSlt03_Used = A_S6_UntStoreSklSlt [20]
    $ A_S3_EftSlt04_Used = A_S6_UntStoreSklSlt [21]
    $ A_S3_EftSlt05_Used = A_S6_UntStoreSklSlt [22]
    $ A_S3_EftSlt06_Used = A_S6_UntStoreSklSlt [23]
#-------------------------------
#-------------------------------
    $ A_S6_EftSlt01 = A_S3_UntStoreSklSlt [0]
    $ A_S6_EftSlt02 = A_S3_UntStoreSklSlt [1]
    $ A_S6_EftSlt03 = A_S3_UntStoreSklSlt [2]
    $ A_S6_EftSlt04 = A_S3_UntStoreSklSlt [3]
    $ A_S6_EftSlt05 = A_S3_UntStoreSklSlt [4]
    $ A_S6_EftSlt06 = A_S3_UntStoreSklSlt [5]
    $ A_S6_EftSlt01_No = A_S3_UntStoreSklSlt [6]
    $ A_S6_EftSlt02_No = A_S3_UntStoreSklSlt [7]
    $ A_S6_EftSlt03_No = A_S3_UntStoreSklSlt [8]
    $ A_S6_EftSlt04_No = A_S3_UntStoreSklSlt [9]
    $ A_S6_EftSlt05_No = A_S3_UntStoreSklSlt [10]
    $ A_S6_EftSlt06_No = A_S3_UntStoreSklSlt [11]
    $ A_S6_EftSlt01_Type = A_S3_UntStoreSklSlt [12]
    $ A_S6_EftSlt02_Type = A_S3_UntStoreSklSlt [13]
    $ A_S6_EftSlt03_Type = A_S3_UntStoreSklSlt [14]
    $ A_S6_EftSlt04_Type = A_S3_UntStoreSklSlt [15]
    $ A_S6_EftSlt05_Type = A_S3_UntStoreSklSlt [16]
    $ A_S6_EftSlt06_Type = A_S3_UntStoreSklSlt [17]
    $ A_S6_EftSlt01_Used = A_S3_UntStoreSklSlt [18]
    $ A_S6_EftSlt02_Used = A_S3_UntStoreSklSlt [19]
    $ A_S6_EftSlt03_Used = A_S3_UntStoreSklSlt [20]
    $ A_S6_EftSlt04_Used = A_S3_UntStoreSklSlt [21]
    $ A_S6_EftSlt05_Used = A_S3_UntStoreSklSlt [22]
    $ A_S6_EftSlt06_Used = A_S3_UntStoreSklSlt [23]
#-------------------------------
    return
