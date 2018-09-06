
label SQ_Load_BasicSetting:

    $ config.keymap['dismiss'].append('e')

    define SQ_TileSpace = 50
    define SQ_StartX = 100
    define SQ_StartY = 100

    define SQ_Pos_Col00 = SQ_StartX - SQ_TileSpace
    define SQ_Pos_Col01 = SQ_StartX
    define SQ_Pos_Col02 = SQ_Pos_Col01 + SQ_TileSpace
    define SQ_Pos_Col03 = SQ_Pos_Col02 + SQ_TileSpace
    define SQ_Pos_Col04 = SQ_Pos_Col03 + SQ_TileSpace
    define SQ_Pos_Col05 = SQ_Pos_Col04 + SQ_TileSpace
    define SQ_Pos_Col06 = SQ_Pos_Col05 + SQ_TileSpace
    define SQ_Pos_Col07 = SQ_Pos_Col06 + SQ_TileSpace
    define SQ_Pos_Col08 = SQ_Pos_Col07 + SQ_TileSpace
    define SQ_Pos_Col09 = SQ_Pos_Col08 + SQ_TileSpace

    define SQ_Pos_Row00 = SQ_StartY - SQ_TileSpace
    define SQ_Pos_Row01 = SQ_StartY
    define SQ_Pos_Row02 = SQ_Pos_Row01 + SQ_TileSpace
    define SQ_Pos_Row03 = SQ_Pos_Row02 + SQ_TileSpace
    define SQ_Pos_Row04 = SQ_Pos_Row03 + SQ_TileSpace
    define SQ_Pos_Row05 = SQ_Pos_Row04 + SQ_TileSpace
    define SQ_Pos_Row06 = SQ_Pos_Row05 + SQ_TileSpace
    define SQ_Pos_Row07 = SQ_Pos_Row06 + SQ_TileSpace
    define SQ_Pos_Row08 = SQ_Pos_Row07 + SQ_TileSpace
    define SQ_Pos_Row09 = SQ_Pos_Row08 + SQ_TileSpace

    define Key_Pressed = 0
    define SQ_Exit = False
    define SQ_Move = 0
    define SQ_Moving_Time = 0.05
    define SQ_Char_Meet = 0
    define SQ_Store_Character_X = 0
    define SQ_Store_Character_Y = 0
    define SQ_PredictTile = 0

    $ SQ_LEFT_Pressed     = SetVariable ("Key_Pressed", "LEFT"),    Hide ("SQ_Keymap"), Jump ("Key_Pressed")
    $ SQ_RIGHT_Pressed   = SetVariable ("Key_Pressed", "RIGHT"),  Hide ("SQ_Keymap"), Jump ("Key_Pressed")
    $ SQ_UP_Pressed       = SetVariable ("Key_Pressed", "UP"),      Hide ("SQ_Keymap"), Jump ("Key_Pressed")
    $ SQ_DOWN_Pressed  = SetVariable ("Key_Pressed", "DOWN"), Hide ("SQ_Keymap"), Jump ("Key_Pressed")
    $ SQ_E_Pressed        = SetVariable ("Key_Pressed", "E"),       Hide ("SQ_Keymap"), Jump ("Key_Pressed")

    python:

        class SQ_CharPOS:
            def __init__ (self,Name, Pos_X, Pos_Y, North, South, West, East):
                self.Name =  Name
                self.X = Pos_X
                self.Y = Pos_Y
                self.N = North
                self.S = South
                self.W = West
                self.E = East

        class SQ_Tiles:
            def __init__ (self, Tile_X, Tile_Y, Type):
                self.X = Tile_X
                self.Y = Tile_Y
                self.Type = Type

                
        SQ_Character = SQ_CharPOS("Char" ,SQ_Pos_Col01 ,SQ_Pos_Row01 , 0, 0, 0, 0)

        SQ_01 = SQ_Tiles (SQ_Pos_Col00,SQ_Pos_Row01,"...")
        SQ_02 = SQ_Tiles (SQ_Pos_Col00,SQ_Pos_Row02,"...")
        SQ_03 = SQ_Tiles (SQ_Pos_Col00,SQ_Pos_Row03,"...")
        SQ_04 = SQ_Tiles (SQ_Pos_Col00,SQ_Pos_Row04,"...")
        SQ_05 = SQ_Tiles (SQ_Pos_Col00,SQ_Pos_Row05,"...")
        SQ_06 = SQ_Tiles (SQ_Pos_Col00,SQ_Pos_Row06,"...")
        SQ_07 = SQ_Tiles (SQ_Pos_Col00,SQ_Pos_Row07,"...")
        SQ_08 = SQ_Tiles (SQ_Pos_Col00,SQ_Pos_Row08,"...")
        SQ_09 = SQ_Tiles (SQ_Pos_Col00,SQ_Pos_Row09,"...")

        SQ_10 = SQ_Tiles (SQ_Pos_Col01,SQ_Pos_Row00,"...")
        SQ_20 = SQ_Tiles (SQ_Pos_Col02,SQ_Pos_Row00,"...")
        SQ_30 = SQ_Tiles (SQ_Pos_Col03,SQ_Pos_Row00,"...")
        SQ_40 = SQ_Tiles (SQ_Pos_Col04,SQ_Pos_Row00,"...")
        SQ_50 = SQ_Tiles (SQ_Pos_Col05,SQ_Pos_Row00,"...")
        SQ_60 = SQ_Tiles (SQ_Pos_Col06,SQ_Pos_Row00,"...")
        SQ_70 = SQ_Tiles (SQ_Pos_Col07,SQ_Pos_Row00,"...")
        SQ_80 = SQ_Tiles (SQ_Pos_Col08,SQ_Pos_Row00,"...")
        SQ_90 = SQ_Tiles (SQ_Pos_Col09,SQ_Pos_Row00,"...")

        SQ_11 = SQ_Tiles (SQ_Pos_Col01,SQ_Pos_Row01,"...")
        SQ_12 = SQ_Tiles (SQ_Pos_Col01,SQ_Pos_Row02,"...")
        SQ_13 = SQ_Tiles (SQ_Pos_Col01,SQ_Pos_Row03,"...")
        SQ_14 = SQ_Tiles (SQ_Pos_Col01,SQ_Pos_Row04,"...")
        SQ_15 = SQ_Tiles (SQ_Pos_Col01,SQ_Pos_Row05,"...")
        SQ_16 = SQ_Tiles (SQ_Pos_Col01,SQ_Pos_Row06,"...")
        SQ_17 = SQ_Tiles (SQ_Pos_Col01,SQ_Pos_Row07,"...")
        SQ_18 = SQ_Tiles (SQ_Pos_Col01,SQ_Pos_Row08,"...")
        SQ_19 = SQ_Tiles (SQ_Pos_Col01,SQ_Pos_Row09,"...")

        SQ_21 = SQ_Tiles (SQ_Pos_Col02,SQ_Pos_Row01,"NPC")
        SQ_22 = SQ_Tiles (SQ_Pos_Col02,SQ_Pos_Row02,"...")
        SQ_23 = SQ_Tiles (SQ_Pos_Col02,SQ_Pos_Row03,"...")
        SQ_24 = SQ_Tiles (SQ_Pos_Col02,SQ_Pos_Row04,"...")
        SQ_25 = SQ_Tiles (SQ_Pos_Col02,SQ_Pos_Row05,"...")
        SQ_26 = SQ_Tiles (SQ_Pos_Col02,SQ_Pos_Row06,"...")
        SQ_27 = SQ_Tiles (SQ_Pos_Col02,SQ_Pos_Row07,"...")
        SQ_28 = SQ_Tiles (SQ_Pos_Col02,SQ_Pos_Row08,"...")
        SQ_29 = SQ_Tiles (SQ_Pos_Col02,SQ_Pos_Row09,"...")

        SQ_31 = SQ_Tiles (SQ_Pos_Col03,SQ_Pos_Row01,"...")
        SQ_32 = SQ_Tiles (SQ_Pos_Col03,SQ_Pos_Row02,"...")
        SQ_33 = SQ_Tiles (SQ_Pos_Col03,SQ_Pos_Row03,"...")
        SQ_34 = SQ_Tiles (SQ_Pos_Col03,SQ_Pos_Row04,"...")
        SQ_35 = SQ_Tiles (SQ_Pos_Col03,SQ_Pos_Row05,"...")
        SQ_36 = SQ_Tiles (SQ_Pos_Col03,SQ_Pos_Row06,"...")
        SQ_37 = SQ_Tiles (SQ_Pos_Col03,SQ_Pos_Row07,"...")
        SQ_38 = SQ_Tiles (SQ_Pos_Col03,SQ_Pos_Row08,"...")
        SQ_39 = SQ_Tiles (SQ_Pos_Col03,SQ_Pos_Row09,"...")

        SQ_41 = SQ_Tiles (SQ_Pos_Col04,SQ_Pos_Row01,"...")
        SQ_42 = SQ_Tiles (SQ_Pos_Col04,SQ_Pos_Row02,"...")
        SQ_43 = SQ_Tiles (SQ_Pos_Col04,SQ_Pos_Row03,"...")
        SQ_44 = SQ_Tiles (SQ_Pos_Col04,SQ_Pos_Row04,"...")
        SQ_45 = SQ_Tiles (SQ_Pos_Col04,SQ_Pos_Row05,"...")
        SQ_46 = SQ_Tiles (SQ_Pos_Col04,SQ_Pos_Row06,"...")
        SQ_47 = SQ_Tiles (SQ_Pos_Col04,SQ_Pos_Row07,"...")
        SQ_48 = SQ_Tiles (SQ_Pos_Col04,SQ_Pos_Row08,"...")
        SQ_49 = SQ_Tiles (SQ_Pos_Col04,SQ_Pos_Row09,"...")

        SQ_51 = SQ_Tiles (SQ_Pos_Col05,SQ_Pos_Row01,"...")
        SQ_52 = SQ_Tiles (SQ_Pos_Col05,SQ_Pos_Row02,"...")
        SQ_53 = SQ_Tiles (SQ_Pos_Col05,SQ_Pos_Row03,"...")
        SQ_54 = SQ_Tiles (SQ_Pos_Col05,SQ_Pos_Row04,"...")
        SQ_55 = SQ_Tiles (SQ_Pos_Col05,SQ_Pos_Row05,"NPC")
        SQ_56 = SQ_Tiles (SQ_Pos_Col05,SQ_Pos_Row06,"...")
        SQ_57 = SQ_Tiles (SQ_Pos_Col05,SQ_Pos_Row07,"...")
        SQ_58 = SQ_Tiles (SQ_Pos_Col05,SQ_Pos_Row08,"...")
        SQ_59 = SQ_Tiles (SQ_Pos_Col05,SQ_Pos_Row09,"...")

        SQ_61 = SQ_Tiles (SQ_Pos_Col06,SQ_Pos_Row01,"...")
        SQ_62 = SQ_Tiles (SQ_Pos_Col06,SQ_Pos_Row02,"...")
        SQ_63 = SQ_Tiles (SQ_Pos_Col06,SQ_Pos_Row03,"...")
        SQ_64 = SQ_Tiles (SQ_Pos_Col06,SQ_Pos_Row04,"...")
        SQ_65 = SQ_Tiles (SQ_Pos_Col06,SQ_Pos_Row05,"...")
        SQ_66 = SQ_Tiles (SQ_Pos_Col06,SQ_Pos_Row06,"...")
        SQ_67 = SQ_Tiles (SQ_Pos_Col06,SQ_Pos_Row07,"...")
        SQ_68 = SQ_Tiles (SQ_Pos_Col06,SQ_Pos_Row08,"...")
        SQ_69 = SQ_Tiles (SQ_Pos_Col06,SQ_Pos_Row09,"...")

        SQ_71 = SQ_Tiles (SQ_Pos_Col07,SQ_Pos_Row01,"...")
        SQ_72 = SQ_Tiles (SQ_Pos_Col07,SQ_Pos_Row02,"...")
        SQ_73 = SQ_Tiles (SQ_Pos_Col07,SQ_Pos_Row03,"...")
        SQ_74 = SQ_Tiles (SQ_Pos_Col07,SQ_Pos_Row04,"...")
        SQ_75 = SQ_Tiles (SQ_Pos_Col07,SQ_Pos_Row05,"...")
        SQ_76 = SQ_Tiles (SQ_Pos_Col07,SQ_Pos_Row06,"...")
        SQ_77 = SQ_Tiles (SQ_Pos_Col07,SQ_Pos_Row07,"...")
        SQ_78 = SQ_Tiles (SQ_Pos_Col07,SQ_Pos_Row08,"...")
        SQ_79 = SQ_Tiles (SQ_Pos_Col07,SQ_Pos_Row09,"...")

        SQ_81 = SQ_Tiles (SQ_Pos_Col08,SQ_Pos_Row01,"...")
        SQ_82 = SQ_Tiles (SQ_Pos_Col08,SQ_Pos_Row02,"...")
        SQ_83 = SQ_Tiles (SQ_Pos_Col08,SQ_Pos_Row03,"...")
        SQ_84 = SQ_Tiles (SQ_Pos_Col08,SQ_Pos_Row04,"...")
        SQ_85 = SQ_Tiles (SQ_Pos_Col08,SQ_Pos_Row05,"...")
        SQ_86 = SQ_Tiles (SQ_Pos_Col08,SQ_Pos_Row06,"...")
        SQ_87 = SQ_Tiles (SQ_Pos_Col08,SQ_Pos_Row07,"...")
        SQ_88 = SQ_Tiles (SQ_Pos_Col08,SQ_Pos_Row08,"...")
        SQ_89 = SQ_Tiles (SQ_Pos_Col08,SQ_Pos_Row09,"...")

        SQ_91 = SQ_Tiles (SQ_Pos_Col09,SQ_Pos_Row01,"...")
        SQ_92 = SQ_Tiles (SQ_Pos_Col09,SQ_Pos_Row02,"...")
        SQ_93 = SQ_Tiles (SQ_Pos_Col09,SQ_Pos_Row03,"...")
        SQ_94 = SQ_Tiles (SQ_Pos_Col09,SQ_Pos_Row04,"...")
        SQ_95 = SQ_Tiles (SQ_Pos_Col09,SQ_Pos_Row05,"...")
        SQ_96 = SQ_Tiles (SQ_Pos_Col09,SQ_Pos_Row06,"...")
        SQ_97 = SQ_Tiles (SQ_Pos_Col09,SQ_Pos_Row07,"...")
        SQ_98 = SQ_Tiles (SQ_Pos_Col09,SQ_Pos_Row08,"...")
        SQ_99 = SQ_Tiles (SQ_Pos_Col09,SQ_Pos_Row09,"...")

        SQ_TileMap = [
         SQ_01, SQ_02, SQ_03, SQ_04, SQ_05, SQ_06, SQ_07, SQ_08, SQ_09,
         SQ_10, SQ_20, SQ_30, SQ_40, SQ_50, SQ_60, SQ_70, SQ_80, SQ_90,
         SQ_11, SQ_12, SQ_13, SQ_14, SQ_15, SQ_16, SQ_17, SQ_18, SQ_19,
         SQ_21, SQ_22, SQ_23, SQ_24, SQ_25, SQ_26, SQ_27, SQ_28, SQ_29,
         SQ_31, SQ_32, SQ_33, SQ_34, SQ_35, SQ_36, SQ_37, SQ_38, SQ_39,
         SQ_41, SQ_42, SQ_43, SQ_44, SQ_45, SQ_46, SQ_47, SQ_48, SQ_49,
         SQ_51, SQ_52, SQ_53, SQ_54, SQ_55, SQ_56, SQ_57, SQ_58, SQ_59,
         SQ_61, SQ_62, SQ_63, SQ_64, SQ_65, SQ_66, SQ_67, SQ_68, SQ_69,
         SQ_71, SQ_72, SQ_73, SQ_74, SQ_75, SQ_76, SQ_77, SQ_78, SQ_79,
         SQ_81, SQ_82, SQ_83, SQ_84, SQ_85, SQ_86, SQ_87, SQ_88, SQ_89,
         SQ_91, SQ_92, SQ_93, SQ_94, SQ_95, SQ_96, SQ_97, SQ_98, SQ_99,
        ]

    $ SQ_01.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_02.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_03.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_04.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_05.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_06.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_07.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_08.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_09.Type = renpy.random.choice(['Wall', 'Exit'])

    $ SQ_10.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_20.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_30.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_40.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_50.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_60.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_70.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_80.Type = renpy.random.choice(['Wall', 'Exit'])
    $ SQ_90.Type = renpy.random.choice(['Wall', 'Exit'])
    
    

