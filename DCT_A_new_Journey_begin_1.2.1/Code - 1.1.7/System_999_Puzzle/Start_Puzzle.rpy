init:
    define PS_PiecePicked = 0

    define PS_S_00 = 0
    define PS_S_11 = 1
    define PS_S_12 = 2
    define PS_S_13 = 3
    define PS_S_21 = 4
    define PS_S_22 = 5
    define PS_S_23 = 6
    define PS_S_31 = 7
    define PS_S_32 = 8
    define PS_S_33 = 9
    define PS_S_41 = 10
    define PS_S_42 = 11
    define PS_S_43 = 12

    $ PS_S_00_Picked = SetVariable ("PS_PiecePicked","PS_S_00"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")
    $ PS_S_11_Picked = SetVariable ("PS_PiecePicked","PS_S_11"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked") 
    $ PS_S_12_Picked = SetVariable ("PS_PiecePicked","PS_S_12"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")
    $ PS_S_13_Picked = SetVariable ("PS_PiecePicked","PS_S_13"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")
    $ PS_S_21_Picked = SetVariable ("PS_PiecePicked","PS_S_21"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")
    $ PS_S_22_Picked = SetVariable ("PS_PiecePicked","PS_S_22"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")
    $ PS_S_23_Picked = SetVariable ("PS_PiecePicked","PS_S_23"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")
    $ PS_S_31_Picked = SetVariable ("PS_PiecePicked","PS_S_31"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")
    $ PS_S_32_Picked = SetVariable ("PS_PiecePicked","PS_S_32"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")
    $ PS_S_33_Picked = SetVariable ("PS_PiecePicked","PS_S_33"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")
    $ PS_S_41_Picked = SetVariable ("PS_PiecePicked","PS_S_41"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")
    $ PS_S_42_Picked = SetVariable ("PS_PiecePicked","PS_S_42"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")
    $ PS_S_43_Picked = SetVariable ("PS_PiecePicked","PS_S_43"), Hide ("PS_Scr_PickPuzzle"), Jump ("PS_Chk_PiecePicked")

label Start_Puzzle:
    show screen PS_Scr_PickPuzzle
    $ renpy.pause (hard=True)
    return

label PS_Chk_PiecePicked:
#-----------------------------------------------------
    if PS_PiecePicked == "PS_S_00":
        if PS_S_11 == 0:
            $ PS_S_11 = PS_S_00
            $ PS_S_00 = 0

    elif PS_PiecePicked == "PS_S_11":
        if PS_S_00 == 0:
            $ PS_S_00 = PS_S_11
            $ PS_S_11 = 0
        elif PS_S_12 == 0:
            $ PS_S_12 = PS_S_11
            $ PS_S_11 = 0
        elif PS_S_21 == 0:
            $ PS_S_21 = PS_S_11
            $ PS_S_11 = 0

    elif PS_PiecePicked == "PS_S_12":
        if PS_S_11 == 0:
            $ PS_S_11 = PS_S_12
            $ PS_S_12 = 0
        elif PS_S_13 == 0:
            $ PS_S_13 = PS_S_12
            $ PS_S_12 = 0
        elif PS_S_22 == 0:
            $ PS_S_22 = PS_S_12
            $ PS_S_12 = 0

    elif PS_PiecePicked == "PS_S_13":
        if PS_S_12 == 0:
            $ PS_S_12 = PS_S_13
            $ PS_S_13 = 0
        elif PS_S_23 == 0:
            $ PS_S_23 = PS_S_13
            $ PS_S_13 = 0
#-----------------------------------------------------
    elif PS_PiecePicked == "PS_S_21":
        if PS_S_11 == 0:
            $ PS_S_11 = PS_S_21
            $ PS_S_21 = 0
        elif PS_S_22 == 0:
            $ PS_S_22 = PS_S_21
            $ PS_S_21 = 0
        elif PS_S_31 == 0:
            $ PS_S_31 = PS_S_21
            $ PS_S_21 = 0

    elif PS_PiecePicked == "PS_S_22":
        if PS_S_12 == 0:
            $ PS_S_12 = PS_S_22
            $ PS_S_22 = 0
        elif PS_S_21 == 0:
            $ PS_S_21 = PS_S_22
            $ PS_S_22 = 0
        elif PS_S_23 == 0:
            $ PS_S_23 = PS_S_22
            $ PS_S_22 = 0
        elif PS_S_32 == 0:
            $ PS_S_32 = PS_S_22
            $ PS_S_22 = 0

    elif PS_PiecePicked == "PS_S_23":
        if PS_S_13 == 0:
            $ PS_S_13 = PS_S_23
            $ PS_S_23 = 0
        elif PS_S_22 == 0:
            $ PS_S_22 = PS_S_23
            $ PS_S_23 = 0
        elif PS_S_33 == 0:
            $ PS_S_33 = PS_S_23
            $ PS_S_23 = 0
#-----------------------------------------------------
    elif PS_PiecePicked == "PS_S_31":
        if PS_S_21 == 0:
            $ PS_S_21 = PS_S_31
            $ PS_S_31 = 0
        elif PS_S_32 == 0:
            $ PS_S_32 = PS_S_31
            $ PS_S_31 = 0
        elif PS_S_41 == 0:
            $ PS_S_41 = PS_S_31
            $ PS_S_31 = 0

    elif PS_PiecePicked == "PS_S_32":
        if PS_S_22 == 0:
            $ PS_S_22 = PS_S_32
            $ PS_S_32 = 0
        elif PS_S_31 == 0:
            $ PS_S_31 = PS_S_32
            $ PS_S_32 = 0
        elif PS_S_33 == 0:
            $ PS_S_33 = PS_S_32
            $ PS_S_32 = 0
        elif PS_S_42 == 0:
            $ PS_S_42 = PS_S_32
            $ PS_S_32 = 0

    elif PS_PiecePicked == "PS_S_33":
        if PS_S_23 == 0:
            $ PS_S_23 = PS_S_33
            $ PS_S_33 = 0
        elif PS_S_32 == 0:
            $ PS_S_32 = PS_S_33
            $ PS_S_33 = 0
        elif PS_S_43 == 0:
            $ PS_S_43 = PS_S_33
            $ PS_S_33 = 0
#-----------------------------------------------------
    elif PS_PiecePicked == "PS_S_41":
        if PS_S_31 == 0:
            $ PS_S_31 = PS_S_41
            $ PS_S_41 = 0
        elif PS_S_42 == 0:
            $ PS_S_42 = PS_S_41
            $ PS_S_41 = 0

    elif PS_PiecePicked == "PS_S_42":
        if PS_S_41 == 0:
            $ PS_S_41 = PS_S_42
            $ PS_S_42 = 0
        elif PS_S_32 == 0:
            $ PS_S_32 = PS_S_42
            $ PS_S_42 = 0
        elif PS_S_43 == 0:
            $ PS_S_43 = PS_S_42
            $ PS_S_42 = 0

    elif PS_PiecePicked == "PS_S_43":
        if PS_S_33 == 0:
            $ PS_S_33 = PS_S_43
            $ PS_S_43 = 0
        elif PS_S_42 == 0:
            $ PS_S_42 = PS_S_43
            $ PS_S_43 = 0

    jump Start_Puzzle

screen PS_Scr_PickPuzzle:
    textbutton "{size=40}[PS_S_00]{/size}" action PS_S_00_Picked align (0.1,0.1)
    textbutton "{size=40}[PS_S_11]{/size}" action PS_S_11_Picked align (0.2,0.1)
    textbutton "{size=40}[PS_S_12]{/size}" action PS_S_12_Picked align (0.2,0.2)
    textbutton "{size=40}[PS_S_13]{/size}" action PS_S_13_Picked align (0.2,0.3)
    textbutton "{size=40}[PS_S_21]{/size}" action PS_S_21_Picked align (0.3,0.1)
    textbutton "{size=40}[PS_S_22]{/size}" action PS_S_22_Picked align (0.3,0.2)
    textbutton "{size=40}[PS_S_23]{/size}" action PS_S_23_Picked align (0.3,0.3)
    textbutton "{size=40}[PS_S_31]{/size}" action PS_S_31_Picked align (0.4,0.1)
    textbutton "{size=40}[PS_S_32]{/size}" action PS_S_32_Picked align (0.4,0.2)
    textbutton "{size=40}[PS_S_33]{/size}" action PS_S_33_Picked align (0.4,0.3)
    textbutton "{size=40}[PS_S_41]{/size}" action PS_S_41_Picked align (0.5,0.1)
    textbutton "{size=40}[PS_S_42]{/size}" action PS_S_42_Picked align (0.5,0.2)
    textbutton "{size=40}[PS_S_43]{/size}" action PS_S_43_Picked align (0.5,0.3)