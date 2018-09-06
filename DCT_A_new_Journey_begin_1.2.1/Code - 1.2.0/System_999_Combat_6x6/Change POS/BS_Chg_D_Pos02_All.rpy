
label BS_Chg_D_Pos02_01:
    $ D_S2_CanAct = 0
    call BS_Chg_D_UntPos02_01
    call BS_Chg_D_LedPos02_01
    call BS_Chg_D_UntStoreSklSlt02_01
    call BS_Update_D_S2_MaxExp
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

label BS_Chg_D_Pos02_03:
    $ D_S2_CanAct = 0
    call BS_Chg_D_UntPos02_03
    call BS_Chg_D_LedPos02_03
    call BS_Chg_D_UntStoreSklSlt02_03
    call BS_Update_D_S2_MaxExp
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

label BS_Chg_D_Pos02_04:
    $ D_S2_CanAct = 0
    call BS_Chg_D_UntPos02_04
    call BS_Chg_D_LedPos02_04
    call BS_Chg_D_UntStoreSklSlt02_04
    call BS_Update_D_S2_MaxExp
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

label BS_Chg_D_Pos02_05:
    $ D_S2_CanAct = 0
    call BS_Chg_D_UntPos02_05
    call BS_Chg_D_LedPos02_05
    call BS_Chg_D_UntStoreSklSlt02_05
    call BS_Update_D_S2_MaxExp
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

label BS_Chg_D_Pos02_06:
    $ D_S2_CanAct = 0
    call BS_Chg_D_UntPos02_06
    call BS_Chg_D_LedPos02_06
    call BS_Chg_D_UntStoreSklSlt02_06
    call BS_Update_D_S2_MaxExp
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

