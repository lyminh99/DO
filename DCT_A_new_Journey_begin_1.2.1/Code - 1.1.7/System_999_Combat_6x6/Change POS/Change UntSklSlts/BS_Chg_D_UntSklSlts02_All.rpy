
#=====================================================
label BS_Chg_D_UntStoreSklSlt02_01:
#=====================================================
#-------------------------------
    call BS_Update_D_S2_UntStoreSklSlt
    call BS_Update_D_S1_UntStoreSklSlt
#-------------------------------
    $ D_S2_EftSlt01 = D_S1_UntStoreSklSlt [0]
    $ D_S2_EftSlt02 = D_S1_UntStoreSklSlt [1]
    $ D_S2_EftSlt03 = D_S1_UntStoreSklSlt [2]
    $ D_S2_EftSlt04 = D_S1_UntStoreSklSlt [3]
    $ D_S2_EftSlt05 = D_S1_UntStoreSklSlt [4]
    $ D_S2_EftSlt06 = D_S1_UntStoreSklSlt [5]
    $ D_S2_EftSlt01_No = D_S1_UntStoreSklSlt [6]
    $ D_S2_EftSlt02_No = D_S1_UntStoreSklSlt [7]
    $ D_S2_EftSlt03_No = D_S1_UntStoreSklSlt [8]
    $ D_S2_EftSlt04_No = D_S1_UntStoreSklSlt [9]
    $ D_S2_EftSlt05_No = D_S1_UntStoreSklSlt [10]
    $ D_S2_EftSlt06_No = D_S1_UntStoreSklSlt [11]
    $ D_S2_EftSlt01_Type = D_S1_UntStoreSklSlt [12]
    $ D_S2_EftSlt02_Type = D_S1_UntStoreSklSlt [13]
    $ D_S2_EftSlt03_Type = D_S1_UntStoreSklSlt [14]
    $ D_S2_EftSlt04_Type = D_S1_UntStoreSklSlt [15]
    $ D_S2_EftSlt05_Type = D_S1_UntStoreSklSlt [16]
    $ D_S2_EftSlt06_Type = D_S1_UntStoreSklSlt [17]
    $ D_S2_EftSlt01_Used = D_S1_UntStoreSklSlt [18]
    $ D_S2_EftSlt02_Used = D_S1_UntStoreSklSlt [19]
    $ D_S2_EftSlt03_Used = D_S1_UntStoreSklSlt [20]
    $ D_S2_EftSlt04_Used = D_S1_UntStoreSklSlt [21]
    $ D_S2_EftSlt05_Used = D_S1_UntStoreSklSlt [22]
    $ D_S2_EftSlt06_Used = D_S1_UntStoreSklSlt [23]
#-------------------------------
#-------------------------------
    $ D_S1_EftSlt01 = D_S2_UntStoreSklSlt [0]
    $ D_S1_EftSlt02 = D_S2_UntStoreSklSlt [1]
    $ D_S1_EftSlt03 = D_S2_UntStoreSklSlt [2]
    $ D_S1_EftSlt04 = D_S2_UntStoreSklSlt [3]
    $ D_S1_EftSlt05 = D_S2_UntStoreSklSlt [4]
    $ D_S1_EftSlt06 = D_S2_UntStoreSklSlt [5]
    $ D_S1_EftSlt01_No = D_S2_UntStoreSklSlt [6]
    $ D_S1_EftSlt02_No = D_S2_UntStoreSklSlt [7]
    $ D_S1_EftSlt03_No = D_S2_UntStoreSklSlt [8]
    $ D_S1_EftSlt04_No = D_S2_UntStoreSklSlt [9]
    $ D_S1_EftSlt05_No = D_S2_UntStoreSklSlt [10]
    $ D_S1_EftSlt06_No = D_S2_UntStoreSklSlt [11]
    $ D_S1_EftSlt01_Type = D_S2_UntStoreSklSlt [12]
    $ D_S1_EftSlt02_Type = D_S2_UntStoreSklSlt [13]
    $ D_S1_EftSlt03_Type = D_S2_UntStoreSklSlt [14]
    $ D_S1_EftSlt04_Type = D_S2_UntStoreSklSlt [15]
    $ D_S1_EftSlt05_Type = D_S2_UntStoreSklSlt [16]
    $ D_S1_EftSlt06_Type = D_S2_UntStoreSklSlt [17]
    $ D_S1_EftSlt01_Used = D_S2_UntStoreSklSlt [18]
    $ D_S1_EftSlt02_Used = D_S2_UntStoreSklSlt [19]
    $ D_S1_EftSlt03_Used = D_S2_UntStoreSklSlt [20]
    $ D_S1_EftSlt04_Used = D_S2_UntStoreSklSlt [21]
    $ D_S1_EftSlt05_Used = D_S2_UntStoreSklSlt [22]
    $ D_S1_EftSlt06_Used = D_S2_UntStoreSklSlt [23]
