label Ch1P1_C2_E:

#Cảnh: Nhà thờ
#Thời gian: Chiều
#//Delay 1s

    stop music fadeout 1.0
    play music "Soundtracks/007 - Memories - Composed.ogg" fadein 1.0
    scene BG_9 with fade
    $ renpy.pause (2.0)
    
#Cảnh: Thánh đường
#Thời gian: Chiều
#//SFX: Tiếng mở cửa.
    scene BG_1 with fade
    
    play sound "sfx/door-1-close.mp3" fadein 1.0
    
    A" Do excuse me!"

    " The elegant cathedral fills my view the moment I pushed the doors open."
    " Never do they lock the doors."

    A" Father Fredo?"

    nvlDC" I call into the emptiness. Standing underneath the tall ceiling makes one uneasy, however warm the gaze of the Creator is wont to be."
    nvlDC" I touched the neatly aligned benches. It is as if Father Fredo has just cleaned everything from one end to the other again."
    nvlDC" \n"
    nvlDC" \n The cloth he uses to dust them everyday is now  spread across the foremost bench, but the man himself is nowhere in sight."
    nvlDC" A careful man, suddenly leaving behind a mess. Has an emergency happened?"
    nvlDC" His acolyte Hanes, too, is nowhere in sight. The whole cathedral has then turned into a huge empty cage."
    nvlDC" A piece of paper was obviously left behind, informing the possible pilgrim of Father Fredo's sudden absence."
    nvlDC" Becoming a high-ranking man of the cloth does entail a massive workload. Father Fredo, already seventy odd, is no exception. Wherever duty calls, there he goes."
    nvlDC" \n His endurance and perseverance is the subject of much admiration from the public. "
    nvl clear
    
#------------------------------------------------

    A"  ..."

    " I put the piece of paper back to where it belongs."
    " Perhaps I should leave. Let's not disturb this holy place unnecessarily. Not that I had any business here anyway."
    " I pray for a bit, and then leave."

    return