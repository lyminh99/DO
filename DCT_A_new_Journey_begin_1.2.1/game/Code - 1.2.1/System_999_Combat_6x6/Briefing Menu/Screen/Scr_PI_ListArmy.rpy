
screen Scr_PI_ListArmy:

    if BS_Ctl_PlayerSide == 3 or BS_Ctl_PlayerSide == 1:

    #=====================================================
        frame:
            background im.Scale("Images/Briefing Menu/BM_ListArmy_BG.jpg", 300, 800)
            align (1.0, 0.6)
            top_padding 10 bottom_padding 50
            left_padding 10 right_padding 10
            has side "c r":
                area (0, 0, 300, 760)
                viewport id "A_vp":
                    mousewheel True
                    yadjustment ui.adjustment (value=0, range=999999)   # err... works, but...
                    vbox:
    #=====================================================
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_A_ListArmy_Slots_001.Ocu == 1:
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_A_ListArmy_Slots_001.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_A_ListArmy_Slots_001.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_A_ListArmy_Slots_001.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_A_ListArmy_Slots_001.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_A_Slot001_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_001 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_A_ListArmy_Slots_002.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_A_ListArmy_Slots_002.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_A_ListArmy_Slots_002.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_A_ListArmy_Slots_002.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_A_ListArmy_Slots_002.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_A_Slot002_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_002 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_A_ListArmy_Slots_003.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_A_ListArmy_Slots_003.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_A_ListArmy_Slots_003.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_A_ListArmy_Slots_003.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_A_ListArmy_Slots_003.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_A_Slot003_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_003 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_A_ListArmy_Slots_004.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_A_ListArmy_Slots_004.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_A_ListArmy_Slots_004.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_A_ListArmy_Slots_004.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_A_ListArmy_Slots_004.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_A_Slot004_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_004 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_A_ListArmy_Slots_005.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_A_ListArmy_Slots_005.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_A_ListArmy_Slots_005.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_A_ListArmy_Slots_005.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_A_ListArmy_Slots_005.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_A_Slot005_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_005 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_A_ListArmy_Slots_006.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_A_ListArmy_Slots_006.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_A_ListArmy_Slots_006.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_A_ListArmy_Slots_006.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_A_ListArmy_Slots_006.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_A_Slot006_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_006 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_A_ListArmy_Slots_007.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_A_ListArmy_Slots_007.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_A_ListArmy_Slots_007.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_A_ListArmy_Slots_007.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_A_ListArmy_Slots_007.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_A_Slot007_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_007 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_A_ListArmy_Slots_008.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_A_ListArmy_Slots_008.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_A_ListArmy_Slots_008.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_A_ListArmy_Slots_008.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_A_ListArmy_Slots_008.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_A_Slot008_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_008 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_A_ListArmy_Slots_009.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_A_ListArmy_Slots_009.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_A_ListArmy_Slots_009.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_A_ListArmy_Slots_009.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_A_ListArmy_Slots_009.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_A_Slot009_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_009 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_A_ListArmy_Slots_010.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_A_ListArmy_Slots_010.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_A_ListArmy_Slots_010.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_A_ListArmy_Slots_010.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_A_ListArmy_Slots_010.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_A_Slot010_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_010 Empty"

    #=====================================================
                vbar value YScrollValue("A_vp") bar_invert True:
                    xalign 0.5 yalign 0.0
                    xmaximum 7
                    ymaximum 760
                    left_bar Frame("gui/config_bar_full.png", 5, 0) 
                    right_bar Frame("gui/config_bar_empty.png", 5, 0)
    #=====================================================

