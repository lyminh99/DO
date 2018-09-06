
label Start_SubQuest:

    call SQ_Load_BasicSetting
    $ renpy.pause (0.5, hard=True)

    e "Nhấn E để tương tác, Dùng bàn phím mũi tên để di chuyển 4 hướng"
    call SQ_MainLabel

    return

label SQ_MainLabel:

    if SQ_Exit == True:
        return
    else:

        $ SQ_77.Type = renpy.random.choice(['X', '...'])
        $ SQ_78.Type = renpy.random.choice(['X', '...'])
        $ SQ_79.Type = renpy.random.choice(['X', '...'])
        $ SQ_87.Type = renpy.random.choice(['X', '...'])
        $ SQ_88.Type = renpy.random.choice(['X', '...'])
        $ SQ_89.Type = renpy.random.choice(['X', '...'])
        $ SQ_97.Type = renpy.random.choice(['X', '...'])
        $ SQ_98.Type = renpy.random.choice(['X', '...'])
        $ SQ_99.Type = renpy.random.choice(['X', '...'])

        show screen SQ_Keymap
        show screen Sys_SQ_CharPOS
        show screen Sys_SQ_Map
        $ renpy.pause (hard=True)
