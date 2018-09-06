
label CS_Start:

    call CS_Load_BasicSetting

    $ CS_Place = renpy.random.randint(1, 3)
    $ CS_Char = renpy.random.choice (['Azu', 'Ele'])
    call CS_Start_Conversation

    return

label CS_Start_Conversation:

    $ CS_Turn += 1
    call CS_Chk_Emotion
    call CS_Chk_Status
    call CS_Chk_Attack

    if CS_Turn <= CS_MaxTurn:
        show screen CS_Scr_Info
        show screen CS_Scr_Char
        show screen CS_Scr_Topics
        $ renpy.pause (hard = True)
    else:
        hide screen CS_Scr_Topics
        call CS_Chk_Point
        e "Hôm nay nói chuyện đến đây thôi nha"
        hide screen CS_Scr_Info
        hide screen CS_Scr_Char

    return
