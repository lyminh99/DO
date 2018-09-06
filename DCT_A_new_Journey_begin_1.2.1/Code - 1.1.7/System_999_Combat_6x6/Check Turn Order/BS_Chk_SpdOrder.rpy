label BS_Chk_SpdOrder:

    if A_S1_Spd > 0 and A_S1_CanAct == 1:
        if A_S1_Spd > Turn_No_1 and A_S1_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = A_S1_Spd
            $ Turn_DislayNo_1 = "A_S1"
            $ A_S1_SpdChked = 1
        elif A_S1_Spd > Turn_No_2 and A_S1_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = A_S1_Spd
            $ Turn_DislayNo_2 = "A_S1"
            $ A_S1_SpdChked = 1
        elif A_S1_Spd > Turn_No_3 and A_S1_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = A_S1_Spd
            $ Turn_DislayNo_3 = "A_S1"
            $ A_S1_SpdChked = 1
        elif A_S1_Spd > Turn_No_4 and A_S1_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = A_S1_Spd
            $ Turn_DislayNo_4 = "A_S1"
            $ A_S1_SpdChked = 1
        elif A_S1_Spd > Turn_No_5 and A_S1_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = A_S1_Spd
            $ Turn_DislayNo_5 = "A_S1"
            $ A_S1_SpdChked = 1
        elif A_S1_Spd > Turn_No_6 and A_S1_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = A_S1_Spd
            $ Turn_DislayNo_6 = "A_S1"
            $ A_S1_SpdChked = 1
        elif A_S1_Spd > Turn_No_7 and A_S1_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = A_S1_Spd
            $ Turn_DislayNo_7 = "A_S1"
            $ A_S1_SpdChked = 1
        elif A_S1_Spd > Turn_No_8 and A_S1_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = A_S1_Spd
            $ Turn_DislayNo_8 = "A_S1"
            $ A_S1_SpdChked = 1
        elif A_S1_Spd > Turn_No_9 and A_S1_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = A_S1_Spd
            $ Turn_DislayNo_9 = "A_S1"
            $ A_S1_SpdChked = 1
        elif A_S1_Spd > Turn_No_10 and A_S1_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = A_S1_Spd
            $ Turn_DislayNo_10 = "A_S1"
            $ A_S1_SpdChked = 1
        elif A_S1_Spd > Turn_No_11 and A_S1_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = A_S1_Spd
            $ Turn_DislayNo_11 = "A_S1"
            $ A_S1_SpdChked = 1
        elif A_S1_Spd > Turn_No_12 and A_S1_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = A_S1_Spd
            $ Turn_DislayNo_12 = "A_S1"
            $ A_S1_SpdChked = 1

    if D_S1_Spd > 0 and D_S1_CanAct == 1:
        if D_S1_Spd > Turn_No_1 and D_S1_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = D_S1_Spd
            $ Turn_DislayNo_1 = "D_S1"
            $ D_S1_SpdChked = 1
        elif D_S1_Spd > Turn_No_2 and D_S1_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = D_S1_Spd
            $ Turn_DislayNo_2 = "D_S1"
            $ D_S1_SpdChked = 1
        elif D_S1_Spd > Turn_No_3 and D_S1_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = D_S1_Spd
            $ Turn_DislayNo_3 = "D_S1"
            $ D_S1_SpdChked = 1
        elif D_S1_Spd > Turn_No_4 and D_S1_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = D_S1_Spd
            $ Turn_DislayNo_4 = "D_S1"
            $ D_S1_SpdChked = 1
        elif D_S1_Spd > Turn_No_5 and D_S1_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = D_S1_Spd
            $ Turn_DislayNo_5 = "D_S1"
            $ D_S1_SpdChked = 1
        elif D_S1_Spd > Turn_No_6 and D_S1_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = D_S1_Spd
            $ Turn_DislayNo_6 = "D_S1"
            $ D_S1_SpdChked = 1
        elif D_S1_Spd > Turn_No_7 and D_S1_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = D_S1_Spd
            $ Turn_DislayNo_7 = "D_S1"
            $ D_S1_SpdChked = 1
        elif D_S1_Spd > Turn_No_8 and D_S1_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = D_S1_Spd
            $ Turn_DislayNo_8 = "D_S1"
            $ D_S1_SpdChked = 1
        elif D_S1_Spd > Turn_No_9 and D_S1_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = D_S1_Spd
            $ Turn_DislayNo_9 = "D_S1"
            $ D_S1_SpdChked = 1
        elif D_S1_Spd > Turn_No_10 and D_S1_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = D_S1_Spd
            $ Turn_DislayNo_10 = "D_S1"
            $ D_S1_SpdChked = 1
        elif D_S1_Spd > Turn_No_11 and D_S1_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = D_S1_Spd
            $ Turn_DislayNo_11 = "D_S1"
            $ D_S1_SpdChked = 1
        elif D_S1_Spd > Turn_No_12 and D_S1_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = D_S1_Spd
            $ Turn_DislayNo_12 = "D_S1"
            $ D_S1_SpdChked = 1

    if A_S2_Spd > 0 and A_S2_CanAct == 1:
        if A_S2_Spd > Turn_No_1 and A_S2_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = A_S2_Spd
            $ Turn_DislayNo_1 = "A_S2"
            $ A_S2_SpdChked = 1
        elif A_S2_Spd > Turn_No_2 and A_S2_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = A_S2_Spd
            $ Turn_DislayNo_2 = "A_S2"
            $ A_S2_SpdChked = 1
        elif A_S2_Spd > Turn_No_3 and A_S2_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = A_S2_Spd
            $ Turn_DislayNo_3 = "A_S2"
            $ A_S2_SpdChked = 1
        elif A_S2_Spd > Turn_No_4 and A_S2_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = A_S2_Spd
            $ Turn_DislayNo_4 = "A_S2"
            $ A_S2_SpdChked = 1
        elif A_S2_Spd > Turn_No_5 and A_S2_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = A_S2_Spd
            $ Turn_DislayNo_5 = "A_S2"
            $ A_S2_SpdChked = 1
        elif A_S2_Spd > Turn_No_6 and A_S2_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = A_S2_Spd
            $ Turn_DislayNo_6 = "A_S2"
            $ A_S2_SpdChked = 1
        elif A_S2_Spd > Turn_No_7 and A_S2_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = A_S2_Spd
            $ Turn_DislayNo_7 = "A_S2"
            $ A_S2_SpdChked = 1
        elif A_S2_Spd > Turn_No_8 and A_S2_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = A_S2_Spd
            $ Turn_DislayNo_8 = "A_S2"
            $ A_S2_SpdChked = 1
        elif A_S2_Spd > Turn_No_9 and A_S2_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = A_S2_Spd
            $ Turn_DislayNo_9 = "A_S2"
            $ A_S2_SpdChked = 1
        elif A_S2_Spd > Turn_No_10 and A_S2_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = A_S2_Spd
            $ Turn_DislayNo_10 = "A_S2"
            $ A_S2_SpdChked = 1
        elif A_S2_Spd > Turn_No_11 and A_S2_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = A_S2_Spd
            $ Turn_DislayNo_11 = "A_S2"
            $ A_S2_SpdChked = 1
        elif A_S2_Spd > Turn_No_12 and A_S2_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = A_S2_Spd
            $ Turn_DislayNo_12 = "A_S2"
            $ A_S2_SpdChked = 1

    if D_S2_Spd > 0 and D_S2_CanAct == 1:
        if D_S2_Spd > Turn_No_1 and D_S2_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = D_S2_Spd
            $ Turn_DislayNo_1 = "D_S2"
            $ D_S2_SpdChked = 1
        elif D_S2_Spd > Turn_No_2 and D_S2_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = D_S2_Spd
            $ Turn_DislayNo_2 = "D_S2"
            $ D_S2_SpdChked = 1
        elif D_S2_Spd > Turn_No_3 and D_S2_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = D_S2_Spd
            $ Turn_DislayNo_3 = "D_S2"
            $ D_S2_SpdChked = 1
        elif D_S2_Spd > Turn_No_4 and D_S2_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = D_S2_Spd
            $ Turn_DislayNo_4 = "D_S2"
            $ D_S2_SpdChked = 1
        elif D_S2_Spd > Turn_No_5 and D_S2_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = D_S2_Spd
            $ Turn_DislayNo_5 = "D_S2"
            $ D_S2_SpdChked = 1
        elif D_S2_Spd > Turn_No_6 and D_S2_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = D_S2_Spd
            $ Turn_DislayNo_6 = "D_S2"
            $ D_S2_SpdChked = 1
        elif D_S2_Spd > Turn_No_7 and D_S2_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = D_S2_Spd
            $ Turn_DislayNo_7 = "D_S2"
            $ D_S2_SpdChked = 1
        elif D_S2_Spd > Turn_No_8 and D_S2_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = D_S2_Spd
            $ Turn_DislayNo_8 = "D_S2"
            $ D_S2_SpdChked = 1
        elif D_S2_Spd > Turn_No_9 and D_S2_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = D_S2_Spd
            $ Turn_DislayNo_9 = "D_S2"
            $ D_S2_SpdChked = 1
        elif D_S2_Spd > Turn_No_10 and D_S2_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = D_S2_Spd
            $ Turn_DislayNo_10 = "D_S2"
            $ D_S2_SpdChked = 1
        elif D_S2_Spd > Turn_No_11 and D_S2_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = D_S2_Spd
            $ Turn_DislayNo_11 = "D_S2"
            $ D_S2_SpdChked = 1
        elif D_S2_Spd > Turn_No_12 and D_S2_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = D_S2_Spd
            $ Turn_DislayNo_12 = "D_S2"
            $ D_S2_SpdChked = 1

    if A_S3_Spd > 0 and A_S3_CanAct == 1:
        if A_S3_Spd > Turn_No_1 and A_S3_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = A_S3_Spd
            $ Turn_DislayNo_1 = "A_S3"
            $ A_S3_SpdChked = 1
        elif A_S3_Spd > Turn_No_2 and A_S3_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = A_S3_Spd
            $ Turn_DislayNo_2 = "A_S3"
            $ A_S3_SpdChked = 1
        elif A_S3_Spd > Turn_No_3 and A_S3_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = A_S3_Spd
            $ Turn_DislayNo_3 = "A_S3"
            $ A_S3_SpdChked = 1
        elif A_S3_Spd > Turn_No_4 and A_S3_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = A_S3_Spd
            $ Turn_DislayNo_4 = "A_S3"
            $ A_S3_SpdChked = 1
        elif A_S3_Spd > Turn_No_5 and A_S3_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = A_S3_Spd
            $ Turn_DislayNo_5 = "A_S3"
            $ A_S3_SpdChked = 1
        elif A_S3_Spd > Turn_No_6 and A_S3_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = A_S3_Spd
            $ Turn_DislayNo_6 = "A_S3"
            $ A_S3_SpdChked = 1
        elif A_S3_Spd > Turn_No_7 and A_S3_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = A_S3_Spd
            $ Turn_DislayNo_7 = "A_S3"
            $ A_S3_SpdChked = 1
        elif A_S3_Spd > Turn_No_8 and A_S3_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = A_S3_Spd
            $ Turn_DislayNo_8 = "A_S3"
            $ A_S3_SpdChked = 1
        elif A_S3_Spd > Turn_No_9 and A_S3_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = A_S3_Spd
            $ Turn_DislayNo_9 = "A_S3"
            $ A_S3_SpdChked = 1
        elif A_S3_Spd > Turn_No_10 and A_S3_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = A_S3_Spd
            $ Turn_DislayNo_10 = "A_S3"
            $ A_S3_SpdChked = 1
        elif A_S3_Spd > Turn_No_11 and A_S3_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = A_S3_Spd
            $ Turn_DislayNo_11 = "A_S3"
            $ A_S3_SpdChked = 1
        elif A_S3_Spd > Turn_No_12 and A_S3_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = A_S3_Spd
            $ Turn_DislayNo_12 = "A_S3"
            $ A_S3_SpdChked = 1

    if D_S3_Spd > 0 and D_S3_CanAct == 1:
        if D_S3_Spd > Turn_No_1 and D_S3_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = D_S3_Spd
            $ Turn_DislayNo_1 = "D_S3"
            $ D_S3_SpdChked = 1
        elif D_S3_Spd > Turn_No_2 and D_S3_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = D_S3_Spd
            $ Turn_DislayNo_2 = "D_S3"
            $ D_S3_SpdChked = 1
        elif D_S3_Spd > Turn_No_3 and D_S3_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = D_S3_Spd
            $ Turn_DislayNo_3 = "D_S3"
            $ D_S3_SpdChked = 1
        elif D_S3_Spd > Turn_No_4 and D_S3_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = D_S3_Spd
            $ Turn_DislayNo_4 = "D_S3"
            $ D_S3_SpdChked = 1
        elif D_S3_Spd > Turn_No_5 and D_S3_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = D_S3_Spd
            $ Turn_DislayNo_5 = "D_S3"
            $ D_S3_SpdChked = 1
        elif D_S3_Spd > Turn_No_6 and D_S3_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = D_S3_Spd
            $ Turn_DislayNo_6 = "D_S3"
            $ D_S3_SpdChked = 1
        elif D_S3_Spd > Turn_No_7 and D_S3_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = D_S3_Spd
            $ Turn_DislayNo_7 = "D_S3"
            $ D_S3_SpdChked = 1
        elif D_S3_Spd > Turn_No_8 and D_S3_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = D_S3_Spd
            $ Turn_DislayNo_8 = "D_S3"
            $ D_S3_SpdChked = 1
        elif D_S3_Spd > Turn_No_9 and D_S3_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = D_S3_Spd
            $ Turn_DislayNo_9 = "D_S3"
            $ D_S3_SpdChked = 1
        elif D_S3_Spd > Turn_No_10 and D_S3_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = D_S3_Spd
            $ Turn_DislayNo_10 = "D_S3"
            $ D_S3_SpdChked = 1
        elif D_S3_Spd > Turn_No_11 and D_S3_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = D_S3_Spd
            $ Turn_DislayNo_11 = "D_S3"
            $ D_S3_SpdChked = 1
        elif D_S3_Spd > Turn_No_12 and D_S3_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = D_S3_Spd
            $ Turn_DislayNo_12 = "D_S3"
            $ D_S3_SpdChked = 1

    if A_S4_Spd > 0 and A_S4_CanAct == 1:
        if A_S4_Spd > Turn_No_1 and A_S4_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = A_S4_Spd
            $ Turn_DislayNo_1 = "A_S4"
            $ A_S4_SpdChked = 1
        elif A_S4_Spd > Turn_No_2 and A_S4_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = A_S4_Spd
            $ Turn_DislayNo_2 = "A_S4"
            $ A_S4_SpdChked = 1
        elif A_S4_Spd > Turn_No_3 and A_S4_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = A_S4_Spd
            $ Turn_DislayNo_3 = "A_S4"
            $ A_S4_SpdChked = 1
        elif A_S4_Spd > Turn_No_4 and A_S4_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = A_S4_Spd
            $ Turn_DislayNo_4 = "A_S4"
            $ A_S4_SpdChked = 1
        elif A_S4_Spd > Turn_No_5 and A_S4_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = A_S4_Spd
            $ Turn_DislayNo_5 = "A_S4"
            $ A_S4_SpdChked = 1
        elif A_S4_Spd > Turn_No_6 and A_S4_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = A_S4_Spd
            $ Turn_DislayNo_6 = "A_S4"
            $ A_S4_SpdChked = 1
        elif A_S4_Spd > Turn_No_7 and A_S4_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = A_S4_Spd
            $ Turn_DislayNo_7 = "A_S4"
            $ A_S4_SpdChked = 1
        elif A_S4_Spd > Turn_No_8 and A_S4_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = A_S4_Spd
            $ Turn_DislayNo_8 = "A_S4"
            $ A_S4_SpdChked = 1
        elif A_S4_Spd > Turn_No_9 and A_S4_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = A_S4_Spd
            $ Turn_DislayNo_9 = "A_S4"
            $ A_S4_SpdChked = 1
        elif A_S4_Spd > Turn_No_10 and A_S4_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = A_S4_Spd
            $ Turn_DislayNo_10 = "A_S4"
            $ A_S4_SpdChked = 1
        elif A_S4_Spd > Turn_No_11 and A_S4_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = A_S4_Spd
            $ Turn_DislayNo_11 = "A_S4"
            $ A_S4_SpdChked = 1
        elif A_S4_Spd > Turn_No_12 and A_S4_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = A_S4_Spd
            $ Turn_DislayNo_12 = "A_S4"
            $ A_S4_SpdChked = 1

    if D_S4_Spd > 0 and D_S4_CanAct == 1:
        if D_S4_Spd > Turn_No_1 and D_S4_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = D_S4_Spd
            $ Turn_DislayNo_1 = "D_S4"
            $ D_S4_SpdChked = 1
        elif D_S4_Spd > Turn_No_2 and D_S4_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = D_S4_Spd
            $ Turn_DislayNo_2 = "D_S4"
            $ D_S4_SpdChked = 1
        elif D_S4_Spd > Turn_No_3 and D_S4_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = D_S4_Spd
            $ Turn_DislayNo_3 = "D_S4"
            $ D_S4_SpdChked = 1
        elif D_S4_Spd > Turn_No_4 and D_S4_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = D_S4_Spd
            $ Turn_DislayNo_4 = "D_S4"
            $ D_S4_SpdChked = 1
        elif D_S4_Spd > Turn_No_5 and D_S4_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = D_S4_Spd
            $ Turn_DislayNo_5 = "D_S4"
            $ D_S4_SpdChked = 1
        elif D_S4_Spd > Turn_No_6 and D_S4_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = D_S4_Spd
            $ Turn_DislayNo_6 = "D_S4"
            $ D_S4_SpdChked = 1
        elif D_S4_Spd > Turn_No_7 and D_S4_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = D_S4_Spd
            $ Turn_DislayNo_7 = "D_S4"
            $ D_S4_SpdChked = 1
        elif D_S4_Spd > Turn_No_8 and D_S4_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = D_S4_Spd
            $ Turn_DislayNo_8 = "D_S4"
            $ D_S4_SpdChked = 1
        elif D_S4_Spd > Turn_No_9 and D_S4_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = D_S4_Spd
            $ Turn_DislayNo_9 = "D_S4"
            $ D_S4_SpdChked = 1
        elif D_S4_Spd > Turn_No_10 and D_S4_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = D_S4_Spd
            $ Turn_DislayNo_10 = "D_S4"
            $ D_S4_SpdChked = 1
        elif D_S4_Spd > Turn_No_11 and D_S4_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = D_S4_Spd
            $ Turn_DislayNo_11 = "D_S4"
            $ D_S4_SpdChked = 1
        elif D_S4_Spd > Turn_No_12 and D_S4_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = D_S4_Spd
            $ Turn_DislayNo_12 = "D_S4"
            $ D_S4_SpdChked = 1

    if A_S5_Spd > 0 and A_S5_CanAct ==1:
        if A_S5_Spd > Turn_No_1 and A_S5_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = A_S5_Spd
            $ Turn_DislayNo_1 = "A_S5"
            $ A_S5_SpdChked = 1
        elif A_S5_Spd > Turn_No_2 and A_S5_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = A_S5_Spd
            $ Turn_DislayNo_2 = "A_S5"
            $ A_S5_SpdChked = 1
        elif A_S5_Spd > Turn_No_3 and A_S5_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = A_S5_Spd
            $ Turn_DislayNo_3 = "A_S5"
            $ A_S5_SpdChked = 1
        elif A_S5_Spd > Turn_No_4 and A_S5_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = A_S5_Spd
            $ Turn_DislayNo_4 = "A_S5"
            $ A_S5_SpdChked = 1
        elif A_S5_Spd > Turn_No_5 and A_S5_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = A_S5_Spd
            $ Turn_DislayNo_5 = "A_S5"
            $ A_S5_SpdChked = 1
        elif A_S5_Spd > Turn_No_6 and A_S5_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = A_S5_Spd
            $ Turn_DislayNo_6 = "A_S5"
            $ A_S5_SpdChked = 1
        elif A_S5_Spd > Turn_No_7 and A_S5_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = A_S5_Spd
            $ Turn_DislayNo_7 = "A_S5"
            $ A_S5_SpdChked = 1
        elif A_S5_Spd > Turn_No_8 and A_S5_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = A_S5_Spd
            $ Turn_DislayNo_8 = "A_S5"
            $ A_S5_SpdChked = 1
        elif A_S5_Spd > Turn_No_9 and A_S5_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = A_S5_Spd
            $ Turn_DislayNo_9 = "A_S5"
            $ A_S5_SpdChked = 1
        elif A_S5_Spd > Turn_No_10 and A_S5_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = A_S5_Spd
            $ Turn_DislayNo_10 = "A_S5"
            $ A_S5_SpdChked = 1
        elif A_S5_Spd > Turn_No_11 and A_S5_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = A_S5_Spd
            $ Turn_DislayNo_11 = "A_S5"
            $ A_S5_SpdChked = 1
        elif A_S5_Spd > Turn_No_12 and A_S5_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = A_S5_Spd
            $ Turn_DislayNo_12 = "A_S5"
            $ A_S5_SpdChked = 1

    if D_S5_Spd > 0 and D_S5_CanAct ==1:
        if D_S5_Spd > Turn_No_1 and D_S5_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = D_S5_Spd
            $ Turn_DislayNo_1 = "D_S5"
            $ D_S5_SpdChked = 1
        elif D_S5_Spd > Turn_No_2 and D_S5_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = D_S5_Spd
            $ Turn_DislayNo_2 = "D_S5"
            $ D_S5_SpdChked = 1
        elif D_S5_Spd > Turn_No_3 and D_S5_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = D_S5_Spd
            $ Turn_DislayNo_3 = "D_S5"
            $ D_S5_SpdChked = 1
        elif D_S5_Spd > Turn_No_4 and D_S5_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = D_S5_Spd
            $ Turn_DislayNo_4 = "D_S5"
            $ D_S5_SpdChked = 1
        elif D_S5_Spd > Turn_No_5 and D_S5_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = D_S5_Spd
            $ Turn_DislayNo_5 = "D_S5"
            $ D_S5_SpdChked = 1
        elif D_S5_Spd > Turn_No_6 and D_S5_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = D_S5_Spd
            $ Turn_DislayNo_6 = "D_S5"
            $ D_S5_SpdChked = 1
        elif D_S5_Spd > Turn_No_7 and D_S5_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = D_S5_Spd
            $ Turn_DislayNo_7 = "D_S5"
            $ D_S5_SpdChked = 1
        elif D_S5_Spd > Turn_No_8 and D_S5_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = D_S5_Spd
            $ Turn_DislayNo_8 = "D_S5"
            $ D_S5_SpdChked = 1
        elif D_S5_Spd > Turn_No_9 and D_S5_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = D_S5_Spd
            $ Turn_DislayNo_9 = "D_S5"
            $ D_S5_SpdChked = 1
        elif D_S5_Spd > Turn_No_10 and D_S5_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = D_S5_Spd
            $ Turn_DislayNo_10 = "D_S5"
            $ D_S5_SpdChked = 1
        elif D_S5_Spd > Turn_No_11 and D_S5_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = D_S5_Spd
            $ Turn_DislayNo_11 = "D_S5"
            $ D_S5_SpdChked = 1
        elif D_S5_Spd > Turn_No_12 and D_S5_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = D_S5_Spd
            $ Turn_DislayNo_12 = "D_S5"
            $ D_S5_SpdChked = 1

    if A_S6_Spd > 0 and A_S6_CanAct == 1:
        if A_S6_Spd > Turn_No_1 and A_S6_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = A_S6_Spd
            $ Turn_DislayNo_1 = "A_S6"
            $ A_S6_SpdChked = 1
        elif A_S6_Spd > Turn_No_2 and A_S6_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = A_S6_Spd
            $ Turn_DislayNo_2 = "A_S6"
            $ A_S6_SpdChked = 1
        elif A_S6_Spd > Turn_No_3 and A_S6_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = A_S6_Spd
            $ Turn_DislayNo_3 = "A_S6"
            $ A_S6_SpdChked = 1
        elif A_S6_Spd > Turn_No_4 and A_S6_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = A_S6_Spd
            $ Turn_DislayNo_4 = "A_S6"
            $ A_S6_SpdChked = 1
        elif A_S6_Spd > Turn_No_5 and A_S6_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = A_S6_Spd
            $ Turn_DislayNo_5 = "A_S6"
            $ A_S6_SpdChked = 1
        elif A_S6_Spd > Turn_No_6 and A_S6_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = A_S6_Spd
            $ Turn_DislayNo_6 = "A_S6"
            $ A_S6_SpdChked = 1
        elif A_S6_Spd > Turn_No_7 and A_S6_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = A_S6_Spd
            $ Turn_DislayNo_7 = "A_S6"
            $ A_S6_SpdChked = 1
        elif A_S6_Spd > Turn_No_8 and A_S6_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = A_S6_Spd
            $ Turn_DislayNo_8 = "A_S6"
            $ A_S6_SpdChked = 1
        elif A_S6_Spd > Turn_No_9 and A_S6_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = A_S6_Spd
            $ Turn_DislayNo_9 = "A_S6"
            $ A_S6_SpdChked = 1
        elif A_S6_Spd > Turn_No_10 and A_S6_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = A_S6_Spd
            $ Turn_DislayNo_10 = "A_S6"
            $ A_S6_SpdChked = 1
        elif A_S6_Spd > Turn_No_11 and A_S6_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = A_S6_Spd
            $ Turn_DislayNo_11 = "A_S6"
            $ A_S6_SpdChked = 1
        elif A_S6_Spd > Turn_No_12 and A_S6_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = A_S6_Spd
            $ Turn_DislayNo_12 = "A_S6"
            $ A_S6_SpdChked = 1

    if D_S6_Spd > 0 and D_S6_CanAct == 1:
        if D_S6_Spd > Turn_No_1 and D_S6_SpdChked == 0:
            call BS_Chg_Order_1
            $ Turn_No_1 = D_S6_Spd
            $ Turn_DislayNo_1 = "D_S6"
            $ D_S6_SpdChked = 1
        elif D_S6_Spd > Turn_No_2 and D_S6_SpdChked == 0:
            call BS_Chg_Order_2
            $ Turn_No_2 = D_S6_Spd
            $ Turn_DislayNo_2 = "D_S6"
            $ D_S6_SpdChked = 1
        elif D_S6_Spd > Turn_No_3 and D_S6_SpdChked == 0:
            call BS_Chg_Order_3
            $ Turn_No_3 = D_S6_Spd
            $ Turn_DislayNo_3 = "D_S6"
            $ D_S6_SpdChked = 1
        elif D_S6_Spd > Turn_No_4 and D_S6_SpdChked == 0:
            call BS_Chg_Order_4
            $ Turn_No_4 = D_S6_Spd
            $ Turn_DislayNo_4 = "D_S6"
            $ D_S6_SpdChked = 1
        elif D_S6_Spd > Turn_No_5 and D_S6_SpdChked == 0:
            call BS_Chg_Order_5
            $ Turn_No_5 = D_S6_Spd
            $ Turn_DislayNo_5 = "D_S6"
            $ D_S6_SpdChked = 1
        elif D_S6_Spd > Turn_No_6 and D_S6_SpdChked == 0:
            call BS_Chg_Order_6
            $ Turn_No_6 = D_S6_Spd
            $ Turn_DislayNo_6 = "D_S6"
            $ D_S6_SpdChked = 1
        elif D_S6_Spd > Turn_No_7 and D_S6_SpdChked == 0:
            call BS_Chg_Order_7
            $ Turn_No_7 = D_S6_Spd
            $ Turn_DislayNo_7 = "D_S6"
            $ D_S6_SpdChked = 1
        elif D_S6_Spd > Turn_No_8 and D_S6_SpdChked == 0:
            call BS_Chg_Order_8
            $ Turn_No_8 = D_S6_Spd
            $ Turn_DislayNo_8 = "D_S6"
            $ D_S6_SpdChked = 1
        elif D_S6_Spd > Turn_No_9 and D_S6_SpdChked == 0:
            call BS_Chg_Order_9
            $ Turn_No_9 = D_S6_Spd
            $ Turn_DislayNo_9 = "D_S6"
            $ D_S6_SpdChked = 1
        elif D_S6_Spd > Turn_No_10 and D_S6_SpdChked == 0:
            call BS_Chg_Order_10
            $ Turn_No_10 = D_S6_Spd
            $ Turn_DislayNo_10 = "D_S6"
            $ D_S6_SpdChked = 1
        elif D_S6_Spd > Turn_No_11 and D_S6_SpdChked == 0:
            call BS_Chg_Order_11
            $ Turn_No_11 = D_S6_Spd
            $ Turn_DislayNo_11 = "D_S6"
            $ D_S6_SpdChked = 1
        elif D_S6_Spd > Turn_No_12 and D_S6_SpdChked == 0:
            call BS_Chg_Order_12
            $ Turn_No_12 = D_S6_Spd
            $ Turn_DislayNo_12 = "D_S6"
            $ D_S6_SpdChked = 1

    return