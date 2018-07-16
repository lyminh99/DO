
screen SMM_Home_Scr_GoOut_Map:
    
    tag menu
    modal True
    add "SMM_Home_BG_002"

    frame:
        align (0.8, 0.1)
        vbox:
            textbutton "{size=24} Trường học {/size}" action Jump ("SMM_Home_Place_School")
            textbutton "{size=24} Công viên {/size}" action Jump ("SMM_Home_Place_Park")
            textbutton "{size=24} Quán Cafe {/size}" action Jump ("SMM_Home_Place_CoffeBar")
            textbutton "{size=24} Siêu thị {/size}" action Jump ("SMM_Home_Place_Supermarket")
            textbutton "{size=24} Hồ nước {/size}" action Jump ("SMM_Home_Place_Lake")
            textbutton "{size=24} Về nhà {/size}" action Jump ("SMM_Home_Place_BackHome")
