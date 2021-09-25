# The game starts here.

label ch3:

hide mori jacket srs
show mori jacket smile

"Without a word, he pulls me along with him him, his palm sliding down my arm to grab my hand."
"It's sweaty..."
"Not the most pleasant thing in the world, honestly, but I can't deny that I do feel a lot better with someone looking out for me."
"Ahead of him I can make out the tall, thick figure of the vocalist and the rest of the band, moving with purpose towards the exit."
"... and then I realize something."
"The cops are almost entirely focused on getting people out of the way so they can get to the band."

hide mori jacket smile
show mori jacket chaos

"Actually, there's wild gesticulating and I can see the nearest cop's mouth move.  I can't make out his words over the noise but he's looking right at {i}Mori{/i}."
"And now me, who he's dragging along bodily."

mori "Stay with me, you go down in a crowd like this you'll get hurt!"
mori "Just like Black Friday CCTV footage!"

"He nimbly sidesteps to the right, avoiding a {i}very{/i} aggravated looking officer by only a scant few inches, hauling me along like I weigh nothing."
"Mori cackles loudly, looking- impossibly- delighted and 99 percent unconcerned with the situation at large."
"But he's caught up in the momentary victory... and doesn't see the next cop lunging at us from the side."

pov "Watch out!"
"I pull back suddenly, reaffirming my grip on his hand, and yank his arm to keep him from charging directly into them."

hide mori jacket chaos
show mori jacket grin

mori "hehehh"
mori "Thanks!  I didn't even see him!"

"He spares a second to smirk widely at me.  He's actually, {i}really{/i} enjoying this, isn't he?"
"The cop recovers and makes to lunge again but Mori- without an iota of hesitation- shoulder checks him roughly and lets out another loud crow of laughter even as the cop sags, winded and bruised."
"Okay, no, this really is fun for him."

pov "They're gonna toss you straight in jail when they catch you!"

mori "Ha, they gotta catch me first."

"His smile is huge an earnest and there's a chaotic glint to his eyes that is, admittedly, a little adrenalizing to see."
"At the staircase there's a solid wall of bottlenecked people and- without slowing at all- Mori suddenly veers to the left, moving away from his bandmates and pulling me with him."
"He dodges around sound equipment and the plastic drink table with ease while I stagger along in his wake.  He lets go of my hand to throw his shoulder against a huge amp in the corner."
"With a slight grunt, it shifts and reveals a small metal ladder bolted into the concrete wall."
"A fire escape."
"I follow it up with my eyes towards a dusty ceiling hatch, leading to the floors above."

mori "Up. Hurry."

hide mori jacket jacket grin with dissolve

"Obliging, I launch up as quick as I can.  The metal warps slightly beneath me, especially once Mori climbs up beneathe me.  I reach the hatch without issue and yank on the ancient, grime-coated release lever."
"But it won't budge."
"The scene below is still utter chaos and I can feel panicked sweat start to break out on my forehead as several furious cops point out our location to more fighting their way down from the alley entrance."
"I yank as hard as I can, I can feel the latch digging painfully deep into the meat of my palm...!"
"But it won't move."

show mori jacket srs with moveinbottom

"Mori pulls himself up a few more rungs and presses me against the ladder, stretching to reach over me and grab the release, his tattooed hand closing over mine."
"He jerks it open with apparent ease on the first try, though it showers us with dust as he shoves it open with a low chuckle."

hide mori jacket grin
show mori jacket smile

mori "Keep climbing to the roof, they'll be swarming the streets."
pov "What about your bandmates?  They were headed towards the main entrance!"
mori "They'll be fine, this isn't the first run in they've had.  Besides, they're after-"

show bg venue with vpunch
play sound "audio/thump.ogg"

hide mori jacket smile
show mori jacket srs

pov "Mori!"
"He nearly falls as he's jerked violently downwards.  There's a cop halfway up the ladder, yanking on his leg with the full intent of tearing him right off it."
"Without even pausing to consider whether it was a remotely good idea or not, Mori wrenches his leg back and kicks down, {i}hard{/i}, catching the cop in the side of the head and pulling all the way free."
mori "Let's go, we gotta hurry."
pov "Are you {i}trying{/i} to get charged with assaulting an officer?  They're gonna throw the book at you if they catch you."

hide mori jacket srs
show mori jacket chaos

mori "You think hitting a cop is the worst thing they want me for?"

menu:
    "Okay, that's not creepy and mildly threatening at all.":
        jump ch3_convo1
    "What did you do {i}tonight{/i} that warrants this!?.":
         jump ch3_convo1b

label ch3_convo1:        
    
    hide mori jacket chaos
    show mori jacket grin

    mori "Sorry, I'm well meaning.  I promise."
    "We definitely don't have time to argue, but I do manage to shoot him a withering glare."    
    jump ch3_movingon

label ch3_convo1b:
    
    hide mori jacket chaos
    show mori jacket smile

    mori "Tonight?  Nothing!"
    "He flashes me a smirk that I find grudgingly disarming.  Mori's apparent comfort with chaos makes him... a little rougish and while I definitely don't trust him yet, he doesn't really seem all that dangerous."
   
label ch3_movingon:
    "And then I'm climbing again, trying to get up to the ground floor before the cops can make a more concerted effort to pull Mori down into the mass of people below."
    "I shake my head a little and keep moving while we have the chance.  I can figure him out later."

scene black with dissolve
$ renpy.pause(1)
show bg shop with fade

"The ground floor is an empty cafe.  It's late after all but there's tons of movement and noise outside.  Beams of red and blue police lights streak across the walls."
"He drops the hatch closed behind us and while we don't have time to waste neither of us can really help ourselves from covertly watching for a second as the flood of punks escaping Pitrats cause a ruckus."
"We keep moving upwards.  Another hatch leading to the second level and, again, he forces it open for me.  Which is frankly pretty impressive because those handles feel like they've never been opened before and Mori isn't particularly bulked up."
"He drops each one closed behind us and after the fourth or fifth one, the series of drab, dark ceilings opens up to a clouded night sky."

show bg roof with fade
stop music fadeout 1.0
play music "audio/roof.ogg" fadein 3.0 volume 0.25

"While the fresh air is a relief on my sweaty skin and general nervousness, my brain is assaulting me wiht the image of us trapped on the roof and surrounded by angry cops."
"As Mori deftly pulls himself up behind me, I can see he looks casually alert but not really stressed, even as he moves to close the hatch."
"His comfortable confidence is mildly infectious, I suppose, but it also really makes this seem like some kind of game to him."


#################  MF choice 3
menu:
    "I think he might be insane.":
        jump ch3_convo2
    "I think he might be insane and it's a little hot.":
        $ ending_progress = ending_progress + 1
        jump ch3_convo2

label ch3_convo2:
    "After a second, I move to join him as he takes a look over the ledge."

hide mori jacket smile
show mori jacket srs

"And I make a disconcerting realization."
"There's no fire escape back down the side of the building."
pov "Shit, how are we gonna get down...?"
pov "Do you think we can hide up here until the coast is clear?"
mori "Nah, it's too late for that."
"I turn to press him for solutions- this is his fault, after all- but I can tell immediately something's not right."









return
