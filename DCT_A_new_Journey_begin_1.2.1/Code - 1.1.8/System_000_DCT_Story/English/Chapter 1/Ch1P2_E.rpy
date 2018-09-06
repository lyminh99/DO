label Ch1P2_E:

#Cảnh: Công viên
#Thời gian: Chiều

    stop music fadeout 1.0
    play music "Soundtracks/004 - Lovely Bubbles.ogg" fadein 1.0
    scene BG_6 with dissolve

    " The park is one of the only places where the dying light has not been blocked off by all sorts of buildings. I can see the sunset sky from here!"
    " Whenever the endless grey walls tire me, I would come here, watching the bundles of leaves hanging atop oak branches as the smell of fresh paint wafts into my nostrils."
    " Welcome to Anatolio Pietro's painting workshop. Ever since I was a child, my pictures have gotten me no ends of praise."
    " It seems as if but a few days has passed since then."
    " Today I am tired – it is more prudent, perhaps, to find a corner to nod off. At least, that is my intention."
    " In truth, my luck tends to betray me when I most need it – all the benches surrounding me have been taken."
    " Anatolio: Just my luck."
    " I'd best find some other place then."

     
#//Màn hình nẩy lên 5s

    with sshake3
    stop music fadeout 1.0

    A"  !!!"

    " An earthquake?"
    " Wait, hold on, isn't the crowd over there a little restless too?"
    " Shouldn't I run out of here and hide my behind underneath a bench or something?"

    C0" EARTHQUAKE! EARTHQUAKE! OUTTA THE WAY!"
    A"  Wait a sec. Shouldn't an earthquake not say it's coming?"

    " Nope. That's one voice I know well."
    " I dodge to the side out of reflex. "
    " Unfortunately, there happens to be a rather large molehill behind me."

#//Màn hình nảy lên.

    with sshake

    C0" Owwiee..."

    " The figure sprawling before me is familiar enough, that much is true."
    " A young lady, about my age, endowed with a flowing mass of oily blond hair. "
    " She pushes herself up, dusting her skirt and sleeve, as though trying to attract every else's attention. "
    " In her arms there is a thick book with a chestnut cover that she has simply refused to let go."

    A"  Azzurra!"
    
    show Azu P58 at center    
    
    AZ"  Anatolio?"

