init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

##############################

    $ dissolve3 = Dissolve(0.3)
    $ fade3 = Fade(1, 2, 1)
    $ fade2 = Fade(0, 0, 1)
    $ dissolve2 = Dissolve(0.2)
    $ dissolve5 = Dissolve(0.5)
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

    $ style.nvl_dialogue.justify = True
    $ sshake = Shake((1, 0, 1, 0), 1.0, dist=150)
    $ sshake2 = Shake((1, 0, 1, 0), 3.0, dist=150)
    $ sshake3 = Shake((1, 0, 1, 0), 5.0, dist=150)

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

    transform right_to_left:
        linear 0.3 xalign 0.1
    transform center:
      align (.5,1.0)
      on replaced:
        linear .2 alpha .0
    transform left:
      align (.2,1.0)
      on replaced:
        linear .2 alpha .0
    transform right:
      align (.9,1.0)
      on replaced:
        linear .2 alpha .0