init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

##############################

    $ dissolve3 = Dissolve(0.3)
    $ fade3 = Fade(1, 2, 1)
    $ fade2 = Fade(0, 0, 1)
    $ dissolve2 = Dissolve(0.2)
    $ dissolve5 = Dissolve(0.5)
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

    $ style.nvl_dialogue.justify = True
    $ sshake = Shake((1, 0, 1, 0), 1.0, dist=150)
    $ sshake2 = Shake((1, 0, 1, 0), 3.0, dist=150)
    $ sshake3 = Shake((1, 0, 1, 0), 5.0, dist=150)
##############################
# Declare characters used by this game.
##############################
    define Azu = Character('Azzurra', color="#c8ffc8")
    define Ana = Character('Anatolio', color="#c8ffc8")
    define Fre = Character('Mục sư Fredo', color="#c8ffc8")
    define Ele = Character('Elena', color="#c8ffc8")
    define Sub01 = Character('Ông hàng xóm', color="#c8ffc8")
    define Sub02 = Character('Vợ ông hàng xóm', color="#c8ffc8")
    define Sub03 = Character('Bố tôi', color="#c8ffc8")
    define Sub04 = Character('Mục sư Hanes', color="#c8ffc8")
    define Sub05 = Character('Cô hầu gái', color="#c8ffc8")
    define Sub06 = Character('Chú chó', color="#c8ffc8")

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
                            what_xpos=-500,
                            what_ypos=-500,
                            what_text_align=0,
                            what_slow_cps=15,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            #window_xalign=0.01,
                            #window_yalign=0.1
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
                            window_yalign=0.99
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
                            window_yalign=0.5
                            ) 

    # Declare an nvl-version of eileen.
    $ nvlDC = Character(_(""),
                        color="#c8ffc8", kind=nvl)
    $ nvl_Center = Character(_(""),
                        color="#c8ffc8",
                        what_xalign=0.5,
                        kind=nvl)
    $ nvl_Right = Character(_(""),
                        color="#c8ffc8",
                        what_xalign=0,
                        kind=nvl)
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
    $ nvlDC2 = Character(_(""),
                        color="#c8ffc8",
                        what_text_align=0.5, kind=nvl)


    $ config.adv_nvl_transition = dissolve
    $ config.nvl_adv_transition = dissolve
    transform right_to_left:
        linear 0.3 xalign 0.1
    transform center:
      align (.5,1.0)
      on replaced:
        linear .2 alpha .0
    transform left:
      align (.2,1.0)
      on replaced:
        linear .2 alpha .0
    transform right:
      align (.9,1.0)
      on replaced:
        linear .2 alpha .0

    image movie = Movie(size=(1920, 1080), xalign=0.0, yalign=0.0)

init python hide:
    for file in renpy.list_files():
        if file.startswith('bg') and file.endswith('.jpg'):
            name = file.replace('BG/','').replace('/', ' ').replace('.jpg','')
            renpy.image(name, Image(file))

