# The game starts here.

label ch1:

    image pitrats = "images/pitrats.png"

    scene black with dissolve
    scene bg ch1 with dissolve
    $ renpy.pause(15)

    scene bg city with dissolve
    play music "audio/city.ogg" 


    prename "So.  The {i}city{/i}.  Sure, it has its problems.  Lots of them.  But one of the benefits is that there's stuff to do even late at night."
    prename "Even very, {i}very{/i} late at night."
    prename "Insomnia knocks and there's not much I can do besides try to find some distraction.  Sleep will come...  When, I can't say.  But definitely not now and I can only lay around in bed so much."
    prename "There's this place... a music venue.  It's a couple of blocks from my flat.  Mostly, it caters to punks though I did catch a couple goth bands there last weekend."
    
    scene bg alley with dissolve
    stop music fadeout 1.0
    play music "audio/punkmuffled.ogg" fadein 1.0 volume 0.50
    show pitrats at Position(xpos=0.7, ypos=0.6)
    with dissolve

    prename "Pitrat's is very small.  It's kind of gross and a little seedy but it's fun and the crowds are energetic.  I've been to bigger venues before but this skanky little place has its own charm."

    

    pov ""

   
    return
