
label BS_Chg_D_Pos05_01:
    $ D_S5_CanAct = 0
    call BS_Chg_D_UntPos05_01
    call BS_Chg_D_LedPos05_01
    call BS_Chg_D_UntStoreSklSlt05_01
    call BS_Update_D_S5_MaxExp
    call BS_Update_D_S1_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

label BS_Chg_D_Pos05_02:
    $ D_S5_CanAct = 0
    call BS_Chg_D_UntPos05_02
    call BS_Chg_D_LedPos05_02
    call BS_Chg_D_UntStoreSklSlt05_02
    call BS_Update_D_S5_MaxExp
    call BS_Update_D_S2_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

label BS_Chg_D_Pos05_03:
    $ D_S5_CanAct = 0
    call BS_Chg_D_UntPos05_03
    call BS_Chg_D_LedPos05_03
    call BS_Chg_D_UntStoreSklSlt05_03
    call BS_Update_D_S5_MaxExp
    call BS_Update_D_S3_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

label BS_Chg_D_Pos05_04:
    $ D_S5_CanAct = 0
    call BS_Chg_D_UntPos05_04
    call BS_Chg_D_LedPos05_04
    call BS_Chg_D_UntStoreSklSlt05_04
    call BS_Update_D_S5_MaxExp
    call BS_Update_D_S4_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

label BS_Chg_D_Pos05_06:
    $ D_S5_CanAct = 0
    call BS_Chg_D_UntPos05_06
    call BS_Chg_D_LedPos05_06
    call BS_Chg_D_UntStoreSklSlt05_06
    call BS_Update_D_S5_MaxExp
    call BS_Update_D_S6_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

