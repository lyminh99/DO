
screen SMM_Home_Scr_HomeMenu:
    
    tag menu
    modal True
    add "SMM_Home_BG_000"

    frame:
        align (0.1, 0.1)
        vbox:
            if HS_Date == 1:
                text "{size=24} Thứ 2 {/size}"
            elif HS_Date == 2:
                text "{size=24} Thứ 3 {/size}"
            elif HS_Date == 3:
                text "{size=24} Thứ 4 {/size}"
            elif HS_Date == 4:
                text "{size=24} Thứ 5 {/size}"
            elif HS_Date == 5:
                text "{size=24} Thứ 6 {/size}"
            elif HS_Date == 6:
                text "{size=24} Thứ 7 {/size}"
            elif HS_Date == 7:
                text "{size=24} Chủ nhật {/size}"
            text "{size=24} Ngày: [HS_Day] {/size}"
            text "{size=24} Tháng: [HS_Month] {/size}"
            text "{size=24} Thời tiết: [HS_Weather] {/size}"

    frame:
        align (0.8, 0.1)
        vbox:
            textbutton "{size=24} Girls status {/size}" action Hide("SMM_Home_Scr_HomeMenu"), Show ("SMM_Home_Scr_GirlsStatus") 
            textbutton "{size=24} My Schedule {/size}" action Hide("SMM_Home_Scr_HomeMenu"), Show ("SMM_Home_Scr_MySchedule") 
            textbutton "{size=24} Go out {/size}" action Hide("SMM_Home_Scr_HomeMenu"), Show ("SMM_Home_Scr_GoOut_Map") 
            textbutton "{size=24} Rest {/size}" action Jump("SMM_Home_Pick_Rest")
            text "{size=24} --- --- {/size}"
            textbutton "{size=24} Save {/size}" action ShowMenu("save")
            textbutton "{size=24} Load {/size}" action ShowMenu("load")
            textbutton "{size=24} Quit {/size}" action MainMenu()
