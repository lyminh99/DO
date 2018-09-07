###############################################################
# The game starts here.
# Prologue 1.

label start:

    show screen Scr_Sys_Controls

    stop music
    menu:
    
        "DCT":
            call Sys_DCT_Chk_Ending
        "DCT - Line Checking mode":
            call Sys_DCT_Chk_Lines
        "SMM":
            call Sys_SMM_Storyline_VN
        "SMM - Home":
            call Sys_SMM_Start_Check
        "Conversation":
            call CS_Start
        "Puzzle ":
            call Start_Puzzle
        "Sub quest":
            call Start_SubQuest
        "Character Creation":
            call Start_CharCreation
            menu:
                "How about a match ?"
                "Yes":
                    call Battle_Start
                "No":
                    pass
        "Battle System":
            call Battle_Start
        "Start the game Normally":
            if persistent.Sys_Current_Game == "DCT":
                call Sys_DCT_Chk_Ending
            elif persistent.Sys_Current_Game == "SMM":
                call Sys_SMM_Storyline_VN

    e"Game end (real)"

    return