#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dungeon: a text format escape game in Python code.
By: Max Sundberg.
"""
import rooms
import storyLine
import info
import sys
import getopt


def forward(room, inventory, item=0):
    """
    Go one room further to the exit.
    """
    if room == 0:
        if item >= 2:
            room += 1
            storyLine.roomEntry(room)
            room += 1
            look(room, inventory, item)
        else:
            print("That gate won't budge!")
    elif room == 2:
        if item >= 4:
            room += 1
            storyLine.roomEntry(room)
            room += 1
            look(room, inventory, item)
        else:
            print("That gate won't budge!")
    elif room == 4:
        if item >= 5 and "portable torch" not in inventory:
            print("Woah! Too dark and scary, I need a light of some sort...")
        elif item >= 5 and "portable torch" in inventory:
            room += 1
            storyLine.roomEntry(room)
            room += 1
            inventory.remove("portable torch")
            look(room, inventory, item)
        else:
            print("Locked shut and way to thick to get through!")
    elif room == 6:
        print("...Where?")
    elif room == 8:
        if item != 10:
            print("...Where?")
        else:
            room += 1
            storyLine.roomEntry(room)
            room += 1
            rooms.roomInfo(room)
    elif room == 10:
        if item != 12:
            print("...Where?")
        else:
            room += 1
            storyLine.roomEntry(room)
            room += 1
            print("""
                                'Welcome mortal!
                            I am Beelzebub, ruler of Hell!
                What are a puny intruder like you doing in my kingdom?'""")
    elif room == 12:
        print("There is no where to escape!")
    return room



def back(room):
    """
    Go back one room further to the start.
    """
    if room == 0:
        print("You try to go back in the dark, but you only smack your head against the wall.")
        room = 0
    elif room == 6:
        print("You have no lightsource and it's way too dark to go back there!")
    else:
        room = room - 2
        storyLine.roomBack(room)

    return room



def kick(objectName, inventory, room, item=0):
    """
    Kick an object in the room and see what happens.
    """
    # room 1
    if room == 0:
        if objectName == "barrel":
            print("*SPLASH!* Well, that's a way to clean yourself...")
        elif objectName == "stick":
            if "sticky-stick" not in inventory:
                print("*Clack* The stick hits the wall and falls back to it's original position.")
            else:
                print("There is no stick there!")
        elif objectName == "gate":
            print("I do love to kick, but kick a rusty metal gate? Nu-uh!")


    # room 2
    elif room == 2:
        if objectName == "mirror":
            if item == 2:
                print("""
    You do a flying karate kick on the mirror in pure frustration and get
    'glass shatters' everywhere!
    'OUCH!', you step in the shatters with your bare feet and
    start to bleed.""")
                item += 1
            else:
                print("The mirror is already kicked to death!")
        elif objectName == "chairs":
            print("OUCH, they may be old, but man do they hurt my toes!")
        elif objectName == "torch":
            print("I won't kick a freaking burning torch dude!")
        elif objectName == "gate":
            print("I do love to kick, but kick a rusty metal gate? Nu-uh!")


    # room 3
    elif room == 4:
        if objectName == "haystack":
            print("No time to hit the hay!")
        elif objectName == "torches":
            print("I won't kick some freaking burning torches dude!")
        elif objectName == "odd wall":
            print("You attack the wall with a scream!\nAnd bounces right off...")
            print("Like it's made out of rubber or something.")
        elif objectName == "door":
            print("Looks too sturdy to kick down. No thanks.")


    # room 4
    elif room == 6:
        if objectName == "torches":
            print("I won't kick some freaking burning torches dude!")
        elif objectName == "ceiling":
            print("How am I supposed to do that?")
        elif objectName == "devil":
            print("I rather not, he looks too spooky!")
        elif objectName == "pictures":
            print("Kick a picture? Why?")
        elif objectName == "carpet":
            print("You start to scrub your bare feet on the fancy carpet laughing a bit.")
            print("'It tickles!'")
            print("Luckily it's red so you don't see the bloodstains from your injured foot too easy...")


    # room 5
    elif room == 8:
        if objectName == "hay":
            print("'Weeehooo!'")
            print("The hay flies around in the room.")
        if objectName == "box":
            print("'OUCH!'")

    # room 6
    elif room == 10:
        if objectName == "lava":
            print("'A bit too far down, and I rather not try anyway...'")
        if objectName == "box":
            print("'OUCH!'")

    # room 7
    elif room == 12:
        if objectName == "devil":
            print("'Whoa! Are you crazy man?!'")
        if objectName == "pentagram":
            print("You kick the ground. Nothing happens...")
        if objectName in inventory:
            print("The 'Devil' looks confused at you when you stand and kick the air...")
        elif objectName == "skin":
            if inventory == []:
                inventory.append("skin")
                print("You kick down the tightened skin and sees it dissappear in the everburning flames of hell.")
            else:
                input("The 'Devil' laughs and says: Game over, mortal. Game. Over...")
                info.theEnd()
        elif objectName == "chairs":
            if "skin" in inventory:
                inventory.append("chairs")
                print("The chairs fall down and the only thing you can hear is the hypnotising sound of eternal fire.")
            else:
                input("The 'Devil' laughs and says: Game over, mortal. Game. Over...")
                info.theEnd()
        elif objectName == "key":
            if "chairs" in inventory:
                inventory.append("key")
                print("*Ching* The key flies away and the 'Devil' smirks.")
            else:
                input("The 'Devil' laughs and says: Game over, mortal. Game. Over...")
                info.theEnd()
        elif objectName == "barrel":
            if "key" in inventory:
                inventory.append("barrel")
                print("With your last energy you succeed to push the barrel filled with blood over the edge...")
            else:
                input("The 'Devil' laughs and says: Game over, mortal. Game. Over...")
                info.theEnd()
        elif objectName == "olaf":
            if "barrel" in inventory:
                print("Do you really want to kick the half dead poor old coughing man down in eternal torture?")
                olafChoice = input("(y/n): ")
                if olafChoice == "n":
                    input("""
    Trying to hold back your tears and kick the old innocent man you feel that it's impossible...""")
                    input("""
    The 'Devil' looks disappointed at you.
                                'So you don't want to live?'""")
                    input("""
    You see Olaf flying away after the 'Devil' smacks him with the back of his hand.
    The 'Devil' smiles at you and comes closer... Maby you should have done this in a different way?""")
                    input("The 'Devil' laughs and says: Game over, mortal. Game. Over...")
                    info.theEnd()
                if olafChoice == "y":
                    input("""
    While you say sorry to Olaf, praying to God... You kick him hard in the chest.""")
                    input("""
    The only thing he responds with is a gasp for air and stares at you as he dissappears...""")
                    input("""
                                The 'Devil' says...
                    'Delightful, little mortal. Most amusing!'""")
                    input("""
                       'Tho' the praying to.. pffft! GOD?!'""")
                    input("""
                The 'Devil' takes one giant step over to you and says:
                               'Ain't no God here!
               Atleast you won't have to suffer for eternity, HAHAHA!'""")
                    input("""
    The last thing you see is the thousand fangs of the 'Devil' slowly closing in to your
    poor exhausted head...""")
                    info.theEnd()

    if objectName == "olaf" and room != 12:
        print("What's wrong with you? I won't kick an old man!")


    return item



