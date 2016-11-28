#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Information texts and logos for the game Dungeon.
"""
import adventure

def gameLogo():
    """
    Store ascii logo of the game in a separat variabel as a raw string
    """
    return r"""
































    ▓█████▄  █    ██  ███▄    █   ▄████ ▓█████  ▒█████   ███▄    █
    ▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒ ██ ▀█   █
    ░██   █▌▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░  ██▒▓██  ▀█ ██▒
    ░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒
    ░▒████▓ ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░▒████▒░ ████▓▒░▒██░   ▓██░
    ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒
    ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
    ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░   ░    ░   ░ ░ ░ ▒     ░   ░ ░
    ░       ░              ░       ░    ░  ░    ░ ░           ░
    ░









    """


def helpText():
    """
    Command instructions
    """
    print(r"""
        x-------------------------------------------------x
        |   _  _ ____ _    ___     ___  ____ ____ ____    |
        |   |__| |___ |    |__]    |__] |__| | __ |___ .  |
        |   |  | |___ |___ |       |    |  | |__] |___ .  |
        |                                                 |
        x-------------------------------------------------x

------------------------Main Controls------------------------

 python3 adventure.py +
 -h, --help  -  Gives you this information page.
 -i, --info  -  Information about the game.
 -v, -- version  -  Game version.
 -a, --about  -  About the creator of the game.
 -c, --cheat  -  If you just want to win the game.


------------------------IN-GAME Controls------------------------

                        Command Controls:

 h, help  -  Gives you this information page.
 look  -  Description of the room you're currently in.
 forward  -  Go to the next room, if possible.
 back  -  Go back to the previous room, if possible.
 hint  -  Get a hint if you're stuck.
 q, quit  -  Leave the game.
 object  -  Get printout of all objects in room.


                        Object controls:

 inspect [object]  -  Get description of particular object.
 grab [object]  -  Grab the object (if possible).
 kick [object]  -  Kick the object (and if possible, destroy it!).
 open [object]  -  Open the object (if possible).
 move [object]  -  Move the object (if possible).


                        Inventory controls:

inv, inventory  -  Get list of all objects you're currently holding.
drop [object]  -  Throw away the object you don't want to keep any more.
use [object]  -  Try to use the object.
    """)


def infoText():
    """
    Information about the game
    """
    print(r"""
                    x~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~x
                    |    ____ ___  ____ _  _ ___    |
                    |    |__| |__] |  | |  |  |     |
                    |    |  | |__] |__| |__|  |     |
                    |                               |
                    |        ___ _  _ ____          |
                    |         |  |__| |___          |
                    |         |  |  | |___          |
                    |                               |
                    |     ____ ____ _  _ ____       |
                    |     | __ |__| |\/| |___ .     |
                    |     |__] |  | |  | |___ .     |
                    |                               |
                    x~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~x

    Dungeon is a short text based game inspired by Dungeons & Dragons,
    Hitchhikers Guide To The Galaxy, Monkey Island and other bigger role playing games.

    A seven room puzzle escape game that takes place in a mystical dungeon
    where the hero and his newfound companion have to find the way through
    each room to get one step closer to freedom!
    Smashing, grabing, using and observing objects and the rooms themselves are the
    main actions that you do and (hopefully) will take you further
    to the goal...


    For nice ASCII-fonts, check out:
    http://patorjk.com/software/taag/#p=display&h=0&f=3D%20Diagonal&t=
    ASCII-art:
    http://ascii.co.uk/art
    """)


def versionText():
    """
    Prints out version of the program.
    """
    programVersion = "1.1.0"

    print(gameLogo())
    print("""                   Program version: """, programVersion)


def aboutText():
    """
    Information about the creator of the game
    """
    print(r"""
            x~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~x
            |          ____ ___  ____ _  _ ___          |
            |          |__| |__] |  | |  |  |           |
            |          |  | |__] |__| |__|  |           |
            |                                           |
            |              ___ _  _ ____                |
            |               |  |__| |___                |
            |               |  |  | |___                |
            |                                           |
            |    ____ ____ ____ ____ ___ ____ ____      |
            |    |    |__/ |___ |__|  |  |  | |__/ .    |
            |    |___ |  \ |___ |  |  |  |__| |  \ .    |
            |                               	        |
            x~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~x

    The name of the creator of the game Dungeon is Max Sundberg.

    Born and raised in Uppsala, Sweden and have started the course packages
    'webutv' and 'webprog' at Blekinge Tekniska Högskola.
    I'm a foodtruck burger-flipping guy who smacks the drums and travels the world
    when the keyboard's not in my lap to get through the courses.

    For more info about the courses (in Swedish), please visit my webpage:
    http://www.student.bth.se/~masb16/dbwebb-kurser/htmlphp/me/kmom06/me6/me.php
    """)


def cheatText():
    """
    Runthrough of the whole game. Fastest way possible.
    """
    print("""
                            Room 1:
    Grab stick
    Grab shiny thing
    Use 'barrel-key'
    Use 'sticky-stick'
    Forward

                            Room 2:
    Kick 'mirror'
    Use 'sticky-stick'
    Inspect 'glass shatters'
    Grab 'glass shatters'
    Use 'mirror-key'
    Forward

                            Room 3:
    Use 'glass shatter'
    Inspect 'destroyed skin'
    Use 'bone-key'
    Forward

                            Room 4:
    Grab 'pictures'
    Choose picture 3 and 4
    Use 'water', any option works
    Use 'bowl'
    Inspect 'stone bowl'
    Use 'blood'
    Forward

                            Room 5:
    Inspect 'box'
    Use 'magnet'
    Forward

                            Room 6:
    Use 'magnet'
    Inspect 'button', press 'y'
    Forward

                            Room 7:
    Kick 'skin'
    Kick 'chairs'
    Kick 'key'
    Kick 'barrel'
    Kick 'olaf', press 'y'

                And then you die any way! Whoop whoop!
    """)



def theEnd():
    """
    The End ASCII and options to quit or restart the game.
    """
    print(r"""
































        ████████▓ ██░ ██ ▓█████    ▓█████  ███▄    █ ▓█████▄
        ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
        ▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ▓██  ▀█ ██▒░██   █▌
        ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
          ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒████▒▒██░   ▓██░░▒████▓
          ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒
            ░     ▒ ░▒░ ░ ░ ░  ░    ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒
          ░       ░  ░░ ░   ░         ░      ░   ░ ░  ░ ░  ░
                  ░  ░  ░   ░  ░      ░  ░         ░    ░
                                                      ░











""")
    while True:
        restart = input("Play again?\n(y/n): ")
        try:
            if restart == "y":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                adventure.main()
            elif restart == "n":
                quit()
        except Exception:
            continue
