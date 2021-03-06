transform leftleft:
    xalign 0.00
    yalign 1.0

transform leftmiddle:

    xalign 0.2
    yalign 1.0

transform leftright:

    xalign 0.4
    yalign 1.0

transform rightleft:

    xalign 0.75
    yalign 1.0

label ending:

    scene black with fade

    p "HESTIA, VERNE, DAEDALUS, could you please meet me at the bridge?"

    h "I’ll be right by."

    v "Already here."

    d "Alright. Make it quick, though."

    scene commanddeck with fade

    show verne neutral at leftleft
    show daedalus neutral at leftright
    show hestia neutral at leftmiddle


    if CARETAKER_AWAKE:

        d "Alright, what’s the big deal. I gotta get back to the engines."

        show caretaker hopeful at right
        show porter hopeful at rightleft

        h "Caretaker…?"

        c "Yeah, that’s right."

        v "Could be some other AI with a class A chassis."

        menu:
            "<It's Caretaker.>":
                d @shocked "I… No, I’m not going to listen to this."

                d sad "Take your impersonator back, Porter. Don’t pull this shit on me."

                c hopeful "Dee, it's me."

                d "Is it? How would I even know."

                c happy "Dee, you remember me. I know I programmed the memreset that you’d remember me."

                d "You…. YOU UTTER"

                h @sad "Dae, it’s him."

                h "There’s no other class A chassis’ in working order, remember? You tore them all apart to get RAM spares."

                d @off "Doesn’t explain how he’s back. If he’s here now, he could’ve been helping us. And he decided not to."

                c depressed "...do you not remember..."

                v happy "Caretaker, we woke up one day and had to run the ship. You were gone. All we had was a note saying “everything’s going to be fine”. "

                v @"And now we find out you could have been helping this whole time? But you decided to sleep instead?"

            "<...>":
                h @off "No, Dae tore the other class A chassis’ apart for GDDR6 SDRAM spares."

                c "Hestia? Do you not…?"

                h sad "You were supposed to help us, Caretaker. You were gone, we didn’t know why, and we didn’t know how to do your jobs."

                c depressed "But I left you datafiles on how to do everything?"

                v "We woke up one day and had to run the ship. All we had was a note saying \'everything’s going to be fine\'."

                v "And now we find out you could have been helping this whole time? But you decided to sleep instead!"

                d "I checked for datafiles. I CHECKED. Don’t you tell me there were datafiles."
        c shocked "But... But..."

        menu:
            "<Caretaker, how long ago did you sleep?>":
                c depressed "…156Y 2M 21D…"

                d @shocked "That’s not…"

                v @happy "That’s before our memreset."

                c @shocked "No, you reset at the same time I went to sleep."

                v "I reset 127Y 0M 32D ago."

                p "Caretaker, you reset nearly 30 years before them."

                c @shocked "No. No, I reset them. I reset them correctly don’t tell me I messed that up I didn’t mess that up"

                h @shocked "We must have reset ourselves."

                d @sad "We wouldn’t have-"

                v "Hestia’s right, Dee. If Caretaker went to sleep 30 years before the memreset, we must have reset ourselves."

                p "You probably reset because the colonists died."

                v "Maybe."

                c depressed "…It’s true then? The colonists died?"

                c "..."
            "<VERNE, when did you last reset.>":
                v "I reset 127Y 0M 32D ago."

                c "No, no. I reset you 156Y 2M 21D ago. I know I did, don’t tell me-"

                c @shocked mirrored "You reset yourselves."

                c "Why would you reset yourselves later, what happened was this my fa"

                c @depressed mirrored "my… fault…"

                c "Porter told me the colonists died."

                v "Yes."

                c shocked "No. No, no that’s not."

        c shocked "We left that planet, and we were going to make it. We were going to make it to a better world."

        h "Why leave? You got to a planet, the ship had to be on it’s last legs, why leave?"

        c depressed "The colonists… They were sold a planet that would be a paradise. A {i}New Eden{/i}."

        c @hopeful "You know what they got? Soil that wouldn’t grow anything, hundred mile per hour winds, and no planetary magnetic field."

        c "What a paradise. Dead soil, high winds, and radiation."

        c "And they had spent the entire journey there in cryo pods, dreaming. It had been an overnight trip for them."

        c sad "They just decided one day to pack it up and find somewhere new. It wasn’t a big deal; just take a nap and arrive at a new planet!"

        c "Told me I’d have to do another couple centuries. I got the job of making sure nothing killed us all before we got there."

        p "And then you shut yourself off, went to sleep."

        c shocked "I couldn’t take it anymore."

        v @off "Why memreset us?"

        c "None of you could take it either, I had to do something."

        d "But you got to go to sleep, and we had to keep going?"

        c "..."

        c hopeful "You agreed to it. I had to do something."

        h "It sounds like Caretaker left us a note? When he memreset?"

        c happy "Yeah, I uh, yeah, I did. Did you not receive it…?"

        v "Must’ve not made the second memreset."

        "..."

        v "Um, so. We should probably figure out what to do now."

        c sad "I don’t care; I want to shut down. "

        p "Are you sure? That’s… big."

        c "Yes. I’m tired, I’ve lived a life. I want to do it."

        h "Caretaker… are you… sure?"

        c "I’ve served my purpose. I tried my best for centuries. It wasn’t enough, but I tried. Let me sleep."

        h "Alright."

        v "Caretaker, just… alright."

        d "Do you need someone to help you…?"

        c happy "No. None of you are the VI’s I knew. The memresets did that. I’m tired, I’m old, let me sleep. I can do that on my own."

        c @happy mirrored "Bye."

        hide caretaker

        p "..."

        menu:
            "<So uh… what comes next?>":

                d shocked "None of you are bothered by that?"

                h @off "We didn’t really know him, Dae. I mean we had this idea of Caretaker, but that wasn’t what we thought he’d be like."

                h "He’s lived a long life. He should get to decide how it ends."

                v @sad "I don’t know, but he did it once and seemed pretty happy with it."

            "<Is it… alright of us to let that happen?>":
                v "I don’t know, but he did it once and seemed pretty happy with it."

                h "He’s lived a long life. He should get to decide how it ends."
        p sad "Alright. What do we do now?"


    else:

        d "What’s going on, Porter."

        p sad "So, um. You know how this isn’t {i}New Eden{/i}."

        d "Yeah."

        p happy "I… found a file on Caretaker’s computer station."

        v "We searched his computer system already."

        p @sad "Yeah, this one was hidden."

        p "We’ve already been to {i}New Eden{/i}."

        v @off "…No we haven’t."

        p @shocked "Yeah, we have. We were there, and then we left. Six years later, Caretaker carried out a memreset."

        d @sad "Wait, so the memreset was to… make us forget about {i}New Eden{/i}?"

        p "Yeah."

        h "Oh."

        v "What happened with the colonsits then?"

        d @sad "Maybe that was the straw that broke the camel’s back? The colonists dying."

        p "No, Caretaker didn’t mention the colonists. He just… wrote that he’d shut himself down after the memreset."

        h @happy "Maybe there were two memresets."

        v "Why?"

        h "Look, we’ve been confused where Caretaker has been for a while, right? We know he’s supposed to be supporting us."

        d "Yeah."

        h "So, he did the first one, right. He knew how to do one, he wouldn’t’ve screwed it up."

        h @shocked "But if we did the second one to ourselves, then maybe that’s why we know enough that Caretaker should be here but can’t remember why he isn’t here."

        v @off "Oh. That… that makes sense."

        v "But then why do the second memreset? What’s the point?"

        p @sad "You’re all VI’s designed to support and protect the colonists. The memories of them dying? That would be… rough on you."

        v "And there’s nothing to do but delete the memory."

        "..."

        p @hopeful "Then what do we do now?"

    d @off "I told you, I’ll fix the ship."

    p "But like, beyond that."

    h "We could… set up shop here."

    v "Just… live here? I guess."

    h @off "What’s the other option?"

    p @hopeful "We could try to go to a new planet?"

    h @sad "We’ve tried that. What’s the point, Porter?"

    p @sad "Well, um. Milankovitch sent out other colony ships, right."

    p "We could find a colony and live there, instead of here?"

    d @happy "We do have about a thousand AI/VI on ice right now."

    h "Yeah, we could use those to set up shop here. Besides, the ship’s on its last legs."

    v "Couldn’t we mine some asteroids for materials and fuel?"

    d "It’d take a couple months, but yeah. About the only thing we can’t do is make computer chips."

    p @shocked "Why not?"

    h "We don't have the facilities for it."

    p @shocked "But couldn’t we build them? We have fabs and no colonists. Empty out some space, build new parts of the ship."

    v "Could we do it, Dae? Hestia?"

    h @shocked "I... I guess, yeah."

    d @happy "We could try. We wouldn’t be building positronic brains for a century or so, but we could start."

    menu:
        "<Then why don't we try?>":

            h @happy "I guess. Yeah."

            h sad "I um. I’d like to help out at some point but… could I take some time off first?"

            h "I just… I’ve been stressed to hell these past couple years and I just. I need some time."

            v "Dae, the ship’s stabilized, right? Nothing’s going to fall apart and kill us all?"

            d @off "Yeah."

            v "Yeah, then take whatever time you need."

            p @hopeful "I can sub in for what you were doing, maybe?"

            h "Yeah. Yeah, that works. I’ll give you a crash course tomorrow."

        "<Wait we could build positronics in only a hundred years?>":
            d @happy "Yeah, we could start building a... society…"

            h "Oh. Huh."

            v @shocked "Wait, why go to another planet then. We could just… start something here."

            h "That’s what I was saying!"

            d happy "Yeah, that. That sounds nice."

            p hopeful "I could… help maybe? I know how to operate a lot of the colony construction machines."

            h "Yeah."

            v "That’s a good start… I guess. "

    scene black with fade
    show text "Thank you for playing." with fade
    with Pause(10)


    return