def inventoryList(inventory, room):
    """
    Show players inventory.
    """
    if room != 12:
        inventoryNames = ""
        print("You empty your pockets and look at your hands...")
        if not inventory:
            print("Your hands contain nothing! Bummer.")
        else:
            for item in inventory:
                inventoryNames = inventoryNames + item + " "
            print("You are currently holding: \n%s" % inventoryNames)
            print("in your hands.")
    else:
        print("You have nothing on you!")



def look(room, inventory=None, item=0):
    """
    Prints all items in the room.
    """
    # room 1
    if room == 0:
        if "portable torch" in inventory or "portable torch" not in inventory:
            if "barrel-key" not in inventory and "sticky-stick" not in inventory and item == 0:
                rooms.roomInfo(room)
                print("""
    'Olaf' lays sturdy on the floor, the 'barrel' stands as the half full,
    half empty container as it is. Some kind of 'stick' lays on the ground and
    the 'gate' looks shut indeed.""")
            elif "barrel-key" not in inventory and "sticky-stick" in inventory and item == 0:
                rooms.roomChange(room)
                print("""
    'Olaf' lays sturdy on the floor, the 'barrel' stands as the half full, half empty
    container as it is. The 'gate' looks shut indeed.""")
            elif "barrel-key" in inventory and "sticky-stick" not in inventory and item == 0:
                rooms.roomInfo(room)
                print("""
    'Olaf' lays sturdy on the floor, the barrels water still rocks back and forth after
    your mission to pick up the barrel-key. Some kind of 'stick' lays on the ground
    and the 'gate' looks shut indeed.""")
            elif "barrel-key" in inventory and "sticky-stick" in inventory and item == 0:
                rooms.roomChange(room)
                print("""
    'Olaf' lays sturdy on the floor, the barrels water still rocks back and forth after
    your mission to pick up the barrel-key. The 'gate' looks shut indeed.""")
            elif "sticky-stick" not in inventory and item == 1:
                rooms.roomInfo(room)
                print("""
    'Olaf' lays sturdy on the floor, the barrels water still rocks back and forth after
    your mission to pick up the barrel-key. Some kind of 'stick' lays on the ground and
    the 'gate' is unlocked but rusted shut.""")
            elif "sticky-stick" in inventory and item == 1:
                rooms.roomChange(room)
                print("""
    'Olaf' lays sturdy on the floor, the barrels water still rocks back and forth after
    your mission to pick up the barrel-key. The 'gate' is unlocked but rusted shut.""")
            elif item == 2:
                rooms.roomChange(room)
                print("""
    'Olaf' lays sturdy on the floor, the barrels water still rocks back and forth after
    your mission to pick up the barrel-key. The 'gate' is unlocked and opened just so you can get through.""")


    # room 2
    elif room == 2:
        if item == 2:
            rooms.roomInfo(room)
            print("""
    'Olaf' holds himself to the entry of the second room and you can see a 'mirror'
    mounted to the left wall, a flaming 'torch' fixed in the wall next to you
    and some really old wooden 'chairs' in the corner next to the torch. On the other side
    of the room another 'gate' is interrupting your way out to freedom. And it's getting
    even warmer!""")
        if item == 3:
            rooms.roomChange(room)
            print("""
    'Olaf' holds himself to the entry of the second room. 'Glass shatters' everywhere
    on the floor after your unnecessary flykick...
    A flaming 'torch' is fixed in the wall next to you
    and some really old wooden 'chairs' in the corner next to the torch. On the other side
    of the room another 'gate' is interrupting your way out to freedom. And it's getting
    even warmer!""")
        if item >= 4:
            rooms.roomChange(room)
            print("""
    'Olaf' holds himself to the entry of the second room. 'Glass shatters' everywhere
    on the floor after your unnecessary flykick...
    A flaming 'torch' is fixed in the wall next to you
    and some really old wooden 'chairs' in the corner next to the torch. On the other side
    of the room the 'gate' is wide open. Let's get out of here!""")


    # room 3
    elif room == 4:
        if item == 4:
            rooms.roomInfo(room)
            print("""
    'Olaf' lays still on the 'haystack', with some blood bubbling from the corner
    of his mouth. Must mean he is still alive atleast!
    On the other side of the room you see some 'torches' fixed in the wall,
    to your left you see a 'odd wall' and to your right there is a HUGE
    wooden 'door' with demonic metal faces all over. Creepy!""")
        if item == 5:
            rooms.roomChange(room)
            print("""
    'Olaf' lays still on the haystack, with some blood bubbling from the corner
    of his mouth. Must mean he is still alive atleast!
    On the other side of the room you see some 'torches' fixed in the wall,
    to your left you see some 'destroyed skin' and to your right
    there is a HUGE wooden 'door' with demonic metal faces all over. Creepy!""")
        if item == 6:
            rooms.roomChange(room)
            print("""
    'Olaf' lays still on the haystack, with some blood bubbling from the corner
    of his mouth. Must mean he is still alive atleast!
    On the other side of the room you see some 'torches' fixed in the wall,
    to your left you see some 'destroyed skin' and to your right the
    huge 'door' is opened and darkness once again is gaping infront of you...""")


    # room 4
    elif room == 6:
        if item == 6:
            rooms.roomInfo(room)
            print("""
    The 'ceiling' must be ten meters up and the octagon shaped room has four
    'pictures' in each second corner. On the long sides both left and right
    of you, heaps of burning 'torches' are stuck to the walls.

    On the other side of the room there is a fancy red 'carpet' leading to the
    gigantic statue of a demon holding something up in the sky.
    Or is it supposed to be the 'Devil'?""")
        if item == 7:
            if "water" in inventory:
                rooms.roomChange(room)
                print("""
    The 'ceiling' must be ten meters up and the octagon shaped room has three
    'pictures' hanging in different corners. On the long sides both left and right
    of you, heaps of burning 'torches' are stuck to the walls.

    On the other side of the room there is a fancy red 'carpet' leading to the
    gigantic statue of a demon holding something up in the sky.
    Or is it supposed to be the 'Devil'?""")
            if "water" not in inventory:
                rooms.roomChange(room)
                print("""
    The 'ceiling' must be ten meters up and the octagon shaped room has three
    'pictures' hanging in different corners. On the long sides both left and right
    of you, heaps of burning 'torches' are stuck to the walls.

    On the other side of the room there is a fancy red 'carpet' leading to the
    gigantic statue of a gaping demon holding down a 'stone bowl' containing something.
    Or is it supposed to be the 'Devil'?""")
        if item == 8:
            if "bandages" not in inventory:
                rooms.roomChange(room + 1)
                print("""
    The 'ceiling' must be ten meters up and the octagon shaped room has only two
    'pictures' hanging on the walls left. On the long sides both left and right
    of you, heaps of burning 'torches' are stuck to the walls.

    On the other side of the room there is a fancy red 'carpet' leading to the
    gigantic statue of a gaping demon holding down a 'stone bowl' containing something.
    Or is it supposed to be the 'Devil'?""")
            if "bandages" in inventory:
                rooms.roomChange(room + 1)
                print("""
    The 'ceiling' must be ten meters up and the octagon shaped room has three
    'pictures' in different corners. On the long sides both left and right
    of you, heaps of burning 'torches' are stuck to the walls.

    On the other side of the room there is a fancy red 'carpet' leading to the
    gigantic statue of a gaping demon holding an empty 'stone bowl'.
    Or is it supposed to be the 'Devil'?""")
        if item >= 9:
            if "bandages" not in inventory:
                rooms.roomChange(room + 1)
                print("""
    The 'ceiling' must be ten meters up and the octagon shaped room has only two
    'pictures' hanging on the walls left. On the long sides both left and right
    of you, heaps of burning 'torches' are stuck to the walls.

    On the other side of the room there is a fancy red 'carpet' leading to the
    gigantic statue of a gaping demon holding a 'stone bowl' containing something.
    Or is it supposed to be the 'Devil'?""")
            if "bandages" in inventory:
                rooms.roomChange(room + 1)
                print("""
    The 'ceiling' must be ten meters up and the octagon shaped room has only two
    'pictures' hanging on the walls left. On the long sides both left and right
    of you, heaps of burning 'torches' are stuck to the walls.

    On the other side of the room there is a fancy red 'carpet' leading to the
    gigantic statue of a gaping demon holding a 'stone bowl' containing nothing.
    Or is it supposed to be the 'Devil'?""")


    # room 5
    elif room == 8:
        if "bandages" in inventory:
            rooms.roomInfo(room)
            input("""
    Trying to stand up, you can see that the blood has made a terrible mess in the
    haystack. Feeling too dizzy to move any more, you pass out before being able
    to get the bandages around your foot...""")
            input("""
    You fall down into the eternal sleep.

    Maby should've taken the chance while you still had the strength to stop the blood loss...""")
            info.theEnd()
        if item == 11:
            rooms.roomInfo(room)
            print("""
    The room is filled with 'hay' uptil your waist, and can't be more than two square meters big.
    In the corner where you have scraped away the 'hay' there is a metal hatch hopefully leading
    out from this room!

    Right infront of you, there is a weird looking 'box' with a 'button'.""")
        else:
            rooms.roomInfo(room)
            input("""
    The room is filled with 'hay' uptil your waist, and can't be more than two square meters big.

    No door, no nothing, except a weird looking 'box' with a 'button' right infront of you...""")


    # room 6
    elif room == 10:
        rooms.roomInfo(room)
        print("""
    Standing in the middle of the extremely warm room, you want to find a way out
    as fast as possible!
    'Lava' is surrounding the room, the ceiling is dotted with small handmade tunnels,
    The platform you're standing on burns your feet and in the middle of everything
    you see a 'box' in a circle.""")



    # room 7
    elif room == 12:
        rooms.roomInfo(room)
        print("""
    You are standing in the middle of a 'Pentagram', staring the 'Devil' himself
    in the eyes...

    You are completly unarmed, and too exhausted to fight any way.""")



