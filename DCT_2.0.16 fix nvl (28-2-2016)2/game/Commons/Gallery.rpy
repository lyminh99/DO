﻿##############################################################################
#
#Galleries:
########################################################################

init 5 python:
    #Galleries settings - start
    #list the CG gallery images here: ĐIỀN TÊN CÁC CG VÀO
    gallery_cg_items = ["cg_1", "cg_2", "cg_3", "cg_4", "cg_7", "cg_11", "cg_12", "cg_13", "cg_14"]
#"BG_1", "BG_2", "BG_3", "BG_4a", "BG_4b", "BG_5", "BG_6", "BG_6b", "BG_7", "BG_8", "BG_9", "BG_10",
#"BG_11", "BG_12", "BG_13", "BG_14", "BG_15", "BG_16", "BG_17", "BG_18", "BG_19", "BG_20",
# "BG_22", "BG_23"
#"cg_1", "cg_2", "cg_3", "cg_4", "cg_5", "cg_6", "cg_7", "cg_8", "cg_9", "cg_10", "cg_11", "cg_12", "Screen_title"]
    #list the BG gallery images here (do not include variations, such as night version):
    gallery_bg_items = []
#"BG_1", "BG_2", "BG_3", "BG_4a", "BG_4b", "BG_5", "BG_6", "BG_6b", "BG_7", "BG_8", "BG_9", "BG_10",
#"BG_11", "BG_12", "BG_13", "BG_14", "BG_15", "BG_16", "BG_17", "BG_18", "BG_19", "BG_20",
# "BG_22", "BG_23"
#"cg_1", "cg_2", "cg_3", "cg_4", "cg_5", "cg_6", "cg_7", "cg_8", "cg_9", "cg_10", "cg_11", "Screen_title"]
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 320#267
    thumbnail_y = 180#150
    #the setting above (267x150) will work well with 16:9 screen ratio. Make sure to adjust it, if your are using 4:3 or something else.
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
    g_cg.transition = fade
    cg_page=0

    g_bg = Gallery()
    for gal_item in gallery_bg_items:
        g_bg.button(gal_item + " butt")
        g_bg.image(gal_item)
        g_bg.unlock(gal_item)
        #if BGs have variations, such as night version, uncomment the lines below and copy paste them for each BG with variations
#        if gal_item == "bg kitchen":
#            g_bg.image("bg kitchen dining")
#            g_bg.unlock("bg kitchen dining")
    g_bg.transition = fade
    bg_page=0

    #Here we create the thumbnails. We create a grayscale thumbnail image for BGs, but we use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
    for gal_item in gallery_bg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        renpy.image (gal_item + " butt dis", im.Grayscale(ImageReference(gal_item + " butt")))

########################################################################

screen cg_gallery:
    tag menu
    add "Images/Themes/Gallery.JPG"
    frame background None xpos 160:
        grid gal_rows gal_cols:
            ypos 220
            $ i = 0
            $ next_cg_page = cg_page + 1            
            if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                $ next_cg_page = 0
            for gal_item in gallery_cg_items:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    add g_cg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("images/Interface/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_cg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('cg_page', next_cg_page), ShowMenu("cg_gallery")]
    imagebutton auto "Gui/Music_room/Return_%s.png" xpos 1765 ypos 817 focus_mask True action Hide ('cg_gallery'), ShowMenu("main_menu2") hovered [ Play ("test_one", "sfx/click.ogg")] 

########################################################################

screen bg_gallery:
#The BG gallery screen is more or less copy pasted from the CG screen above, I only changed "make_button" to include a grayscale thumbnail for locked items
    tag menu
    use navigation
    frame background None xpos 10:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_bg_page = bg_page + 1
            if next_bg_page > int(len(gallery_bg_items)/gal_cells):
                $ next_bg_page = 0
            for gal_item in gallery_bg_items:
                $ i += 1
                if i <= (bg_page+1)*gal_cells and i>bg_page*gal_cells:
                    add g_bg.make_button(gal_item + " butt", gal_item + " butt", gal_item + " butt dis", xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (bg_page+1)*gal_cells):
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_bg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('bg_page', next_bg_page), ShowMenu("bg_gallery")]
    imagebutton auto "Gui/Music_room/Return_%s.png" xpos 1765 ypos 817 focus_mask True action Hide ('bg_gallery'), ShowMenu("main_menu2") hovered [ Play ("test_one", "sfx/click.ogg")] 