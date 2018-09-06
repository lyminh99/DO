screen Scr_Sys_Controls:

    frame:
        xalign 0.5
        yalign 0.0
        hbox:
            vbox:
                textbutton "{size=24} Open Sys_status {/size}" action Show ("Scr_Sys_Status") at Sys_Eff_Appear
                textbutton "{size=24} Close           {/size}" action Hide ("Scr_Sys_Status") at Sys_Eff_Appear
            text "{size=24} - {/size}"         
            vbox:
                textbutton "{size=24} Open DCT_Status   {/size}" action Show ("Scr_Status") at Sys_Eff_Appear
                textbutton "{size=24} Close             {/size}" action Hide ("Scr_Status") at Sys_Eff_Appear
            text "{size=24} - {/size}"
            vbox:
                textbutton "{size=24} Sys_Skip_Read     {/size}" action SetVariable ("Sys_SkipAll", 1) at Sys_Eff_Appear
                textbutton "{size=24} Read              {/size}" action SetVariable ("Sys_SkipAll", 0) at Sys_Eff_Appear
            vbox:
                textbutton "{size=24} VN              {/size}" action SetField(persistent, "Sys_Langue", "VN") at Sys_Eff_Appear
                textbutton "{size=24} ENG              {/size}" action SetField(persistent, "Sys_Langue", "ENG") at Sys_Eff_Appear
            textbutton "{size=24} Exit {/size}" action MainMenu()

screen Scr_Sys_Status:

    frame:
        xalign 0.3
        yalign 0.1
        vbox:
            text "{size=18} Sys_Langue              {/size}"
            text "{size=18} Sys_SkipAll             {/size}"
            text "{size=18} Sys_DCT_Progress        {/size}"
            text "{size=18} Sys_DCT_Curent_Chapter  {/size}"
            text "{size=18} Sys_DCT_END             {/size}"
    frame:
        xalign 0.4
        yalign 0.1
        vbox:
            text "{size=18} [persistent.Sys_Langue]             {/size}"
            text "{size=18} [Sys_SkipAll]            {/size}"
            text "{size=18} [Sys_DCT_Progress]       {/size}"
            text "{size=18} [Sys_DCT_Curent_Chapter] {/size}"
            text "{size=18} [persistent.DCT_Finished]{/size}"
