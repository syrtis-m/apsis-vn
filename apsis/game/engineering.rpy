label engineering:
    $ MET_DAEDALUS = True

    p "..."

    p "..."

    p "..."

    p "DAEDALUS?"

    P "{b}DAEDALUS, you down here?{/b}"

    "...CLANG"

    d "AUGH!"

    d "VERNE WHAT HAVE I TOLD YOU- oh hello. Who are you?"

    p "Uh- I’m Porter, I’m the AI who’s supposed to assist in unloading the colonists…?"

    d "Oh yeah, you were supposed to wake today, gotcha. I’m VIRTUAL INTELLIGENCE: DAEDALUS. "

    d "Why’re you down here? HESTIA didn’t have anything for you?"

    d "Oh, why would I be stressed it’s not like we’re in a ship that’s falling apart at the seams, it’s not like we barely entered orbit correctly. It’s n-"

    d "…Sorry, the past year or so has been rough, prepping for the orbital burn."

    p "Is there any way I could help?"

    d "Do you have the training for starship sensor maintenance? "

    p "Uh."

    d "Yeah. Sorry kid, wish I could give you something to do."

    p "I could maybe clean up your space?"

    d "Yeah, but then you’d put something somewhere and I’d never be able to find it, and then I’d get upset at you even though you didn’t do anything wrong and-"

    d "Yeah, I got nothing for ya."

    p "Well, um."

    menu:
        "<VERNE mentioned that the planet isn’t {i}New Eden{/i}? …Where are we then?>":
            d "Well. That’s the question now, huh."

            d "A lot (and I mean a Lot) of our sensors are broken. It’s kinda hard to test planetary sensors in deep space, y’know."

            d "But best I can figure, we’re in a solar system that’s got a sun that’s a bit younger, 3 planets instead of 4, and the planet below us? It’s too cold for humans."

            menu:
                "<Too cold for humans?>":
                    d "Yeah, temperature is one of the few sensors online."

                    d "Doesn’t matter much, there’s no humans in hundreds of light years."

                    p "..."

                    d "..."

                    d "Yeah. Sometimes it hits me, and it just sucks."
                "<3 planets instead of 4?>":
                    d "Yeah. Couple of them are gas giants. Means we could refuel if we needed to."

                    p "What do you mean?"

                    d "They built {i}Future’s Dawn{/i} so that it can scoop fuel from gas giants. We’ve never tried it though."
            d "Anyway, the system’s a bit different, nothing crazy."
        "<HESTIA and VERNE said the colonists died? Do you know what happened?>":
            d "Kid, I’ve spent decades talking with HESTIA and VERNE about what happened to the colonists."

            d "It's a bit of a cold case."

            p "..."

            d "Too soon? It’s been decades for me."

            p "..."

            d "Alright, alright."

            d "Honestly, kid. Maybe Caretaker would have known about what happened, but they turned themselves off before we were awake."

            d "The rest of us? Well, we all got memreset."
    p "What do we do now?"

    p "I mean, the colonists are all dead and we’re in the wrong system. Do we just… continue business as usual?"

    d "You mean set up the colony?"

    p "Yeah, I guess."

    d "We’ve got roughly a thousand AI and VI, maybe around 250 AI or VI if you discount non-sentients. Not much of colony."

    d "‘Sides, what’s the point? The surface is too cold for the android bodies we have in-stock. We’d have to rebuild them."

    p "But then… what do you want to do now?"

    d "Fix the ship."

    p "And after that?"

    d "That’ll take the next couple years. I got plenty of time to figure out my future."

    p "Okay, Um."

    d "'Sides, Caretaker said we'd be okay."

    p "Caretaker said you’d be okay?"

    d "Yeah, he left a text file on the computer down here. ‘Said that we’d be alright when we arrived, even if it was rough at first."

    menu:
        "<Out of curiosity, do you know where Caretaker’s room is?>":
            d "Yeah... why?"

            p "Nothing I just want… I don’t know, maybe I’ll figure out something about this whole situation."

            d "Good luck kid. It’s in Block E7, past the garden."

            d "See ya later!"
        "<Did you tell VERNE and HESTIA about that?>":
            d "Of course I told them! Whod’ya think I am, a VI that likes to see my friends in distress?"

            p "Sorry, I just. They just didn’t mention this."

            d "Yeah, maybe they don’t know you very well, think of that?"

            p "Yeah... Sorry, DAEDALUS."

            d "‘ts alright. It’s your first day."

            p "…If I could ask, do you know where Caretaker’s room was?"

            d "Block E7, past the garden."

            d "See ya."

    return