def inspect(objectName, inventory, room, item=0):
    """
    Let's player inspect the chosen object.
    """
    if objectName == "olaf" and room <= 4:
        if "portable torch" in inventory or room > 1:
            print("The old dirty white-bearded man is tired and overheated.")
    if objectName == "sticky-stick" and "sticky-stick" in inventory:
        print("Eeeeeewwwww...!")
    if objectName == "portable torch" and "portable torch" in inventory:
        print("Phiew', it's getting hot in here.")
    if objectName == "glass shatter" and "glass shatter" in inventory:
        print("A sharp piece of mirror glass!")
    # room 1
    if room == 0:
        if objectName == "barrel":
            if "barrel-key" not in inventory:
                print("""
    You look into the dark waters of the barrel and understand
    that some kind of lightsource must exist somewhere, since you can
    see some kind of 'shiny thing' on the bottom of the barrel.""")
            else:
                print("Yep, a half-emptied barrel of water.")
        if objectName == "barrel-key":
            if "barrel-key" in inventory:
                print("A shimmering key from the barrel.")
            else:
                print("What?")
        if objectName == "stick":
            if "sticky-stick" not in inventory:
                print("It looks like a stick!")
            else:
                print("What?")
        if objectName == "olaf":
            if "portable torch" not in inventory:
                print("A siluett of a person resting on the ground.")
        if objectName == "gate":
            if item == 0:
                print("A very closed gate indeed.")
            elif item == 1:
                print("A unlocked, unopened rusted gate indeed.")
            else:
                print("Just enough room to squeeze through!")

    # room 2
    if room == 2:
        if objectName == "chairs":
            print("Pffft. Not even worthy to be firewood.")
        if objectName == "torch":
            print("Don't want to go too close, it's warm enough here!")
            print("It looks like it's stuck to the wall anyway...")
        if objectName == "gate":
            if item <= 3:
                print("A very closed and locked gate indeed.")
            else:
                print("The gate is opened, what are we waiting for?!")
        if objectName == "mirror":
            if item < 3:
                print("You see a sweaty reflection of the man you once were.")
                print("'Could really use a bath...")
            else:
                print("A little late to get a look of yourself now, eh?")
                print("The mirror is on the floor in thousand pieces of 'glass shatters'!")
        if objectName == "glass shatters":
            if "mirror-key" not in inventory and item < 4:
                inventory.append("mirror-key")
                print("Along the sharp pieces of mirror glass, you find a key.")
                print("\nThe 'mirror-key' is now in your pocket!")
            else:
                print("Better be careful, don't want to cut my feet again!")

    # room 3
    if room == 4:
        if objectName == "torches":
            print("Whiew! Can't they use some modern light in this place?")
            print("These just escalate the heat!")
        if objectName == "door":
            print("That's one scary door! The demon faces seems to look at yo wherever you stand!")
        if objectName == "odd wall":
            print("Hmm, looks fake. And feels fake as well! Like it's some kind of painted skin!")
        if objectName == "haystack":
            print("Wouldn't mind get some rest next to Olaf, but it's too small and darnit we need to get out of here!")
        if objectName == "destroyed skin":
            inventory.append("bone-key")
            input("AH! Spiders! Cockroaches! HUMAN SKULLS?!")
            print("Oooooh, and a key!\nYou now got the 'bone-key' in your pocket")
            item += 1
            return item

    # room 4
    if room == 6:
        if objectName == "torches":
            print("Whiew! Can't they use some modern light in this place?")
            print("These just escalate the heat!")
        if objectName == "devil":
            if item == 7 and "water" not in inventory or item == 8 and "bandages" not in inventory:
                print("You can hear the breath of the Devil statue and see it's mouth open and arms lowered!")
                print("Something is in the 'stone bowl'!")
            elif item >= 8 and "bandages" in inventory:
                print("You can hear the breath of the Devil statue and see it's mouth open and arms lowered!")
                print("The 'stone bowl' is empty!")
            elif item <= 7 and "water" in inventory:
                print("The Devil holds up a big bowl made out of stone.")
                print("Unreachable and you don't feel like climbing with a hurt foot...")
                print("His intense red ruby eyes watches you while glittering from the dancing fires around him.")
        if objectName == "stone bowl":
            if "bandages" not in inventory:
                print("In the bowl are some 'bandages'.")
                print("You now have 'bandages' in your inventory!")
                inventory.append("bandages")
                item += 1
            else:
                print("The 'stone bowl' is empty!")
        if objectName == "ceiling":
            print("Even if I would be able to climb to the top, it seems like there is no exit...")
        if objectName == "carpet":
            print("Looks like it's nailed to the floor!")
            print("it's impossible to move but you can feel some kind of edges under it. Hmmmm...")
        if objectName == "pictures":
            pictureChoice = input("Wich picture do you want to look at?\n(1/2/3/4): ")
            if pictureChoice == "1":
                print("An old picture resembling a man hanging from a rope tied to a tree trunk. Well that's morbid...")
            elif pictureChoice == "2":
                print("An old picture resembling a cloaked rider on his skeletal horse.\n'Brrrrr!'")
            elif pictureChoice == "3":
                print("An old picture resembling... YOU?! In this very room!")
            elif pictureChoice == "4":
                print("An old picture resembling the Devil or some other foul demon, feasting on human flesh.\n'Yuck!'")
            else:
                print("There are only four pictures on the walls!")

    # room 5
    if room == 8:
        if objectName == "hay":
            print("A lot of hay indeed!")
            print("You're lucky you don't have that portable torch with you any more!")
        if objectName == "box":
            inventory.append("magnet")
            print("The box is made out of metal, almost steaming of the heat that surrounds you.")
            print("On top is a red 'button' and by observing the box all around, you find something behind it!")
            print("You pull the strong 'magnet' from the box and put it in your pocket!")
        if objectName == "button":
            print("Do you really want to press the red 'do-not-touch'y' button?")
            buttonChoice = input("(y/n): ")
            if buttonChoice == "y":
                input("""
    You press the irresistible red button and the ceiling starts to move downwards...""")
                input("""
    Olaf lays in his own bed of hay, breathing his last breaths and hears a terrifying
    lowpichted scream from the dark tunnel. His face turns white and before he dies of
    dehydration, the heartattack gets to him.""")
                info.theEnd()
            if buttonChoice == "n":
                print("Hard to resist, but you leave the button for now...")

    # room 6
    if room == 10:
        if objectName == "box":
            if item == 11:
                print("This 'box' also have a red 'button' and the whole thing is sparkling!")
            else:
                print("This 'box' also have a red 'button'!")
        if objectName == "button":
            print("Do you want to press it?")
            buttonChoice = input("(y/n): ")
            if buttonChoice == "n":
                print("Ok... what's next?")
            if buttonChoice == "y":
                input("""
    *CLANK* Something mechanical starts!""")
                input("""
    Before you know it, you realise that the platform has started to sink down to
    the vessel under it.""")
                if item >= 11:
                    input("""
    When you finally reached the bottom, wet of sweat and dried again of the heat,
    salt crystals covering your clothes, you see a small hatch opened in the vessel...""")
                    item += 1
                else:
                    input("""
    When you finally reached the bottom, wet of sweat and dried again of the heat,
    salt crystals covering your clothes, nothing else happens.""")
                    input("""
    After a couple of minutes in panic, the heat gets to you, and you fall
    into the eternal slumber, while your blood slowly starts to boil in your veins...""")
                    info.theEnd()

    # room 7
    if room == 12:
        print(inventory)
        if objectName == "devil":
            rooms.devil()
        if objectName == "pentagram":
            print("In each tip of the 'Pentagram' you see different objects.")
            print("""
    x A 'barrel'
    x Some 'chairs'
    x 'Skin', tightened and painted to look like a wall
    x 'Olaf'!
    x A 'key'""")
            input("""
    The 'Devil' sees your confused look and laughs with a delight...

    If you want to live, you must play a game with me!""")
            input("""
    Push down each... "item"... down from the 'Pentagram's edge, to be consumed
    in the hellfire.""")
            input("""
    But you may only do it in the reversed order of where you first got to see
    the... hehe.. "items"...""")
            input("""
    If you fail, even once, eternal pain of licking fire awaits you...""")
        if objectName == "olaf":
            print("The old man Olaf is alive!!! Almost not dead at least...")
        if objectName == "barrel":
            print("It's filled with blood... uuuäh!")
        if objectName == "chairs":
            print("Some good ol' wooden chairs.")
        if objectName == "skin":
            print("While observing the streched skin you step back giving away a little high pitched scream.")
            print("The reason is the human face holes in one of the corners. This is bloody disgusting!")
        if objectName == "key":
            print("A little key is shimmering in one of the 'Pentagram's tips.")


    return item



