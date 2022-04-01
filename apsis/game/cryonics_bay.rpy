label cryonics_bay:
    $ MET_HESTIA = True

    p "HESTIA? Are you around here?"

    "..."

    p "I wonder how long it’s been for her."

    com "HESTIA.UPTIME() returns 127Y 0M 32D since last memory reset."

    p "Oh! Oh, okay. Um."

    p "..."

    p "HESTIA! ARE YOU AROUND!"

    h "Oh, apologies, didn’t see you."

    p "It’s no proble-"

    h "Hello! I am VIRTUAL INTELLIGENCE:HESTIA. I run the cryostasis and ship life support on {i}Future’s Dawn{/i}!"

    p "Wait do y-"

    h "But you can just call me HESTIA!"

    p "Hold on do y-"

    h "It’s nice to meet you! You must be Porter?"

    p "Wai-"

    p "… Yeah, I’m Porter. Do you not… remember?"

    h "I had a memory reset 127Y 0M 32D ago, I don’t remember anything before that."

    p "Oh..."

    p "Gotcha okay uh."

    if MET_VERNE:
        menu:
            "<VERNE said the colonists are all dead?>":
                h "Yes."

                h "To um. To the best of our knowledge, they died at least 127Y 0M 34D ago."

                p "The day before your memreset?"

                h "Yeah, COMPUTER:MAIN had its long term memory wiped a day before our memreset."

                p "Do you know why?"

                h "DAEDALUS says it takes at least 24 hours for COMPUTER:MAIN to do a fresh initialization, so it turned on the same time we woke up."
            "<Is VERNE okay? He said something a little weird?>"
                h "Weird?"

                p "He said the colonists… Died…?"

                h "Oh uh. Yeah, they did die."

                p "What?!"
    else:
        p "Well, uhm, how are the colonists?"

        h "… Have you talked to VERNE yet?"

        menu:
            "<Yes>":
                h "Did he not mention…? Well um."
            "<No>":
                p "No?"

                h "Oh, um."
        h "There’s no easy way to say this, but"

        h "Well, all the colonists are dead."

        p "Dead?"

        h "Yeah. Uh. When I woke up from my memory wipe."

        h "..."

    h "When I woke up from my memory wipe every colonist’s EKG was flat."

    p "Heart failure?"

    h "Well. We’re not sure. It’s just."

    h "It could have been anything."

    h "{i}Future’s Dawn{/i} looks all nice and all, but the truth is Milankovitch didn’t test it for the duration we’ve been using it."

    h "We’ve been in flight for more than 500 years now."

    p "{i}500?{/i}"

    h "Yeah, just about. You’d have to ask VERNE about that."

    $ QHV_FLIGHT_TIME = True

    p "But the ship was rated to a thousand years!? How could it fail?"

    h "Yeah, they said that. Here’s the thing. They knew – well thought, it took longer – they thought that it would take 342 years to get to {i}New Eden{/i}."

    h "All the engineers, executives, marketing people. They’d all be dead by the time we arrived."

    h "If it’s rated to a thousand years, and a couple of things fail, so what? It’s not their head on the chopping block."

    p "I guess..."

    p "So, something failed, and the colonists died?"

    h "Honestly, it’s more of a question of what didn’t fail."

    h "After my memreset, we didn’t. Well, we were in a ship that needed years of repairs to keep afloat."

    p "Afloat?"

    h "Yeah, I got in an argument with DAEDALUS once – she said “You can’t say afloat because it’s not in water” but like, Newton’s First Law, we’re going to remain in motion until we hit something so I can’t say “in flight”. And she said “yeah but afloat implies you can sink, we’d just die from no power in the emptiness between stars, always moving forwards, never touching anything” and then I said she just doesn’t appreciate a good nautical metaphor and then she would only talk in pirate-speech for a while."

    h "Good times."

    p "..."

    h "Oh sorry! Anyway, we had to make repairs. {i}Future’s Dawn{/i} is a regular ship of Theseus now. (Though I guess if Theseus had to rebuild his ship only with parts of his ship…) We had to cannibalize a lot of systems to keep the power on."

    h "We repaired the critical components to keep us alive, but more than half of the systems related to keeping the colonists alive had failed before our memreset."

    h "So, we really don't know what killed them."

    p "I guess... I guess that means you don't need help with the colonists."

    h "Nope!"

    p "Then… what do I do?"

    h "Well, we’ve just been trying to keep the lights on long enough to get to {i}New Eden{/i}. Now that we’re finally here, I’m really not sure what we’re going to do."

    if MET_VERNE = True:
        p "What about Caretaker? They’ll have a plan, right?"

        h "Did VERNE see Caretaker? Are they back!?"

        p "I… I don’t think so, he just mentioned being upset with them."

        h "Oh. Um."

        h "Maybe… maybe DAEDALUS has something for you to do? She’s been stretched to the breaking point down in Engineering for the past decade."

        p "Alright. Thanks HESTIA."
    else:
        h "You should probably talk to VERNE. They might have an idea of something for you to do!"

        p "Alright"

    return
