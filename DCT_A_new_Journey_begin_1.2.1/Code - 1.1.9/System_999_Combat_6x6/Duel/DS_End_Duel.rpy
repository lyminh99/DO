label DS_End_Duel:

    call Call_Hide_Main_Scr_Duel
    call Update_Scr_BackGround_On
    call Update_Scr_Cls_All_Phase_03_On
    call Update_Scr_BattleInfo_On

    $ DuelTurn = DuelTurn_Max
    $ DS_A_Scores = 0
    $ DS_D_Scores = 0
    $ DS_Lv_odd = 0

    return
