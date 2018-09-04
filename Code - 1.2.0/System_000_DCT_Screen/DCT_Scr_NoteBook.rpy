init:
    $ DCT_NoteBook_But000 = Hide("DCT_NoteBook_001"), Hide("DCT_NoteBook_002"), Hide("DCT_NoteBook_003"), Hide("DCT_NoteBook_004"), Hide("DCT_NoteBook_005"), Hide("DCT_NoteBook_006"), Hide("DCT_NoteBook_007"), Hide("DCT_NoteBook_008"), Hide("DCT_NoteBook_009"), Hide("DCT_NoteBook_010"), Hide("DCT_NoteBook_011"), Hide("DCT_NoteBook_012"), Hide("DCT_NoteBook_013"), Hide("DCT_NoteBook_014"), Hide("DCT_NoteBook_015"),       Hide("DCT_NoteBook_016"), Hide("DCT_NoteBook_017"), Hide("DCT_NoteBook_018"), Hide("DCT_NoteBook_019"), Hide("DCT_NoteBook_020"), Hide("DCT_NoteBook_021"), Hide("DCT_NoteBook_022"), Hide("DCT_NoteBook_023"), Hide("DCT_NoteBook_024"), Hide("DCT_NoteBook_025"), Hide("DCT_NoteBook_026"), Hide("DCT_NoteBook_027"), Hide("DCT_NoteBook_028"), Hide("DCT_NoteBook_029"), Hide("DCT_NoteBook_030"),        Hide("DCT_NoteBook_031"), Hide("DCT_NoteBook_032"), Hide("DCT_NoteBook_033"), Hide("DCT_NoteBook_034"), Hide("DCT_NoteBook_035"), Hide("DCT_NoteBook_036"), Hide("DCT_NoteBook_037"), Hide("DCT_NoteBook_038"), Hide("DCT_NoteBook_039"), Hide("DCT_NoteBook_040"), Hide("DCT_NoteBook_041")

