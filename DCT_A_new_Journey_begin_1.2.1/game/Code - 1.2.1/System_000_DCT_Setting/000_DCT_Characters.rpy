init:

    $ config.adv_nvl_transition = dissolve
    $ config.nvl_adv_transition = dissolve
    $ NVL = Character(None, kind=nvl)
    $ narrator = Character(None)
    
#-------------------------------------------------------------------------------------------------

    $ NVL_center = Character(None, kind=nvl, what_xalign=0.5, what_text_align=0.5)

    $ nvl_Center = Character(_(""),
                        color="#c8ffc8",
                        what_xalign=0.5, kind=nvl)
    $ nvl_Right = Character(_(""),
                        color="#c8ffc8",
                        what_xalign=0, kind=nvl)
    $ nvlCB = Character(_(""),
                        color="#c8ffc8",
                        what_prefix="Cậu bé: \"", 
                        what_suffix="\"",
                        what_color="#c8ffc8", kind=nvl)
    $ nvlOG = Character(_(""),
                        color="#c8ffc8",
                        what_prefix="Ông già: \"", 
                        what_suffix="\"",
                        what_color="#c4d551", kind=nvl)
    $ nvlOC = Character(_(""),
                        color="#c8ffc8",
                        what_prefix="Ông cụ: \"", 
                        what_suffix="\"",
                        what_color="#c4d551", kind=nvl)
    $ nvlDC = Character(_(""),
                        color="#ffffff",
                        what_slow_cps=20,
                        what_size=35, kind=nvl)
    #$ config.adv_nvl_transition = dissolve
    #$ config.nvl_adv_transition = dissolve
    $ nvlDC2 = Character(_(""),
                        color="#c8ffc8",
                        what_text_align=0.5, kind=nvl)

#-------------------------------------------------------------------------------------------------

    $ e = "Elena"

    $ eslow = Character("Azzura",
                        color="#ffffff",
                        what_slow_cps=20,
                        show_two_window=True)

    $ DC = Character(None,
                        color="#c8ffc8",
                        show_two_window=True)

    $ A = Character("Anatolio",
                        color="#253897",
                        show_two_window=True) 

    $ A_AZ = Character("Anatolio và Azzurra",
                        color="#70b9f1",
                        show_two_window=True) 

    $ H_AZ = Character("Hanes và Azzurra",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ H_A = Character("Hanes và Anotolio",
                        color="#70b9f1",                        
                        show_two_window=True) 

    $ HC = Character("Hậu cần",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ TK = Character("Thư ký",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ F = Character("Fredo",
                        color="#70b9f1",                        
                        show_two_window=True) 

    $ T = Character("Tiziano",
                        color="#70b9f1",
                        what_slow_cps=20,
                        show_two_window=True) 

    $ TN = Character("Thanh niên",
                        color="#70b9f1",                        
                        show_two_window=True) 

    $ DD = Character("Đám Đông",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ DD2 = Character("???",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ TGM = Character("Tổng giám mục",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ TG = Character("Tổng giám ",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ GM = Character("Giám mục",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ MS = Character("Mục sư",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ GH = Character("Giáo hoàng",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ NHG = Character("Người hộ giáo",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ Alhf = Character("Alhf",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ CN = Character("Công nhân",
                        color="#70b9f1",                        
                        show_two_window=True)

    $ C0 = Character("???",
                        color="#70b9f1",                        
                        show_two_window=True) 

    $ CG = Character("Cô gái",
                        color="#70b9f1",                        
                        show_two_window=True) 

    $ PN1 = Character("Phụ nữ 1",
                        color="#70b9f1",                        
                        show_two_window=True) 

    $ PN2 = Character("Phụ nữ 2",
                        color="#70b9f1",
                        
                        show_two_window=True) 
    $ BA = Character("???",
                        color="#70b9f1",
                        
                        show_two_window=True) 
    $ AS = Character("Ascenderos",
                        color="#70b9f1",
                        
                        show_two_window=True) 
    $ BHX = Character("Bà hàng xóm",
                        color="#70b9f1",
                        
                        show_two_window=True) 
    $ P = Character("Ông Pietro",
                        color="#70b9f1",
                        
                        show_two_window=True)
    $ Pa = Character("Paul Attenborough",
                        color="#70b9f1",
                        
                        show_two_window=True) 
    $ BP = Character("Bà Pietro",
                        color="#70b9f1",
                        
                        show_two_window=True) 
    $ AZ = Character("Azzurra",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ Az = Character("Azzurra",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ AZ2 = Character("Azzurra",
                        color="#ffffff",
                        
                        show_two_window=True,
                        what_size=50)
    $ AZ3 = Character("Azzurra",
                        color="#ffffff",
                        
                        show_two_window=True,
                        what_size=70)
    $ E = Character("Elena",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ Emi = Character("Emilio",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ LG = Character("Lính gác",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ NDO = Character("Người đàn ông",
                        color="#70b9f1",
                        what_slow_cps=20,
                        show_two_window=True)
    $ NDO1 = Character("Người đàn ông 1",
                        color="#70b9f1",
                        
                        show_two_window=True)
    $ NDO2 = Character("Người đàn ông 2",
                        color="#70b9f1",
                        
                        show_two_window=True)
    $ NDO3 = Character("Người đàn ông 3",
                        color="#70b9f1",
                        
                        show_two_window=True)
    $ TT = Character("Thị trưởng",
                        color="#70b9f1",
                        
                        show_two_window=True)
    $ M = Character ("Meyer",
                        color="#fd5413",
                        
                        show_two_window=True)
    $ H = Character ("Hanes",
                        color="#70b9f1",
                        
                        show_two_window=True)
    $ MH = Character ("Mẹ Hanes",
                        color="#70b9f1",
                        
                        show_two_window=True)
    $ OI = Character ("Ông Ines",
                        color="#70b9f1",
                        
                        show_two_window=True)
    $ EA = Character("Elena và Azzurra",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ OC = Character("Ông cụ",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ BC = Character("Bà cụ",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ BaC = Character("Bà chủ",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ BCTS = Character("Bà chủ tiệm sách",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ HNDO = Character("Hai người đàn ông",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ CV1 = Character("Cận vệ 1",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ CV2 = Character("Cận vệ 2",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ QC = Character("Quý cô",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ CB = Character("Cậu bé",
                        color="#ffffff",
                        
                        show_two_window=True)
    $ god = Character("{font=fonts/times_0.ttf}ָאוֹר{/font}",
                        color="#ffffff",
                        
                        show_two_window=True)
    
    $ esub = Character(None,
                            what_size=48,
                            what_color="#000033",
                            what_layout="subtitle",
                            what_xpos= -200,
                            what_ypos= -500,
                            what_text_align=0,
                            what_slow_cps=15,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False, 
                            #window_xalign=0.01,
                            #window_yalign=0.1, show ('quick_menu') = False
                            )
    $ esub2 = Character(None,
                            what_size=48,
                            what_color="#000033",
                            what_layout="subtitle",
                            what_xalign=0.99,
                            what_text_align=1,
                            what_slow_cps=15,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.99,
                            window_yalign=0.99, 
                            )
    $ esub3 = Character(None,
                            what_size=48,
                            color="#c8ffc8",
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_ypos=-250,
                            what_text_align=0.5,
                            what_slow_cps=15,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5,
                            window_yalign=0.5, 
                            ) 
