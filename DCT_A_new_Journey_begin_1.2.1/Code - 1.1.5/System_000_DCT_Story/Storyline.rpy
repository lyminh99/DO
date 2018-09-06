label Storyline:
    stop music fadeout 1.0
    #if persistent.Demo_finish == True:
        #call Secret_garden 

#------------------------------------------------------
    $ Sys_GameProgress = "prologue2"
    $ Sys_MapPoints += 1    # = 1
    if Sys_SkipAll > 0:
        call prologue2
#------------------------------------------------------
    $ Sys_GameProgress = "gc_chuong1"
    $ Sys_MapPoints += 1    # = 2
    if Sys_SkipAll > 0:
        call gc_chuong1
#------------------------------------------------------
    $ Sys_GameProgress = "gc_chuong21"
    $ Sys_MapPoints += 1    # = 3
    if Sys_SkipAll > 0:
        call gc_chuong2
#------------------------------------------------------
    $ Sys_GameProgress = "gc_chuong3"
    $ Sys_MapPoints += 1    # = 4
    if Sys_SkipAll > 0:
        call gc_chuong3
#------------------------------------------------------
    $ Sys_GameProgress = "gc_chuong4"
    $ Sys_MapPoints += 1    # = 5
    if Sys_SkipAll > 0:
        call gc_chuong4
#------------------------------------------------------
    $ Sys_GameProgress = "Ch1P1"
    $ Sys_MapPoints += 1    # = 6
    if Sys_SkipAll > 0:
        call Ch1P1
#------------------------------------------------------

################################################################################
#Choice 1
    if Sys_SkipAll > 0:
        scene BG_6 with dissolve
    menu:
        "Tiếp tục dạo phố":
            $ Sys_GameProgress = "Ch1_choice_001_played"
            $ Ch1_choice_001_played = 1
        "Đến Nhà thờ.":
            $ Sys_GameProgress = "Ch1P1_C2"
            $ Ch1P1_C2_played = 1
            $ Church += 1
            if Sys_SkipAll > 0:
                call Ch1P1_C2
        "Đi vòng quanh nơi khác":
            $ Sys_GameProgress = "Ch1P1_C3_played"
            $ Ch1P1_C3_played = 1
            if Sys_SkipAll > 0:
                call Ch1P1_C3
            menu:
                "Nói thật cho cậu ta":
                    $ Sys_GameProgress = "Ch1P1_C3C1"
                    $ Ch1P1_C3C1 = 1
                    if Sys_SkipAll > 0:
                        call Ch1P1_C3C1
                "Tiếp tục gạt cho đến cùng":
                    $ Sys_GameProgress = "Ch1P1_C3C2"
                    $ Ch1P1_C3C2 = 1
                    if Sys_SkipAll > 0:
                        call Ch1P1_C3C2
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Ch1P2"
    $ Sys_MapPoints += 1 # = 7
    $ Azzurra_Point += 1
    if Sys_SkipAll > 0:
        call Ch1P2
#------------------------------------------------------

################################################################################
#Choice 2
    menu:
        "Thọt lét":
            $ Sys_GameProgress = "Ch1P2B1_C1"
            $ Ch1P2B1_C1_played = 1
            if Sys_SkipAll > 0:
                call Ch1P2B1_C1
        "Nhéo má":
            $ Sys_GameProgress = "Ch1P2B1_C2"
            $ Ch1P2B1_C2_played = 1
            if Sys_SkipAll > 0:
                call Ch1P2B1_C2
        "Cụng đầu":
            $ Sys_GameProgress = "Ch1P2B1_C3"
            $ Ch1P2B1_C3_played = 1
            if Sys_SkipAll > 0:
                call Ch1P2B1_C3
        "Tôi không biết":
            $ Sys_GameProgress = "Ch1P2B1_C4"
            $ Ch1P2B1_C4_played = 1
            if Sys_SkipAll > 0:
                call Ch1P2B1_C4
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Ch1P3"
    $ Sys_MapPoints += 1 # = 8
    if Sys_SkipAll > 0:
        call Ch1P3
#------------------------------------------------------

