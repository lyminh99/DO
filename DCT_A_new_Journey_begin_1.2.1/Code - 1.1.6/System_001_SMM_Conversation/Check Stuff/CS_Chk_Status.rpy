
label CS_Chk_Status:

    if CS_Place == 1:
        $ CS_Staus = "High"
    elif CS_Place == 2:
        $ CS_Staus = "Med"
    elif CS_Place == 3:
        $ CS_Staus = "Low"

    return
