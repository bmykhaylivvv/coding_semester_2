'''
Module for running adventure game.
'''
import game

stryiska = game.Place("Stryiskiy Park")
stryiska.set_description("Stryiskyi Park sits in south Lviv between Stryiska Street and the upper \
part of Franko Street, on a ridge where Soroka Creek had its source.")

kozelnytska = game.Place("Andrey Sheptytsky Center")
kozelnytska.set_description("The Metropolitan Andrey Sheptytsky Center is an \
information and resource center at Ukrainian Catholic University which includes a number of \
lecture and conference halls, several rooms for administrative purposes, public cultural \
space, a kids’ zone, a café, a bookstore, an exhibition zone and a library.")

franka = game.Place("Lviv University")
franka.set_description("The oldest university in Ukraine, established in 1784 by the emperor of \
Austria Joseph II with Latin as the language of instruction.")

shevchenka = game.Place("Monument of Taras Shevchenko")
shevchenka.set_description("The monument to the Ukrainian national poet was opened on 24 August 1992. \
By 1996, it was complemented with a 12-meter decorative stele with reliefs, supposed to \
symbolize the wave of national revival.")

krakivska = game.Place("Krakovsky Outdoor Market")
krakivska.set_description("Here one can purchase both clothes and fresh foods like meat, fruits and \
vegetables. The Farmer's Market has fresh delicious dairy items. You can also find local \
Ukrainian cookies, biscuits and pastries.")

stryiska.link_room(krakivska, "backward")
stryiska.link_room(kozelnytska, "forward")
kozelnytska.link_room(stryiska, "backward")
kozelnytska.link_room(franka, "forward")
franka.link_room(kozelnytska, "backward")
franka.link_room(shevchenka, "forward")
shevchenka.link_room(franka, "backward")
shevchenka.link_room(krakivska, "forward")
krakivska.link_room(shevchenka, "backward")
krakivska.link_room(stryiska, "forward")


lotr = game.Enemy("Kavaler", "A terrible villain")
lotr.set_conversation("What's up, dude! I'll catch you!")
lotr.set_weakness("cheese")
kozelnytska.set_character(lotr) 

zbui = game.Enemy("Zbui", "Cunning robber in black mask!")
zbui.set_conversation("Sssss... Who is there?")
zbui.set_weakness("coin")
franka.set_character(zbui)

laidak = game.Enemy("Laidka", "Scary man with a big bag.")
laidak.set_conversation("Ahhhhh, what`re you doing there?")
laidak.set_weakness("nuts")
krakivska.set_character(laidak)


cheese = game.Item("cheese")
cheese.set_description("A large and smelly block of cheese")
stryiska.set_item(cheese)

coin = game.Item("coin")
coin.set_description("An ancient silver coin")
krakivska.set_item(coin)


nuts = game.Item("nuts")
nuts.set_description("Neat little bag with nuts")
shevchenka.set_item(nuts)


current_room = stryiska
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["forward", "backward"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 3:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)