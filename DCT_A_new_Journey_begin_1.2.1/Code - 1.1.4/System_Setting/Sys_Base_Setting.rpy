
init -1900 python:

    config.automatic_images = [ '/', ' ' ]
    config.automatic_images_strip = ["images", "DCT", "Sprites", "Azzurra"]

    # directories including images for composite images.
    config.automatic_images_parts = None

    # directories including not necessary images for composite images.
    config.automatic_images_not_necessary_parts = []

init python:

    #Make all the main menu buttons be the same size.
    #style.mm_button.size_group = "mm"
    style.mm_button.background = None
    #style.mm_button_text.outlines = [(3, "#000", 0, 0)]
    style.mm_button_text.hover_outlines = [(3, "#282", 0, 0)]
    #style.mm_button_text.drop_shadow = [(-5, -5), (1, -1), (-1, 1), (1, 1), (2, 2)]
    #style.mm_button_text.hover_drop_shadow_color = "#282"

init:
    $_game_menu_screen = None
    image movie = Movie(size=(1920, 1080), xalign=0.0, yalign=0.0)