# The game starts here.

label ch1:

    image pitrats = "images/pitrats.png"

    scene black with dissolve
    scene bg ch1 with dissolve
    $ renpy.pause(15)

    scene bg city with dissolve
    play music "audio/city.ogg" 


    "So.  The {i}city{/i}.  Sure, it has its problems.  Lots of them.  But one of the benefits is that there's stuff to do even late at night."
    prename "Even very, {i}very{/i} late at night."
    prename "Insomnia knocks and there's not much I can do besides try to find some distraction.  Sleep will come...  When, I can't say.  But definitely not now and I can only lay around in bed so much."
    prename "There's this place... a music venue.  It's a couple of blocks from my flat.  Mostly, it caters to punks though I did catch a couple goth bands there last weekend."
    
    scene bg alley with dissolve
    stop music fadeout 1.0
    play music "audio/punkmuffled.ogg" fadein 1.0 volume 0.25
    show pitrats at Position(xpos=0.7, ypos=0.6)
    with dissolve

    prename "Pitrats is very small.  It's kind of gross and a little seedy but it's fun and the crowds are energetic.  I've been to bigger venues before but this skanky little place has its own charm."
    prename "I don't really consider myself like a Diehard Punk or anything but Pitrats has been a godsend on these sleepless nights.  I give the bouncer my $5 cover and head down the dark, dank stairs underground."

    hide pitrats
    scene bg venue with dissolve
    play music "audio/punk.ogg" fadein 1.0 volume 0.35

    prename "Inside, it smells like cheap cigarettes and stale beer.  Among other things.  But the energy hits me before I've even fully entered the larger basement room a the bottom of the steps."
    prename "The bass pounds in my guts and there's a vocalist scream-singing words I can't really understand.  There's a bigger crowd here tonight than usual and the floor is jam-packed."
    prename "At the front of the crowd, I can see the frenzied movements of the mosh pit and past that, the stage sits... It's maybe ten or so inches off the concrete floor and shoddily made out of plywood."
    
    stop music fadeout 1.0

    prename "The cacophany dies down after another second, the band finishing their set with a last smashing chord that vibrates through the building and sends a wave of shouts up from the jumping crowd."


    


   
    return
