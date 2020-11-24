#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
import py_compile
import zlib

beemovie = """According to all known laws of aviation, there is no way that a
bee should be able to fly. Its wings are too small to get its fat little body
off the ground. The bee, of course, flies anyway. Because bees don’t care what
humans think is impossible. SEQ. 75 - “INTRO TO BARRY” INT. BENSON HOUSE - DAY
ANGLE ON: Sneakers on the ground. Camera PANS UP to reveal BARRY BENSON’S
BEDROOM ANGLE ON: Barry’s hand flipping through different sweaters in his
closet. BARRY Yellow black, yellow black, yellow black, yellow black, yellow
black, yellow black...oohh, black and yellow... ANGLE ON: Barry wearing the
sweater he picked, looking in the mirror. BARRY (CONT’D) Yeah, let’s shake it up
a little. He picks the black and yellow one. He then goes to the sink, takes the
top off a CONTAINER OF HONEY, and puts some honey into his hair. He squirts some
in his mouth and gargles. Then he takes the lid off the bottle, and rolls some
on like deodorant. CUT TO: INT. BENSON HOUSE KITCHEN - CONTINUOUS Barry's
mother, JANET BENSON, yells up at Barry. JANET BENSON Barry, breakfast is ready!
CUT TO: "Bee Movie" - JS REVISIONS 8/13/07 1. INT. BARRY'S ROOM - CONTINUOUS
BARRY Coming! SFX: Phone RINGING. Barry’s antennae vibrate as they RING like a
phone. Barry’s hands are wet. He looks around for a towel. BARRY (CONT’D) Hang
on a second! He wipes his hands on his sweater, and pulls his antennae down to
his ear and mouth. BARRY (CONT'D) Hello? His best friend, ADAM FLAYMAN, is on
the other end. ADAM Barry? BARRY Adam? ADAM Can you believe this is happening?
BARRY Can’t believe it. I’ll pick you up. Barry sticks his stinger in a
sharpener. SFX: BUZZING AS HIS STINGER IS SHARPENED. He tests the sharpness with
his finger. SFX: Bing. BARRY (CONT’D) Looking sharp. ANGLE ON: Barry hovering
down the hall, sliding down the staircase bannister. Barry’s mother, JANET
BENSON, is in the kitchen. JANET BENSON Barry, why don’t you use the stairs?
Your father paid good money for those. "Bee Movie" - JS REVISIONS 8/13/07 2.
BARRY Sorry, I’m excited. Barry’s father, MARTIN BENSON, ENTERS. He’s reading a
NEWSPAPER with the HEADLINE, “Queen gives birth to thousandtuplets: Resting
Comfortably.” MARTIN BENSON Here’s the graduate. We’re very proud of you, Son.
And a perfect report card, all B’s. JANET BENSON (mushing Barry’s hair) Very
proud. BARRY Ma! I’ve got a thing going here. Barry re-adjusts his hair, starts
to leave. JANET BENSON You’ve got some lint on your fuzz. She picks it off.
BARRY Ow, that’s me! MARTIN BENSON Wave to us. We’ll be in row 118,000. Barry
zips off. BARRY Bye! JANET BENSON Barry, I told you, stop flying in the house!
CUT TO: SEQ. 750 - DRIVING TO GRADUATION EXT. BEE SUBURB - MORNING A GARAGE DOOR
OPENS. Barry drives out in his CAR. "Bee Movie" - JS REVISIONS 8/13/07 3. ANGLE
ON: Barry’s friend, ADAM FLAYMAN, standing by the curb. He’s reading a NEWSPAPER
with the HEADLINE: “Frisbee Hits Hive: Internet Down. Bee-stander: “I heard a
sound, and next thing I knew...wham-o!.” Barry drives up, stops in front of
Adam. Adam jumps in. BARRY Hey, Adam. ADAM Hey, Barry. (pointing at Barry’s
hair) Is that fuzz gel? BARRY A little. It’s a special day. Finally graduating.
ADAM I never thought I’d make it. BARRY Yeah, three days of grade school, three
days of high school. ADAM Those were so awkward. BARRY Three days of college.
I’m glad I took off one day in the middle and just hitchhiked around the hive.
ADAM You did come back different. They drive by a bee who’s jogging. ARTIE Hi
Barry! BARRY (to a bee pedestrian) Hey Artie, growing a mustache? Looks good.
Barry and Adam drive from the suburbs into the city. ADAM Hey, did you hear
about Frankie? "Bee Movie" - JS REVISIONS 8/13/07 4. BARRY Yeah. ADAM You going
to his funeral? BARRY No, I’m not going to his funeral. Everybody knows you
sting someone you die, you don’t waste it on a squirrel. He was such a hot head.
ADAM Yeah, I guess he could’ve just gotten out of the way. The DRIVE through a
loop de loop. BARRY AND ADAM Whoa...Whooo...wheee!! ADAM I love this
incorporating the amusement park right into our regular day. BARRY I guess
that’s why they say we don’t need vacations. CUT TO: SEQ. 95 - GRADUATION EXT.
GRADUATION CEREMONY - CONTINUOUS Barry and Adam come to a stop. They exit the
car, and fly over the crowd to their seats. * BARRY * (re: graduation ceremony)
* Boy, quite a bit of pomp...under * the circumstances. * They land in their
seats. BARRY (CONT’D) Well Adam, today we are men. "Bee Movie""".replace('\n', '')

data = open('payload.py', 'rb').read()
compress = zlib.compress(data)
encoded = base64.b64encode(compress).decode('ascii') + '_ _ _' + base64.b64encode(beemovie.encode('ascii', 'ignore')).decode('ascii')

k = open('logo.txt').read()

out = []

i = 0

new = ""
for byte in k:
    if i < len(encoded) and byte == '#':
        new += encoded[i]
        i += 1
    else:
        new += byte

cool = 'magic = """\n{}\n"""'.format(new)

execy = base64.b64encode(b"""
import random
import hashlib
import zlib
exec(zlib.decompress(base64.b64decode(''.join(magic.replace('.','').split('\\n')).split('_ _ _')[0])))
fun()
""").decode('ascii')

print(open('./template.py').read().format(cool, execy))