def grab(objectName, inventory, room, item=0):
    """
    Player grabs an object and puts in pockets if possible.
    """
    if objectName == "olaf":
        print("I'm not into that kind of things...")
    if objectName == "torch" or objectName == "torches":
        print("Stuck in the wall!")


    # room 1
    if room == 0:
        if objectName == "gate":
            print("Rusty 'n sturdy!")
        if objectName == "shiny thing":
            if "barrel-key" not in inventory:
                inventory.append("barrel-key")
                print("You reach down in the water and fish up the shiny object that seems to be a key.")
                print("Hmmm, wonder where it fits...")
                print("\nYou now have the 'barrel-key' in your pocket.")
            else:
                print("The shiny thing, that was a key, is already in your pocket!")
        elif objectName == "stick":
            if "sticky-stick" not in inventory:
                inventory.append("sticky-stick")
                print("You fumble in the dark and reach for the stick. Eeeew, it's sticky!")
                print("\nYou now have the 'sticky-stick' in your hand.")
            else:
                print("You already got the sticky-stick in your pocket!")


    # room 2
    if room == 2:
        if objectName == "chairs":
            print("...why?")
        if objectName == "mirror":
            print("...why?")
        if objectName == "gate":
            print("Yep, a sturdy 'n rusty gate alright!")
        if objectName == "glass shatters":
            if "glass shatter" not in inventory:
                inventory.append("glass shatter")
                print("Maby a piece of this will come in handy...")
                print("\nYou now have a piece of 'glass shatter' in your pocket.")
                print("Like livin' dangerous I see!")
            else:
                print("No.. one piece is enough!")


    # room 3
    if room == 4:
        if objectName != "haystack":
            print("..?")
        else:
            print("You grab a piece of hay and throw it in the air! Weeeeeee!")


    # room 4
    if room == 6:
        if objectName == "carpet":
            print("You try to rip the carpet from the ground but it's impossible!")
        if objectName == "ceiling":
            print("Too far up to reach!")
        if objectName == "devil":
            print("You walk up to the Devil and tries to reach the valuable eyes without any result.")
            print("Your foot hurts too much to climb up. Damn teasing!")
        if objectName == "pictures":
            print("Wich picture do you want to try to grab?")
            pictureChoice = input("(1/2/3/4): ")
            if pictureChoice == "1":
                input("""
    You try to lift away the picture of the hanging man and hears a clicking sound.""")
                input("""
    The floor disappear under your feet and you react too slow to grab the edges,
    falling down into the complete darkness while screaming in terror...""")
                info.theEnd()
            if pictureChoice == "2":
                input("""
    When you carefully lift the picture resembling one of the four horse riders
    away from the nail in the wall you hear a clicking sound and a shriek from above!""")
                input("""
    While you just manage to see what happens, the very same skeletal horse and
    it's rider falls dead straight on your head...""")
                info.theEnd()
            if pictureChoice == "3":
                if "water" not in inventory:
                    input("""
    A precise picture of you, just about to take the very same picture away from the wall!""")
                    input("""
    As you do on the picture, you find... a bowl of 'water'! Oh my, you must be thirsty!""")
                    print("""
    You now got a bowl of 'water' in your hands!""")
                    inventory.append("water")
                    item += 1
                else:
                    print("The picture of you is laying on the floor.")
            if pictureChoice == "4":
                if item == 6 or \
                    item == 7 and "water" in inventory or \
                    item == 7 and "bowl" in inventory or \
                    item == 7 and "blood" in inventory:
                    input("""
    The demons eyes stare as intense on the picture as on the sculpture.""")
                    input("""
    While taking the picture of the wall, a growl makes all your hairs stand up.
    Looking around you, you now see the demons mouth has opened wide!""")
                    item += 1
                else:
                    print("The picture of the Devil is laying on the floor.")


    # room 5
    if room == 8:
        if objectName == "hay":
            print("You grab a handful of hay, stares at it and drop it back.")
        if objectName == "box":
            print("The box is fixed to the ground! Impossible to move!")


    # room 6
    if room == 10:
        if objectName == "lava":
            print("You lay down at the edge of the platform, trying to reach some lava.")
            print("'Uuugghh, it's impossible! It must be atleast 10 meters down!")
        if objectName == "box":
            print("The box is fixed to the ground! Imppossible to move!")


    # room 7
    if room == 12:
        if objectName == "devil":
            print("Noooooo-hoho.. No no no. No.")
        if objectName == "pentagram":
            print("You touch the 'Pentagram'. It feels alive.")

    return item



