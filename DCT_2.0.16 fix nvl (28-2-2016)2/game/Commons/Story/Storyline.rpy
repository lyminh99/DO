label Storyline:
    stop music fadeout 1.0
    if persistent.Demo_finish == True:
        call Secret_garden from _call_Secret_garden 
    call prologue2 from _call_prologue2 
    call gc_chuong1 from _call_gc_chuong1 
    call gc_chuong2 from _call_gc_chuong2 
    call gc_chuong3 from _call_gc_chuong3 
    call gc_chuong4 from _call_gc_chuong4

#------------------------------------------------------
    call Chapter_001_p1 from _call_Chapter_001_p1 
#------------------------------------------------------

##########
#Choice 1
    scene BG_6 with dissolve
    menu:
        "Tiếp tục dạo phố":
            pass
        "Đến Nhà thờ.":
            call Chapter_001_choice_002 from _call_Chapter_001_choice_002
        "Đi vòng quanh nơi khác":
            call Chapter_001_choice_003 from _call_Chapter_001_choice_003
##########

#------------------------------------------------------
    call Chapter_001_p2 from _call_Chapter_001_p2 
#------------------------------------------------------

##########
#Choice 2
    menu:
        "Thọt lét":
            call Chapter_001_E001_C001 from _call_Chapter_001_E001_C001 
        "Nhéo má":
            call Chapter_001_E001_C002 from _call_Chapter_001_E001_C002 
        "Cụng đầu":
            call Chapter_001_E001_C003 from _call_Chapter_001_E001_C003 
        "Tôi không biết":
            call Chapter_001_E001_C004 from _call_Chapter_001_E001_C004 
##########

#------------------------------------------------------
    call Chapter_001_p3 from _call_Chapter_001_p3 
#------------------------------------------------------

##########
#Choice 4
    menu:
        "Đi theo Elena đến nhà sách":
            call Chapter_001_E002_C001 from _call_Chapter_001_E002_C001
        "Đi hỏi trực tiếp Azzurra":
            call Chapter_001_E002_C002 from _call_Chapter_001_E002_C002
        "Tạm tin Elena":
            call Chapter_001_E002_C003 from _call_Chapter_001_E002_C003 
##########

#------------------------------------------------------
    call Chapter_001_p4 from _call_Chapter_001_p4 
#------------------------------------------------------

    if Chapter_001_E002_C002_played == 1:
        call Chapter_001_p4_Branch001 from _call_Chapter_001_p4_Branch001 
    if (Chapter_001_choice_003_played == 1):
        call Chapter_001_p4_Branch002 from _call_Chapter_001_p4_Branch002 
    if (Chapter_001_choice_003_played == 0):
        call Chapter_001_p4_Branch003 from _call_Chapter_001_p4_Branch003 

#------------------------------------------------------
    call Chapter_001_p5 from _call_Chapter_001_p5 
#------------------------------------------------------

##########
#Choice 6
    menu:
        "Cho Hanes vào nhóm":
            call Chapter_001_p5_C001 from _call_Chapter_001_p5_C001
        "Không cho Hanes vào nhóm":
            call Chapter_001_p5_C002 from _call_Chapter_001_p5_C002
        "Không cho Hanes vào nhóm":
            call Chapter_001_p5_C002 from _call_Chapter_001_p5_C002_1 
##########

#------------------------------------------------------
    call Chapter_001_p6 from _call_Chapter_001_p6 
    call Chapter_002_p1 from _call_Chapter_002_p1 
#------------------------------------------------------

##########
#Choice 6.3
    menu:
        "Chơi cậu ta một vố":
            call Chapter_002_choice_001 from _call_Chapter_002_choice_001
        "Khuyên cậu ta":
            call Chapter_002_choice_002 from _call_Chapter_002_choice_002
##########

#------------------------------------------------------
    call Chapter_002_p2 from _call_Chapter_002_p2 
#------------------------------------------------------

##########
#Choice 6.3.1
    menu:
        "Moment xoắn":
            call Chapter_002_p1_choice_001 from _call_Chapter_002_p1_choice_001 
        "Lực ly tâm":
            call Chapter_002_p1_choice_002 from _call_Chapter_002_p1_choice_002 
        "Phép thuật":
            call Chapter_002_p1_choice_003 from _call_Chapter_002_p1_choice_003 
##########

#------------------------------------------------------
    call Chapter_002_p3 from _call_Chapter_002_p3 
    call gc2 from _call_gc2 
    call Chapter_003_p1 from _call_Chapter_003_p1 
#------------------------------------------------------

