label introduction:

    scene eden with fade

    n "NASA calls it Kepler-186f. We call it {i}New Eden{/i}."

    n "With an Earth-like orbit, liquid water, and comfortable temperatures year-round, it’s a new home for humanity."

    n "A state-of-the-art colony ship, {i}Future’s Dawn{/i}, will ferry colonists to the new world. When it’s finished, {i}Future’s Dawn{/i} will carry 30,000 passengers to a new home in the stars."

    n "Crewed and supported by over 1,000 AI & VI units, {i}Future’s Dawn{/i} represents the cutting edge of interstellar technology."

    n "Upon arrival, AI units will build and run an upscale colony – no need to plow fields, chop wood, or fiddle with technology. AI will handle everything so you can relax in Eden."

    n "Reserve your spot today - join humanity’s new beginning!"

    n "{i}New Eden{/i} Colony Corporation is a subsidiary of Milankovitch. Milankovitch: Building the Future, Today."

    scene black with fade
    with Pause(3)

    #TODO get a bg of the area porter wakes up in

    com "Good morning, Porter."

    com "Today is Monday, January 1st, 0000."

    com "We have arrived in orbit above {i}New Eden{/i}."

    com "How was your sleep?"

    menu:
        "<It was alright>":
            com "Good, Porter"

            com "Your diagnostics are all green. Please prepare to assist HESTIA with preparing to wake the colonists."

        "<Sleep? I'm an AI>":

            com "Yes, Porter. You’ve been in sleep mode since we left the Sol system."

            com "Your diagnostics are all green. Please prepare to assist HESTIA with preparing to wake the colonists."

        "<Where am I??>"
            com "You’re onboard the {i}Future’s Dawn{/i}. We’ve reached {i}New Eden{/i}."

            com "Your diagnostics are all green. Please prepare to assist HESTIA with preparing to wake the colonists."

    menu:
        "<What are the conditions planetside?>":
            com "Average Surface Gravity is: NaN m/s."

            com "Atmospheric Composition is: ERROR 212."

            com "Average Temperature is: NaN"

            com "Surface Biosign Monitor reports: ERROR 325."

            p "Errors?"

            com "I’m sorry Porter, I don’t know what that means."

            p "What does “Atmospheric Composition is ERROR 212” mean?"

            com "I’m sorry Porter, I don’t know what that means."

            p "..."

    menu:
        "<Who should I report problems to?>":
            com "VERNE oversees Futures Dawn. VERNE is currently in COMMAND DECK"

        "<Where is HESTIA?>":
            com "HESTIA is currently in CRYONICS BAY 2"

    com "Please prepare to aid HESTIA with preparing to wake the colonists."

    p "Hm..."

    jump ship_map
