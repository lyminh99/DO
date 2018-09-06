
#==========================================
label Call_Show_Main_Scr_Duel:
#==========================================
    hide screen Scr_DuelTurn
    hide screen Scr_Duel
    hide screen Scr_Led_Sts
    show screen Scr_Duel
    show screen Scr_Led_Sts
    show screen Scr_DuelTurn
    return

#==========================================
label Call_Hide_Main_Scr_Duel:
#==========================================
    hide screen Scr_DuelTurn
    hide screen Scr_Duel
    hide screen Scr_Led_Sts
    return

#==========================================
label Call_Show_Scr_Duel:
#==========================================
    hide screen Scr_Duel
    show screen Scr_Duel
    return