#-------------------------------
    return

#=====================================================
label BS_Chg_D_UntStoreSklSlt02_03:
#=====================================================
#-------------------------------
    call BS_Update_D_S2_UntStoreSklSlt
    call BS_Update_D_S3_UntStoreSklSlt
#-------------------------------
    $ D_S2_EftSlt01 = D_S3_UntStoreSklSlt [0]
    $ D_S2_EftSlt02 = D_S3_UntStoreSklSlt [1]
    $ D_S2_EftSlt03 = D_S3_UntStoreSklSlt [2]
    $ D_S2_EftSlt04 = D_S3_UntStoreSklSlt [3]
    $ D_S2_EftSlt05 = D_S3_UntStoreSklSlt [4]
    $ D_S2_EftSlt06 = D_S3_UntStoreSklSlt [5]
    $ D_S2_EftSlt01_No = D_S3_UntStoreSklSlt [6]
    $ D_S2_EftSlt02_No = D_S3_UntStoreSklSlt [7]
    $ D_S2_EftSlt03_No = D_S3_UntStoreSklSlt [8]
    $ D_S2_EftSlt04_No = D_S3_UntStoreSklSlt [9]
    $ D_S2_EftSlt05_No = D_S3_UntStoreSklSlt [10]
    $ D_S2_EftSlt06_No = D_S3_UntStoreSklSlt [11]
    $ D_S2_EftSlt01_Type = D_S3_UntStoreSklSlt [12]
    $ D_S2_EftSlt02_Type = D_S3_UntStoreSklSlt [13]
    $ D_S2_EftSlt03_Type = D_S3_UntStoreSklSlt [14]
    $ D_S2_EftSlt04_Type = D_S3_UntStoreSklSlt [15]
    $ D_S2_EftSlt05_Type = D_S3_UntStoreSklSlt [16]
    $ D_S2_EftSlt06_Type = D_S3_UntStoreSklSlt [17]
    $ D_S2_EftSlt01_Used = D_S3_UntStoreSklSlt [18]
    $ D_S2_EftSlt02_Used = D_S3_UntStoreSklSlt [19]
    $ D_S2_EftSlt03_Used = D_S3_UntStoreSklSlt [20]
    $ D_S2_EftSlt04_Used = D_S3_UntStoreSklSlt [21]
    $ D_S2_EftSlt05_Used = D_S3_UntStoreSklSlt [22]
    $ D_S2_EftSlt06_Used = D_S3_UntStoreSklSlt [23]
