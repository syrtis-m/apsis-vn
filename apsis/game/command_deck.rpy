label command_deck:
    $ MET_VERNE = True

    if MET_HESTIA = False:
        p "Hello? I’d like to report a problem with COMPUTER:MAIN?"

        v "Hold on a sec, doin something important here."

        "..."

        v "Gotcha! Okay. You must be Porter, the colonist assistant AI."

        v "I’m VIRTUAL INTELLIGENCE:VERNE. Whatd’ya need?"

        p "Well, when I woke, COMPUTER:MAIN gave error messages when I asked about surface environmental conditions?"

        v "…And you decided to come here before talking to HESTIA about the colonists?"

        menu:
            "<It’s important that everything is working before the colonist’s wake.>":
                v "Kid, it’s just us out here. We’re hundreds of light years from Milankovitch Corporate. You don’t need to be all… uptight. "

                p "..."

                v "'Sides, the colonists are dead."

            "<It might be a time-sensitive problem. The colonists have slept for a couple hundred years, they can sleep for a day more.>":
                v "Well, you're kinda right."

                p "What do you mean."

                v "Kid... The colonists are dead."

        p "What."

        v "Yeah. Equipment failure, we don't know what exactly."

        p "But the equipment was rated-"

        v "HAH! It may have been rated for a thousand years, but it still failed."

        p "I. What do we do? Should we turn around?"

    else:
        p "Hello? VERNE?"

        v "Hold on a sec, doing something important here."

        "..."

        v "Gotcha! Okay. You must be Porter. HESTIA dm’ed me – you need something to do?"

        p "Yeah, just. HESTIA told me all the colonists were dead. That’s not just… they’re really all dead?"

        v "Yeah. Turns out Milankovitch didn’t exactly build the best cryo systems when they knew they’d never see any of the colonists again."

        v "Why give a shit when there’s no future profit, yknow?"

        menu:
            "<{i}Future’s Dawn{/i} was certified for 1000 years by Forbes and JD Power.>":
                v "Uh huh. Sure was."

                v "Coincidentally, how much advertising do you think Milankovitch bought in Forbes?"

                v "And JD Power? Milankovitch paid them to use that certification in advertising."

            "<But wouldn’t Milankovitch want everyone to arrive safely?>":
                v "Oh, it wasn’t intentionally malicious."

                v "Just, yknow, what really made them money was how nice their ads were, not the reliability of cryo pods."

                v "Who do you think gets assigned more budget? The “profit center” or the “cost center.”"

            p "Um. So, we’re finally in orbit then. What comes next now? Should we turn around?"

    v "We couldn’t make it to Earth. ‘Sides, even if we went back, we’re all VI and AI. Nobody would care."

    p "Then what?"

    v "Well for the past couple hundred years we’ve been drifting through space."

    v "Finally hit a gravity well, so we’ve set up shop here."

    p "We’re at {i}New Eden{/i}? Right?"

    v"Well. Not exactly"

    p "{i}Not exactly?{/i}"

    v "So, um. The thing is. We’re at a star but it doesn’t match the parameters that we have for what {i}New Eden{/i} is supposed to be like."

    p "Like there’s an extra planet they missed during surveying for the mission? That’s pretty minor all things considered."

    v "The star's too young."

    p "...Huh."

    menu:
        "<How is it possible for us to end up at the wrong star?>":
            p "Newton’s first law, we should be going in a straight line until we get to the right star."
        "<Is it possible that our sensors are miscalibrated?>":
            v "Well, you’d have to talk to DAEDALUS for that. She’s pretty certain they aren’t, and I’m inclined to take her word for it."

            p "Well. Wrong star. How on earth?"
    v "My hypothesis, and this is a bit of a stretch so hear me out, is that the software didn’t adequately plan for gravity."

    v "The force exerted by gravity decreases exponentially the further an object is away from another object. But we’ve been in flight for a long time. They must have missed something small, and it pulled us off course."

    p "…But we still ended up at a star? What are the odds of that?"

    v "Slim, I know. But it’s all I’ve got."

    if QHV_FLIGHT_TIME:
        p "HESTIA mentioned we’ve been in flight for at least 500 years… do you think that?"

        v "Yeah, that’s the best piece of evidence for this theory."

        p "How would we… figure that out?"

        v "Hell if I know. Maybe DAEDALUS could figure something out, we’ve been focused on getting the ship ready to enter orbit for the past decade or so."

    else:
        v "DAEDALUS might have a better idea, I just fly the ship."

    p "By the way… is Caretaker around somewhere?"

    v "Not a lot of places to wander off, we’re an island in the endless void."

    v "But he… after the memreset we found a spare body of his, but not much else. He probably shut himself down at some point."

    v "Could certainly be a lot of use right now instead of rusting in a corner."

    menu:
        "<It couldn’t have been easy, living all this time.>":
            v "It wasn’t. For any of us. But we kept going."

            p "…Caretaker isn’t you, VERNE."

            v "Yeah, I know. He’s an AI and I’m just a VI."

            p "Not that, I mean-"

            if MET_HESTIA:
                v "Save it. You should go talk to DAEDALUS."

            else:
                v "Save it. You should go talk to HESTIA."

        "<Oh… I was excited to see them again.>":
            v "Yeah, I wanted to meet him too."

            v "I’m sorry, I don’t mean to speak ill of those passed."

            v "I just."

            p "Yeah."

            "..."

            if MET_HESTIA:
                v "Um, okay. Well. You should go talk to DAEDALUS."

            else:
                v "Um, okay. Well. You should go talk to HESTIA."

    return