################################################################################
#Choice 4
    menu:
        "Đi theo Elena đến nhà sách":
            $ Sys_GameProgress = "Ch1P3B2_C1"
            $ Ch1P3B2_C1_played = 1
            $ Elena_Point += 1
            if Sys_SkipAll > 0:
                call Ch1P3B2_C1
        "Đi hỏi trực tiếp Azzurra":
            $ Sys_GameProgress = "Ch1P3B2_C2"
            $ Ch1P3B2_C2_played = 1
            $ Azzurra_Point += 1
            if Sys_SkipAll > 0:
                call Ch1P3B2_C2
        "Tạm tin Elena":
            $ Sys_GameProgress = "Ch1P3B2_C3"
            $ Ch1P3B2_C3_played = 1
            if Sys_SkipAll > 0:
                call Ch1P3B2_C3
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Ch1P4"
    $ Sys_MapPoints += 1 # = 9
    if Sys_SkipAll > 0:
        call Ch1P4
#------------------------------------------------------

    if Ch1P3B2_C2_played == 1:
        $ Sys_GameProgress = "Ch1P4_B1"
        if Sys_SkipAll > 0:
            call Ch1P4_B1
    elif (Ch1P1_C3_played == 1):
        $ Sys_GameProgress = "Ch1P4_B2"
        if Sys_SkipAll > 0:
            call Ch1P4_B2
    elif (Ch1P1_C3_played == 0):
        $ Sys_GameProgress = "Ch1P4_B3"
        if Sys_SkipAll > 0:
            call Ch1P4_B3

#------------------------------------------------------
    $ Sys_GameProgress = "Ch1P5"
    $ Sys_MapPoints += 1 # = 10
    if Sys_SkipAll > 0:
        call Ch1P5
#------------------------------------------------------

################################################################################
#Choice 6
    menu:
        "Cho Hanes vào nhóm":
            $ Sys_GameProgress = "Ch1P5_C1"
            $ Azzurra_Point += 1
            if Sys_SkipAll > 0:
                call Ch1P5_C1
        "Không cho Hanes vào nhóm":
            $ Sys_GameProgress = "Ch1P5_C2"
            if Sys_SkipAll > 0:
                call Ch1P5_C2
            menu:
                "Cho Hanes vào nhóm":
                    $ Sys_GameProgress = "Ch1P5_C2C1"
                    $ Azzurra_Point += 1
                    if Sys_SkipAll > 0:
                        call Ch1P5_C2C1
                "Không cho Hanes vào nhóm":
                    $ Sys_GameProgress = "Ch1P5_C2C3"
                    if Sys_SkipAll > 0:
                        call Ch1P5_C2C3
                    menu:
                        "Cho Hanes vào nhóm":
                            $ Sys_GameProgress = "Ch1P5_C2C3"
                            $ Azzurra_Point += 1
                            if Sys_SkipAll > 0:
                                call Ch1P5_C2C1
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Ch1P6"
    $ Sys_MapPoints += 1 # = 11
    if Sys_SkipAll > 0:
        call Ch1P6
#------------------------------------------------------
    $ Sys_GameProgress = "Ch2P1"
    $ Sys_MapPoints += 1 # = 12
    if Sys_SkipAll > 0:
        call Ch2P1
#------------------------------------------------------

################################################################################
#Choice 6.3
    menu:
        "Chơi cậu ta một vố":
            $ Sys_GameProgress = "Ch2P1_C1_played"
            $ Ch2P1_C1_played = 1
            if Sys_SkipAll > 0:
                call Ch2P1_C1
        "Khuyên cậu ta":
            $ Ch2P1_C2_played = 1
            $ Sys_GameProgress = "Ch2P1_C2_played"
            if Sys_SkipAll > 0:
                call Ch2P1_C2
                call Ch2P1_C1
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Ch2P2"
    $ Sys_MapPoints += 1 # = 13
    if Sys_SkipAll > 0:
        call Ch2P2
#------------------------------------------------------

################################################################################
#Choice 6.3.1
    menu:
        "Moment xoắn":
            $ Sys_GameProgress = "Ch2P2_C1"
            if Sys_SkipAll > 0:
                call Ch2P2_C1
        "Lực ly tâm":
            $ Sys_GameProgress = "Ch2P2_C2"
            if Sys_SkipAll > 0:
                call Ch2P2_C2
        "Phép thuật":
            $ Sys_GameProgress = "Ch2P2_C3"
            if Sys_SkipAll > 0:
                call Ch2P2_C3
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Ch2P3"
    $ Sys_MapPoints += 1 # = 14
    if Sys_SkipAll > 0:
        call Ch2P3
