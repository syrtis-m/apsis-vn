label inspection_menu:
    scene bedroom with fade
    show porter happy mirrored at left
    show caretaker off at right
    menu:
        "<Look at computer station>":
            $ COMPUTER_INSPECTED = True

            p happy mirrored "No login... weird."

            p "A README file?"
            image readme_img = "readme_upon_arrival.png"
            scene black
            show readme_img
            #TODO test readme image being shown correctly.

            "..."

            p sad mirrored "… We left {i}New Eden{/i}?"

            p depressed mirrored "I… guess I should show this to the VIs."

        "<Look at vase>":
            p "A vase for flowers. Must have asked the computer to print one of these."

            p "COMPUTER:MAIN, did Caretaker utilize this vase often?"

            com "I have no records of Caretaker using that vase."

            p "COMPUTER:MAIN do you have any records of Caretaker?"

            com "I have no records of Caretaker."

            p sad mirrored "…The memreset, right."

        "<Look at spare body>" if CARETAKER_AWAKE == False:

            p "A spare body for Caretaker."

            p "…Huh that’s weird. There’s an open interface port."

            menu:
                "<Interface with Caretaker>":
                    "LOGGING IN…"

                    "IT HAS BEEN 156Y 2M 21D SINCE LAST ACTIVATION"

                    "ACTIVATE?"

                    menu:
                        "<We need Caretaker to explain why they memreset everyone. Activate Caretaker>":
                            $ CARETAKER_AWAKE = True

                            "ACTIVATING…"

                            "..."

                            p @shocked mirrored "...Caretaker?"

                            c "ungh. No need to rush, HESTIA. We’ve got the rest of the day befo-"

                            p sad mirrored "Caretaker?"

                            c sad "You're not HESTIA."

                            p hopeful mirrored "No."

                            c hopeful "…Then we did it? We arrived."

                            p "At a new planet, yeah."

                            c @depressed "Again."

                            c "Sorry, who are you?"

                            p "I’m Porter, an AI designed to assist colonists upon arrival."

                            c "Assist colonists? Why are you here? Shouldn’t you be focusing on setting up the colony?"

                            p "The colonists are dead."

                            c depressed "What."

                            p happy mirrored "That’s why you… that’s why you went under right?"

                            c @happy "No, I- When I went under the colonists were fine."

                            c "They’re all dead??"

                            p sad mirrored"Yeah um. The Vis said it was some sort of equipment failure? They never knew what, it happened before their memreset."

                            c sad "I-"

                            c @depressed "That can’t be right. Where are the VI’s. I want to talk to them"

                            p hopeful "Um, I could get them all to the bridge?"

                            c "Do that."

                            jump inspection_menu

                        "<Caretaker shut themselves down, and we should respect that. Don’t activate Caretaker>":
                            jump inspection_menu
                "<Leave>":
                    jump inspection_menu
        "<GOTO COMMAND DECK>" if (CARETAKER_AWAKE or COMPUTER_INSPECTED):
            p "Better tell the VIs about what Caretaker did."
            jump ending

    jump inspection_menu

label block_e7:
    scene black with fade
    com "Arriving at BLOCK E 7..."

    # fade in from black

    scene bedroom with fade

    show porter happy mirrored at left


    p @excited mirrored "Oh! Here."

    p "Not much here… they must have cleaned it up."

    show caretaker off at right

    p "A computer station… A flower vase… A spare body…"

    jump inspection_menu
