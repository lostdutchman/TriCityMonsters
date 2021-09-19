# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povname]")
define mori = Character("Coordinator")
define e = Character("Eileen")
default povname = "Emcee"
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

    $ povname = renpy.input("Please sign in:")
    $ povname = povname.strip()

    if not povname:
     $povname = "Bababooie"

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