##########
#Choice 6.5
    menu:
        "Bắt chuyện với Azzurra":
            call Chapter_003_choice_001 from _call_Chapter_003_choice_001 
        "Nhờ cha khuấy động không khí":
            call Chapter_003_choice_002 from _call_Chapter_003_choice_002 
##########

#------------------------------------------------------
    call Chapter_003_p2 from _call_Chapter_003_p2 
    call Chapter_004_p1 from _call_Chapter_004_p1 
#------------------------------------------------------

##########
#Choice 6.6
    menu:
        "Tìm Hanes":
            call Chapter_004_choice_001 from _call_Chapter_004_choice_001 
        "Tìm đại một người để hỏi":
            call Chapter_004_choice_002 from _call_Chapter_004_choice_002 
        "Hỏi cha mẹ":
            call Chapter_004_choice_003 from _call_Chapter_004_choice_003 
##########

    if Chapter_004_choice_003_played == 1:
        "Sáng hôm sau, chúng tôi đã chủ động đi tìm Hanes."
        "Tưởng chừng trốn biệt trong Nhà thờ, không biết vô tình hay hữu ý, lù lù xuất hiện trước cửa quán trà của chúa Ascenderos."
    if Chapter_004_choice_003_played == 0:
        " Hanes – sau khi dọa tôi thất kinh vì sự xuất hiện như ma của mình – tỉnh bơ đi vào quán trà của chú Ascenderos."

#------------------------------------------------------
    call Chapter_004_p2 from _call_Chapter_004_p2 
    call Chapter_004_p3 from _call_Chapter_004_p3 
#------------------------------------------------------

##########
#Choice 6.7
    menu:
        "Đi về trung tâm":
            call Chapter_004_E001_C001 from _call_Chapter_004_E001_C001 
        "Đi ra ngoại ô":
            call Chapter_004_E001_C002 from _call_Chapter_004_E001_C002 
        "Lựa chọn tự động":
            call Chapter_004_E001_C003 from _call_Chapter_004_E001_C003 

    if Chapter_004_E001_C003 == 1:
        menu:
            "Đi về trung tâm":
                call Chapter_004_E001_C001 from _call_Chapter_004_E001_C001_1 
            "Đi ra ngoại ô":
                call Chapter_004_E001_C002 from _call_Chapter_004_E001_C002_1 

##########

#------------------------------------------------------
    call Chapter_004_p4 from _call_Chapter_004_p4 
    call gc3 from _call_gc3 
    call Chapter_005 from _call_Chapter_005 
#------------------------------------------------------

##########
#Choice 7
    menu:
        "Làm theo những gì lá thư bảo.":
            call Chapter_005_choice_001 from _call_Chapter_005_choice_001 
        "Đưa lá thư cho Hanes.":
            call Chapter_005_choice_002 from _call_Chapter_005_choice_002 
        "Đưa lá thư cho Cha Fredo.":
            call Chapter_005_choice_003 from _call_Chapter_005_choice_003 

    menu:
        "“Đó là việc Azzurra...”":
            call Chapter_005_choice_001_C001 from _call_Chapter_005_choice_001_C001 
        "“Mình muốn ra ngoại ô...”":
            call Chapter_005_choice_001_C002 from _call_Chapter_005_choice_001_C002 
        "“Lễ hội Mặt trời...”":
            call Chapter_005_choice_001_C003 from _call_Chapter_005_choice_001_C003 
##########

#------------------------------------------------------
    call SchallendorfHouse from _call_SchallendorfHouse 
#------------------------------------------------------

##########
#Choice 7
    menu:
        "Tìm Azzurra.":
            call SchallendorfHouse_choice_001 from _call_SchallendorfHouse_choice_001 
        "Tìm chiếc két sắt.":
            call SchallendorfHouse_choice_002 from _call_SchallendorfHouse_choice_002 
        "Lục soát toàn bộ ngôi nhà.":
            call SchallendorfHouse_choice_003 from _call_SchallendorfHouse_choice_003 
##########

#------------------------------------------------------
    call Azzurra_Corridor from _call_Azzurra_Corridor 
#------------------------------------------------------

##########
#Choice 7.1
    if Lohengramm == 1:
        menu:
            "Tóm lấy Azzurra":
                call Azzurra_Corridor_choice_001 from _call_Azzurra_Corridor_choice_001 
            "Thuyết phục Azzurra":
                call Azzurra_Corridor_choice_002 from _call_Azzurra_Corridor_choice_002 
            "Chứng minh cho Azzurra thấy ý định thật của nhóm Schallendorf":
                call Azzurra_Corridor_choice_003 from _call_Azzurra_Corridor_choice_003 
            "Bỏ về":
                $ Hopeless_Dream_End = 1
                pass
    else:
        menu:
            "Tóm lấy Azzurra":
                call Azzurra_Corridor_choice_001 from _call_Azzurra_Corridor_choice_001_1 
            "Thuyết phục Azzurra":
                call Azzurra_Corridor_choice_002 from _call_Azzurra_Corridor_choice_002_1 
            "Bỏ về":
                $ Hopeless_Dream_End = 1
                pass