init python:

    mr = MusicRoom(fadeout=1.0)

    mr.add("Soundtracks/000 - Joy.ogg", always_unlocked=True)
    mr.add("Soundtracks/000 - Opening song theme.ogg", always_unlocked=True)
    mr.add("Soundtracks/001 - Dark Piano.ogg", always_unlocked=True)
    mr.add("Soundtracks/002 - Finding.ogg", always_unlocked=True)  
    mr.add("Soundtracks/003 - Sincere.ogg", always_unlocked=True)
    mr.add("Soundtracks/004 - Lovely Bubbles.ogg", always_unlocked=True)
    mr.add("Soundtracks/005 - Father and mother.ogg", always_unlocked=True)
    mr.add("Soundtracks/11 2 2014 - 2_2.mp3", always_unlocked=True)
    mr.add("Soundtracks/007 - Memories - Composed.ogg", always_unlocked=True)
    mr.add("Soundtracks/008 - Stream f life.ogg", always_unlocked=True)
    mr.add("Soundtracks/AUTUMN.mp3", always_unlocked=True)
    mr.add("Soundtracks/010 - My love like winter.mp3", always_unlocked=True)
    mr.add("Soundtracks/011 - My childhood.ogg", always_unlocked=True)
    mr.add("Soundtracks/012 - 11 2 2013_2.mp3", always_unlocked=True)
    mr.add("Soundtracks/013 - 11 2 2013_3.mp3", always_unlocked=True)
    mr.add("Soundtracks/014 - Flyin_.mp3", always_unlocked=True)  
    mr.add("Soundtracks/015 - Dying World.mp3", always_unlocked=True)
    mr.add("Soundtracks/016 - Winter when i can_t see you.mp3", always_unlocked=True)
    mr.add("Soundtracks/017 - untitled.mp3", always_unlocked=True)
    mr.add("Soundtracks/018 - Azzura theme - Slowed.mp3", always_unlocked=True)
    mr.add("Soundtracks/019 - Azzura theme.mp3", always_unlocked=True)
    mr.add("Soundtracks/Demo2_3.mp3", always_unlocked=True)
    mr.add("Soundtracks/021 - 2 6 2014_2.mp3", always_unlocked=True)
    mr.add("Soundtracks/022 - Skipping.mp3", always_unlocked=True)


    #Make all the main menu buttons be the same size.
    #style.mm_button.size_group = "mm"
    style.mm_button.background = None
    #style.mm_button_text.outlines = [(3, "#000", 0, 0)]
    style.mm_button_text.hover_outlines = [(3, "#282", 0, 0)]
    #style.mm_button_text.drop_shadow = [(-5, -5), (1, -1), (-1, 1), (1, 1), (2, 2)]
    #style.mm_button_text.hover_drop_shadow_color = "#282"


    renpy.music.register_channel("test_one", "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
    renpy.music.register_channel("test_three", "sfx", False)
    renpy.music.register_channel("test_four", "sfx", False)
    renpy.music.register_channel("test_five", "sfx", False)
    renpy.music.register_channel("test_six", "sfx", False)

init 1:

    image Screen_title = "images/background/Screen_title.jpg"
    image black = "images/background/Black.jpg"
    image black2 = "images/background/Black2.jpg"
    image red = "images/background/red.jpg"
    image white = Solid((255, 255, 255, 255))
    image bg1 = im.Scale("images/background/BG1.jpg", 1920, 1080)
    image fin = "images/Ending/fin.png"
    image fin_white = "images/Ending/fin_white.png" 

    image DCT_tittle = "images/Themes/DCT_tittle.png"
    image cg_gallery = "gallocked.png"
    image Logo = "images/Themes/DO_Logo.jpg"
    image Mun = "images/Animated/Mun.gif"
    image Screen_title = "images/Themes/Screen_title.jpg"
    image Logo = "images/Themes/DO_Logo.jpg"
    image tuong = "images/Cutscenes/tuong.png"
    image che = "images/Cutscenes/che.png"
    image che2 = "images/Cutscenes/che2.png"

    image BG_1 = "images/background/BG_001_The_church.jpg"
    image BG_2 = "images/background/BG_002_The_window.jpg"
    image BG_3 = "images/background/BG_003_The_ field.jpg"
    image BG_4a = "images/background/BG_004_day_sky.jpg"
    image BG_4b = "images/background/BG_004_Night_sky.jpg"
    image BG_5 = "images/background/BG_005_The_sky.jpg"
    image BG_6 = "images/background/BG_006_The_street.jpg"
    image BG_6a = "images/background/BG_006_The_street_2.jpg"
    image BG_6b = "images/background/BG_006_The_street_3.jpg"
    image BG_7 = "images/background/BG_007_Full_book_house.jpg"
    image BG_7a = "images/background/BG_007_Full_book_house2.jpg"
    image BG_8 = "images/background/BG_008_the_vale.jpg"
    image BG_9 = "images/background/BG_009_The_lake.jpg"
    image BG_10 = "images/background/BG_010_two_drawing.jpg"
    image BG_11 = "images/background/BG_011_The_old_tree.jpg"
    image BG_12 = "images/background/BG_012_House_1.jpg"
    image BG_13 = "images/background/BG_013_House_2.jpg"
    image BG_14 = "images/background/BG_014_New_wedding_house.jpg"
    image BG_15 = "images/background/BG_015_The_grave_of_old.jpg"
    image BG_16 = "images/background/BG_006_The_street.jpg"
    image BG_17 = "images/background/BG_017_The_dark_Alley.jpg"
    image BG_18 = "images/background/BG_018_Door_to_the_ouside.jpg"
    image BG_19 = "images/background/BG_019_The_desert.jpg"
    image BG_20 = "images/background/BG_020_The_downtown.jpg"
    #image BG_21 = "images/background/BG_021xxxxxxxxxxx
    image BG_22 = "images/background/BG_022_The_Manor.jpg"
    image BG_22a = "images/background/BG_022_The_Manor2.jpg"
    image BG_23 = "images/background/BG_023_The_Lake.jpg"
    image BG_23a = "images/background/BG_023_The_Lake_night.jpg"
    image BG_24 = "images/background/BG_024.jpg"
    image BG_25 = "images/background/BG_025.jpg"
    image BG_30 = "images/background/BG_030.jpg"
    image BG_31 = "images/background/BG_031.jpg"
    image Banner = "images/KI1/BANNER.png"
    image stan = "images/KI1/standee.png"
    image huongdan = "images/KI1/Huongdan.png"

# Declare CG Used by this game

    image cg_1 = "images/Cutscenes/CG_001_The_little_Thief_1.jpg"
    image cg_2 = "images/Cutscenes/CG_002_The_little_Thief_2.JPG"
    image cg_3 = "images/Cutscenes/CG_003_The_little_Thief_3.JPG"
    image cg_3a = "images/Cutscenes/CG_003_The_little_Thief_4.JPG"
    image cg_4 = "images/Cutscenes/CG_004_what_a_face.JPG"
    image cg_5 = "images/Cutscenes/CG_005_illed_Azzurra.JPG"
    image cg_6 = "images/Cutscenes/CG_006_returning.JPG"
    image cg_7 = "images/Cutscenes/CG_007_a_kiss.JPG"
    image cg_8 = "images/Cutscenes/CG_008_a_welcome.JPG"
    image cg_9 = "images/Cutscenes/CG_009_finding.JPG"
    image cg_10 = "images/Cutscenes/CG_010_found_you.JPG"
    image cg_11 = "images/Cutscenes/CG_011_Elena_at_the_lake.JPG"
    image cg_12 = "images/Cutscenes/CG_012_Elena_at_the_lake_2.JPG"
    image cg_13 = "images/Cutscenes/CG_013_Elena_at_the_lake_3.JPG"
    image cg_gallery = "gallocked.png"
    image cg_0 = "images/background/Screen_title.jpg"
    image bg_0 = "images/background/Screen_title.jpg"
    image bg_1 = "images/background/BG_1_The_church.jpg"
    image bg_2 = "images/background/BG_2_The_window.jpg"
    image bg_3 = "images/background/BG_3_The_ field.jpg"
    image cg_14 = "images/Cutscenes/CG_Ending_elena_azzura_2.jpg"
# And this is the character art we use.
##### Azzurra
    image Azu_sp1 = "images/Sprites/Azzurra/Azzura_split1.jpg"
    image Azu_sp2 = "images/Sprites/Azzurra/Azzura_split2.jpg"
    image Azu_sp3 = "images/Sprites/Azzurra/Azzura_split3.jpg"

##### Little Azzurra 
    image Sma_Azu_P0 = "images/Sprites/Little_Azzurra/Little_Azzurra_P0.png"

##### Mature Azzurra 
    image Lar_Azu_P0 = "images/Sprites/Mature_Azzurra/Mature_Azzurra_P0.png"
    image Azu A P0 = "images/Sprites/Mature_Azzurra/Azu A P0.png"
    image Azu A P1 = "images/Sprites/Mature_Azzurra/Azu A P1.png"
    image Azu A P2 = "images/Sprites/Mature_Azzurra/Azu A P2.png"
    image Azu A P3 = "images/Sprites/Mature_Azzurra/Azu A P3.png"
    image Azu A P4 = "images/Sprites/Mature_Azzurra/Azu A P4.png"
    image Azu A P5 = "images/Sprites/Mature_Azzurra/Azu A P5.png"
    image Azu A P6 = "images/Sprites/Mature_Azzurra/Azu A P6.png"
    image Azu A P7 = "images/Sprites/Mature_Azzurra/Azu A P7.png"

##### Fredo
    image Fre_P0 = "images/Sprites/Fredo/Fredo_P0.png"

##### Elena
    image Azu Ele P000 = "images/Sprites/Elena/Elena_P000.png"
    image Azu Ele P001 = "images/Sprites/Elena/Elena_P001.png"
    image Azu Ele P002 = "images/Sprites/Elena/Elena_P002.png"
    image Azu Ele P003 = "images/Sprites/Elena/Elena_P003.png"
    image Azu Ele P004 = "images/Sprites/Elena/Elena_P004.png"
    image Azu Ele P005 = "images/Sprites/Elena/Elena_P005.png"
    image Azu Ele P006 = "images/Sprites/Elena/Elena_P006.png"
    image Azu Ele P007 = "images/Sprites/Elena/Elena_P007.png"
    image Azu Ele P008 = "images/Sprites/Elena/Elena_P008.png"
    image Azu Ele P009 = "images/Sprites/Elena/Elena_P009.png"
    image Azu Ele P010 = "images/Sprites/Elena/Elena_P010.png"
    image Azu Ele P011 = "images/Sprites/Elena/Elena_P011.png"
    image Azu Ele P012 = "images/Sprites/Elena/Elena_P012.png"
    image Azu Ele P013 = "images/Sprites/Elena/Elena_P013.png"
    image Azu Ele P014 = "images/Sprites/Elena/Elena_P014.png"
    image Azu Ele P015 = "images/Sprites/Elena/Elena_P015.png"
    image Azu Ele P016 = "images/Sprites/Elena/Elena_P016.png"
    image Azu Ele P017 = "images/Sprites/Elena/Elena_P017.png"

##### Sub characters
    image Sub_01 = "images/Sprites/Sub character/Sub01_Drunken_man.png"
    image Sub_02 = "images/Sprites/Sub character/Sub02_Drunken man's wife.png"
    image Sub_03 = "images/Sprites/Sub character/Sub03_Pedler_farther.png"
    image Sub_04 = "images/Sprites/Sub character/Sub04_Priest 2.png"
    image Sub_05 = "images/Sprites/Sub character/Sub05_Cooker.png"
    image Azu BaHangxom P0 = "images/Sprites/Sub character/BaHangxom P0.png"
    image Azu BaPietro = "images/Sprites/Sub character/BaPietro.png"
    image Azu Fredo P0 = "images/Sprites/Sub character/Fredo P0.png"
    image Azu Fredo P1 = "images/Sprites/Sub character/Fredo P1.png"
    image Azu Fredo P2 = "images/Sprites/Sub character/Fredo P2.png"
    image Azu Fredo P3 = "images/Sprites/Sub character/Fredo P3.png"
    image Azu Fredo P4 = "images/Sprites/Sub character/Fredo P4.png"
    image Azu OngHangxom P0 = "images/Sprites/Sub character/OngHangxom P0.png"
    image Azu OngHangxom P1 = "images/Sprites/Sub character/OngHangxom P1.png"
    image Azu OngPietro = "images/Sprites/Sub character/OngPietro.png"
    image Azu Paul P0 = "images/Sprites/Sub character/Paul P0.png"
    image Azu Paul P1 = "images/Sprites/Sub character/Paul P1.png"
    image Azu Paul P2 = "images/Sprites/Sub character/Paul P2.png"
    image Azu Paul P3 = "images/Sprites/Sub character/Paul P3.png"
    image Azu Unknow P0 = "images/Sprites/Sub character/Unknow P0.png"
    image Azu Unknow P1 = "images/Sprites/Sub character/Unknow P1.png"
    image Azu Hanes P0 = "images/Sprites/Sub character/Hanes P0.png"
    image Azu Hanes P1 = "images/Sprites/Sub character/Hanes P1.png"
    image Azu Hanes P2 = "images/Sprites/Sub character/Hanes P2.png"
    image Azu Hanes P3 = "images/Sprites/Sub character/Hanes P3.png"

    define Chapter_001_choice_001_played = 0
    define Chapter_001_choice_002_played = 0
    define Chapter_001_choice_003_played = 0
    define Chapter_001_E001_C001_played = 0
    define Chapter_001_E001_C002_played = 0
    define Chapter_001_E001_C003_played = 0
    define Chapter_001_E001_C004_played = 0

    define Chapter_001_E002_C001_played = 0
    define Chapter_001_E002_C002_played = 0
    define Chapter_001_E002_C003_played = 0

    define Chapter_001_choice_003_C001 = 0
    define Chapter_001_choice_003_C002 = 0

    define Chapter_002_choice_001_played =0
    define Chapter_002_choice_002_played =0
    define Chapter_004_choice_003_played =0

    define Chapter_004_E001_C003 = 0
    define Chapter_005_choice_002 = 0
    define Chapter_005_choice_003 = 0

    define SchallendorfHouse_choice_002a_played = 0

    define Elena_Point = 0
    define Azzurra_Point = 0
    define Azzurra_Persuasion = 0
    define Church = 0
    define Global_ParentPoint = 0
    define RescueTime = 0
    define Lohengramm = 0
    define Azzurra_Stays_With_Fredo = 0
    define Hanes_Truth = 0
    define Anatolio_Defies_Hanes = 0
    define Coin_Toss = 0
    define A_Rich_Happy_Family = 0
    define ElenaRescue = 0
    define Quantum.Physics = 0

    define Force_end_7c = 0
    define Hopeless_Dream_End = 0
    define True_end = 0
    define WAR_END_DEATH_OF_A_SPY = 0
    define WAR_END_REVOLUTION = 0
    define A_Rich_Happy_Family_end = 0
    $ persistent.Demo_finish = False
label splashscreen:

    show Logo with dissolve
    with Pause(1)

    hide logo with dissolve

    $ renpy.movie_cutscene ("videos/DCT_PV.ogv")
