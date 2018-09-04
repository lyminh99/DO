## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = True

    ## These control the width and height of the screen.

    config.screen_width = 1920
    config.screen_height = 1080

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Đường chân trời Volume 1 - 1.0.1"
    #config.windows_icon = None

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "DCT_x.x.x"
    config.version = "1.0.1"

    #########################################
    # Themes
    
    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles. It's
    ## the only theme we currently support.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.diamond(
        ## Theme: Diamond
        ## Color scheme: Favorite Jeans
                                    
        ## The color of an idle widget face.
        widget = "#8495C0",

        ## The color of a focused widget face.
        widget_hover = "#6b7ba1",

        ## The color of the text in a widget.
        widget_text = "#ffffff",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#ffffff",

        ## The color of a disabled widget face. 
        disabled = "#919994",

        ## The color of disabled widget text.
        disabled_text = "#B6BFB9",

        ## The color of informational labels.
        label = "#ffffff",

        ## The color of a frame containing widgets.
        frame = "#3EB142",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "Screentitle.jpg",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "Screentitle.jpg",
      

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = True,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.            
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = Frame("images/Interface/MN_TT_BB03.png", 12, 12)
    style.say_who_window.background = Frame("images/Interface/MN_TT_BB02.png", 15, 15)
    

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    style.window.left_margin = 0
    style.window.right_margin = 0
    style.window.top_margin = 0
    style.window.bottom_margin = 0
    

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 330
    style.window.right_padding = 320
    style.window.top_padding = 370
    style.window.bottom_padding = 0

    style.say_who_window.bottom_margin = -360
    style.say_who_window.left_margin = -20
    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 600
    #Chuyển màu text
    #style.default.color = "#000000"
    

    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.
    #style.default.font = "Fonts/UVNAnhHaiNhe_R.TTF"
    style.default.font = "Fonts/Roboto-Condensed.ttf"
    style.button_text.font = "Fonts/consola.ttf"
    #style.button_text.font = "Fonts/Roboto-Black.TTF"
    #Khoảng cách dòng line
    style.default.line_spacing = 0
    style.default.line_leading = 15

    ## The default size of text.

    style.default.size = 38
    style.button_text.size = 30

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = True

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.ogg"
    # style.imagemap.activate_sound = "click.ogg"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.ogg"
    # config.exit_sound = "click.ogg"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.ogg"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "Soundtracks/004 - Lovely Bubbles.ogg"

    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = dissolve

    ## Used when exiting the game menu to the game.
    config.exit_transition = fade

    ## Used between screens of the game menu.
    config.intra_transition = fade

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = fade

    ## Used when returning to the main menu from the game.
    config.game_main_transition = fade

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = fade

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = fade

    ## Used when a game is loaded.
    config.after_load_transition = fade

    ## Used when the window is shown.
    config.window_show_transition = fade

    ## Used when the window is hidden.
    config.window_hide_transition = fade
    



    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
#python early:
#    config.save_directory = "Now, just chase me-1356919100"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 40
    config.window_icon = "images/Themes/Mini_logo.png"
    config.windows_icon = "images/Themes/Mini_logo.png"

    #########################################
    ## More customizations can go here.
    
#     image main_menu:

#    contains:
#        "DCTtittle.png"
#        yalign .00
#        xalign 1.10

       
        

                         
## This section contains information about how to build your project into 
## distribution files.
init python:
    
    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "DCT_Volume_ngoaitruyen"
    
    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "DCT_Volume_1.1"
    
    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False
    
    ## File patterns:
    ## 
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##    
    ##
    ## In a pattern:
    ##
    ## / 
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    #build.classify('**~', None)
    #build.classify('**.bak', None)
    #build.classify('**/.**', None)
    #build.classify('**/#**', None)
    #build.classify('**/thumbs.db', None)
    
    ## To archive files, classify them as 'archive'.
    
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    #build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.ogv', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.mid', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.otf', 'archive')
    build.classify('game/**.db', 'None')
    #build.classify('game/**.rpy', 'None')
    build.classify('game/**.bak', 'None')
    build.classify('game/**.save', 'None')
    build.classify('game/**.rpyb', 'None')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    
    ##Size of thumbnail save slot
    config.thumbnail_height = 161
    config.thumbnail_width = 287

    config.mouse = {'default':[('images/cursor/cursor1.png', 3, 4),
                               ('images/cursor/cursor2.png', 3, 4),
                               ('images/cursor/cursor3.png', 3, 4),
                               ('images/cursor/cursor4.png', 3, 4),
                                ('images/cursor/cursor5.png', 3, 4)]}
    config.debug_text_overflow = True
    config.auto_voice = "voice/{id}.mp3"

init -1900 python:
    config.automatic_images = [ '/', ' ' ]
    config.automatic_images_strip = ["images", "Sprites", "Azzurra"]

    # directories including images for composite images.
    config.automatic_images_parts = None

    # directories including not necessary images for composite images.
    config.automatic_images_not_necessary_parts = []
init 1900 python hide:

    def create_automatic_composite_images():
        import itertools

        seps = config.automatic_images

        if seps is True:
            seps = [ ' ', '/', '_' ]

        image_parts = dict()

        for dir, fn in renpy.loader.listdirfiles():

            if fn.startswith("_"):
                continue

            # Only .png and .jpg
            if not fn.lower().endswith(".png") and not fn.lower().endswith(".jpg"):
                continue

            # Strip the extension, replace slashes.
            shortfn = fn[:-4].replace("\\", "/")

            #store parts to image_parts
            for i in config.automatic_images_parts:
                if shortfn.find("/"+i+"/") > 0:

                    name = (shortfn[:shortfn.find("/"+i+"/")], )
                    for sep in seps:
                        name = tuple(j for i in name for j in i.split(sep))
                    # Strip name components.
                    while name:
                        for j in config.automatic_images_strip:
                            if name[0] == j:
                                name = name[1:]
                                break
                        else:
                            break

                    parts = (shortfn[shortfn.find("/"+i+"/")+len(i)+2:], )
                    for sep in seps:
                        parts = tuple(j for i in parts for j in i.split(sep))


                    if name not in image_parts:
                        image_parts[name] = { i:[] for i in config.automatic_images_parts }

                    image_parts[name][i].append((parts, fn))

        # define images consisting of several images
        for name in image_parts:
            parts_lists = []
            for part in config.automatic_images_parts:
                if image_parts[name][part]:
                    if part in config.automatic_images_not_necessary_parts:
                        image_parts[name][part].append(None)
                    parts_lists.append(image_parts[name][part])

            all_pattern = map(list, itertools.product(*parts_lists))

            for i in all_pattern:
                name_args = name
                file_args = []
                for k in i:
                    if k is not None:
                        name_args += k[0]
                        file_args.append(k[1])

                # Only names of 2 components or more by default.
                if len(name_args) < config.automatic_images_minimum_components:
                    continue

                # Reject if it already exists.
                if name_args in renpy.display.image.images:
                    continue

                tran = getattr(renpy.store, "default_" + name_args[0], None)
                if tran:
                    renpy.image(name_args, At(Flatten(Fixed(*file_args, fit_first=True)), tran))
                else:
                    renpy.image(name_args, Flatten(Fixed(*file_args, fit_first=True)))
 
    if config.automatic_images and config.automatic_images_parts:
        create_automatic_composite_images()