#-------------------------------
#-------------------------------
    $ D_S3_EftSlt01 = D_S2_UntStoreSklSlt [0]
    $ D_S3_EftSlt02 = D_S2_UntStoreSklSlt [1]
    $ D_S3_EftSlt03 = D_S2_UntStoreSklSlt [2]
    $ D_S3_EftSlt04 = D_S2_UntStoreSklSlt [3]
    $ D_S3_EftSlt05 = D_S2_UntStoreSklSlt [4]
    $ D_S3_EftSlt06 = D_S2_UntStoreSklSlt [5]
    $ D_S3_EftSlt01_No = D_S2_UntStoreSklSlt [6]
    $ D_S3_EftSlt02_No = D_S2_UntStoreSklSlt [7]
    $ D_S3_EftSlt03_No = D_S2_UntStoreSklSlt [8]
    $ D_S3_EftSlt04_No = D_S2_UntStoreSklSlt [9]
    $ D_S3_EftSlt05_No = D_S2_UntStoreSklSlt [10]
    $ D_S3_EftSlt06_No = D_S2_UntStoreSklSlt [11]
    $ D_S3_EftSlt01_Type = D_S2_UntStoreSklSlt [12]
    $ D_S3_EftSlt02_Type = D_S2_UntStoreSklSlt [13]
    $ D_S3_EftSlt03_Type = D_S2_UntStoreSklSlt [14]
    $ D_S3_EftSlt04_Type = D_S2_UntStoreSklSlt [15]
    $ D_S3_EftSlt05_Type = D_S2_UntStoreSklSlt [16]
    $ D_S3_EftSlt06_Type = D_S2_UntStoreSklSlt [17]
    $ D_S3_EftSlt01_Used = D_S2_UntStoreSklSlt [18]
    $ D_S3_EftSlt02_Used = D_S2_UntStoreSklSlt [19]
    $ D_S3_EftSlt03_Used = D_S2_UntStoreSklSlt [20]
    $ D_S3_EftSlt04_Used = D_S2_UntStoreSklSlt [21]
    $ D_S3_EftSlt05_Used = D_S2_UntStoreSklSlt [22]
    $ D_S3_EftSlt06_Used = D_S2_UntStoreSklSlt [23]
#-------------------------------
    return

#=====================================================
label BS_Chg_D_UntStoreSklSlt02_04:
#=====================================================
#-------------------------------
    call BS_Update_D_S2_UntStoreSklSlt
    call BS_Update_D_S4_UntStoreSklSlt
#-------------------------------
    $ D_S2_EftSlt01 = D_S4_UntStoreSklSlt [0]
    $ D_S2_EftSlt02 = D_S4_UntStoreSklSlt [1]
    $ D_S2_EftSlt03 = D_S4_UntStoreSklSlt [2]
    $ D_S2_EftSlt04 = D_S4_UntStoreSklSlt [3]
    $ D_S2_EftSlt05 = D_S4_UntStoreSklSlt [4]
    $ D_S2_EftSlt06 = D_S4_UntStoreSklSlt [5]
    $ D_S2_EftSlt01_No = D_S4_UntStoreSklSlt [6]
    $ D_S2_EftSlt02_No = D_S4_UntStoreSklSlt [7]
    $ D_S2_EftSlt03_No = D_S4_UntStoreSklSlt [8]
    $ D_S2_EftSlt04_No = D_S4_UntStoreSklSlt [9]
    $ D_S2_EftSlt05_No = D_S4_UntStoreSklSlt [10]
    $ D_S2_EftSlt06_No = D_S4_UntStoreSklSlt [11]
    $ D_S2_EftSlt01_Type = D_S4_UntStoreSklSlt [12]
    $ D_S2_EftSlt02_Type = D_S4_UntStoreSklSlt [13]
    $ D_S2_EftSlt03_Type = D_S4_UntStoreSklSlt [14]
    $ D_S2_EftSlt04_Type = D_S4_UntStoreSklSlt [15]
    $ D_S2_EftSlt05_Type = D_S4_UntStoreSklSlt [16]
    $ D_S2_EftSlt06_Type = D_S4_UntStoreSklSlt [17]
    $ D_S2_EftSlt01_Used = D_S4_UntStoreSklSlt [18]
    $ D_S2_EftSlt02_Used = D_S4_UntStoreSklSlt [19]
    $ D_S2_EftSlt03_Used = D_S4_UntStoreSklSlt [20]
    $ D_S2_EftSlt04_Used = D_S4_UntStoreSklSlt [21]
    $ D_S2_EftSlt05_Used = D_S4_UntStoreSklSlt [22]
    $ D_S2_EftSlt06_Used = D_S4_UntStoreSklSlt [23]
