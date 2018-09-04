######################################################################################
# The game starts here.
# Prologue 1.

label start:
    #jump ki1
    if (Force_end_7c == 0) and (
    Hopeless_Dream_End == 0) and (
    WAR_END_DEATH_OF_A_SPY == 0) and (
    WAR_END_REVOLUTION == 0) and (
    A_Rich_Happy_Family == 0):
        call Storyline from _call_Storyline

    $ Force_end_7c = 0
    $ True_end = 0
    $ Hopeless_Dream_End = 0
    $ WAR_END_DEATH_OF_A_SPY = 0
    $ WAR_END_REVOLUTION = 0
    $ A_Rich_Happy_Family = 0

    return