##########

##########
    if (Force_end_7c == 1) or (
    Hopeless_Dream_End == 1):
        jump Check_Ending

    if ElenaRescue == 1:
        call Escape_Choice_001 from _call_Escape_Choice_001 
    if ElenaRescue == 0:
        call Escape_Choice_002 from _call_Escape_Choice_002 
##########

#------------------------------------------------------
    call Escape_p1 from _call_Escape_p1 
#------------------------------------------------------

##########
    if Lohengramm == 0:
        call Escape_Choice_001_E001 from _call_Escape_Choice_001_E001 
    if Lohengramm == 1:
        call Escape_Choice_001_E002 from _call_Escape_Choice_001_E002 

    if ElenaRescue == 0:
        call Escape_E001 from _call_Escape_E001 
    if ElenaRescue == 1:
        call Escape_E002 from _call_Escape_E002 
##########

#------------------------------------------------------
    call Escape_p2 from _call_Escape_p2 
    call Escape_E002_E001 from _call_Escape_E002_E001
#------------------------------------------------------
##########
    menu:
        "Đồng ý giữ bí mật":
            call Escape_E002_E001_Choice_001 from _call_Escape_E002_E001_Choice_001
            $ Hanes_Truth = 0
        "Phải biết sự thật bằng mọi giá!":
            call Escape_E002_E001_Choice_002 from _call_Escape_E002_E001_Choice_002
            $ Hanes_Truth = 1

##########
    if (Lohengramm == 1) and (Azzurra_Persuasion == 0): 
        $ Hanes_Truth = 1
    if (Lohengramm == 1) and (Azzurra_Persuasion == 1):
        $ Hanes_Truth = 2
#------------------------------------------------------
    call Chapter_006_p1 from _call_Chapter_006_p1
#------------------------------------------------------

##########
    if Azzurra_Stays_With_Fredo == 1:
        call Chapter_006_branch001 from _call_Chapter_006_branch001 
    else:
        call Chapter_006_branch002 from _call_Chapter_006_branch002 

    if ((Azzurra_Stays_With_Fredo == 1) and (Hanes_Truth == 0)):
        call Chapter_006_P002_001 from _call_Chapter_006_P002_001 
    if ((Azzurra_Stays_With_Fredo == 0) and (Hanes_Truth == 1)):
        call Chapter_006_P002_002 from _call_Chapter_006_P002_002 
    if ((Azzurra_Stays_With_Fredo == 1) and (Hanes_Truth == 1)):
        call Chapter_006_P002_003 from _call_Chapter_006_P002_003 
    if ((Azzurra_Stays_With_Fredo == 1) and (Hanes_Truth == 2)):
        call Chapter_006_P002_004 from _call_Chapter_006_P002_004 

    if Anatolio_Defies_Hanes == 1:
        call Chapter_006_branch003 from _call_Chapter_006_branch003 
    else:
        call Chapter_006_branch004 from _call_Chapter_006_branch004 

    if (True_end == 1) or (
    WAR_END_DEATH_OF_A_SPY == 1) or (
    WAR_END_REVOLUTION == 1):
        jump Check_Ending
##########

#------------------------------------------------------
    call Chapter_006_p2 from _call_Chapter_006_p2 
#------------------------------------------------------

##########
    if Hanes_Truth > 0:
        call Festival_Bad_Hanes from _call_Festival_Bad_Hanes 
    else:
        call Festival_Good_Hanes from _call_Festival_Good_Hanes 
##########

#------------------------------------------------------
    call Chapter_006_p3 from _call_Chapter_006_p3 
#------------------------------------------------------

##########
    if Lohengramm == 1:
        call Chapter_006_branch005 from _call_Chapter_006_branch005 
##########

#------------------------------------------------------
    call Chapter_006_p4 from _call_Chapter_006_p4
#------------------------------------------------------

    $ persistent.Demo_finish = True

##########
    menu:
        "Cháu sẽ theo Aurora đến cùng!":
            call Chapter_006_E001_choice_001 from _call_Chapter_006_E001_choice_001 
        "Đây không phải con đường cháu muốn đi.":
            call Chapter_006_E001_choice_002 from _call_Chapter_006_E001_choice_002 
##########
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if (A_Rich_Happy_Family == 1):
        jump Check_Ending
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    return