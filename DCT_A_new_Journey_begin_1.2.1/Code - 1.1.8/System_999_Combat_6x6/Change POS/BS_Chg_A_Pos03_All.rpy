
label BS_Chg_A_Pos03_01:
    $ A_S3_CanAct = 0
    call BS_Chg_A_UntPos03_01
    call BS_Chg_A_LedPos03_01
    call BS_Chg_A_UntStoreSklSlt03_01
    call BS_Update_A_S3_MaxExp
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

label BS_Chg_A_Pos03_02:
    $ A_S3_CanAct = 0
    call BS_Chg_A_UntPos03_02
    call BS_Chg_A_LedPos03_02
    call BS_Chg_A_UntStoreSklSlt03_02
    call BS_Update_A_S3_MaxExp
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

label BS_Chg_A_Pos03_04:
    $ A_S3_CanAct = 0
    call BS_Chg_A_UntPos03_04
    call BS_Chg_A_LedPos03_04
    call BS_Chg_A_UntStoreSklSlt03_04
    call BS_Update_A_S3_MaxExp
    call BS_Update_A_S4_MaxExp
    if BS_WhatKindOfChgPOS == "AI_ChgPOS" or BS_WhatKindOfChgPOS == 0:
        return
    elif BS_WhatKindOfChgPOS == "PI_ChgPOS":
        jump BS_Chk_WhoAct
    elif BS_WhatKindOfChgPOS == "BM_PI_ChgPOS":
        jump BM_Start
    else:
        e "Error: Change POS behavior, Who control = None"
        $ renpy.pause (hard=True)

label BS_Chg_A_Pos03_05:
    $ A_S3_CanAct = 0
    call BS_Chg_A_UntPos03_05
    call BS_Chg_A_LedPos03_05
    call BS_Chg_A_UntStoreSklSlt03_05
    call BS_Update_A_S3_MaxExp
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

label BS_Chg_A_Pos03_06:
    $ A_S3_CanAct = 0
    call BS_Chg_A_UntPos03_06
    call BS_Chg_A_LedPos03_06
    call BS_Chg_A_UntStoreSklSlt03_06
    call BS_Update_A_S3_MaxExp
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

