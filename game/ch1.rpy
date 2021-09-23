# The game starts here.

label ch1:

    image pitrats = "images/pitrats.png"

    scene black with dissolve
    scene bg ch1 with dissolve
    $ renpy.pause(15)

    scene bg city with dissolve
    play music "audio/city.ogg" 


    pov "So.  The {i}city{/i}.  Sure, it has its problems.  Lots of them.  But one of the benefits is that there's stuff to do even late at night."
    "Even very, {i}very{/i} late at night."
    "Insomnia knocks and there's not much I can do besides try to find some distraction.  Sleep will come...  When, I can't say.  But definitely not now and I can only lay around in bed so much."
    "There's this place... a music venue.  It's a couple of blocks from my flat.  Mostly, it caters to punks though I did catch a couple goth bands there last weekend."
    
    scene bg alley with dissolve
    stop music fadeout 1.0
    play music "audio/punkmuffled.ogg" fadein 1.0 volume 0.25
    show pitrats at Position(xpos=0.7, ypos=0.6)
    with dissolve

    "Pitrats is very small.  It's kind of gross and a little seedy but it's fun and the crowds are energetic.  I've been to bigger venues before but this skanky little place has its own charm."
    "I don't really consider myself like a Diehard Punk or anything but Pitrats has been a godsend on these sleepless nights."
    "I give the bouncer my $5 cover and head down the dark, dank stairs underground."

    hide pitrats
    scene bg venue with dissolve
    play music "audio/punk.ogg" fadein 1.0 volume 0.35

    "Inside, it smells like cheap cigarettes and stale beer.  Among other things.  But the energy hits me before I've even fully entered the larger basement room a the bottom of the steps."
    "The bass pounds in my guts and there's a vocalist scream-singing words I can't really understand.  There's a bigger crowd here tonight than usual and the floor is jam-packed."
    "At the front of the crowd, I can see the frenzied movements of the mosh pit and past that, the stage sits... It's maybe ten or so inches off the concrete floor and shoddily made out of plywood."
    
    stop music fadeout 1.0

    "The cacophany dies down after another second, the band finishing their set with a last smashing chord that vibrates through the building and sends a wave of shouts up from the jumping crowd."
    "The band files off stage, replaced by a new group who immediately get to work adjusting equipment.  I know there's going to be a lull for a few minutes while they set up..."
    "I might as well hit up the drink table while i have the chance."

    show mori jacket drunk with moveinright

    "Just as I'm about to reach the table, some dude barrels in front of me, slaps down a crushed wad of singles and takes two plastic cups of nearly stale beer without a word to the vendor."
    "He drinks both in a matter of seconds and lets out he most theatrical {i}AHHHHHH{/i} I've literally ever heard."
    "He turns around and it's suddenly clear he must have just gotten out of the mosh pit.  He's sweaty.  Dark hair is plastered to his forehead and his face is flushed with (I'm assuming) more exertion than alcohol."

    morix "Oh, my bad.  Did I cut in front of you?"

    "He smiles and it's actually relatively earnest-looking.  He might be oblivious but he doesn't seem like an asshole."

    morix "Can I buy you a drink?"






    


   
    return