def drop(objectName, inventory=None):
    """
    Player drops an object to the ground.
    """
    if inventory == None:
        inventory = []
    if objectName in inventory:
        inventory.remove(objectName)
        input("You throw the %s as far away as you can. Good riddance..." % objectName)
        input("""
    For hours you try to get further, but it is impossible.

    In the end you fall to the ground of thirst and hunger, and never wake up again...""")
        info.theEnd()
    else:
        print("If you really want to drop something, try something that you accually have in your pockets...")



def use(objectName, inventory, room=0, item=0):
    """
    Use item from pocket.
    """
    if objectName in inventory:
        if objectName == "barrel-key":
            if room == 0 and item == 0:
                print("""
    You stare at the key and wonders where it could possibly fit
    until Olaf rolls with his eyes...
        - Maby try it with the gate lock?

    The old, wise man has it right ofcourse, when you hear the lock clicks open.
    The only problem now is that the gate still can't open!
    The hinge is completly rusty!""")
                inventory.remove("barrel-key")
                item += 1
        elif objectName == "sticky-stick":
            if room == 0:
                if item == 0:
                    print("What am I supposed to do with this?")
                elif item == 1:
                    print("""
    You put the sticky stick in the gate entrance and start to bend
    as hard as you can! The hinge creeks and squeal until it finally
    gives up and the gate door opens up just enough for the both of you
    to slip through.""")
                    item += 1
            elif room >= 2:
                inventory.remove("sticky-stick")
                inventory.append("portable torch")
                print("When the sticky stick touches the fire of the torch, it sparkels.")
                print("Soon enough you got your own medival flashligt!")
                print("\nThe 'portable torch' is now in your hand!")
        elif objectName == "mirror-key":
            if room == 0:
                print("This doesn't seem to fit anywhere...")
            if room == 2:
                print("The key fits perfectly in the gates lock!\n The gate slides open, smooth and easy.")
                inventory.remove("mirror-key")
                item += 1
        elif objectName == "glass shatter":
            if room <= 2:
                print("HA-HAAAA! You wave it arond and pretend to be a pirate. Phiew, that was exhausting...")
            elif room == 4:
                if item == 4:
                    print("You go forward to the thick skin-wall and start to stab it!")
                    print("Finally yuu succeed to puncture it and rip it open!\nNow it's just some 'destroyed skin'.")
                    item += 1
            else:
                print("HA-HAAAA! You wave it arond and pretend to be a pirate. Phiew, that was exhausting...")
        elif objectName == "bone-key":
            if room <= 2:
                print("This doesn't seem to fit anywhere...")
            if room == 4:
                if item == 5:
                    print("""
    You put the bone-key in the keyhole that is in fact the largest
    demons mouth! As soon as the key is turned and the lock clicks open,
    the demons jaws claps together!!! Little bone splinters of the key
    spread over the room... The door automatically swings open and
    a pitch black windy tunnel appears infront of you.""")
                    item += 1
                    inventory.remove("bone-key")
        elif objectName == "portable torch":
            if room == 0:
                print("Oh, so this is how it looks like in here!\nJust the same but brighter!")
            if room >= 2:
                while True:
                    try:
                        if room == 2:
                            print("Are you sure you want to use the portable torch on the old wooden chairs?")
                            deathwish = input("(y/n): ")
                        if room == 4:
                            print("Are you sure you want to use the portable torch on Olafs provisional bed of hay?")
                            deathwish = input("(y/n): ")
                        if deathwish == "n":
                            print("You escape your dark thoughts of more heat.")
                            print("You lower the portable torch to continue the quest of escaping.")
                            break
                        elif deathwish == "y":
                            input("""
    You throw the torch on the ground next to the ignitable object and laugh hysterically!
        - WHAT ARE YOU DOING?!?!, Olaf screams, while you both starts to cough.

    There is nowhere to escape this smokefilled hole. The only thing you can do
    is to stumble in the fog of death while the tears are running down your dirty
    cheeks and slowly drift away into the eternal slumber...""")
                            info.theEnd()
                    except Exception:
                        continue
        elif objectName == "water":
            print("What do you want to do with the bowl of 'water'?")
            devilChoice = input("1) Drink it!\n2) Pour it into the Devil's bowl! : ")
            if devilChoice == "1":
                inventory.remove("water")
                inventory.append("bowl")
                print("You drink the lovely refreshing water and already feel a bit better!")
                print("You now have a 'bowl' in your hands!")
            elif devilChoice == "2":
                if item <= 7:
                    print("I can't reach it!")
                elif item >= 8 and "bandages" not in inventory:
                    print("There is something in the bowl, I don't wanna pour water on it!")
                else:
                    inventory.remove("water")
                    inventory.append("bowl")
                    print("You pour the lovely water into the Devil's bowl.")
                    print("The water slides down and dissapear in the stone cracks.")
                    print("Nothing more happens...")
                    print("\nYou now have a 'bowl' in your hands!")
        elif objectName == "bandages":
            if "blood" in inventory:
                print("You bandage the foot tight and the blood stops escaping the nasty wound.")
                inventory.remove("bandages")
            else:
                print("Are you sure you want to tighten up that bloody foot right away?")
                bandageChoice = input("1) Yes\n2) No : ")
                if bandageChoice == "1":
                    input("""
    You bandage the foot as tight as possible and the blood stops escaping the nasty wound...
    Now the waiting game starts, and soon your hunger and thirst makes you tired.""")
                    input("""
    You fall into the sleep of no return...""")
                    info.theEnd()
                if bandageChoice == "2":
                    print("You descide that it may be smarter to try something else first.")
        elif objectName == "bowl":
            inventory.remove("bowl")
            inventory.append("blood")
            print("You let the blood from your foot run down in the bowl.")
            input("You now have a bowl of 'blood'!")
            print("...weirdo.")
            item += 1
        elif objectName == "blood":
            if item < 9:
                print("You want to pour the blood into the Devil's 'stone bowl'.")
                print("But it is something in there already!")
            else:
                inventory.remove("glass shatter")
                inventory.remove("blood")
                input("""
    You pour the blood into the Devil's bowl, and his eyes starts to shine even more!

    You try to back a bit, but you are already walking in the air,
    since the carpet-hidden trapdoor under it has been activated.""")
                room += 1
                storyLine.roomEntry(room)
                room += 1
                look(room, inventory, item)
        elif objectName == "magnet":
            if room == 8:
                print("You use the 'magnet' around the haystack, trying to find the metaphorical needle.")
                input("Success! A *clonk* in the 'magnet' indicates that something not that hay-y stuck to it!")
                print("A hatch! Oh lord-y-lord! Let's see where it leads shall we?")
                item += 1
            else:
                inventory.remove("magnet")
                print("You put the magnet on the box, and it starts buzzing and sparkle!")
                item += 1
    if objectName != "blood":
        return item
    else:
        return room



