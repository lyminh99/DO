
init -1 python hide:

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
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 0

    ## The default auto-forward time setting.

    config.default_afm_time = 10

    #########################################
    ## More customizations can go here.


    config.developer = True

    config.screen_width = 1920
    config.screen_height = 1080

    config.window_title = u"DCT_A_new_Journey_begin - 1.1.2"

    config.name = "DCT_NJB"
    config.version = "1.1.2"

python early:
    config.save_directory = "DCT_A_new_Journey_begin_Saves"