#------------------------------------------------------
    $ Sys_GameProgress = "gc2"
    $ Sys_MapPoints += 1 # = 15
    if Sys_SkipAll > 0:
        call gc2
#------------------------------------------------------
    $ Sys_GameProgress = "Ch3P1"
    $ Sys_MapPoints += 1 # = 16
    if Sys_SkipAll > 0:
        call Ch3P1
#------------------------------------------------------

################################################################################
#Choice 6.5
    menu:
        "Bắt chuyện với Azzurra":
            $ Sys_GameProgress = "Ch3P1_C1"
            $ Azzurra_Point += 1
            if Sys_SkipAll > 0:
                call Ch3P1_C1
        "Nhờ cha khuấy động không khí":
            $ Sys_GameProgress = "Ch3P1_C2"
            $ Global_ParentPoint += 1
            if Sys_SkipAll > 0:
                call Ch3P1_C2
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Ch3P2"
    $ Sys_MapPoints += 1 # = 17
    if Sys_SkipAll > 0:
        call Ch3P2
#------------------------------------------------------
    $ Sys_GameProgress = "Ch4P1"
    $ Sys_MapPoints += 1 # = 18
    if Sys_SkipAll > 0:
        call Ch4P1
#------------------------------------------------------

################################################################################
#Choice 6.6
    menu:
        "Tìm Hanes":
            $ Sys_GameProgress = "Ch4P1_C1"
            if Sys_SkipAll > 0:
                call Ch4P1_C1
        "Tìm đại một người để hỏi":
            $ Sys_GameProgress = "Ch4P1_C2"
            if Sys_SkipAll > 0:
                call Ch4P1_C2
        "Hỏi cha mẹ":
            $ Sys_GameProgress = "Ch4P1_C3"
            $ Ch4P1_C3_played = 1
            $ Global_ParentPoint += 1
            if Sys_SkipAll > 0:
                call Ch4P1_C3
################################################################################

    if Ch4P1_C3_played == 1:
        if Sys_SkipAll > 0:
            "Sáng hôm sau, chúng tôi đã chủ động đi tìm Hanes."
            "Tưởng chừng trốn biệt trong Nhà thờ, không biết vô tình hay hữu ý, lù lù xuất hiện trước cửa quán trà của chúa Ascenderos."
    if Ch4P1_C3_played == 0:
        if Sys_SkipAll > 0:
            " Hanes – sau khi dọa tôi thất kinh vì sự xuất hiện như ma của mình – tỉnh bơ đi vào quán trà của chú Ascenderos."

#------------------------------------------------------
    $ Sys_GameProgress = "Ch4P2"
    $ Sys_MapPoints += 1 # = 19
    if Sys_SkipAll > 0:
        call Ch4P2
#------------------------------------------------------
    $ Sys_GameProgress = "Ch4P3"
    $ Sys_MapPoints += 1 # = 20
    if Sys_SkipAll > 0:
        call Ch4P3
#------------------------------------------------------

################################################################################
#Choice 6.7
    menu:
        "Đi về trung tâm":
            $ Sys_GameProgress = "Ch4P3B1_C1"
            if Sys_SkipAll > 0:
                call Ch4P3B1_C1
        "Đi ra ngoại ô":
            $ Sys_GameProgress = "Ch4P3B1_C2"
            if Sys_SkipAll > 0:
                call Ch4P3B1_C2
        "Lựa chọn tự động":
            $ Sys_GameProgress = "Ch4P3B1_C3"
            $ Ch4P3B1_C3 = 1
            if Sys_SkipAll > 0:
                call Ch4P3B1_C3

    if Ch4P3B1_C3 == 1:
        menu:
            "Đi về trung tâm":
                $ Sys_GameProgress = "Ch4P3B1_C1"
                if Sys_SkipAll > 0:
                    call Ch4P3B1_C1
            "Đi ra ngoại ô":
                $ Sys_GameProgress = "Ch4P3B1_C2"
                if Sys_SkipAll > 0:
                    call Ch4P3B1_C2

################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Ch4P4"
    $ Sys_MapPoints += 1 # = 21
    if Sys_SkipAll > 0:
        call Ch4P4
#------------------------------------------------------
    $ Sys_GameProgress = "gc3"
    $ Sys_MapPoints += 1 # = 22
    if Sys_SkipAll > 0:
        call gc3
#------------------------------------------------------
    $ Sys_GameProgress = "Ch5"
    $ Sys_MapPoints += 1 # = 23
    if Sys_SkipAll > 0:
        call Ch5