#-------------------------------
#-------------------------------
    $ D_S4_EftSlt01 = D_S2_UntStoreSklSlt [0]
    $ D_S4_EftSlt02 = D_S2_UntStoreSklSlt [1]
    $ D_S4_EftSlt03 = D_S2_UntStoreSklSlt [2]
    $ D_S4_EftSlt04 = D_S2_UntStoreSklSlt [3]
    $ D_S4_EftSlt05 = D_S2_UntStoreSklSlt [4]
    $ D_S4_EftSlt06 = D_S2_UntStoreSklSlt [5]
    $ D_S4_EftSlt01_No = D_S2_UntStoreSklSlt [6]
    $ D_S4_EftSlt02_No = D_S2_UntStoreSklSlt [7]
    $ D_S4_EftSlt03_No = D_S2_UntStoreSklSlt [8]
    $ D_S4_EftSlt04_No = D_S2_UntStoreSklSlt [9]
    $ D_S4_EftSlt05_No = D_S2_UntStoreSklSlt [10]
    $ D_S4_EftSlt06_No = D_S2_UntStoreSklSlt [11]
    $ D_S4_EftSlt01_Type = D_S2_UntStoreSklSlt [12]
    $ D_S4_EftSlt02_Type = D_S2_UntStoreSklSlt [13]
    $ D_S4_EftSlt03_Type = D_S2_UntStoreSklSlt [14]
    $ D_S4_EftSlt04_Type = D_S2_UntStoreSklSlt [15]
    $ D_S4_EftSlt05_Type = D_S2_UntStoreSklSlt [16]
    $ D_S4_EftSlt06_Type = D_S2_UntStoreSklSlt [17]
    $ D_S4_EftSlt01_Used = D_S2_UntStoreSklSlt [18]
    $ D_S4_EftSlt02_Used = D_S2_UntStoreSklSlt [19]
    $ D_S4_EftSlt03_Used = D_S2_UntStoreSklSlt [20]
    $ D_S4_EftSlt04_Used = D_S2_UntStoreSklSlt [21]
    $ D_S4_EftSlt05_Used = D_S2_UntStoreSklSlt [22]
    $ D_S4_EftSlt06_Used = D_S2_UntStoreSklSlt [23]
#-------------------------------
    return

#=====================================================
label BS_Chg_D_UntStoreSklSlt02_05:
#=====================================================
#-------------------------------
    call BS_Update_D_S2_UntStoreSklSlt
    call BS_Update_D_S5_UntStoreSklSlt
#-------------------------------
    $ D_S2_EftSlt01 = D_S5_UntStoreSklSlt [0]
    $ D_S2_EftSlt02 = D_S5_UntStoreSklSlt [1]
    $ D_S2_EftSlt03 = D_S5_UntStoreSklSlt [2]
    $ D_S2_EftSlt04 = D_S5_UntStoreSklSlt [3]
    $ D_S2_EftSlt05 = D_S5_UntStoreSklSlt [4]
    $ D_S2_EftSlt06 = D_S5_UntStoreSklSlt [5]
    $ D_S2_EftSlt01_No = D_S5_UntStoreSklSlt [6]
    $ D_S2_EftSlt02_No = D_S5_UntStoreSklSlt [7]
    $ D_S2_EftSlt03_No = D_S5_UntStoreSklSlt [8]
    $ D_S2_EftSlt04_No = D_S5_UntStoreSklSlt [9]
    $ D_S2_EftSlt05_No = D_S5_UntStoreSklSlt [10]
    $ D_S2_EftSlt06_No = D_S5_UntStoreSklSlt [11]
    $ D_S2_EftSlt01_Type = D_S5_UntStoreSklSlt [12]
    $ D_S2_EftSlt02_Type = D_S5_UntStoreSklSlt [13]
    $ D_S2_EftSlt03_Type = D_S5_UntStoreSklSlt [14]
    $ D_S2_EftSlt04_Type = D_S5_UntStoreSklSlt [15]
    $ D_S2_EftSlt05_Type = D_S5_UntStoreSklSlt [16]
    $ D_S2_EftSlt06_Type = D_S5_UntStoreSklSlt [17]
    $ D_S2_EftSlt01_Used = D_S5_UntStoreSklSlt [18]
    $ D_S2_EftSlt02_Used = D_S5_UntStoreSklSlt [19]
    $ D_S2_EftSlt03_Used = D_S5_UntStoreSklSlt [20]
    $ D_S2_EftSlt04_Used = D_S5_UntStoreSklSlt [21]
    $ D_S2_EftSlt05_Used = D_S5_UntStoreSklSlt [22]
    $ D_S2_EftSlt06_Used = D_S5_UntStoreSklSlt [23]
