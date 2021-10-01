# The game starts here.

label ch6:

stop music fadeout 1.5
hide mori shirt neu
show bg apartment with dissolve
show mori shirt neu with moveinright

play music "audio/roof.ogg" fadein 1.0 volume 1.5

"The walk to Mori's apartment is only a few blocks and we hurriedly leave the area before any more cops and/or demons can get in our way."
"Like before, he seems alert but not stressed, passively scanning the alleys as we pass but his posture remains relaxed and fluid, for the most part."

mori "I gotta admit, I'm kinda surprised you haven't run off screaming."

menu: 
    "You've answered approximately zero of my questions.":
        jump ch6_convo1
    "Dude, I came {i}real{/i} close":
        jump ch6_convo1b

label ch6_convo1:
    mori "True.  You must have a few."
    "I scoff."
    pov "I have a few questions about cops flooding into Pitrats.  I have a LOT of questions about monsters and Furries and..."
    "I guesture vaguely to all of him."
    "To which he snorts softly and pushes some errant hair out of his face."
    mori "Alright.  Don't blame me if you don't like what you hear, though.  It's not nearly as dramatic as it seems."
    jump ch6_movingon

label ch6_convo1b:
    pov "I've... never had to deal with anything like that.  There were so many moments where my body just... froze up."
    "Mori deliberates for a moment before he clears his throat in a way that's uncharacteristically self conscious."
    mori "I wouldn't have blamed you, to be honest.  Mixing normies and demon bullshit is a recipe for disaster."
    mori "But for what it's worth, I'm pretty glad you stuck around, [povname]."

label ch6_movingon:
    "We turn a corner and come upon a solid brick apartment building.  Mori gestures to and external fire escape and leads me up to a second-story balcony."

pov "After all that you're not even going to invite me inside?"

hide mori shirt neu
show mori shirt smile

mori "Oh, its a {i}mess{/i}, not ready for you to see how I'm living just yet.  Try again next time."

"I shake my head a little exasperatedly but I can't really help but smirk."

pov "You're a mess."
mori "Pretty much."

"He shrugs nonchalantly and then moves to stand on the brick wall of the balcony.  Like he really can't stand not being reckless for a few short minutes."
"He's definitely rough around the edges, but I can't help thinking he's pretty kind underneath it all.  He did save me a couple times tonight.  And I'm still wearing his jacket."

hide mori shirt smile
show mori shirt neu

pov "So... this is common for you?  Getting chased by cops that are actually monsters in disguise?"
mori "Listen, I don't want to beat a dead horse but think really carefully about whether you want to know the truth.  You can't unhear it."

menu: 
    "For the last time, yes.":
        jump ch6_convo2
    "You're really afraid, huh?":
        jump ch6_convo2b

label ch6_convo2:
    mori "Fine."
    "He takes a deep breath and runs a hand through his messy hair, obviously trying to gather himself for an explanation."
    jump ch6_movingon2

label ch6_convo2b:
    mori "For myself?  Not so much.  Dragging normies into this, though...  That's different."

label ch6_movingon2:
    "He struggles to find the words for a good long minute, staring at the city open before him and still standing on the ledge while I lean against it, feet firmly on solid ground."

hide mori shirt neu
show mori shirt srs