#------------------------------------------------------

################################################################################
#Choice 7
    menu:
        "Làm theo những gì lá thư bảo.":
            $ Sys_GameProgress = "Ch5_C1"
            if Sys_SkipAll > 0:
                call Ch5_C1
        "Đưa lá thư cho Hanes.":
            $ Sys_GameProgress = "Ch5_C2"
            $ Ch5_C2 = 1
            if Sys_SkipAll > 0:
                call Ch5_C2
                call Ch5_C1
        "Đưa lá thư cho Cha Fredo.":
            $ Sys_GameProgress = "Ch5_C3"
            $ Ch5_C3 = 1
            if Sys_SkipAll > 0:
                call Ch5_C3
                call Ch5_C1

    menu:
        "“Đó là việc Azzurra...”":
            $ Sys_GameProgress = "Ch5_C1C1"
            $ RescueTime = 3
            if Sys_SkipAll > 0:
                call Ch5_C1C1
        "“Mình muốn ra ngoại ô...”":
            $ Sys_GameProgress = "Ch5_C1C2"
            $ RescueTime = 2
            if Sys_SkipAll > 0:
                call Ch5_C1C2
        "“Lễ hội Mặt trời...”":
            $ Sys_GameProgress = "Ch5_C1C3"
            $ RescueTime = 1
            if Sys_SkipAll > 0:
                call Ch5_C1C3
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "SchallendorfHouse"
    $ Sys_MapPoints += 1 # = 24
    if Sys_SkipAll > 0:
        call SchallendorfHouse
#------------------------------------------------------

################################################################################
#Choice 7
    if SchallendorfHouse_choice_played == 0:
        menu:
#------------------------------------------------------
            "Tìm Azzurra.":
                $ Sys_GameProgress = "SchallendorfHouse"
                $ Azzurra_Point += 1
                if Sys_SkipAll > 0:
                    call SchallendorfHouse_choice_001
#------------------------------------------------------
            "Tìm chiếc két sắt.":
                $ SchallendorfHouse_choice_played += 1
                $ Sys_GameProgress = "SchallendorfHouse_choice_002"
                if SchallendorfHouse_choice_played ==2:
                    menu:
                        "Tìm Azzurra.":
                            $ Sys_GameProgress = "SchallendorfHouse_choice_001"
                            if Sys_SkipAll > 0:
                                call SchallendorfHouse_choice_001
                else:
                    if (RescueTime <= 2) :
                        " Không, không được! Tôi không có đủ thời gian – họ có thể về ngay bây giờ, và như thế thì hỏng bét!"
                        " Phải tính cách khác thôi!"
                        menu:
                            "Tìm Azzurra.":
                                $ Sys_GameProgress = "SchallendorfHouse_choice_001"
                                if Sys_SkipAll > 0:
                                    call SchallendorfHouse_choice_001
                            "Lục soát toàn bộ ngôi nhà.":
                                $ Sys_GameProgress = "SchallendorfHouse_choice_003"
                                if Sys_SkipAll > 0:
                                    call SchallendorfHouse_choice_003
                    else:
                        if Sys_SkipAll > 0:
                            call SchallendorfHouse_choice_002
#------------------------------------------------------
            "Lục soát toàn bộ ngôi nhà.":
                $ SchallendorfHouse_choice_played += 1   
                $ Sys_GameProgress = "SchallendorfHouse_choice_003"
                if SchallendorfHouse_choice_played ==2:
                    menu:
                        "Tìm Azzurra.":
                            $ Sys_GameProgress = "SchallendorfHouse_choice_001"
                            if Sys_SkipAll > 0:
                                call SchallendorfHouse_choice_001
                else:    
                    if (RescueTime <= 2) :
                        " Không, không được! Tôi không có đủ thời gian – họ có thể về ngay bây giờ, và như thế thì hỏng bét!"
                        " Phải tính cách khác thôi!"
                        menu:
                            "Tìm Azzurra.":
                                $ Sys_GameProgress = "SchallendorfHouse_choice_001"
                                if Sys_SkipAll > 0:
                                    call SchallendorfHouse_choice_001
                            "Tìm chiếc két sắt.":
                                $ Sys_GameProgress = "SchallendorfHouse_choice_002"
                                if Sys_SkipAll > 0:
                                    call SchallendorfHouse_choice_002
                    else:
                        $Lohengramm = 1
                        if Sys_SkipAll > 0:
                            call SchallendorfHouse_choice_003
