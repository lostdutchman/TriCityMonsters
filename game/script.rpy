# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povname]")
define mori = Character("Coordinator")
define e = Character("Eileen")
default povname = "Emcee"

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
default ending_progress = 0
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
    
# The game starts here.

label start:
    call ch1

    call nameselection

    pov "My name is [povname]!"

    label pronoun:

        call pronounselection # This calls a choice menu to select pronouns.
   
    hide coord wave

    show eileen normal

    e "Thanks, [povname]."
    e "[they!t!c] go[es] and eat[s] the apple."

   
  
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