def hint(room):
    """
    Hints for each room
    """
    if room == 0:
        print("""
    Inspect, look, grab and use everything!

    Everything that has ''<-(single quotation marks) can be used in some way.""")
    if room == 2:
        print("""
    Try to kick some objects! Keys are for doors, and sticky sticks may be sticky for a reason.""")
    if room == 4:
        print("""
    Odd wall huh? Maby you can use something from a room furher back that is sharp?""")
    if room == 6:
        print("""
    The pictures are maby moveable, try the second half of the room, just be careful!
    Blood is maby necessary before wraping the foot up!

    Always try to grab, use and inspect everything.""")
    if room == 8:
        print("""
    Buttons may be dangerous! But inspecting is always nice! And using stuff!""")
    if room == 10:
        print("""
    You still have that magnet haven't you?""")
    if room == 12:
        print("""
    Oookay... Just go back in your memory, what did you meet with first?
    Go forward in your memory. When you got everything, kick 'em backwards!""")



def openObject(objectName, inventory):
    """
    Let's player open the object if it's possible.
    """
    if objectName not in inventory:
        print("It's unopenable!")
    else:
        print("Say what?")



def moveObject(objectName, inventory):
    """
    Let's player move object if it's possible.
    """
    if objectName not in inventory:
        print("It's unmoveable!")
    else:
        print("Say what?")