#Cảnh: công viên có ghế đá
#Thời gian: chiều tối

    scene BG_6 with dissolve
    stop music fadeout 1
    play music "Soundtracks/019 - Azzura theme.mp3" fadein 2.0

    " We have found a fortunately unoccupied bench. Even more fortunately, Azzurra looks fine but for a tiny scrape."
    " There she sits and smiles at her incredibly handsome friend. Her hands cradles and caresses the book as if it were a dear pet." 
    " I'm still waiting – no, I bet she's just going to thank the incredibly handsome fellow who has come to her aid." 
    " Not to say I claim to be incredibly handsome. That would be so arrogant." 
    " Ahem – back to the story. Friends, citizens, countrymen – may I introduce Azzurra Ines, a granddaughter of Mr. Tiziano Ines, our old neighbor." 
    " Not much is known about Azzurra's parents: all I know is that they abandoned her and left her in old Tiziano's care. She never seemed to leave him for a moment." 
    " Hers was a sad tale: it was no wonder she has always been given preferential treatment by everyone else." 
    " Her name apparently means “blue” - yet I have always been meeting her when the sky is dyed red – like today. How ironic." 

    A" Feeling better?"
    
    show Azu P43_1 at center  
    
    AZ" But for a lump."
    A"  Did you have to run like that?"
    
    show Azu P7 at center
    
    AZ"  Well, here's the deal-"

    " Azzurra's face turns red as a beetroot. She freezes in her seat."

    A" Ah well. New book, isn't it?"

    " I don't think I have any better option than changing the topic."
    " Azzurra doesn't talk all that much and one of the worst person you can find in the city at initiating a conversation."
    " Is it any surprise she has a very few friends?"
    
    show Azu P17 at center
    
    AZ" Uh…"

    show black with dissolve
    
    show Azu_sp1 with dissolve3:
        yalign 0.008
        xalign 1.0
        linear 3.0 xalign 0.48

    show Azu_sp2 with dissolve3:
        yalign 0.5
        xalign 0.0
        linear 3.0 xalign 0.5

    show Azu_sp3 with dissolve3:
        yalign 0.992
        xalign 1.0
        linear 3.0 xalign 0.5

    $ renpy.pause(5.0)

    scene BG_6 :
        yalign 0.5
        xalign 0.5
        zoom 2.5
        linear 0.5 zoom 1.0

    show Azu P3 with dissolve2:
        yalign 0.99
        xalign 0.5
        zoom 2.5
        linear 0.5 zoom 1.0 

    " No, not at all."
    " In any case, ever since Mr. Ines passed away, Azzurra has lived alone. She began speaking more. A good sign, my parents thought. "
    " After all, to them she has been practically a daughter."
    " But it took her merely a few months to abandon that good habit. "
    " Instead, she began burying herself in books."
    " If you go to the bottom of it all, that might be my fault."
    " You see, I have always been a sucker for the secrets of the world, but has reading alone ever been fun? "
    " I was lucky, then, that Azzurra exists, and that she shares in my interest. One thing led to another, and in time she became my reading buddy."
    " But then it wasn't entirely my fault, mind you. "
    " As it happened, a child like Azzurra couldn't for the life of her understand all the books Mr. Ines had to offer. "
    " It was my father's idea to let her borrow from my family's collection."
    " By then I had long finished them all – whether I wanted to or not, to her I have become a senior, a companion and a teacher rolled into one. "
    " The distance between her and I have ever been narrowing since then."

    A"  Azu, isn't that a waste of money?"

    " I spoke in the deepest voice I could muster."
    " Azzurra widens her eyes at me. Then, as though having understood the crux of the matter, casts her glance at the book and tries to laugh it off."
    
    show Azu P21 at center
    
    Az" But... but it's a wonderful book!"

    " As time passed, my family collection began to peter out. Yet Mr. Ines' collection remains way beyond her reach (and mine)."
    " To fill in the gap, every month Azzurra would burn a bunch of cash to build her very own personal library."
    " I feel a pang of remorse some time."

    show Azu P25 at center
    
    Az" Anyway, haven't I told you already? Stop calling me Azu, you... crazy Ana!"
    A" Hey, hey, your fault for giving me that girly nickname to begin with! "
    A" Seriously, I'm going to–"
    
    show Azu P29 at center
    
    Az" You're going to do what?"

    " Azzurra tossed her hair. A challenge – she has a habit of doing that whenever she interrupts me like so."

    A" I'm going home!"
    
    show Azu P34 at center
    
    Az" Well, suit yourself then, Cra-zy Ana. Scare-dy Ana—"
    A" AAARRGH!"

#//Màn hình lắc rung.

    with sshake
    
    " Show of hands: Who thinks I'm totally justified to have my name changed?"

#oOo
#Cảnh: Đường phố
#Thời gian: Chiều

    scene BG_6 with dissolve
    stop music fadeout 1
    play music "Soundtracks/022 - Skipping.mp3" fadein 2.0
    
    " Why am I sitting here reading with Azzurra again? "
    " If I am to be rational, probably because reading and verbally sparring with someone beats sitting alone in a corner any day. "


    A" Alright, I give up. Accept my apology, my dear lady."

    " Yeah, well, let's do that. Someone has to give, and Azzurra definitely isn't that someone."

    show Azu P57 at center
    
    Az" Admitted defeat, huh?"
    A" Sure, sure, sure, it's a no, Big Sister Azzurra."
    
    show Azu P22 at center
    
    Az" Haha, that's my good little bro."

    " That was actually rather scary, Azzurra."

    A"  Well if you say so."
    A"  Anyway... where did this book come from?"

    " It looked like a precious volume, meticulously bound and strapped."

    show Azu P27 at center
    
    Az" I bought it."
    A" That's fishy – haven't you spent the last penny in this month's allowance just the other day?"

    " If memory serves me well, she had to borrow me some spare changes yesterday. "

    show Azu P31 at center
    
    Az" ...."
    A" Where did this book come from then? Don't tell me you were literally raiding the bookstore..."
    
    show Azu P59 at center
    
    Az" N-not telling!"
    A" Not even for some taffy?"
    
    show Azu P36 at center
    
    Az" I said no!"
    A" Well I'll be terribly curious-"
    
    show Azu P37 at center
    
    Az" Not my business."
    A" I'll have a stroke from sheer excitement!"
    
    show Azu P34 at center
    
    Az" Like I care?"
    A" I'll die wide open!"
    
    show Azu P33_1 at center
    
    Az" Fine – call me when your funeral comes."
    A" ..."

    " Azzurra steals a glance at me. I am willing to bet she hasn't actually been reading anything from that tome all the while."

    A" Well then, I'll be off. See you later."

    " I dust my sleeve and make a show of standing up. Azzurra doesn't bulge an inch."
    " Well, that is until I start taking a few steps towards the opposite direction."

    show Azu P15_1 at center
    
    Az" Hey hey hey hey hey! Where're you going? "

    " Of course she'd do that. Azzurra Ines, for everyone's information, is not known for being too aggressive or too wise, and probably can't bully anyone except your humble sincerely."
    " A price to pay for being nice..."
    
    A" Well then, tell me."

