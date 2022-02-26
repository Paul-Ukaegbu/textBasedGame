

print('''Welcome to your entrance exam for Draco Academy!
This exam will determine if you are worthy of acceptance into the school. 
You will be navigating 8 rooms, picking up all weapons and health 
needed to defeat the monster that will be waiting for you at the final room. ''')

bagPack = []

roomAndWeapons = {
    "Room1": "Sword",
    "Room2": "Shield",
    "Room4": "Helmet",
    "Room7": "Body Armor",
    "Room5": "Carrots",
    "Room6": "Time Amulet"
}


def room_one():
    print()
    print('''Hi welcome to the hall of Einstein!In this room there is a Sword.''')
    get_sword = input("Would you like to add this sword to your bag pack? ")
    if get_sword == 'Y':
        bagPack.append(roomAndWeapons["Room1"])
        del roomAndWeapons['Room1']
        print(f"Your bag pack now has {bagPack}")
        print()

    print("You can go east or you can go south. I'll recommend going east first ;)")
    enter_direction = input("What direction would you like to go? ")
    if enter_direction == "go east":
        return room_seven()
    elif enter_direction == "go south":
        return room_three()
    elif enter_direction == "go north" or "go west":
        print("You can't go that direction.")
    else:
        print("Enter a valid direction.")


def room_two():
    print()
    print('''Hi welcome to the hall of Faraday! In this room there is a Shield.''')
    get_shield = input("Would you like to add this shield to your bag pack? ")
    if get_shield == 'Y' or 'y':
        bagPack.append(roomAndWeapons["Room2"])
        del roomAndWeapons['Room2']
        print(f"Your bag pack now has {bagPack}")
        print()

    print("You can only go east. This should take you back to the main room")
    enter_direction = input("What direction would you like to go? ")
    if enter_direction == "go east":
        return room_three()
    elif enter_direction == "go north" or "go west" or "go south":
        print("You can't go that direction.")
    else:
        print("Enter a valid direction.")
    # North and east
    return 0


def room_three():
    count = 0
    print()
    print('''Welcome to the main room. In this room you can go in any direction.''')
    
    ready_to_play = input("Are you ready to play? ")
    while ready_to_play != 'no':
        enter_direction = input("Enter a direction ('go north', 'go east', 'go west', 'go south'): ")
        if enter_direction == 'go north':
            return room_one()
        elif enter_direction == 'go south':
            return room_two()
        elif enter_direction == 'go west':
            return room_four()
        elif enter_direction == 'go east':
            return room_five()
        else:
            print("Enter a valid room")


def room_four():
    print()
    print('''Hi welcome to the hall of Nikola Tesla! In this room there is an Helmet.''')
    get_helmet = input("Would you like to add this helmet to your bag pack? ")
    if get_helmet == 'Y' or 'y':
        bagPack.append(roomAndWeapons["Room4"])
        del roomAndWeapons['Room4']
        print(f"Your bag pack now has {bagPack}")
        print()

    print("You can only go east. This should take you back to the main room")
    enter_direction = input("What direction would you like to go? ")
    if enter_direction == "go east":
        return room_three()
    elif enter_direction == "go north" or "go west" or "go south":
        print("You can't go that direction.")
    else:
        print("Enter a valid direction.")
    #east


def room_five():
    print()
    print('''Hi welcome to the wall of Mercedez! In this room there are carrots.''') 
    get_carrots = input("Would you like to add carrots to your bag pack? ")
    if get_carrots == 'Y' or 'y':
        bagPack.append(roomAndWeapons["Room5"])
        del roomAndWeapons['Room5']
        print(f"Your bag pack now has {bagPack}")
        print()

    print("Only directions to go are north or west. If you go west you will be facing the monster.")
    enter_direction = input("What direction would you like to go? ")
    if enter_direction == "go west":
        return room_three()
    elif enter_direction == "go north":
        return room_eight()
    # west and north


def room_six():
    print('''Hi welcome to the wall of Einstein.''')
    # west


def room_seven():
    print()
    print('''Hi welcome to the Hall of Dumbledore. In this room there is a Body Armor.''')
    get_body_armor = input("Would you like to add this body armor to your bag pack? ")
    if get_body_armor == 'Y':
        bagPack.append(roomAndWeapons["Room7"])
        del roomAndWeapons['Room7']
        print(f"Your bag pack now has {bagPack}")
        print()

    print("Only way to go now is West. Back to Einstein hall.")
    enter_direction = input("What direction would you like to go? ")
    if enter_direction == "go west":
        return room_one()
    else:
        print("There is no way or room to go except west")

    # west


def room_eight():
    print('''Now you face the monster Dragon. The only way to defeat the monster is to have all items.
    Let's see if you cam prepared''')
    print(f"Items you have are {bagPack}")
    if len(bagPack) >= 6:
        print("You win! you have the items to defeat the monster")
    else:
        print("You lose! try again next time.")
    # monster room


room_three()

for room in roomAndWeapons:
    print(roomAndWeapons[room])