#-------------------------------
#-------------------------------
    $ D_S5_EftSlt01 = D_S2_UntStoreSklSlt [0]
    $ D_S5_EftSlt02 = D_S2_UntStoreSklSlt [1]
    $ D_S5_EftSlt03 = D_S2_UntStoreSklSlt [2]
    $ D_S5_EftSlt04 = D_S2_UntStoreSklSlt [3]
    $ D_S5_EftSlt05 = D_S2_UntStoreSklSlt [4]
    $ D_S5_EftSlt06 = D_S2_UntStoreSklSlt [5]
    $ D_S5_EftSlt01_No = D_S2_UntStoreSklSlt [6]
    $ D_S5_EftSlt02_No = D_S2_UntStoreSklSlt [7]
    $ D_S5_EftSlt03_No = D_S2_UntStoreSklSlt [8]
    $ D_S5_EftSlt04_No = D_S2_UntStoreSklSlt [9]
    $ D_S5_EftSlt05_No = D_S2_UntStoreSklSlt [10]
    $ D_S5_EftSlt06_No = D_S2_UntStoreSklSlt [11]
    $ D_S5_EftSlt01_Type = D_S2_UntStoreSklSlt [12]
    $ D_S5_EftSlt02_Type = D_S2_UntStoreSklSlt [13]
    $ D_S5_EftSlt03_Type = D_S2_UntStoreSklSlt [14]
    $ D_S5_EftSlt04_Type = D_S2_UntStoreSklSlt [15]
    $ D_S5_EftSlt05_Type = D_S2_UntStoreSklSlt [16]
    $ D_S5_EftSlt06_Type = D_S2_UntStoreSklSlt [17]
    $ D_S5_EftSlt01_Used = D_S2_UntStoreSklSlt [18]
    $ D_S5_EftSlt02_Used = D_S2_UntStoreSklSlt [19]
    $ D_S5_EftSlt03_Used = D_S2_UntStoreSklSlt [20]
    $ D_S5_EftSlt04_Used = D_S2_UntStoreSklSlt [21]
    $ D_S5_EftSlt05_Used = D_S2_UntStoreSklSlt [22]
    $ D_S5_EftSlt06_Used = D_S2_UntStoreSklSlt [23]
#-------------------------------
    return

#=====================================================
label BS_Chg_D_UntStoreSklSlt02_06:
#=====================================================
#-------------------------------
    call BS_Update_D_S2_UntStoreSklSlt
    call BS_Update_D_S6_UntStoreSklSlt
