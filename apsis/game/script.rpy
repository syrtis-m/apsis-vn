# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define com = Character("COMPUTER:MAIN")
define p = Character("AI:Porter", image="porter")
define c = Character("AI:Caretaker", image="caretaker")
define v = Character("VI:VERNE", image="verne")
define h = Character("VI:HESTIA", image="hestia")
define d = Character("VI:DAEDALUS", image="daedalus")

label ship_map:
    scene hallway with fade
    show porter hopeful mirrored at left
    menu:
        "<GOTO CRYONICS BAY 2>" if MET_HESTIA == False:
                call cryonics_bay from _call_cryonics_bay
        "<GOTO COMMAND DECK>" if MET_VERNE == False:
                call command_deck from _call_command_deck
        "<GOTO ENGINEERING>" if ((MET_HESTIA and MET_VERNE) and (MET_DAEDALUS ==False)):
                call engineering from _call_engineering
        "<GOTO BLOCK E7>" if MET_DAEDALUS:
                jump block_e7
    jump ship_map
# The game starts here.

label start:

    python:
        MET_HESTIA = False
        MET_VERNE = False
        MET_DAEDALUS = False
        CARETAKER_AWAKE = False
        COMPUTER_INSPECTED = False
        QHV_FLIGHT_TIME = False

    jump introduction

    return
