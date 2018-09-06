label Hopeless_Dream_End_E:

#Cảnh: Anatolio (Về già), ngồi dưới gốc cây cổ thụ trên một chiếc xe lăn, nhìn lên bầu trởi đầy sao.
#//NVL
    stop music fadeout 1.0
    play music "Soundtracks/Demo2_3.mp3" fadein 1.0
    scene BG_5 with fade
    nvlDC"I had, then, hoped it was just a temporary parting."
    nvlDC"\n But that was truly the last I've seen of Azzurra."
    nvlDC"\n After the Sun Festival, the Schallendorf faction, with Azzurra in town, left that house of theirs."
    nvlDC"\n Mr. Attenborough didn't look for me any more. At the end of the day, I have failed, and no one, no organization, would need a failure like me."
    nvlDC"\n How the Schallendorf faction's adventure end, I'm equally clueless about. Did they get away from our tiny world? Did they not? And does that even matter?"
    nvlDC"\n What I do know is that over the half a century since then, the Church still rules supreme, warts and all. A world out there, if any, is forever beyond our grasp."
    nvlDC"\n Now, I sit here still under the tree, my life draining away. I look up there, at the sky, wondering if I have made the right decisions. The answer, perhaps, is no."
    nvlDC"\n Many reincarnations may pass, and I will still regret the choices I have made."
    nvlDC"\n There, up in the high heavens, the horizon reigns supreme, as if mocking the effort of us little people, trying in vain to escape its grasp and failing to overcome our own limits."
    nvl clear

#Cảnh: Bầu trời sao

    A" Because to be human is to reach for unreachable dreams."
    $ show_quick_menu1 = False
    show fin_white:
     yalign 0
     xalign 0.9
     alpha 0
     linear 2 alpha 1
    $renpy.pause (2)
    hide fin_white 

    return