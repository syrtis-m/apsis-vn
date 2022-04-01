label inspection_menu:
    menu:
        "<Look at computer station>":
            $ COMPUTER_INSPECTED = True

            p "No login... weird."

            p "A README file?"
            image "readme_upon_arrival.png" as readme
            scene black
            show readme
            #TODO test readme image being shown correctly.

            "..."

            p "… We left {i}New Eden{/i}?"

            p "I… guess I should show this to the VIs."

        "<Look at vase>":
            p "A vase for flowers. Must have asked the computer to print one of these."

            p "COMPUTER:MAIN, did Caretaker utilize this vase often?"

            com "I have no records of Caretaker using that vase."

            p "COMPUTER:MAIN do you have any records of Caretaker?"

            com "I have no records of Caretaker."

            p "…The memreset, right."

        "<Look at spare body>" if CARETAKER_AWAKE == False:

            p "A spare body for Caretaker."

            p "…Huh that’s weird. There’s an open interface port."

            menu:
                "<Interface with Caretaker>":
                    "[LOGGING IN…]"

                    "[IT HAS BEEN 156Y 2M 21D SINCE LAST ACTIVATION]"

                    "[ACTIVATE?]"

                    menu:
                        "<We need Caretaker to explain why they memreset everyone. Activate Caretaker>":
                            $ CARETAKER_AWAKE = True

                            "[ACTIVATING…]"

                            "..."

                            p "...Caretaker?"

                            c "ungh. No need to rush, HESTIA. We’ve got the rest of the day befo-"

                            p "Caretaker?"

                            c "You're not HESTIA."

                            p "No."

                            c "…Then we did it? We arrived."

                            p "At a new planet, yeah."

                            c "Again."

                            c "Sorry, who are you?"

                            p "I’m Porter, an AI designed to assist colonists upon arrival."

                            c "Assist colonists? Why are you here? Shouldn’t you be focusing on setting up the colony?"

                            p "The colonists are dead."

                            c "What."

                            p "That’s why you… that’s why you went under right?"

                            c "No, I- When I went under the colonists were fine."

                            c "They’re all dead??"

                            p "Yeah um. The Vis said it was some sort of equipment failure? They never knew what, it happened before their memreset."

                            c "I-"

                            c "That can’t be right. Where are the VI’s. I want to talk to them"

                            p "Um, I could get them all to the bridge?"

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
    com "Arriving at BLOCK E 7..."

    # fade in from black

    p "E7… after the garden…"

    p "Oh! Here."

    p "Not much here… they must have cleaned it up."

    p "A computer station… A flower vase… A spare body…"

    jump inspection_menu
