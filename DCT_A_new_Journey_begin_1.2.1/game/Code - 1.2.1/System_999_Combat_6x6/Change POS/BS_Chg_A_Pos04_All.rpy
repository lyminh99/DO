
label BS_Chg_A_Pos04_01:
    $ A_S4_CanAct = 0
    call BS_Chg_A_UntPos04_01
    call BS_Chg_A_LedPos04_01
    call BS_Chg_A_UntStoreSklSlt04_01
    call BS_Update_A_S4_MaxExp
    call BS_Update_A_S1_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

label BS_Chg_A_Pos04_02:
    $ A_S4_CanAct = 0
    call BS_Chg_A_UntPos04_02
    call BS_Chg_A_LedPos04_02
    call BS_Chg_A_UntStoreSklSlt04_02
    call BS_Update_A_S4_MaxExp
    call BS_Update_A_S2_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

label BS_Chg_A_Pos04_03:
    $ A_S4_CanAct = 0
    call BS_Chg_A_UntPos04_03
    call BS_Chg_A_LedPos04_03
    call BS_Chg_A_UntStoreSklSlt04_03
    call BS_Update_A_S4_MaxExp
    call BS_Update_A_S3_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

label BS_Chg_A_Pos04_05:
    $ A_S4_CanAct = 0
    call BS_Chg_A_UntPos04_05
    call BS_Chg_A_LedPos04_05
    call BS_Chg_A_UntStoreSklSlt04_05
    call BS_Update_A_S4_MaxExp
    call BS_Update_A_S5_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

label BS_Chg_A_Pos04_06:
    $ A_S4_CanAct = 0
    call BS_Chg_A_UntPos04_06
    call BS_Chg_A_LedPos04_06
    call BS_Chg_A_UntStoreSklSlt04_06
    call BS_Update_A_S4_MaxExp
    call BS_Update_A_S6_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