#-------------------------------
    $ D_S2_EftSlt01 = D_S6_UntStoreSklSlt [0]
    $ D_S2_EftSlt02 = D_S6_UntStoreSklSlt [1]
    $ D_S2_EftSlt03 = D_S6_UntStoreSklSlt [2]
    $ D_S2_EftSlt04 = D_S6_UntStoreSklSlt [3]
    $ D_S2_EftSlt05 = D_S6_UntStoreSklSlt [4]
    $ D_S2_EftSlt06 = D_S6_UntStoreSklSlt [5]
    $ D_S2_EftSlt01_No = D_S6_UntStoreSklSlt [6]
    $ D_S2_EftSlt02_No = D_S6_UntStoreSklSlt [7]
    $ D_S2_EftSlt03_No = D_S6_UntStoreSklSlt [8]
    $ D_S2_EftSlt04_No = D_S6_UntStoreSklSlt [9]
    $ D_S2_EftSlt05_No = D_S6_UntStoreSklSlt [10]
    $ D_S2_EftSlt06_No = D_S6_UntStoreSklSlt [11]
    $ D_S2_EftSlt01_Type = D_S6_UntStoreSklSlt [12]
    $ D_S2_EftSlt02_Type = D_S6_UntStoreSklSlt [13]
    $ D_S2_EftSlt03_Type = D_S6_UntStoreSklSlt [14]
    $ D_S2_EftSlt04_Type = D_S6_UntStoreSklSlt [15]
    $ D_S2_EftSlt05_Type = D_S6_UntStoreSklSlt [16]
    $ D_S2_EftSlt06_Type = D_S6_UntStoreSklSlt [17]
    $ D_S2_EftSlt01_Used = D_S6_UntStoreSklSlt [18]
    $ D_S2_EftSlt02_Used = D_S6_UntStoreSklSlt [19]
    $ D_S2_EftSlt03_Used = D_S6_UntStoreSklSlt [20]
    $ D_S2_EftSlt04_Used = D_S6_UntStoreSklSlt [21]
    $ D_S2_EftSlt05_Used = D_S6_UntStoreSklSlt [22]
    $ D_S2_EftSlt06_Used = D_S6_UntStoreSklSlt [23]
#-------------------------------
#-------------------------------
    $ D_S6_EftSlt01 = D_S2_UntStoreSklSlt [0]
    $ D_S6_EftSlt02 = D_S2_UntStoreSklSlt [1]
    $ D_S6_EftSlt03 = D_S2_UntStoreSklSlt [2]
    $ D_S6_EftSlt04 = D_S2_UntStoreSklSlt [3]
    $ D_S6_EftSlt05 = D_S2_UntStoreSklSlt [4]
    $ D_S6_EftSlt06 = D_S2_UntStoreSklSlt [5]
    $ D_S6_EftSlt01_No = D_S2_UntStoreSklSlt [6]
    $ D_S6_EftSlt02_No = D_S2_UntStoreSklSlt [7]
    $ D_S6_EftSlt03_No = D_S2_UntStoreSklSlt [8]
    $ D_S6_EftSlt04_No = D_S2_UntStoreSklSlt [9]
    $ D_S6_EftSlt05_No = D_S2_UntStoreSklSlt [10]
    $ D_S6_EftSlt06_No = D_S2_UntStoreSklSlt [11]
    $ D_S6_EftSlt01_Type = D_S2_UntStoreSklSlt [12]
    $ D_S6_EftSlt02_Type = D_S2_UntStoreSklSlt [13]
    $ D_S6_EftSlt03_Type = D_S2_UntStoreSklSlt [14]
    $ D_S6_EftSlt04_Type = D_S2_UntStoreSklSlt [15]
    $ D_S6_EftSlt05_Type = D_S2_UntStoreSklSlt [16]
    $ D_S6_EftSlt06_Type = D_S2_UntStoreSklSlt [17]
    $ D_S6_EftSlt01_Used = D_S2_UntStoreSklSlt [18]
    $ D_S6_EftSlt02_Used = D_S2_UntStoreSklSlt [19]
    $ D_S6_EftSlt03_Used = D_S2_UntStoreSklSlt [20]
    $ D_S6_EftSlt04_Used = D_S2_UntStoreSklSlt [21]
    $ D_S6_EftSlt05_Used = D_S2_UntStoreSklSlt [22]
    $ D_S6_EftSlt06_Used = D_S2_UntStoreSklSlt [23]
#-------------------------------
    return
