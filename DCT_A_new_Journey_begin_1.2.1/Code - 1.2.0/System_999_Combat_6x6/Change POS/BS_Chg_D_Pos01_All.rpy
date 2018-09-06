
label BS_Chg_D_Pos01_02:
    $ D_S1_CanAct = 0
    call BS_Chg_D_UntPos01_02
    call BS_Chg_D_LedPos01_02
    call BS_Chg_D_UntStoreSklSlt01_02
    call BS_Update_D_S1_MaxExp
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

label BS_Chg_D_Pos01_03:
    $ D_S1_CanAct = 0
    call BS_Chg_D_UntPos01_03
    call BS_Chg_D_LedPos01_03
    call BS_Chg_D_UntStoreSklSlt01_03
    call BS_Update_D_S1_MaxExp
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

label BS_Chg_D_Pos01_04:
    $ D_S1_CanAct = 0
    call BS_Chg_D_UntPos01_04
    call BS_Chg_D_LedPos01_04
    call BS_Chg_D_UntStoreSklSlt01_04
    call BS_Update_D_S1_MaxExp
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

label BS_Chg_D_Pos01_05:
    $ D_S1_CanAct = 0
    call BS_Chg_D_UntPos01_05
    call BS_Chg_D_LedPos01_05
    call BS_Chg_D_UntStoreSklSlt01_05
    call BS_Update_D_S1_MaxExp
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

label BS_Chg_D_Pos01_06:
    $ D_S1_CanAct = 0
    call BS_Chg_D_UntPos01_06
    call BS_Chg_D_LedPos01_06
    call BS_Chg_D_UntStoreSklSlt01_06
    call BS_Update_D_S1_MaxExp
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

