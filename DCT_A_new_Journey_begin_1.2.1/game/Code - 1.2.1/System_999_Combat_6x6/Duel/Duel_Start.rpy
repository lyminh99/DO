label Duel_Start:

    hide screen Scr_Atker
    hide screen Scr_Cls_All_Phase_02
    hide screen Scr_BattleInfo
    hide screen Scr_SkillEffect_Icon

    call DS_BackGround
    call Call_Show_Main_Scr_Duel

    call DS_Load_Basic_Setting
    call DS_Load_Led_Setting
    call DS_Load_Led_Stats
    call DS_Load_Led_CaculatedStats
    #call DS_Load_A_Led_BasStsRdm
    #call DS_Load_D_Led_BasStsRdm

    $ Duel = True
    $ renpy.pause(SecWait_Engage, hard = True)
    call DS_A_Chk_DmgType
    call DS_D_Chk_DmgType
    call Duel_Engage
    call DS_Chk_EndDuel
    call DS_End_Duel

    return

label Duel_Engage:

    if Duel == False:
        return
    else:
        if (DS_A_HP == 0 or DS_D_HP == 0) or DuelTurn <= 0:
            $ Duel = False
        elif DS_Which_Side == "Attacker":
            call DS_A_ActTurn
            jump Duel_Engage
        elif DS_Which_Side == "Deffender":
            call DS_D_ActTurn
            jump Duel_Engage

    return
        