screen DCT_Scr_NoteBook:   

    tag menu
    add "NoteBook_000"
    
    frame:
        background None
        xalign .99
        yalign .3
        top_padding 20 
        bottom_padding 20 
        left_padding 20
        right_padding 20
            #vbar value YScrollValue("vp") bar_invert True
        has side "c r":
            area (0, 0, 300, 700)
            viewport id "vp":
                
                mousewheel True
                yadjustment ui.adjustment (value=1, range=99999)   # err... works, but...

                vbox:
                    if persistent.Sys_Langue == "VN":
                        if DCT_UnLock_NoteBook_001 == 1:
                            textbutton "Ghi chép 01" action DCT_NoteBook_But000, Show("DCT_NoteBook_001") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_002 == 1:
                            textbutton "Ghi chép 02" action DCT_NoteBook_But000, Show("DCT_NoteBook_002") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_003 == 1:
                            textbutton "Ghi chép 03" action DCT_NoteBook_But000, Show("DCT_NoteBook_003") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_004 == 1:
                            textbutton "Ghi chép 04" action DCT_NoteBook_But000, Show("DCT_NoteBook_004") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_005 == 1:
                            textbutton "Ghi chép 05" action DCT_NoteBook_But000, Show("DCT_NoteBook_005") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_006 == 1:
                            textbutton "Ghi chép 06" action DCT_NoteBook_But000, Show("DCT_NoteBook_006") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_007 == 1:
                            textbutton "Ghi chép 07" action DCT_NoteBook_But000, Show("DCT_NoteBook_007") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_008 == 1:
                            textbutton "Ghi chép 08" action DCT_NoteBook_But000, Show("DCT_NoteBook_008") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_009 == 1:
                            textbutton "Ghi chép 09" action DCT_NoteBook_But000, Show("DCT_NoteBook_009") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_010 == 1:
                            textbutton "Ghi chép 10" action DCT_NoteBook_But000, Show("DCT_NoteBook_010") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_011 == 1:
                            textbutton "Ghi chép 11" action DCT_NoteBook_But000, Show("DCT_NoteBook_011") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_012 == 1:
                            textbutton "Ghi chép 12" action DCT_NoteBook_But000, Show("DCT_NoteBook_012") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_013 == 1:
                            textbutton "Ghi chép 13" action DCT_NoteBook_But000, Show("DCT_NoteBook_013") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_014 == 1:
                            textbutton "Ghi chép 14" action DCT_NoteBook_But000, Show("DCT_NoteBook_014") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_015 == 1:
                            textbutton "Ghi chép 15" action DCT_NoteBook_But000, Show("DCT_NoteBook_015") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_016 == 1:
                            textbutton "Ghi chép 16" action DCT_NoteBook_But000, Show("DCT_NoteBook_016") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_017 == 1:
                            textbutton "Ghi chép 17" action DCT_NoteBook_But000, Show("DCT_NoteBook_017") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_018 == 1:
                            textbutton "Ghi chép 18" action DCT_NoteBook_But000, Show("DCT_NoteBook_018") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_019 == 1:
                            textbutton "Ghi chép 19" action DCT_NoteBook_But000, Show("DCT_NoteBook_019") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_020 == 1:
                            textbutton "Ghi chép 20" action DCT_NoteBook_But000, Show("DCT_NoteBook_020") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_021 == 1:
                            textbutton "Ghi chép 21" action DCT_NoteBook_But000, Show("DCT_NoteBook_021") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_022 == 1:
                            textbutton "Ghi chép 22" action DCT_NoteBook_But000, Show("DCT_NoteBook_022") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_023 == 1:
                            textbutton "Ghi chép 23" action DCT_NoteBook_But000, Show("DCT_NoteBook_023") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_024 == 1:
                            textbutton "Ghi chép 24" action DCT_NoteBook_But000, Show("DCT_NoteBook_024") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_025 == 1:
                            textbutton "Ghi chép 25" action DCT_NoteBook_But000, Show("DCT_NoteBook_025") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_026 == 1:
                            textbutton "Ghi chép 26" action DCT_NoteBook_But000, Show("DCT_NoteBook_026") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_027 == 1:
                            textbutton "Ghi chép 27" action DCT_NoteBook_But000, Show("DCT_NoteBook_027") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_028 == 1:
                            textbutton "Ghi chép 28" action DCT_NoteBook_But000, Show("DCT_NoteBook_028") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_029 == 1:
                            textbutton "Ghi chép 29" action DCT_NoteBook_But000, Show("DCT_NoteBook_029") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_030 == 1:
                            textbutton "Ghi chép 30" action DCT_NoteBook_But000, Show("DCT_NoteBook_030") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_031 == 1:
                            textbutton "Ghi chép 31" action DCT_NoteBook_But000, Show("DCT_NoteBook_031") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_032 == 1:
                            textbutton "Ghi chép 32" action DCT_NoteBook_But000, Show("DCT_NoteBook_032") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_033 == 1:
                            textbutton "Ghi chép 33" action DCT_NoteBook_But000, Show("DCT_NoteBook_033") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_034 == 1:
                            textbutton "Ghi chép 34" action DCT_NoteBook_But000, Show("DCT_NoteBook_034") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_035 == 1:
                            textbutton "Ghi chép 35" action DCT_NoteBook_But000, Show("DCT_NoteBook_035") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_036 == 1:
                            textbutton "Ghi chép 36" action DCT_NoteBook_But000, Show("DCT_NoteBook_036") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_037 == 1:
                            textbutton "Ghi chép 37" action DCT_NoteBook_But000, Show("DCT_NoteBook_037") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_038 == 1:
                            textbutton "Ghi chép 38" action DCT_NoteBook_But000, Show("DCT_NoteBook_038") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_039 == 1:
                            textbutton "Ghi chép 39" action DCT_NoteBook_But000, Show("DCT_NoteBook_039") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_040 == 1:
                            textbutton "Ghi chép 40" action DCT_NoteBook_But000, Show("DCT_NoteBook_040") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_041 == 1:
                            textbutton "Ghi chép 41" action DCT_NoteBook_But000, Show("DCT_NoteBook_041") at Sys_Eff_Appear
                        else:
                            text "..."
                        
                    elif persistent.Sys_Langue == "ENG":
                    
                        if DCT_UnLock_NoteBook_001 == 1:
                            textbutton "Note book 01" action DCT_NoteBook_But000, Show("DCT_NoteBook_001") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_002 == 1:
                            textbutton "Note book 02" action DCT_NoteBook_But000, Show("DCT_NoteBook_002") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_003 == 1:
                            textbutton "Note book 03" action DCT_NoteBook_But000, Show("DCT_NoteBook_003") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_004 == 1:
                            textbutton "Note book 04" action DCT_NoteBook_But000, Show("DCT_NoteBook_004") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_005 == 1:
                            textbutton "Note book 05" action DCT_NoteBook_But000, Show("DCT_NoteBook_005") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_006 == 1:
                            textbutton "Note book 06" action DCT_NoteBook_But000, Show("DCT_NoteBook_006") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_007 == 1:
                            textbutton "Note book 07" action DCT_NoteBook_But000, Show("DCT_NoteBook_007") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_008 == 1:
                            textbutton "Note book 08" action DCT_NoteBook_But000, Show("DCT_NoteBook_008") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_009 == 1:
                            textbutton "Note book 09" action DCT_NoteBook_But000, Show("DCT_NoteBook_009") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_010 == 1:
                            textbutton "Note book 10" action DCT_NoteBook_But000, Show("DCT_NoteBook_010") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_011 == 1:
                            textbutton "Note book 11" action DCT_NoteBook_But000, Show("DCT_NoteBook_011") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_012 == 1:
                            textbutton "Note book 12" action DCT_NoteBook_But000, Show("DCT_NoteBook_012") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_013 == 1:
                            textbutton "Note book 13" action DCT_NoteBook_But000, Show("DCT_NoteBook_013") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_014 == 1:
                            textbutton "Note book 14" action DCT_NoteBook_But000, Show("DCT_NoteBook_014") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_015 == 1:
                            textbutton "Note book 15" action DCT_NoteBook_But000, Show("DCT_NoteBook_015") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_016 == 1:
                            textbutton "Note book 16" action DCT_NoteBook_But000, Show("DCT_NoteBook_016") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_017 == 1:
                            textbutton "Note book 17" action DCT_NoteBook_But000, Show("DCT_NoteBook_017") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_018 == 1:
                            textbutton "Note book 18" action DCT_NoteBook_But000, Show("DCT_NoteBook_018") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_019 == 1:
                            textbutton "Note book 19" action DCT_NoteBook_But000, Show("DCT_NoteBook_019") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_020 == 1:
                            textbutton "Note book 20" action DCT_NoteBook_But000, Show("DCT_NoteBook_020") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_021 == 1:
                            textbutton "Note book 21" action DCT_NoteBook_But000, Show("DCT_NoteBook_021") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_022 == 1:
                            textbutton "Note book 22" action DCT_NoteBook_But000, Show("DCT_NoteBook_022") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_023 == 1:
                            textbutton "Note book 23" action DCT_NoteBook_But000, Show("DCT_NoteBook_023") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_024 == 1:
                            textbutton "Note book 24" action DCT_NoteBook_But000, Show("DCT_NoteBook_024") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_025 == 1:
                            textbutton "Note book 25" action DCT_NoteBook_But000, Show("DCT_NoteBook_025") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_026 == 1:
                            textbutton "Note book 26" action DCT_NoteBook_But000, Show("DCT_NoteBook_026") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_027 == 1:
                            textbutton "Note book 27" action DCT_NoteBook_But000, Show("DCT_NoteBook_027") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_028 == 1:
                            textbutton "Note book 28" action DCT_NoteBook_But000, Show("DCT_NoteBook_028") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_029 == 1:
                            textbutton "Note book 29" action DCT_NoteBook_But000, Show("DCT_NoteBook_029") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_030 == 1:
                            textbutton "Note book 30" action DCT_NoteBook_But000, Show("DCT_NoteBook_030") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_031 == 1:
                            textbutton "Note book 31" action DCT_NoteBook_But000, Show("DCT_NoteBook_031") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_032 == 1:
                            textbutton "Note book 32" action DCT_NoteBook_But000, Show("DCT_NoteBook_032") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_033 == 1:
                            textbutton "Note book 33" action DCT_NoteBook_But000, Show("DCT_NoteBook_033") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_034 == 1:
                            textbutton "Note book 34" action DCT_NoteBook_But000, Show("DCT_NoteBook_034") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_035 == 1:
                            textbutton "Note book 35" action DCT_NoteBook_But000, Show("DCT_NoteBook_035") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_036 == 1:
                            textbutton "Note book 36" action DCT_NoteBook_But000, Show("DCT_NoteBook_036") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_037 == 1:
                            textbutton "Note book 37" action DCT_NoteBook_But000, Show("DCT_NoteBook_037") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_038 == 1:
                            textbutton "Note book 38" action DCT_NoteBook_But000, Show("DCT_NoteBook_038") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_039 == 1:
                            textbutton "Note book 39" action DCT_NoteBook_But000, Show("DCT_NoteBook_039") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_040 == 1:
                            textbutton "Note book 40" action DCT_NoteBook_But000, Show("DCT_NoteBook_040") at Sys_Eff_Appear
                        else:
                            text "..."
                        if DCT_UnLock_NoteBook_041 == 1:
                            textbutton "Note book 41" action DCT_NoteBook_But000, Show("DCT_NoteBook_041") at Sys_Eff_Appear
                        else:
                            text "..."

        vbar value YScrollValue("vp") bar_invert True:
                    xalign 0.1 yalign 0.9
                    xmaximum 15 
                    ymaximum 750

    if persistent.Sys_Langue == "VN":
        textbutton ("Trở lại") action DCT_NoteBook_But000, Hide("DCT_Scr_NoteBook"), Show('Sys_MainMenu2') xalign .97 yalign .9 style "Style_MainMenu" at Sys_Eff_Appear
    elif persistent.Sys_Langue == "ENG":
        textbutton ("Return") action DCT_NoteBook_But000, Hide("DCT_Scr_NoteBook"), Show('Sys_MainMenu2') xalign .97 yalign .9 style "Style_MainMenu" at Sys_Eff_Appear

