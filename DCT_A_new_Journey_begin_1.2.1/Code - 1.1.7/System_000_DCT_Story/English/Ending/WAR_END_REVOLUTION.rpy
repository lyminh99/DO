label WAR_END_REVOLUTION_E:

#Chương 7C: Chiến thắng
    stop music fadeout 1.0
    play music "Soundtracks/Demo2_3.mp3" fadein 1.0
    " Ten years later"

#Cảnh: Phòng làm việc (Có chăng một lá cờ nền vàng có hình mặt trời đang trồi lên khỏi đỉnh núi)
#Thời gian: Sáng

    show Azu Unknow P0 at center
    HC" Reporting in, sir!"
    show Azu Unknow P0 at center
    HC" Mr. President, Sir! Victory! Victory at long last!"
    show Azu Unknow P0 at center
    HC" The enemy's last stronghold has fallen!"
    show Azu Unknow P0 at center
    HC" The last of House De'Rovere's cavalry have finally surrendered, unconditionally! It's over, sir, over at last!"
    show Azu OngPietro at center
    P" And the Pope and the rest of the Templar?"
    show Azu Unknow P0 at center
    HC" To the afterlife, everyone of them, sir!"
    show Azu OngPietro at center
    P" … How fare our brothers and sisters?"
    show Azu Unknow P0 at center
    HC" Battalion 30 took the brunt of the last assault, sir, and lost two hundred just yesterday alone. Battalion 16 lost eighty – fifty dead, thirty injured."
    show Azu Unknow P0 at center
    HC" The remaining pockets of resistance surrendered without much of a fight, sir, thankfully!"
    show Azu OngPietro at center
    P" It's been a long night, son. You've earned a good rest."
    show Azu Unknow P0 at center
    HC" Yes sir!"

    "The now-president turns over to his assistant, who has been waiting without a word on his side."

    show Azu OngPietro at center
    P" You too, friend. I wish to be left alone for the moment."
    show Azu Unknow P1 at center
    TK" Sir, yes, sir."

    " …"
    " He reclines on his chair, looking at the ceiling."

    show Azu OngPietro at center
    P" Let's hope these are the last who have to perish in this war of ours."
    show Azu OngPietro at center
    P" Ten years... ten years isn't that long for a world, all told."
    show Azu OngPietro at center
    P" And you, too, Anatolio Pietro. You'd created a change you probably didn't think you would have. Or that you'd have to pay with your life for that change."
    show Azu OngPietro at center
    P" It is a pity, is it not? Such is the way of the world."
    show Azu OngPietro at center
    P" What can I say about that? Not much, except that..."
    show Azu OngPietro at center
    P" That which you haven't been able to do in your short existence-"

#//Mode:NVL
    nvlDC"
He glances at his oval-shaped table, "
    nvlDC"\n upon which three sets of documents await his signature.
\n "
    nvlDC"\n “RESOLUTION 19B-167 ON THE POSTHUMOUS AWARD OF THE ORDER OF THE RISING SUN TO MR. ANATOLIO PIETRO, ESQ.”.
\n "
    nvlDC"\n and:"
    nvlDC"\n “RESOLUTION 19B-168 ON THE CREATION OF THE EXTRATERRESTRIAL SPACE RESEARCH CENTER ”.
"
    nvlDC"\n (AS PROPOSED BY DR. AZZURRA INES)
    "
    nvl clear

#Cảnh: đen
    scene black with fade
    show Azu OngPietro at center
    P"  Everything has been taken care of. Everything."

    show fin_white:
     yalign 0
     xalign 0.9
     alpha 0
     linear 2 alpha 1
    $renpy.pause (2)
    hide fin_white 

    return