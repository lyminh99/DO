
label BS_Chg_D_Pos06_01:
    $ D_S6_CanAct = 0
    call BS_Chg_D_UntPos06_01
    call BS_Chg_D_LedPos06_01
    call BS_Chg_D_UntStoreSklSlt06_01
    call BS_Update_D_S6_MaxExp
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

label BS_Chg_D_Pos06_02:
    $ D_S6_CanAct = 0
    call BS_Chg_D_UntPos06_02
    call BS_Chg_D_LedPos06_02
    call BS_Chg_D_UntStoreSklSlt06_02
    call BS_Update_D_S6_MaxExp
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

label BS_Chg_D_Pos06_03:
    $ D_S6_CanAct = 0
    call BS_Chg_D_UntPos06_03
    call BS_Chg_D_LedPos06_03
    call BS_Chg_D_UntStoreSklSlt06_03
    call BS_Update_D_S6_MaxExp
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

label BS_Chg_D_Pos06_04:
    $ D_S6_CanAct = 0
    call BS_Chg_D_UntPos06_04
    call BS_Chg_D_LedPos06_04
    call BS_Chg_D_UntStoreSklSlt06_04
    call BS_Update_D_S6_MaxExp
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

label BS_Chg_D_Pos06_05:
    $ D_S6_CanAct = 0
    call BS_Chg_D_UntPos06_05
    call BS_Chg_D_LedPos06_05
    call BS_Chg_D_UntStoreSklSlt06_05
    call BS_Update_D_S6_MaxExp
    call BS_Update_D_S5_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

