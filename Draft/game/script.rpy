# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define MC = Character("[mcname]")
default mcname = "Emcee"
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

    #enter name screen
    $ mcname = renpy.input("My name's:")
    $ mcname = mcname.strip()

    if not mcname:
        $mcname = "Emcee"
        pov "[mcname]."


#enter pronouns screen
    
    MC "My pronouns are..."

    menu:
        "She/Her":
            $ pronoun1 = "She"
            $ pronoun2 = "Her"
            $ pronoun3 = "Her"
            jump sexchosen1

        "He/Him":
            $ pronoun1 = "He"
            $ pronoun2 = "Her"
            $ pronoun3 = "His"
            jump sexchosen2

        "They/Them":
            $ pronoun1 = "They"
            $ pronoun2 = "Them"
            $ pronoun3 = "Their"
            jump sexchosen3

        "Other (Choose Your Own)":
            jump inputpronoun

    # use %(pronoun1)s to call it 

    label inputpronoun:

    $ pronoun1 = renpy.input("Generic (like she, he, or they)")
    $ pronoun1 = pronoun1.strip()
    if pronoun1 == "":
        $ pronoun1="They"

    $ pronoun2 = renpy.input("Referred to by (like her, him, or them)")
    $ pronoun2 = pronoun2.strip()
    if pronoun2 == "":
        $ pronoun2="Them"

    $ pronoun3 = renpy.input("Possessive (like her, him, or their)")
    $ pronoun3 = pronoun3.strip()
    if pronoun3 == "":
        $ pronoun3="Their"
        
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

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
