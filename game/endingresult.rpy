
label endingresult:

if ending_progress > 2:
    jump monster
else:
    jump human

label monster:
    "monster"

label human:
    "human"

return