#"Azzurra (tiu nghỉu): 

    show Azu P21 at center

    Az" In truth..."

#//Hiệu ứng gợn sóng đồng tâm
#cảnh: công viên
#thời gian: chiều

    scene BG_6 with fade

    A" What? "

#//Màn hình nẩy lên// 

    with sshake
    
    A" You stole it???"

    show Azu P15_1 at center
    
    Az" Shhhh. Stealing is such an ugly word. It's not like I did it on purpose-"
    A" It does seem like stealing to me."
    
    show Azu P16 at center
    
    Az" Not really? The bookstore owner dropped it first!"
    
    show Azu P21 at center
    
    Az" I'm not a thief, Anatolio…"
    
    " Azzurra pinches me on my sleeve. She is capable of laying down the hurt, all right."
    
    A" Hmm…"

    " Azzurra's interpretation, after all, isn't exactly 'wrong'. Mr. Ascenderos and his six fingers aren't exactly known for being careful book handlers."
    " It isn't uncommon to have him fling his books all over the place while carting them from the storeroom on the opposite side of the road."
    " You would think an alcoholic with hand-eye coordination problems like him should just stop being such a miser and hire some capable employees."

#Thời gian: quá khứ

    scene BG_6 with fade
    show Azu P50 at center
    
    Az" I simply saw the book just lying there when I walked past – that's no way to treat such a pretty book! "

#Thời gian: chiều

    scene BG_6 with fade
    
    Az" Only when the owner came out did I know-"
    
    " In other words, she pocketed it. Finders keepers, as they like to say."
    
    A "And then he chased you here?"
    
    show Azu P51 at center
    
    Az" Nope."
    A" … you were running, you know."
    
    show Azu P53 at center
    
    Az" Just as a precaution."
    
    " A wasted precaution, I think. Knowing our dear Uncle Ascenderos... it isn't like him to keep track of his inventory. "
    " Maybe Azzurra is the only person in this whole city who'd be running like mad for fear of him."
    " But then again..."


#//Màn hình nảy lên
    with sshake
    
    A" That is still stealing! Give it back!"
    
    show Azu P59 at center
    
    Az" No no no! I'm still reading!"
    A" Then finish it and then give it back."
    
    show Azu P59_1 at center
    
    Az" Nope! I have to reread too!"
    A" Are you going to give it back or not?"
    
    show Azu P19 at center
    
    Az" Hey. For you."
    
    " Azzurra whips out a piece of paper, weathered and yellowed, from the pages of the book."
    
    A" And this is?"
    
    show Azu P12 at center
    
    Az" Look!"

    " The writing is legible still – aside from a few parts eaten by termites, it is quite obviously a love poem."

#Cảnh: đen

    scene black with dissolve

