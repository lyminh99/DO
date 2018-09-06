# The game starts here. Phần test các công cụ screen
label Sys_SMM_Storyline_VN:

    if Sys_SkipAll == 0:
        #play music "Soundtracks/Piano tragic part1.ogg"
        #play music "Soundtracks/Piano tragic part2.ogg"
        play music ["Soundtracks/Piano tragic part1.ogg", "Soundtracks/Piano tragic part2.ogg", "Soundtracks/Piano tragic part2.ogg"] 

        call  SMM_Chapter_000_The_Prologue_p1
        call  SMM_Chapter_000_The_Prologue_p2
        call  SMM_Chapter_001 
        call  SMM_Chapter_002
        call  SMM_Chapter_003
        call  SMM_Chapter_004
    #    call  SMM_Chapter_006
        
    return