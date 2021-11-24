define pov = Character("[povname]", color="#FFFFFF",  what_prefix='"', what_suffix='"')
define morix = Character("Some Dude", color="#0095ac", what_prefix='"', what_suffix='"')
define mori = Character("Mori", color="#0095ac", what_prefix='"', what_suffix='"')
define prename = Character("---", color="#FFFFFF", what_prefix='"', what_suffix='"')
define frontman = Character ("Band Frontman", color="#e78801", what_prefix='"', what_suffix='"')
define thing = Character ("THING", what_font="fonts/HauntAOE.ttf", color="#960000", what_font_size = 72)
default povname = "Emcee"
default ending_progress = 0
default same_name_flag = False
image splash = "splash.png"
image splas2 = "splash2.png"

label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    # scene black with dissolve
    # with Pause(1)

    # show splash2 with dissolve
    # with Pause(2)

    scene black with dissolve
    with Pause(1)

    return
    
label start:
    stop music fadeout 1.0

    call title from _call_title
    
    call ch1 from _call_ch1
      
    call ch2 from _call_ch2

    call ch3 from _call_ch3

    call ch4 from _call_ch4

    call ch5 from _call_ch5

    call ch6 from _call_ch6

    call consentscene from _call_consentscene

    return