#------------------------------------------------------
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Azzurra_Corridor"
    $ Sys_MapPoints += 1 # = 25
    if Sys_SkipAll > 0:
        call Azzurra_Corridor
#------------------------------------------------------

################################################################################
#Choice 7.1
    if Lohengramm == 1:
        menu:
            "Tóm lấy Azzurra":
                $ Sys_GameProgress = "Azzurra_Corridor_choice_001"
                $ Force_end_7c = 1
                if Sys_SkipAll > 0:
                    call Azzurra_Corridor_choice_001
            "Thuyết phục Azzurra":
                $ Sys_GameProgress = "Azzurra_Corridor_choice_002"
                if Azzurra_Point <= 2:
                    $ Hopeless_Dream_End = 1
                    if Sys_SkipAll > 0:
                        call Azzurra_Corridor_choice_002a
                elif Azzurra_Point >= 3:
                    $ Azzurra_Persuasion = 1
                    if Sys_SkipAll > 0:
                        call Azzurra_Corridor_choice_002b
            "Chứng minh cho Azzurra thấy ý định thật của nhóm Schallendorf":
                $ Sys_GameProgress = "Azzurra_Corridor_choice_003"
                if Sys_SkipAll > 0:
                    call Azzurra_Corridor_choice_003
            "Bỏ về":
                $ Hopeless_Dream_End = 1
                pass
    else:
        menu:
            "Tóm lấy Azzurra":
                $ Sys_GameProgress = "Azzurra_Corridor_choice_001"
                $ Force_end_7c = 1
                if Sys_SkipAll > 0:
                    call Azzurra_Corridor_choice_001
            "Thuyết phục Azzurra":
                $ Sys_GameProgress = "Azzurra_Corridor_choice_002"
                if Azzurra_Point <= 2:
                    $ Hopeless_Dream_End = 1
                    if Sys_SkipAll > 0:
                        call Azzurra_Corridor_choice_002a
                elif Azzurra_Point >= 3:
                    $ Azzurra_Persuasion = 1
                    if Sys_SkipAll > 0:
                        call Azzurra_Corridor_choice_002b
            "Bỏ về":
                $ Hopeless_Dream_End = 1
                pass
################################################################################

################################################################################
    if (Force_end_7c == 1) or (
    Hopeless_Dream_End == 1):
        jump Check_Ending

    if ElenaRescue == 1:
        $ Sys_GameProgress = "Escape_Choice_001"
        if Sys_SkipAll > 0:
            call Escape_Choice_001
            call OutIf_ElenaRescue_1
    if ElenaRescue == 0:
        $ Sys_GameProgress = "Escape_Choice_002"
        if Sys_SkipAll > 0:
            call Escape_Choice_002
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Escape_p1"
    $ Sys_MapPoints += 1 # = 26
    if Sys_SkipAll > 0:
        call Escape_p1
#------------------------------------------------------

################################################################################
    if Lohengramm == 0:
        $ Sys_GameProgress = "Escape_Choice_001_E001"
        if Sys_SkipAll > 0:
            call Escape_Choice_001_E001
    if Lohengramm == 1:
        $ Sys_GameProgress = "Escape_Choice_001_E002"
        if Sys_SkipAll > 0:
            call Escape_Choice_001_E002

    if ElenaRescue == 0:
        $ Sys_GameProgress = "Escape_E001"
        if Sys_SkipAll > 0:
            call Escape_E001
    if ElenaRescue == 1:
        $ Sys_GameProgress = "Escape_E002"
        if Sys_SkipAll > 0:
            call Escape_E002
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Escape_p2"
    $ Sys_MapPoints += 1 # = 27
    if Sys_SkipAll > 0:
        call Escape_p2
#------------------------------------------------------
    $ Sys_GameProgress = "Escape_E002_E001"
    $ Sys_MapPoints += 1 # = 28
    if Sys_SkipAll > 0:
        call Escape_E002_E001
#------------------------------------------------------

