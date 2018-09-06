label Ch6P2_C1_E:

#OutIF 6.1
#(If Azzurra_Stays_With_Fredo =1 AND Hanes_Truth = 0)
#Cảnh: Lễ hội
#Thời gian: Sáng
    stop music fadeout 1.0
    play music "Soundtracks/015 - Dying World.mp3" fadein 1.0
    scene BG_6b with fade
    " Morning of the Day. Anatolio, reporting in."
    "All... is not well."

    nvlDC" If someone had told me two week ago that there would be a time my parents' shouting would sound so surreal, I would have laughed him off."
    nvlDC"\n And now, here I am, looking at and listening to everything as if they were all otherworldly. Like I've gone to a new world with new worries and challenges, and forced now to look back at the world I have left, and those still stuck in it."
    nvlDC"\n But to focus on the positive: The streets are so beautiful today. So beautiful as to be contradictory."
    nvlDC"\n The festival shall take place at the central piazza. Every road leading there has been elegantly decorated: flowers and banners and the sign of the Holy Light."
    nvlDC"\n They've put up a series of great arches along the main street. Not a scrap of litter anywhere, nor a single open shop. Every eyes are supposed to be on a large stage at the center of the piazza, under which a huge altar has been erected under the great statue of the Creator's Court."
    nvlDC"\n The Creator Meyr stands in the middle of the statue, his great blade pointing down at the altar. Looks like I shall be standing right about there. He shall be the judge as to whether I am deserving of being human or not."
    nvlDC"\n To think of it, one of the most sacred moment in a person's life is supposed to be the scariest. Being a grown and accepted citizen, well, that's meant to be a privilege, not a right, and can be revoked if you do not live up to it."
    nvlDC"\n But then it's not all gloomy and stiff-necked, you see."
    nvlDC"\n The shops that have closed? Well, that's because lots and lots of little tents have been put up around the altar. Ceremony for us and a grand fair for the rest: food and games and fun, and even tents where venerable fathers would take the time to debate the sacred scripture to the pious who would hear their theological thoughts."
    nvlDC"\n The aroma of sweets and pastries and flowers and perfumes and sacred candle... You've got to be there to know such atmosphere does exist in this boring mortal coil."
    nvlDC"\n Everyone can enter the piazza as they please, though the grand stage is barred to all until the moment. A dozen ceremonial Templars in mail and tabard and all the panoplies of war stand guard, still as a row of live-sized statues."
    nvlDC"\n For a while I stand before the grand stage. It's still rather early, but I'm still joined by some dozens my age: male and female, thin and pudgy, dwarvishly short to twiggily tall..."
    nvlDC"\n Once every so often one would nervously approach the guards and show their medals. “Come back later” was all they got. That's right, we're all too early."
    nvlDC"\n I look around the place. My face heats up."
    nvlDC"\n Azzurra is nowhere in sight. And not because I haven't looked either."
    nvlDC"\n Her signature blue skirt and golden hair can't so easily melt into the crowd."
    nvlDC"\n I'm still looking around... when a hand taps on my shoulder."
    nvl clear

    show Azu Hanes P0 at center
    H" Oh! A g-g-guest for good old Hanes!"
    A" … Mornin'."
    A" Nice clothes."
    show Azu Hanes P1 at center
    H" B-but of course! M-my big job t'day!"

    " I don't think I've ever seen Hanes so happy. I'm happy for him, and would be much happier if I weren't so preoccupied by Azzurra's problem."

    show Azu Hanes P0 at center
    H" W-what's up? Ready for the Bi-Big Day?"
    A"  Not...exactly. Not yet."
    show Azu Hanes P2 at center
    H" Eh? S-something's the mat-matter?"
    A"  ..."
    show Azu Hanes P1 at center
    H" B-but of course. I've b-been your friend for all t-these years, of c-course I know!"
    show Azu Hanes P2 at center
    H" Azu's problem, no?"
    A" … Yeah."
    show Azu Hanes P0 at center
    H" N-nothing's the matter, I a-a-assure you! Azu's f-family will h-handle everything! "
    show Azu Hanes P2 at center
    H" They pr-promised as much to your p-parents and Father F-Fredo, d-didn't they?"

    " Hanes does look rather well-placated. Looks like he is still blissfully unaware of the troubles over the past few days."

    A" Would be good if that is true. But what if Azzurra's aunt and uncle are fakes?"

    " Hanes rolls his eyes at me."

    show Azu Hanes P2 at center
    H"  Y-you are acc-accusing the Church, are y-you, An-Anatolio?"
    A" T-that's not what I mean! Though..."

    " I feel a cold draft up my back. I was being a fool: Hanes is, after all, part of the clergy."
    " Telling him the truth is going to do me a lot of harm!"

    show Azu Hanes P2 at center
    H" T-though?"
    A" Nothing, nothing much. I'm just wondering if they can actually go to the City in time for the Azzurra's ceremony."
    show Azu Hanes P0 at center
    H" Hah! That's a g-good one. We are n-not going to ab-abandon th-those brave souls who b-boldly stare ev-evil in the eyes out there. "
    show Azu Hanes P2 at center
    H" There will be a w-way for Azzurra. C-certainly!"

    " Hanes' eyes look narrower than they normally are. I can't help but feel unsure: unsure if he's telling the truth or not."

    show Azu Hanes P0 at center
    H" Y-you are overth-overthinking things. L-listen to me, just re-relax. All sh-shall be well."
    A" That would be good..."
    show Azu Hanes P2 at center
    H" T-Trust me! The Creator s-sees all!"
    A" Mmm..."
    show Azu Hanes P0 at center
    H" Oh well… W-why not go e-enjoy yourself unt-until the time? Will be s-so crowded ar-around here later!"
    A" Right, right, right. So, uh... don't let me keep you!"

    " I've never quite been a good actor, and I'm sweating profusely as I speak. Hanes looks at me, as if saying “I know what you hide”. "
    "Then he walks towards the stage, and disappears behind the row of Templars with an air of haughtiness about him."
    "Hanes? Planning something? No, hiding something? Are you still our friend?"
    "And then my mind wanders to the obvious. Azzurra! No, now it's all clear something has gone terribly wrong!"
    "I have to look for her, that's the only thing on top of my mind."
    "And there's only one place I can do that: The chapel!"

#(Jump Church.Resolution)

    return