#//Hiện chữ trắng trên nền cảnh đen
#//NVL
    stop music fadeout 1
    
    play music "Soundtracks/016 - Winter when i can_t see you.mp3" fadein 2.0
    nvl_Center"“O nightingale so feeble,"
    nvl_Center"Binding my soul through threads of silk"
    nvl_Center"Boiling my heart in a crucible of love,"
    nvl_Center"Made of purity and *** unmarred."
    nvl_Center"O nightingale so beauteous!"
    nvl_Center"Let my garden host your wings!"
    nvl_Center"Yours, my heart crimson-gold"
    nvl_Center"Like flowers red, like lions bold."
    nvl_Center"O nightingale so gentle,"
    nvl_Center"Make no excuse, me, your devoted."
    nvl_Center"Though vagarious, let fate not bridle"
    nvl_Center"The oak and the ??? that is yours…"

    nvl_Center" Giovanni de’Rovere"

    nvl clear
#------------------------------------------------
#******************”
#// Giovanni de’Rovere
#//tím
#Cảnh: công viên
#Thời gian: chiều
    stop music fadeout 1
    play music "Soundtracks/022 - Skipping.mp3" fadein 2.0
    scene BG_6 with dissolve

    show Azu P40 at center
    
    Az" It has to be a serenade, from a poor man to a princess or something."
    A" Well it just sounds creepy to me."
    
    show Azu P39 at center
    
    Az" Don't you have a single romantic bone in your body, Anatolio?"
    
    show Azu P42 at center
    
    Az" It's obviously a love poem! Nightingale wings, and giving up one's heart too!"
    
    show Azu P41 at center
    
    Az" I... I just love romances that transcend the class barrier. Like Cinderella, or the Frog Prince, or even Don Quichotte! It's awesome to have poor people who are, well... awesome!"
    
    show Azu P40 at center
    
    Az" I'm just wondering if there will be any gallant prince on a white courser who'd gladly lay bare his heart for me?"

    " I can't help but wonder, what does a silly knightly wannabe charging a windmill have to do with class-transcending romances?"

    A" Hey, don't look at me like that. I have absolutely nothing to do with this-"

#//Azzurra liếc

    A" Azzurra. That's a dangerously overimaginative thinking you're having."
    
    show Azu P26_1 at center
    
    Az" How so?"
    A" To be honest? These sounds to me like a powerful tyrant forcing a maiden to marry him. "
    A" Nothing in this text says anything about a poor man. Nope. Zilch. Nada."

    " The strong words and bloody imageries in this here text do not sit well with me. Spine-chilling."

    show Azu P29 at center
    
    Az" Hmm... that makes sense. A good theory, too."
    A" Theory? I'm certain this is what it is. Believe it or not."
    
    show Azu P27 at center
    
    Az" So... not a romance worthy of songs and art?"
    A" Nope."
    
    show Azu P51 at center
    
    Az" Not a timeless love between a poor peasant and a princess?"
    A" Most certainly not."

    " Azzurra bites her nails. She tends to do that whenever she realizes she'd done something positively ridiculous."
    " I sniffed the yellowed sheet."

    A" It's not even old paper. Sure it might be a little weathered and beaten now, but this is some good paper. Also there's this seal."
    
    show Azu P52 at center
    
    Az" Uh huh-"

    " The sheet was pressed between the pages, but it is obvious the paper could not have been more than a couple decades old. The seal was smudged, but there is something oddly familiar in it."

    A" Aaaaanyway, don't just go about changing the topic like that!"
    A" Are you returning the book or not?"

    " If bad would come to worse, I can afford to pay for the book for her, but that would set a really bad precedent. "
    " The girl needs a lesson."

    show Azu P59 at center
    
    Az" Not gonna! He's such a scary man!"

    " There's the reason I'm looking for. And that's perfectly o-kay."

    A" I'll come with you."
    
    show Azu P49 at center
    
    Az" No, no, no, no!"

#//Màn hình nảy lên.
    with sshake
    show Azu P31_1 at center
    
    Az" I... I gave this book a purpose! Isn't that better than letting it sit there in the storeroom for all eternity?"
    A" The end doesn't justify the means, dear. Give it back."
    
    show Azu P25 at center
    
    Az" Not gonna."
    A" I'll have to use force."
    
    show Azu P24 at center
    
    Az" Go ahead!"
    A" Give me the book!!!!"

#//Màn hình rung lắc mạnh trong ít nhất 10s
    with sshake3
    show Azu P12 at center
    
    Az" No no no no noooo!!!!!!"

    " Not giving up, are you?"
    " Well, your fault. I'll have to..."

    return