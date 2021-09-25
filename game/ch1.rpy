# The game starts here.

label ch1:

    image pitrats = "images/pitrats.png"
    $ quick_menu = True
    scene bg city with dissolve
    play music "audio/city.ogg" 


    "So.  The {i}city{/i}.  Sure, it has its problems.  Lots of them.  But one of the benefits is that there's stuff to do even late at night."
    "Even very, {i}very{/i} late at night."
    "Insomnia knocks and there's not much I can do besides try to find some distraction.  Sleep will come...  When, I can't say.  But definitely not now and I can only lay around in bed so much."
    "There's this place... a music venue.  It's a couple of blocks from my flat.  Mostly, it caters to punks though I did catch a couple goth bands there last weekend."
    
    scene bg alley with dissolve
    stop music fadeout 1.0
    play music "audio/punkmuffled.ogg" fadein 1.0 volume 0.25
    show pitrats at Position(xpos=0.7, ypos=0.6)
    with dissolve

    "Pitrats is very small.  It's kind of gross and a little seedy but it's fun and the crowd's energetic.  I've been to bigger venues before but this skanky little place has its own charm."
    "I don't really consider myself like a {i}diehard{/i} punk or anything but Pitrats has been a godsend on these sleepless nights."
    "I give the bouncer my $5 cover and head down the dark, dank stairs underground."

    hide pitrats with dissolve
    play music "audio/punk.ogg" fadein 0.2 volume 0.35
    scene bg venue with fade

    "Inside, it smells like cheap cigarettes and stale beer.  Among other things.  But the energy hits me before I've even fully entered the larger basement room a the bottom of the steps."
    "The bass pounds in my guts and there's a vocalist scream-singing words I can't really understand.  There's a bigger crowd here tonight than usual and the floor is jam-packed."
    "At the front of the crowd, I can see the frenzied movements of the mosh pit and past that, the stage sits... It's maybe ten or so inches off the concrete floor and shoddily made out of plywood."
    
    "The cacophany dies down after another second, the band finishing their set with a last smashing chord that vibrates through the building and sends a wave of shouts up from the jumping crowd."
    
    stop music fadeout 4.0
    play music "audio/crowd.ogg" fadein 1 volume 0.35
    
    "The band files off stage, replaced by a new group who immediately get to work adjusting equipment.  I know there's going to be a lull for a few minutes while they set up..."
    "I might as well hit up the drink table while i have the chance."

    show mori jacket drunk with moveinright

    "Just as I'm about to reach the table, some dude barrels in front of me, slaps down a crushed wad of singles and takes two plastic cups of nearly stale beer without a word to the vendor."
    "He drinks both in a matter of seconds and lets out he most theatrical {i}AHHHHHH{/i} I've literally ever heard."
    "He turns around and it's suddenly clear he must have just gotten out of the mosh pit.  He's... very sweaty."  
    "Dark hair is plastered to his forehead and his face is flushed with (I'm assuming) more exertion than alcohol."

    morix "Oh, my bad.  Did I cut in front of you?"

    hide mori jacket drunk

    show mori jacket hehe at center

    "He smiles and it's actually relatively earnest-looking.  He might be oblivious but he doesn't seem like an asshole."

    morix "Can I buy you a drink?"

    menu:
        "Yeah, actually, that sounds great.":
            jump ch1_convo1
        "Just water, please.  Thanks, man.":
            jump ch1_convo1b
    
    label ch1_convo1:
        "He nods and quickly grabs me my own very appetizing cup of almost-room-temperature beer."
        morix "That's the good shit, right?"
        "His tone is rife with sarcarsm but at the same time, if you drink at events like this room temperature, flat beer is usually the most readily available."
        "'Warm beer keeping you hydrated in the pit?'"
        morix "No, but that won't stop me.  Pitrats is only Pitrats if there's enough rats in the pit, y'know?"
        
        jump ch1_movingon
    
    label ch1_convo1b: 
        morix "No problem, they usually still have bottles by this time of the night."
        "He turns to the vendor and a second or two later passes me a slightly-cooler-than-room-temperature bottle of water."
        "He seems to deliberate a second before he also grabs a bottle for himself but proceeds to down it as quickly as he put away the beer."

    label ch1_movingon:
        morix "SO."

    hide mori jacket hehe

    show mori jacket smile at center

    morix "I've seen you here a few times.  You usually come late and stay for the punk rock block."

    "He turns to look at me fully, crossing his heavily tattooed arms in front of his chest.  I can see he's a bit more muscular than he looks from further away but I do my best not to get caught staring like a dumbass."
    "Still, his tattoos are very intricate and vibrant, disappearing under his jacket- though there's a few wisps of ink at his torn collar, hinting to more going on under his shirt."
    "He's watching me with some interest however, so I busy myself with my drink and nod faintly."
    "'Yeah... I get restless and like to burn off energy here.  It's cheap entertainment and I get to listen to some pretty badass bands.'"

    morix "Yeah?  Have you seen these guys setting up right now?"

    "I look and I can't say I recognize them.  There's a big frontman adjusting a mic while a bassist and a guitarist arrange pedals and amps.  The drumset at the back of the stage is empty."
    "'No, I don't know who they are.  Are they any good?'"

    hide mori jacket smile

    show mori jacket grin at center
    
    "He smiles broadly, his nose crinkling with the expression"
  
    morix "Yeah, actually they're one of my favorites right now.  Good energy."

    "'Seriously?'"

    morix "Yeah! You'll like them!  Also, their drummer is hot as fuck."

    "I can't help but snort a little at that."

    hide mori jacket grin

    show mori jacket smile at center

    morix "What's your name?  I feel like I see you here a lot."
   
    return
