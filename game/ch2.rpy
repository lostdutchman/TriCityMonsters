# The game starts here.

label ch2:

    scene bg venue
    show mori jacket grin at center

    "He juts out his hand, a demon head tattooed on the back, for a very out-of-place-feeling handshake."
    morix "[povname]."
    "He says it like he's testing it out."
    morix "Nice to officially meet you.  I'm-"
    "But from the stage a deep voice rings out loud and clear over the crowd."

    hide mori jacket grin
    show mori jacket srs

    frontman "MORI!!"

    "The band's vocalist, holding a mic in his inked hand, is looking exasperatedly in our direction."

    frontman "Hey, are we doing this or what!?"

    hide mori jacket srs
    show mori jacket grin    

    "The guy in front of me waves cheerfully and plunges through the crowd at breakneck pace." 
    
    hide mori jacket grin with moveoutleft

    "Then he hops lightly onto the stage."    
    
    show mori jacket hehe at center with dissolve
    
    "He slaps the exasperated vocalist on one huge, leather jacket-clad shoulder before moving quickly past the bassist and the guitarist to take a seat behind the drums."

    pov "That smug little shit."

    "I've never seen him on stage except him using its meager height to launch into the mosh pit."  
    "He pulls a pair of battered drum sticks out of his ratty, studded jacket and takes position with a showy little flourish."

    hide mori jacket hehe 
    show mori jacket chaos

    stop music 
    play music "audio/grim.ogg" volume 0.50

    "And then he just {i}GOES{/i}"
    "In sync the bassist and the guitarist pick up the opening bars at a breakneck pace.  Mori's backing them full force, his sticks just a blur."
    "By the time the frontman takes his cue the whole band is absolutely shredding... with Mori at the back beating the absolute shit out of the drums."
    "He's not just fast, though.  He's {i}good{/i}."

############ MF Choice 1
menu:
    "Get a closer look.":
        $ ending_progress = ending_progress + 1
        jump ch2_convo1
    "Watch from here.":
         jump ch2_convo1b

label ch2_convo1:        
    "Partly of my own volition and partly because everyone at the back of the floor is now pushing forward, I find myself nearer to the stage, just out of swing-range of the mosh pit."
    "Up close, it's even clearer that Mori is damn good.  The band plays to his beat seamlessly and he's always ready with a solid kick whenever they give him an opening."
    "It's loud as hell and I can feel his bass drum reverberating in my ribcage and the snare hits are like gunshots."
    "This energy is intense and it really makes me want to {i}move{/i}."
    
    jump ch2_movingon

label ch2_convo1b:
    "It's apparent from the second the music kicks off that the energy of the crowd is rapidly racheting higher.  The mosh pit is a blur."
    "Everyone else is jumping and screaming and pumping their fists in time with Mori's beat."
    "The crowd's so loud it's actually kind of competing with the band.  It's {i}deafening{/i}.  But the drums are still loud and clear over all the noise, untouchable even with minimal amplification."

label ch2_movingon:
    "Before I really even notice, their set's almost over."
    
"The frontman announces their last song and the band goes at it with renewed vigor.  Mori's whole body is working to keep the energy going."  
"He's drenched in sweat (again), hair starting to come undone from the messy knot at the back of his head.  He keeps sticking his tongue out in concentration."
        
hide mori jacket chaos with dissolve
"I don't even realize something's wrong until someone crashes into me from behind."

show bg venue with hpunch
play sound "audio/thump.ogg"

"There's out-of-place movement behind me.  For a wild second, I wonder if a second mosh pit's broken out back there but when I turn around, what I see instead makes my guts lurch."
    
stop music

"Cops are coming down the rickety steps with flashlights and they're shouting for everyone to stop what they're doing.  It takes a few seconds for the crowd to register the interruption but I watch the wave of realization happen in real time."
    
play music "audio/tense.ogg" fadein 1.0 volume 0.35
    
"Four or five officers move in and my first instinct is that this is some kind of drug bust.  The sight of them inspires panic though, and the people on the floor are now frantically surging around the cops and towards teh very narrow stairs."
"Over all the panic, shouts ring out ordering the fleeing punks to get up against the walls."

############ MF Choice 2
menu:
    "Try to comply.":            
        jump ch2_convo2
    "{i}RUN{/i}.":
        $ ending_progress = ending_progress + 1
        jump ch2_convo2b

label ch2_convo2:
    "The chaos inside is quickly reaching the combustion point.  I keep getting shoved as other people rush towards the exits en masse."

    show bg venue with hpunch
    play sound "audio/thump.ogg"


    "The cops are getting aggressive quickly- most people aren't listening and they can't controle the horde of bodies at all.  I'm certain there mus be more cops outside too and I wonder if they're having more luck coralling people."
    "The alleys above are tight and dark, a few well placed cop cars would severely hinder those trying to escape into the night."

    show bg venue with hpunch
    play sound "audio/thump.ogg"


    "Someone shoves me {i}hard{/i} and I risk falling if I try to shove my way back into the current again... Given the level of panic, I could easily be trampled even if I'm trying to stay with my back to the wall as much as I can."

    jump ch2_movingon2
    
label ch2_convo2b:
    "Fuck that.  I'm not waiting around to get manhandled by a bunch of overzealous cops."
    "I bolt."
    "There are people everywhere, the tiny venue is suddenly extremely dangerous in its smallness.  The crowd's a full on stampede at this point and I try my best to keep up or risk falling."
    show bg venue with hpunch
    play sound "audio/thump.ogg"

    "Something hits me hard in the lower back and I can feel myself start to overbalance."

label ch2_movingon2:
    "Shit, I know this is going to hurt-"

show mori jacket srs with moveinleft

"Calloused hands inked with demon faces grab both my biceps and pull me closer to steady.  It's Mori."
    
return