def objects(room, inventory, item):
    """
    Prints out all the objects in the room
    """
    # Room 1
    if room == 0:
        if "sticky-stick" not in inventory:
            print("Olaf, barrel, stick, gate")
        else:
            print("Olaf, barrel, gate")
    # Room 2
    if room == 2:
        if item == 2:
            print("Olaf, mirror, chairs, torch, gate")
        else:
            print("Olaf, glass shatters, chairs, torch, gate")
    # Room 3
    if room == 4:
        if item == 4:
            print("Olaf, haystack, torches, odd wall, door")
        else:
            print("Olaf, haystack, torches, destroyed skin, door")
    # Room 4
    if room == 6:
        print("Ceiling, pictures, torches, carpet, Devil")
    # Room 5
    if room == 8:
        print("Hay, box, button")
    # Room 6
    if room == 10:
        print("Lava, box")
    # Room 7
    if room == 12:
        print("Devil, pentagram")




def mainGame():
    """
    The main function in the game.
    """
    currentRoom = 0
    item = 0
    inventory = []

    info.gameLogo()
    info.versionText()
    choice = input("""
                Press Enter to start the game.
        Press 'h' or 'help' for command instructions.
                 Press 'q' to quit the game.
                            """)
    if "q" in choice:
        quit()
    elif "h" in choice or "help" in choice:
        info.helpText()
        input()
        main()

    storyLine.roomEntry(currentRoom)

    while True:
        command = input("=|==> ")
        command = command.lower()
        print("\n")

        if "q" in command.split() or "quit" in command.split():
            print("Are you sure?")
            quitChoice = input("(y/n): ")
            if quitChoice == "y":
                print("Ok, thanks for playing!")
                quit()
        if "h" in command.split() or "help" in command.split():
            info.helpText()
        elif "forward" in command.split():
            currentRoom = forward(currentRoom, inventory, item)
        elif "back" in command.split():
            currentRoom = back(currentRoom)
        elif "inv" in command.split() or "inventory" in command.split():
            inventoryList(inventory, currentRoom)
        elif "look" in command.split():
            look(currentRoom, inventory, item)
        elif "drop" in command:
            drop(command[5:len(command)], inventory)
        elif "inspect" in command:
            if "stone bowl" in command:
                item = inspect(command[8:len(command)], inventory, currentRoom, item)
            if "button" in command:
                item = inspect(command[8:len(command)], inventory, currentRoom, item)
            else:
                inspect(command[8:len(command)], inventory, currentRoom, item)
        elif "grab" in command:
            if "pictures" in command:
                item = grab(command[5:len(command)], inventory, currentRoom, item)
            else:
                grab(command[5:len(command)], inventory, currentRoom, item)
        elif "kick" in command:
            if "mirror" in command:
                item = kick(command[5:len(command)], inventory, currentRoom, item)
            else:
                kick(command[5:len(command)], inventory, currentRoom, item)
        elif "use" in command:
            if "barrel-key" in command:
                item = use(command[4:len(command)], inventory, currentRoom, item)
            if "sticky-stick" in command:
                item = use(command[4:len(command)], inventory, currentRoom, item)
            if "portable torch" in command:
                item = use(command[4:len(command)], inventory, currentRoom, item)
            if "mirror-key" in command:
                item = use(command[4:len(command)], inventory, currentRoom, item)
            if "glass shatter" in command:
                item = use(command[4:len(command)], inventory, currentRoom, item)
            if "bone-key" in command:
                item = use(command[4:len(command)], inventory, currentRoom, item)
            if "blood" in command:
                currentRoom = use(command[4:len(command)], inventory, currentRoom, item)
            if "magnet" in command:
                item = use(command[4:len(command)], inventory, currentRoom, item)
            else:
                use(command[4:len(command)], inventory, currentRoom, item)
        elif "hint" in command.split():
            hint(currentRoom)
        elif "open" in command:
            openObject(command[5:len(command)], inventory)
        elif "move" in command:
            moveObject(command[5:len(command)], inventory)
        elif "object" in command.split():
            objects(currentRoom, inventory, item)





def main():
    """
    The main function of the program that checks options and launches the game.
    """
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hivac", [
            "help", "info", "version", "about", "cheat"])

    except getopt.GetoptError:
        print("\nSomething went wrong. Here, have some help commands.")
        info.helpText()
        sys.exit(1)

    for opt, _ in opts:
        if opt in ("-h", "--help"):
            info.helpText()
            sys.exit(0)

        elif opt in ("-i", "--info"):
            info.infoText()
            sys.exit(0)

        elif opt in ("-v", "--version"):
            info.versionText()
            sys.exit(0)

        elif opt in ("-a", "--about"):
            info.aboutText()
            sys.exit(0)

        elif opt in ("-c", "--cheat"):
            info.cheatText()
            sys.exit(0)
    mainGame()

if __name__ == "__main__":
    main()