################################################################################

    menu:
        "Đồng ý giữ bí mật":
            $ Sys_GameProgress = "Escape_E002_E001_Choice_001"
            $ Hanes_Truth = 0
            $ Azzurra_Stays_With_Fredo = 1
            if Sys_SkipAll > 0:
                call Escape_E002_E001_Choice_001
        "Phải biết sự thật bằng mọi giá!":
            $ Sys_GameProgress = "Escape_E002_E001_Choice_002"
            $ Hanes_Truth = 1
            if Sys_SkipAll > 0:
                call Escape_E002_E001_Choice_002
            if Lohengramm == 1:
                $ Sys_GameProgress = "Escape_E002_E001_Choice_002_E001"
                if Sys_SkipAll > 0:
                    call Escape_E002_E001_Choice_002_E001
            if RescueTime == 3:
                $ Sys_GameProgress = "Escape_E002_E001_C002_E001_E001"
                if Sys_SkipAll > 0:
                    call Escape_E002_E001_C002_E001_E001
            elif Lohengramm == 0:
                $ Sys_GameProgress = "Escape_E002_E001_Choice_002_E002"
                if Sys_SkipAll > 0:
                    call Escape_E002_E001_Choice_002_E002

################################################################################
    if (Lohengramm == 1) and (Azzurra_Persuasion == 0): 
        $ Hanes_Truth = 1
    elif (Lohengramm == 1) and (Azzurra_Persuasion == 1):
        $ Hanes_Truth = 2
#------------------------------------------------------
    $ Sys_GameProgress = "Ch6P1"
    $ Sys_MapPoints += 1 # = 29
    if Sys_SkipAll > 0:
        call Ch6P1
#------------------------------------------------------

################################################################################
    if Azzurra_Stays_With_Fredo == 1:
        $ Sys_GameProgress = "Ch6P1B1"
        if Sys_SkipAll > 0:
            call Ch6P1B1
    else:
        $ Sys_GameProgress = "Ch6P1B2"
        if Sys_SkipAll > 0:
            call Ch6P1B2
        if Lohengramm == 1:
            $ Sys_GameProgress = "Ch6P1B2_C1"
            if Sys_SkipAll > 0:
                call Ch6P1B2_C1
            if Quantum.Physics == 1:
                $ Sys_GameProgress = "Ch6P1B2_C1C1"
                if Sys_SkipAll > 0:
                    call Ch6P1B2_C1C1
            else:
                $ Sys_GameProgress = "Ch6P1B2_C1C1_B1"
                if Sys_SkipAll > 0:
                    call Ch6P1B2_C1C1_B1
        else:
            $ Sys_GameProgress = "Ch6P1B2_C2"
            if Sys_SkipAll > 0:
                call Ch6P1B2_C2
#------------------------------------------------------
    if ((Azzurra_Stays_With_Fredo == 1) and (Hanes_Truth == 0)):
        $ Sys_GameProgress = "Ch6P2_C1"
        if Sys_SkipAll > 0:
            call Ch6P2_C1
    if ((Azzurra_Stays_With_Fredo == 0) and (Hanes_Truth == 1)):
        $ Sys_GameProgress = "Ch6P2_C2"
        if Sys_SkipAll > 0:
            call Ch6P2_C2
        if Azzurra_Point <= 4:
            $ Sys_GameProgress = "Ch6P2_C2C1"
            $ True_end = 1
            if Sys_SkipAll > 0:
                call Ch6P2_C2C1
        else: 
            $ Sys_GameProgress = "Ch6P2_C2C2"
            if Sys_SkipAll > 0:
                call Ch6P2_C2C2
#------------------------------------------------------
    if ((Azzurra_Stays_With_Fredo == 1) and (Hanes_Truth == 1)):
        $ Sys_GameProgress = "Ch6P2_C3"
        if Sys_SkipAll > 0:
            call Ch6P2_C3
#------------------------------------------------------
    if ((Azzurra_Stays_With_Fredo == 1) and (Hanes_Truth == 2)):
        $ Sys_GameProgress = "Ch6P2_C4"
        if Sys_SkipAll > 0:
            call Ch6P2_C4
        menu:
            "Đồng ý làm theo lời Hanes":
                $ Sys_GameProgress = "Ch6P2_C4C1"
                $ WAR_END_DEATH_OF_A_SPY = 1
                if Sys_SkipAll > 0:
                    call Ch6P2_C4C1
            "Cho Hanes biết thế nào là lễ độ!":
                $ Sys_GameProgress = "Ch6P2_C4C2"
                $ WAR_END_REVOLUTION = 1
                if Sys_SkipAll > 0:
                    call Ch6P2_C4C2
            "Từ chối làm theo lời Hanes.":
                $ Sys_GameProgress = "Ch6P2_C4C3"
                $ Anatolio_Defies_Hanes = 1
                if Sys_SkipAll > 0:
                    call Ch6P2_C4C3
