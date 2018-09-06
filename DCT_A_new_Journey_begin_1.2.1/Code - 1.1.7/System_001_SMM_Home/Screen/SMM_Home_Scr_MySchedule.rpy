
screen SMM_Home_Scr_MySchedule:
    
    tag menu
    modal True
    add "SMM_Home_BG_000"

    frame:
        align (0.5,0.1)
        text "{size=24} Hôm nay mình sẽ: [HS_MySchedule] {/size}" 
    
    frame:
        align (0.1, 0.5)
        vbox:
            text "{size=24} Sức khỏe : [HS_MyStrength]  +([HS_Growth_Strength]) {/size}" 
            text "{size=24} Thể lực    : [HS_MyStamina]  +([HS_Growth_Stamina]) {/size}" 
            text "{size=24} Trí tuệ      : [HS_MyIntelligence]  +([HS_Growth_Intelligence]) {/size}" 
            text "{size=24} Đẹp trai    : [HS_MyCharm]  +([HS_Growth_Charm]) {/size}" 
            text "{size=24} Hiểu biết  : [HS_MyWisdom]  +([HS_Growth_Wisdom]) {/size}" 
    
    frame:
        align (0.5, 0.8)
        hbox:
            textbutton "{size=24} Ngủ {/size}" action SetVariable ("HS_MySchedule", "Ngủ"), SetVariable (
            "HS_Growth_Strength", 1), SetVariable (
            "HS_Growth_Stamina",1), SetVariable (
            "HS_Growth_Intelligence", 1), SetVariable (
            "HS_Growth_Charm", 1), SetVariable (
            "HS_Growth_Wisdom", 1)
            
            textbutton "{size=24} Học bài {/size}" action SetVariable ("HS_MySchedule", "Học bài"), SetVariable (
            "HS_Growth_Strength", 0), SetVariable (
            "HS_Growth_Stamina", 1), SetVariable (
            "HS_Growth_Intelligence", 5), SetVariable (
            "HS_Growth_Charm", 0), SetVariable (
            "HS_Growth_Wisdom", 2)

            textbutton "{size=24} Tập Gym {/size}" action SetVariable ("HS_MySchedule", "Tập Gym"), SetVariable (
            "HS_Growth_Strength", 4), SetVariable (
            "HS_Growth_Stamina", 3), SetVariable (
            "HS_Growth_Intelligence", 0), SetVariable (
            "HS_Growth_Charm", 1), SetVariable (
            "HS_Growth_Wisdom", 0)

            textbutton "{size=24} Chải chuốt {/size}" action SetVariable ("HS_MySchedule", "Chải chuốt"), SetVariable (
            "HS_Growth_Strength", 0), SetVariable (
            "HS_Growth_Stamina", 2), SetVariable (
            "HS_Growth_Intelligence", 0), SetVariable (
            "HS_Growth_Charm", 5), SetVariable (
            "HS_Growth_Wisdom", 1)

            textbutton "{size=24} Đọc sách {/size}" action SetVariable ("HS_MySchedule", "Đọc sách"), SetVariable (
            "HS_Growth_Strength", 0), SetVariable (
            "HS_Growth_Stamina", 1), SetVariable (
            "HS_Growth_Intelligence", 2), SetVariable (
            "HS_Growth_Charm", 0), SetVariable (
            "HS_Growth_Wisdom", 5)

            textbutton "{size=24} Không làm gì cả {/size}" action SetVariable ("HS_MySchedule", "Không làm gì cả"), SetVariable (
            "HS_Growth_Strength", 0), SetVariable (
            "HS_Growth_Stamina", 0), SetVariable (
            "HS_Growth_Intelligence", 0), SetVariable (
            "HS_Growth_Charm", 0), SetVariable (
            "HS_Growth_Wisdom", 0)


    frame:
        align (0.9, 0.9)
        textbutton "{size=24} Trở lại {/size}" action Hide ("SMM_Home_Scr_MySchedule"), Jump("Sys_SMM_Home_Start")
