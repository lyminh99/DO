
screen SQ_Keymap():

    tag menu
    modal True

    key "K_LEFT"            action SQ_LEFT_Pressed
    key "repeat_K_LEFT"  action SQ_LEFT_Pressed

    key "K_RIGHT"           action SQ_RIGHT_Pressed
    key "repeat_K_RIGHT" action SQ_RIGHT_Pressed

    key "K_UP"                action SQ_UP_Pressed
    key "repeat_K_UP"      action SQ_UP_Pressed

    key "K_DOWN"           action SQ_DOWN_Pressed
    key "repeat_K_DOWN" action SQ_DOWN_Pressed

    key "e" action SQ_E_Pressed

screen Sys_SQ_Map:

    text "{size=20}N: [SQ_Character.N]{/size}" align (0.85 ,0.05)
    text "{size=20}S: [SQ_Character.S]{/size}" align (0.85 ,0.35)
    text "{size=20}W: [SQ_Character.W]{/size}" align (0.75 ,0.2)
    text "{size=20}E: [SQ_Character.E]{/size}" align (0.950 ,0.2)

    text "{size=20}([SQ_Character.X]-[SQ_Character.Y]){/size}" align (0.85 ,0.2)
    text "{size=20}([SQ_Store_Character_X]-[SQ_Store_Character_Y]){/size}" align (0.85 ,0.5)
    text "{size=20}next tile: ([SQ_PredictTile]){/size}" align (0.85 ,0.6)
    text "{size=20}[SQ_Move]{/size}" align (0.85 ,0.7)

    text "{size=20}[SQ_01.Type]{/size}" pos (SQ_Pos_Col00 ,SQ_Pos_Row01)
    text "{size=20}[SQ_02.Type]{/size}" pos (SQ_Pos_Col00 ,SQ_Pos_Row02)
    text "{size=20}[SQ_03.Type]{/size}" pos (SQ_Pos_Col00 ,SQ_Pos_Row03)
    text "{size=20}[SQ_04.Type]{/size}" pos (SQ_Pos_Col00 ,SQ_Pos_Row04)
    text "{size=20}[SQ_05.Type]{/size}" pos (SQ_Pos_Col00 ,SQ_Pos_Row05)
    text "{size=20}[SQ_06.Type]{/size}" pos (SQ_Pos_Col00 ,SQ_Pos_Row06)
    text "{size=20}[SQ_07.Type]{/size}" pos (SQ_Pos_Col00 ,SQ_Pos_Row07)
    text "{size=20}[SQ_08.Type]{/size}" pos (SQ_Pos_Col00 ,SQ_Pos_Row08)
    text "{size=20}[SQ_09.Type]{/size}" pos (SQ_Pos_Col00 ,SQ_Pos_Row09)

    text "{size=20}[SQ_10.Type]{/size}" pos (SQ_Pos_Col01 ,SQ_Pos_Row00)
    text "{size=20}[SQ_20.Type]{/size}" pos (SQ_Pos_Col02 ,SQ_Pos_Row00)
    text "{size=20}[SQ_30.Type]{/size}" pos (SQ_Pos_Col03 ,SQ_Pos_Row00)
    text "{size=20}[SQ_40.Type]{/size}" pos (SQ_Pos_Col04 ,SQ_Pos_Row00)
    text "{size=20}[SQ_50.Type]{/size}" pos (SQ_Pos_Col05 ,SQ_Pos_Row00)
    text "{size=20}[SQ_60.Type]{/size}" pos (SQ_Pos_Col06 ,SQ_Pos_Row00)
    text "{size=20}[SQ_70.Type]{/size}" pos (SQ_Pos_Col07 ,SQ_Pos_Row00)
    text "{size=20}[SQ_80.Type]{/size}" pos (SQ_Pos_Col08 ,SQ_Pos_Row00)
    text "{size=20}[SQ_90.Type]{/size}" pos (SQ_Pos_Col09 ,SQ_Pos_Row00)

    text "{size=20}[SQ_11.Type]{/size}" pos (SQ_Pos_Col01 ,SQ_Pos_Row01)
    text "{size=20}[SQ_12.Type]{/size}" pos (SQ_Pos_Col01 ,SQ_Pos_Row02)
    text "{size=20}[SQ_13.Type]{/size}" pos (SQ_Pos_Col01 ,SQ_Pos_Row03)
    text "{size=20}[SQ_14.Type]{/size}" pos (SQ_Pos_Col01 ,SQ_Pos_Row04)
    text "{size=20}[SQ_15.Type]{/size}" pos (SQ_Pos_Col01 ,SQ_Pos_Row05)
    text "{size=20}[SQ_16.Type]{/size}" pos (SQ_Pos_Col01 ,SQ_Pos_Row06)
    text "{size=20}[SQ_17.Type]{/size}" pos (SQ_Pos_Col01 ,SQ_Pos_Row07)
    text "{size=20}[SQ_18.Type]{/size}" pos (SQ_Pos_Col01 ,SQ_Pos_Row08)
    text "{size=20}[SQ_19.Type]{/size}" pos (SQ_Pos_Col01 ,SQ_Pos_Row09)

    text "{size=20}[SQ_21.Type]{/size}" pos (SQ_Pos_Col02 ,SQ_Pos_Row01)
    text "{size=20}[SQ_22.Type]{/size}" pos (SQ_Pos_Col02 ,SQ_Pos_Row02)
    text "{size=20}[SQ_23.Type]{/size}" pos (SQ_Pos_Col02 ,SQ_Pos_Row03)
    text "{size=20}[SQ_24.Type]{/size}" pos (SQ_Pos_Col02 ,SQ_Pos_Row04)
    text "{size=20}[SQ_25.Type]{/size}" pos (SQ_Pos_Col02 ,SQ_Pos_Row05)
    text "{size=20}[SQ_26.Type]{/size}" pos (SQ_Pos_Col02 ,SQ_Pos_Row06)
    text "{size=20}[SQ_27.Type]{/size}" pos (SQ_Pos_Col02 ,SQ_Pos_Row07)
    text "{size=20}[SQ_28.Type]{/size}" pos (SQ_Pos_Col02 ,SQ_Pos_Row08)
    text "{size=20}[SQ_29.Type]{/size}" pos (SQ_Pos_Col02 ,SQ_Pos_Row09)

    text "{size=20}[SQ_31.Type]{/size}" pos (SQ_Pos_Col03 ,SQ_Pos_Row01)
    text "{size=20}[SQ_32.Type]{/size}" pos (SQ_Pos_Col03 ,SQ_Pos_Row02)
    text "{size=20}[SQ_33.Type]{/size}" pos (SQ_Pos_Col03 ,SQ_Pos_Row03)
    text "{size=20}[SQ_34.Type]{/size}" pos (SQ_Pos_Col03 ,SQ_Pos_Row04)
    text "{size=20}[SQ_35.Type]{/size}" pos (SQ_Pos_Col03 ,SQ_Pos_Row05)
    text "{size=20}[SQ_36.Type]{/size}" pos (SQ_Pos_Col03 ,SQ_Pos_Row06)
    text "{size=20}[SQ_37.Type]{/size}" pos (SQ_Pos_Col03 ,SQ_Pos_Row07)
    text "{size=20}[SQ_38.Type]{/size}" pos (SQ_Pos_Col03 ,SQ_Pos_Row08)
    text "{size=20}[SQ_39.Type]{/size}" pos (SQ_Pos_Col03 ,SQ_Pos_Row09)

    text "{size=20}[SQ_41.Type]{/size}" pos (SQ_Pos_Col04 ,SQ_Pos_Row01)
    text "{size=20}[SQ_42.Type]{/size}" pos (SQ_Pos_Col04 ,SQ_Pos_Row02)
    text "{size=20}[SQ_43.Type]{/size}" pos (SQ_Pos_Col04 ,SQ_Pos_Row03)
    text "{size=20}[SQ_44.Type]{/size}" pos (SQ_Pos_Col04 ,SQ_Pos_Row04)
    text "{size=20}[SQ_45.Type]{/size}" pos (SQ_Pos_Col04 ,SQ_Pos_Row05)
    text "{size=20}[SQ_46.Type]{/size}" pos (SQ_Pos_Col04 ,SQ_Pos_Row06)
    text "{size=20}[SQ_47.Type]{/size}" pos (SQ_Pos_Col04 ,SQ_Pos_Row07)
    text "{size=20}[SQ_48.Type]{/size}" pos (SQ_Pos_Col04 ,SQ_Pos_Row08)
    text "{size=20}[SQ_49.Type]{/size}" pos (SQ_Pos_Col04 ,SQ_Pos_Row09)

    text "{size=20}[SQ_51.Type]{/size}" pos (SQ_Pos_Col05 ,SQ_Pos_Row01)
    text "{size=20}[SQ_52.Type]{/size}" pos (SQ_Pos_Col05 ,SQ_Pos_Row02)
    text "{size=20}[SQ_53.Type]{/size}" pos (SQ_Pos_Col05 ,SQ_Pos_Row03)
    text "{size=20}[SQ_54.Type]{/size}" pos (SQ_Pos_Col05 ,SQ_Pos_Row04)
    text "{size=20}[SQ_55.Type]{/size}" pos (SQ_Pos_Col05 ,SQ_Pos_Row05)
    text "{size=20}[SQ_56.Type]{/size}" pos (SQ_Pos_Col05 ,SQ_Pos_Row06)
    text "{size=20}[SQ_57.Type]{/size}" pos (SQ_Pos_Col05 ,SQ_Pos_Row07)
    text "{size=20}[SQ_58.Type]{/size}" pos (SQ_Pos_Col05 ,SQ_Pos_Row08)
    text "{size=20}[SQ_59.Type]{/size}" pos (SQ_Pos_Col05 ,SQ_Pos_Row09)

    text "{size=20}[SQ_61.Type]{/size}" pos (SQ_Pos_Col06 ,SQ_Pos_Row01)
    text "{size=20}[SQ_62.Type]{/size}" pos (SQ_Pos_Col06 ,SQ_Pos_Row02)
    text "{size=20}[SQ_63.Type]{/size}" pos (SQ_Pos_Col06 ,SQ_Pos_Row03)
    text "{size=20}[SQ_64.Type]{/size}" pos (SQ_Pos_Col06 ,SQ_Pos_Row04)
    text "{size=20}[SQ_65.Type]{/size}" pos (SQ_Pos_Col06 ,SQ_Pos_Row05)
    text "{size=20}[SQ_66.Type]{/size}" pos (SQ_Pos_Col06 ,SQ_Pos_Row06)
    text "{size=20}[SQ_67.Type]{/size}" pos (SQ_Pos_Col06 ,SQ_Pos_Row07)
    text "{size=20}[SQ_68.Type]{/size}" pos (SQ_Pos_Col06 ,SQ_Pos_Row08)
    text "{size=20}[SQ_69.Type]{/size}" pos (SQ_Pos_Col06 ,SQ_Pos_Row09)

    text "{size=20}[SQ_71.Type]{/size}" pos (SQ_Pos_Col07 ,SQ_Pos_Row01)
    text "{size=20}[SQ_72.Type]{/size}" pos (SQ_Pos_Col07 ,SQ_Pos_Row02)
    text "{size=20}[SQ_73.Type]{/size}" pos (SQ_Pos_Col07 ,SQ_Pos_Row03)
    text "{size=20}[SQ_74.Type]{/size}" pos (SQ_Pos_Col07 ,SQ_Pos_Row04)
    text "{size=20}[SQ_75.Type]{/size}" pos (SQ_Pos_Col07 ,SQ_Pos_Row05)
    text "{size=20}[SQ_76.Type]{/size}" pos (SQ_Pos_Col07 ,SQ_Pos_Row06)
    text "{size=20}[SQ_77.Type]{/size}" pos (SQ_Pos_Col07 ,SQ_Pos_Row07)
    text "{size=20}[SQ_78.Type]{/size}" pos (SQ_Pos_Col07 ,SQ_Pos_Row08)
    text "{size=20}[SQ_79.Type]{/size}" pos (SQ_Pos_Col07 ,SQ_Pos_Row09)

    text "{size=20}[SQ_81.Type]{/size}" pos (SQ_Pos_Col08 ,SQ_Pos_Row01)
    text "{size=20}[SQ_82.Type]{/size}" pos (SQ_Pos_Col08 ,SQ_Pos_Row02)
    text "{size=20}[SQ_83.Type]{/size}" pos (SQ_Pos_Col08 ,SQ_Pos_Row03)
    text "{size=20}[SQ_84.Type]{/size}" pos (SQ_Pos_Col08 ,SQ_Pos_Row04)
    text "{size=20}[SQ_85.Type]{/size}" pos (SQ_Pos_Col08 ,SQ_Pos_Row05)
    text "{size=20}[SQ_86.Type]{/size}" pos (SQ_Pos_Col08 ,SQ_Pos_Row06)
    text "{size=20}[SQ_87.Type]{/size}" pos (SQ_Pos_Col08 ,SQ_Pos_Row07)
    text "{size=20}[SQ_88.Type]{/size}" pos (SQ_Pos_Col08 ,SQ_Pos_Row08)
    text "{size=20}[SQ_89.Type]{/size}" pos (SQ_Pos_Col08 ,SQ_Pos_Row09)

    text "{size=20}[SQ_91.Type]{/size}" pos (SQ_Pos_Col09 ,SQ_Pos_Row01)
    text "{size=20}[SQ_92.Type]{/size}" pos (SQ_Pos_Col09 ,SQ_Pos_Row02)
    text "{size=20}[SQ_93.Type]{/size}" pos (SQ_Pos_Col09 ,SQ_Pos_Row03)
    text "{size=20}[SQ_94.Type]{/size}" pos (SQ_Pos_Col09 ,SQ_Pos_Row04)
    text "{size=20}[SQ_95.Type]{/size}" pos (SQ_Pos_Col09 ,SQ_Pos_Row05)
    text "{size=20}[SQ_96.Type]{/size}" pos (SQ_Pos_Col09 ,SQ_Pos_Row06)
    text "{size=20}[SQ_97.Type]{/size}" pos (SQ_Pos_Col09 ,SQ_Pos_Row07)
    text "{size=20}[SQ_98.Type]{/size}" pos (SQ_Pos_Col09 ,SQ_Pos_Row08)
    text "{size=20}[SQ_99.Type]{/size}" pos (SQ_Pos_Col09 ,SQ_Pos_Row09)

screen Sys_SQ_CharMoving:
    text "{size=20}Screen Char Moving{/size}"
    text "{size=20}[SQ_Character.Name]{/size}" at Eft_Moving

screen Sys_SQ_CharPOS:
    text "{size=20}Screen CharPOS{/size}"
    text "{size=20}[SQ_Character.Name]{/size}" pos (SQ_Character.X ,SQ_Character.Y)