#------------------------------------------------------
    if Anatolio_Defies_Hanes == 1:
        $ Sys_GameProgress = "Ch6P1B3"
        if Sys_SkipAll > 0:
            call Ch6P1B3
        if Azzurra_Point <= 4:
            $ Sys_GameProgress = "Ch6P1B3a"
            $ True_end = 1
            if Sys_SkipAll > 0:
                call Ch6P1B3a
    else:
        $ Sys_GameProgress = "Ch6P1B4"
        if Sys_SkipAll > 0:
            call Ch6P1B4
#------------------------------------------------------
    if (True_end == 1) or (
    WAR_END_DEATH_OF_A_SPY == 1) or (
    WAR_END_REVOLUTION == 1):
        jump Check_Ending
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Ch6P2"
    $ Sys_MapPoints += 1 # = 30
    if Sys_SkipAll > 0:
        call Ch6P2
#------------------------------------------------------

################################################################################
    if Hanes_Truth > 0:
        $ Sys_GameProgress = "Ch6P2_Fes_Hanes_B"
        if Sys_SkipAll > 0:
            call Ch6P2_Fes_Hanes_B
    else:
        $ Sys_GameProgress = "Ch6P2_Fes_Hanes_G"
        if Sys_SkipAll > 0:
            call Ch6P2_Fes_Hanes_G
################################################################################

#------------------------------------------------------
    $ Sys_GameProgress = "Ch6P3"
    $ Sys_MapPoints += 1 # = 31
    if Sys_SkipAll > 0:
        call Ch6P3
#------------------------------------------------------

################################################################################
    if Lohengramm == 1:
        $ Sys_GameProgress = "Ch6P3B5"
        if Sys_SkipAll > 0:
            call Ch6P3B5
        menu:
            "Đi gặp ông Attenborough":
                $ Sys_GameProgress = "Ch6P3B5_C1"
                if Sys_SkipAll > 0:
                    call Ch6P3B5_C1
            "Không đi":
                $ Sys_GameProgress = "Ch6P3B5_C2"
                $ A_Rich_Happy_Family = 1
                if Sys_SkipAll > 0:
                    call Ch6P3B5_C2
            "Tung đồng xu":
                $ Sys_GameProgress = "Ch6P3B5_C3"
                if Sys_SkipAll > 0:
                    call Ch6P3B5_C3
                $ Coin_Toss = renpy.random.randint(1, 3)
                if Coin_Toss == 1:
                    $ Sys_GameProgress = "Ch6P3B5_C3a"
                    if Sys_SkipAll > 0:
                        call Ch6P3B5_C3a
                elif Coin_Toss == 0:
                    $ Sys_GameProgress = "Ch6P3B5_C3b"
                    $ A_Rich_Happy_Family = 1
                    if Sys_SkipAll > 0:
                        call Ch6P3B5_C3b

################################################################################

################################################################################
    if (A_Rich_Happy_Family == 1):
        jump Check_Ending
################################################################################
#------------------------------------------------------
    $ Sys_GameProgress = "Ch6P4"
    $ Sys_MapPoints += 1 # = 32
    if Sys_SkipAll > 0:
        call Ch6P4
#------------------------------------------------------

################################################################################
    menu:
        "Cháu sẽ theo Aurora đến cùng!":
            $ Sys_GameProgress = "Ch6P1B1_C1"
            if Sys_SkipAll > 0:
                call Ch6P1B1_C1
            if Hanes_Truth == 1:
                $ Sys_GameProgress = "Ch6P1B1_C1_E1"
                if Sys_SkipAll > 0:
                    call Ch6P1B1_C1_E1
            elif Hanes_Truth == 0:
                $ Sys_GameProgress = "Ch6P1B1_C1_E2"
                if Sys_SkipAll > 0:
                    call Ch6P1B1_C1_E2
        "Đây không phải con đường cháu muốn đi.":
            $ Sys_GameProgress = "Ch6P1B1_C2"
            $ A_Rich_Happy_Family = 1
            if Sys_SkipAll > 0:
                call Ch6P1B1_C2
################################################################################

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    $ persistent.Demo_finish = True
    if (A_Rich_Happy_Family == 1):
        jump Check_Ending
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    return