label BS_BeginChk_SpdOrder:
    
    $ Turn_No_1 = 0
    $ Turn_No_2 = 0
    $ Turn_No_3 = 0
    $ Turn_No_4 = 0
    $ Turn_No_5 = 0
    $ Turn_No_6 = 0
    $ Turn_No_7 = 0
    $ Turn_No_8 = 0
    $ Turn_No_9 = 0
    $ Turn_No_10 = 0
    $ Turn_No_11 = 0
    $ Turn_No_12 = 0
    $ Turn_No_13 = 0
    $ Turn_DislayNo_1 = 0
    $ Turn_DislayNo_2 = 0
    $ Turn_DislayNo_3 = 0
    $ Turn_DislayNo_4 = 0
    $ Turn_DislayNo_5 = 0
    $ Turn_DislayNo_6 = 0
    $ Turn_DislayNo_7 = 0
    $ Turn_DislayNo_8 = 0
    $ Turn_DislayNo_9 = 0
    $ Turn_DislayNo_10 = 0
    $ Turn_DislayNo_11 = 0
    $ Turn_DislayNo_12 = 0
    $ Turn_DislayNo_13 = 0
    $ A_S1_SpdChked = 0
    $ A_S2_SpdChked = 0
    $ A_S3_SpdChked = 0
    $ A_S4_SpdChked = 0
    $ A_S5_SpdChked = 0
    $ A_S6_SpdChked = 0
    $ D_S1_SpdChked = 0
    $ D_S2_SpdChked = 0
    $ D_S3_SpdChked = 0
    $ D_S4_SpdChked = 0
    $ D_S5_SpdChked = 0
    $ D_S6_SpdChked = 0
    $ Total_NoOcu = 0
    $ Total_UnitCanAct = 0

    $ Total_UnitCanAct = (A_S1_CanAct) + (
    A_S2_CanAct) + (
    A_S3_CanAct) + (
    A_S4_CanAct) + (
    A_S5_CanAct) + (
    A_S6_CanAct) + (
    D_S1_CanAct) + (
    D_S2_CanAct) + (
    D_S3_CanAct) + (
    D_S4_CanAct) + (
    D_S5_CanAct) + (
    D_S6_CanAct)

    while Total_UnitCanAct > Total_NoOcu:
        call BS_Chk_SpdOrder

    return