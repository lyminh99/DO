# The code below defines the ATL transform effects for the buttons on the game menu. These effects are triggered when we hover the mouse over them (hover and selected_hover). Effects that are triggered by idle and selected_idle events (when we stop hovering the mouse over them) ensure that the buttons are moved back to the initial state.
#begin nav_eff
init -2:
    transform config_eff:
        on idle:
            easein 0.5 rotate 0
        on selected_idle:
            easein 0.5 rotate 0
        on hover:
            easein 0.3 rotate 5
            easein 0.3 rotate -5
            repeat
        on selected_hover:
            easein 0.3 rotate 5
            easein 0.3 rotate -5
            repeat
    transform nav_eff:
        on idle:
            easein 0.5 xpos 1465
        on selected_idle:
            easein 0.5 xpos 1465
        on hover:
            easein 0.3 xpos 1540
            easein 0.3 xpos 1470
        on selected_hover:
            easein 0.3 xpos 1540
            easein 0.3 xpos 1470

    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
    
    transform left_to_right:
        yalign 0.0
        xalign 0.8
        alpha 0.0
        linear 2.0 xalign 0.9 alpha 1.0
    
    transform top_to_center:
        yalign 0.0
        xalign 2.0
        alpha 1.0
        linear 6.0 xalign 1.1 alpha 1.0
    
    transform Azuicon:
        xpos 100
        alpha 0.0
        easein 1.5 xpos 0 alpha 1.0

    transform Eleicon:
        ypos 100
        alpha 0.0
        easein 1.5 ypos 0 alpha 1.0