mori "The world's a scary place full of desperate people, you know?"
pov "So is that you?  Are you something that makes the world scarier?  Or are you just desperate?"
"He chuckles lowly, his pitch low enough to forcibly remind me of him talking while in that animal form."
mori "I {i}was{/i} a very desperate person.  I did something stupid and I'm paying the price now."
pov "What'd you do?"
"For a second he pauses again and he looks a little scared.  I can't say I really know him, I've seen him around, sure, but tonight is the most time I've spent with him."
"He's chaotic and kind of a wild child but he is well meaning and more open than he probably wants."
"It takes him a solid minute or two to build up the confidence to speak again and when he does he looks uncharacteristically serious."
mori "I died."
mori "Or, well... I got {i}really{/i} close."
mori "It was a couple years ago.  I was staggering-drunk and trying to make my way back home after a show.  I got hit by an undercover cop car at nearly full speed."
"He pauses, gauging my expression carefully but I'm hanging on his every word.  I have no idea what to make of this."
mori "The driver and his partner just dragged me off the road and left.  I was already as good as dead."
mori "Then I had some kind of... vision or something.  Someone spoke to me, asked me if I wanted to form a contract with them."
pov "A contract?"
mori "Yeah. Sign the contract and in exchange for fixing my body, I had to find certain things for them."
pov "And you took it?"
mori "Yeah, in a heartbeat.  I think I must have had seconds left in me, honestly.  I didn't think, there wasn't time."
mori "And then..."
"I wait, trying to let him find the words.  He doesn't look distraught as much as he just looks troubled, like he hasn't had to recap this in a long time."
mori "And then I was healed.  I could move, I could think properly.  Bones snapped back together and I stopped bleeding all over the street.  Then I turned into that... thing."
"Mori lets out a nervous bark of a laugh but it's transparent he's trying to downplay how uncomfortable this conversation is making him."
pov "A cat.  {i}Some{/i} kind of cat, anyway.  Why, though?"
mori "The contract brought me back to life and turned me into a demon.  That's the demon body I was 'blessed' with."
"Mori does air quotes and rolls his dark eyes somewhat irritably."

hide mori shirt srs
show mori shirt neu

mori "Have you ever heard the word kaibyo?  Or bakeneko?"
pov "No, is that what it's called?"
mori "There's a lot of monster cats but those seem like they're the closest match.  Cats that can change shape, talk to spirits..."

hide mori shirt srs with dissolve
show mori spirits srs with dissolve

mori "Which is what this is."
"The blue fire's back and the little orbs hover lazily around Mori's body.  Their glow is admittedly beautiful but it's cold and no warmth eminates from them."
pov "What do they say?"
"Mori watches their lazy movements for a few seconds before he moves to sit on the brick wall, crossing one leg under him."
mori "Nothing much, really.  Sometimes premonitions, sometimes warnings.  They're not as rooted in reality as we are."

hide mori spirits srs with dissolve
show mori shirt srs with dissolve

pov "And you can turn into a demon cat to... find something?"
"To my surprise Mori scoffs loudly."
mori "Yeah, people.  I'm sent messages sometimes, kill a certain number of humans.  Find specific humans.  Deliver the souls to certain places, usually."
mori "Or lead them into traps to get preyed on and forced into loaded bargains by other demons."
"Honestly it's not what I expected to hear and I can't keep the revulsion off my face."
pov "You {i}what{/i}!?"
"He actually laughs at my reaction"

hide mori shirt srs
show mori shirt neu

mori "Oh, no, sorry.  I'm totally AWOL, I don't do anything for them.  I filled a contract once and after I realized what they were asking I just refused to work."
mori "Thats why the enforcers are always out here harping on about me being Contractbound and not fulfilling my end of the deal.  Fuck them though, I'm not doing that."
pov "So the enforcers are those... things."
mori "Yeah, they hide in human skins but those big stretched out crab things is their true nature."
pov "And they disguise themselves as cops?"
mori "Sometimes.  In the city, especially.  They can hide easiest in groups of humans, especially ones that are organized and trained to defend their own very strongly.  So... cops are ideal."
pov "But it doesn't have to be a cop..."
mori "No, it could be anyone."

"I shiver before I can help myself.  This is... a lot to take in but after everything I've seen with my own two eyes tonight..."

mori "If I was a good bootlicker and did what I was told, I would probably have more answers for you.  But I'm not about to drag a bunch of hapless humans into the same loaded deal I was."
mori "And I frankly don't care how many enforcer demons they send, they're not even that hard to kill."

pov "Mori, how long have things been this way?"
mori "I don't know, like threeish years maybe."

"He slides off the brick easily and moves just a tiny bit closer, eyeing th way his jacket sits on my shoulders detachedly."

mori "So is this the part where you pretend you're calm but then the second I turn around and lose sight of you I never see you again?"
"There's a lot of things right then that I want to say.  The audacity of this man, I swear-!"
pov "I'm sorry, you think you're scary?  I'm not even a little afraid of you."

hide mori shirt neu
show mori shirt smile

"Instead of looking irritated at this, he only looks mildly delighted."
mori "Really.  Not afraid of me but back in Pitrats you looked so scared in that crowd."
pov "Mori, you have toe beans.  Some of them are pink."

return