screen DCT_NoteBook_001:
    add "NoteBook_001"
screen DCT_NoteBook_002:
    add "NoteBook_002"
screen DCT_NoteBook_003:
    add "NoteBook_003"
screen DCT_NoteBook_004:
    add "NoteBook_004"
screen DCT_NoteBook_005:
    add "NoteBook_005"
screen DCT_NoteBook_006:
    add "NoteBook_006"
screen DCT_NoteBook_007:
    add "NoteBook_007"
screen DCT_NoteBook_008:
    add "NoteBook_008"
screen DCT_NoteBook_009:
    add "NoteBook_009"
screen DCT_NoteBook_010:
    add "NoteBook_010"
screen DCT_NoteBook_011:
    add "NoteBook_011"
screen DCT_NoteBook_012:
    add "NoteBook_012"
screen DCT_NoteBook_013:
    add "NoteBook_013"
screen DCT_NoteBook_014:
    add "NoteBook_014"
screen DCT_NoteBook_015:
    add "NoteBook_015"
screen DCT_NoteBook_016:
    add "NoteBook_016"
screen DCT_NoteBook_017:
    add "NoteBook_017"
screen DCT_NoteBook_018:
    add "NoteBook_018"
screen DCT_NoteBook_019:
    add "NoteBook_019"
