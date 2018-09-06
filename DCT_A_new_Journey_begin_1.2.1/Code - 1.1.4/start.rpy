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
        "Start the game Normally":
            if Sys_Current_Game == "DCT":
                call Sys_DCT_Chk_Ending
            elif Sys_Current_Game == "SMM":
                call Sys_SMM_Storyline_VN
    e"Game end"

    return