#=====================================================
#=====================================================
#=====================================================
#=====================================================
#=====================================================
#=====================================================
#=====================================================
#=====================================================
#=====================================================


    if BS_Ctl_PlayerSide == 3 or BS_Ctl_PlayerSide == 2:

    #=====================================================
        frame:
            background im.Scale("Images/Briefing Menu/BM_ListArmy_BG.jpg", 300, 800)
            align (0.0, 0.6)
            top_padding 10 bottom_padding 50
            left_padding 10 right_padding 10
            has side "c r":
                area (0, 0, 300, 760)
                viewport id "D_vp":
                    mousewheel True
                    yadjustment ui.adjustment (value=0, range=999999)   # err... works, but...
                    vbox:
    #=====================================================
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_D_ListArmy_Slots_001.Ocu == 1:
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_D_ListArmy_Slots_001.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_D_ListArmy_Slots_001.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_D_ListArmy_Slots_001.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_D_ListArmy_Slots_001.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_D_Slot001_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_001 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_D_ListArmy_Slots_002.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_D_ListArmy_Slots_002.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_D_ListArmy_Slots_002.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_D_ListArmy_Slots_002.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_D_ListArmy_Slots_002.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_D_Slot002_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_002 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_D_ListArmy_Slots_003.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_D_ListArmy_Slots_003.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_D_ListArmy_Slots_003.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_D_ListArmy_Slots_003.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_D_ListArmy_Slots_003.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_D_Slot003_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_003 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_D_ListArmy_Slots_004.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_D_ListArmy_Slots_004.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_D_ListArmy_Slots_004.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_D_ListArmy_Slots_004.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_D_ListArmy_Slots_004.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_D_Slot004_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_004 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_D_ListArmy_Slots_005.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_D_ListArmy_Slots_005.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_D_ListArmy_Slots_005.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_D_ListArmy_Slots_005.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_D_ListArmy_Slots_005.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_D_Slot005_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_005 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_D_ListArmy_Slots_006.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_D_ListArmy_Slots_006.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_D_ListArmy_Slots_006.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_D_ListArmy_Slots_006.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_D_ListArmy_Slots_006.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_D_Slot006_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_006 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_D_ListArmy_Slots_007.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_D_ListArmy_Slots_007.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_D_ListArmy_Slots_007.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_D_ListArmy_Slots_007.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_D_ListArmy_Slots_007.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_D_Slot007_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_007 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_D_ListArmy_Slots_008.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_D_ListArmy_Slots_008.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_D_ListArmy_Slots_008.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_D_ListArmy_Slots_008.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_D_ListArmy_Slots_008.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_D_Slot008_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_008 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_D_ListArmy_Slots_009.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_D_ListArmy_Slots_009.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_D_ListArmy_Slots_009.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_D_ListArmy_Slots_009.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_D_ListArmy_Slots_009.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_D_Slot009_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_009 Empty"
    #               --------------------------------------------------------------
                        text ""
    #               --------------------------------------------------------------
                        if BM_D_ListArmy_Slots_010.Ocu == 1: 
                            frame:
                                background im.Scale("Images/Briefing Menu/BM_SwapArmy_BG.jpg", 250, 120)
                                vbox:
                                    text "{size=18}Name: [BM_D_ListArmy_Slots_010.Name]{/size}" xpos (20)
                                    text "{size=18}Level: [BM_D_ListArmy_Slots_010.Level] {/size}" xpos (20)
                                    text "{size=18}Exp  : [BM_D_ListArmy_Slots_010.Exp]   {/size}" xpos (20)
                                    text "{size=18}Class: [BM_D_ListArmy_Slots_010.Class] {/size}" xpos (20)
                                    hbox:
                                        imagebutton auto "Images/Briefing Menu/Swap_Icon_%s.png" focus_mask True action BM_ListArmy_D_Slot010_Picked at BM_Eft_SwapArmyButton
                        else:
                            text "Slots_010 Empty"

    #=====================================================
                vbar value YScrollValue("D_vp") bar_invert True:
                    xalign 0.5 yalign 0.0
                    xmaximum 7
                    ymaximum 760
                    left_bar Frame("gui/config_bar_full.png", 5, 0) 
                    right_bar Frame("gui/config_bar_empty.png", 5, 0)
    #=====================================================