screen DCT_NoteBook_020:
    add "NoteBook_020"
screen DCT_NoteBook_021:
    add "NoteBook_021"
screen DCT_NoteBook_022:
    add "NoteBook_022"
screen DCT_NoteBook_023:
    add "NoteBook_023"
screen DCT_NoteBook_024:
    add "NoteBook_024"
screen DCT_NoteBook_025:
    add "NoteBook_025"
screen DCT_NoteBook_026:
    add "NoteBook_026"
screen DCT_NoteBook_027:
    add "NoteBook_027"
screen DCT_NoteBook_028:
    add "NoteBook_028"
screen DCT_NoteBook_029:
    add "NoteBook_029"
screen DCT_NoteBook_030:
    add "NoteBook_030"
screen DCT_NoteBook_031:
    add "NoteBook_031"
screen DCT_NoteBook_032:
    add "NoteBook_032"
screen DCT_NoteBook_033:
    add "NoteBook_033"
screen DCT_NoteBook_034:
    add "NoteBook_034"
screen DCT_NoteBook_035:
    add "NoteBook_035"
screen DCT_NoteBook_036:
    add "NoteBook_036"
screen DCT_NoteBook_037:
    add "NoteBook_037"
screen DCT_NoteBook_038:
    add "NoteBook_038"
screen DCT_NoteBook_039:
    add "NoteBook_039"
screen DCT_NoteBook_040:
    add "NoteBook_040"
screen DCT_NoteBook_041:
    add "NoteBook_041"
