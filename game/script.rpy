# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povname]", color="#FFFFFF")
define morix = Character("Some Dude", color="#5a8b90")
define mori = Character("Mori", color="#5a8b90")
define prename = Character("", color="#FFFFFF")
define frontman = Character ("Band Frontman", color="#f0af00")
define thing = Character ("THING", what_font="fonts/Octobercrow.ttf", color="#960000")
default povname = "Emcee"
default ending_progress = 0

# Flags
# Make as many of these as you need to track if the MC has done a thing, or has a thing in their possesion. 
# Initialize them all as false
#
#default book = false
#
# When the MC picks up the book you would use
# $ book = true
#
# When the book is needed you can use an if statement
#if book:
#
# Below is how you track progress toward a specific ending
# Negitive values bring ending toward XXXX positive values bring ending toward XXXX
#$default ending_progress = 0
# 
# Increment or decrement the value like this
# $ ending_progress = ending_progress + 1

image splash = "splash.png"

label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return
    
label start:
    stop music fadeout 1.0

    call title
    
    call ch1
      
    call ch2

    call ch3

    call ch4

    call ch5

    call ch6

    call consentscene

    call credits 

    return
