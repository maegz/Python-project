#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

﻿    ▓█████▄  █    ██  ███▄    █   ▄████ ▓█████  ▒█████   ███▄    █
    ▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒ ██ ▀█   █
    ░██   █▌▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░  ██▒▓██  ▀█ ██▒
    ░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒
    ░▒████▓ ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░▒████▒░ ████▓▒░▒██░   ▓██░
    ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒
    ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
    ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░   ░    ░   ░ ░ ░ ▒     ░   ░ ░
    ░       ░              ░       ░    ░  ░    ░ ░           ░
    ░
				     By: Max Sundberg, version 1.0,
							2016-03-20
------------|
Story Line: |
------------|
"""
import rooms

def roomEntry(room):
    """
    Intro text for each room the player enters.
    """
    name = ""
    # room 1
    if room == 0:
        input("""
    You wake up in a pitch black room, head pounding and body shaking from dehydration.
    The heat is unbearable and suddenly you hear a grunt from somewhere in the room.
    By carefully asking 'Hello?' into the darkness in hope for someone to help you, the grunt stops.
    A rasping whisper finally answers:
        - Wahh... waaaaaater...!""")
        input("""
    You try to fight against the headache and squint as hard as you can, in hope of adjusting the eyes
    enough to the dark that you can see this thirsty person...""")
        input("""
    After several desperate seconds you start to see shapes. Something that you assume is the person
    moving around on the burning floor, and also a big barrel hopefully containing something drinkable!
    You help the person, who appears to be an old man, over to the barrel. And joy, oh joy! It's filled
    to the brim with icecold water!""")
        input("""
    When the old man finally stops slurping the refreshing water, you both sit down on the ground and greet
    eachother.""")
        rooms.roomInfo(room)
        name = input("""
        - Th-th-thank you kind sir!
          I'm Olaf... Could I get the name of my saviour?

        Hero name: """)
        print("""
        - Thank you once again %s!
          Should we try to find a way out of here now before our blood starts to boil, eh?\n""" % name)


    # inbetween room 1 & 2
    if room == 1:
        input("""
    You stumble in the dark trying to find any kind of light source
    while keeping the fragile man from falling down from weakness.
    Finally you see a flare in the distance of what appears to be
    the end of the tunnel!""")

        input("""
    With an effort you try to cheer up the old man Olaf with a weak laugh,
    telling him that everything is going to be alright!
    He just mumbles and scrapes his feet against the floor.
    The heat must be getting to him...""")


    # inbetween room 2 & 3
    if room == 3:
        input("""
    Another long dark tunnel is ahead of you.
    Once again you grab poor ol' Olaf and start to half-carry him while
    your foot leaves a nice trail of blood...

    The tunnel was short enough for Olaf to get through, but when he starts
    to cough blood you see that maby he could use some kind of medicine
    and some sleep.""")

        input("""
    When you enter the third room you conveniently find a stack of hay to
    put Olaf in. He coughs another bit of blood and passes out.""")


    # inbetween room 3 & 4
    if room == 5:
        input("""
    You try to wake Olaf up.
    'OLAF! It's %s! Wake up!'

    The old man just mutters something unhearable, coughs again and passes out.
    You really have to find the exit fast and call for help as soon as possible!""" % name)
        input("""
    You turn yourself to the gaping hole to what seems lead to nothingness itself.

    As you walk down the eternal tunnel with darkess so thick that you can almost
    touch it, you pray for the portable torch to not die... Small tunnels that looks
    handmade are everywhere, but too small for any human to crawl through. Who made these?!""")
        input("""
    The sweat and dirt is sticky and gets in your eyes.
    'GODDAMN HELL HOLE' you scream.
    As the down pitched echo of your voice bounce around the tunnels, you see
    the end further down, leading to some very lit up room.
    'Just in time!' you say to yourself while the portable torch sighs and give up.""")
        input("""
    The enormous room of number four looks like a cathedral and your steps
    echoes as you go in.
    'This must be atleast twenty meters under ground! How is it possible?',
    you think for yourself while you stand in the entry of the room""")

    # room 4
    if room == 6:
        rooms.roomInfo(room)
        input("""
    The 'ceiling' must be ten meters up and the octagon shaped room has four
    'pictures' in each second corner. On the long sides both left and right
    of you, heaps of burning 'torches' are stuck to the walls.

    On the other side of the room there is a fancy red 'carpet' leading to the
    gigantic statue of a demon holding something. Or is it supposed to be the 'Devil'?
    Any how, freaky enough to creep you out!

    Your breath is heavy and your bloody foot starts to pulsate a bit too much.
    You feel dizzy and need something to drink and some bandages.""")


    # inbetween room 4 & 5
    if room == 7:
        input("""
    A high pitched tone drills through your head as you open your eyes...""")
        input("""
    'AAAH, I'M BLIND!!!!' you scream in pure terror!""")
        input("""
    You realise that your scream is muffled, and roll over to your back.
    'Phiew', it was only that you were face down in the haystack that probably
    saved your life from the high fall!""")
        input("""
    The glass shatter luckily didn't kill you, but instead it got pulverised when you landed on it.

    You look around and feel confused. Such a small room!""")


    # inbetween room 5 & 6
    if room == 9:
        input("""
    'As %s climbs down the shaft and crawl through a long dark tunnel,
    the hero finds the source of all the heat. A lava river flowing through a room!'""" % name)
        input("""
    '%s sees only one way, and that's the way over a stone bridge leading to some
    kind of platform in the middle of the room.'""" % name)
        input("""
    'Whilst the hero carefully walks over the ancient bridge, %s can spot some kind of
    metal vessel under the platform, connecting with some kind of pipeline'""" % name)


    # inbetween room 6 & 7
    if room == 11:
        input("""
    Crawling down the hatch, dodging burning lava pieces from all around you,
    finally you are in safety!""")
        input("""
    Or so you thought. You sit in the darkness once again, and sees the ladder
    winding up in the ceiling.""")
        input("""
    *BOOM!* The hatch closes hard and the sound echoes in what must be a quite big
    room.""")
        input("""
    Suddenly a thousand torches starts to burn at the same time!""")
        input("""
    And you can now see that you are sitting in the middle of an enormous 'Pentagram'!""")
        rooms.roomInfo(12)
        input("""
    Outside of the 'Pentagram', the 'Devil' himself stands there staring at you with a big grin...""")
        rooms.devil()
        print("""
                            The 'Devil' greets you.""")




def roomBack(room):
    """
    Going back gives another intro story for different rooms.
    """
    if room == 0:
        rooms.roomChange(room)
        print("""
    After the long passage, you finally squeeze through the half opened gate
    and stand in the darkness of the first room...\n""")

    if room == 2:
        rooms.roomChange(room)
        print("""
    After the short passage, you finally see the good ol' 'chairs' and succeed to
    dodge the 'glass shatters' on the floor. The 'torch' is where it is.\n""")

    if room == 6:
        print("""
        I can't go through there! I will never make it!""")
