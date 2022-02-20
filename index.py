

print('''Welcome to your entrance exam for Draco Academy!
This exam will determine if you are worthy of acceptance into the school. 
You will be navigating 8 rooms, picking up all weapons and health 
needed to defeat the monster that will be waiting for you at the final room. ''')

bagPack = []

roomAndWeapons = {
    "Room1":"Sword",
    "Room2":"Shield",
    "Room4":"Helmet",
    "Room7":"Body Armor",
    "Room5":"Veggies",
    "Room6":"Time Amulet"
}

def roomOne():
    print()
    print('''Hi welcome to the hall of Einstein!In this room there is a Sword.''')
    getSword = input("Would you like to add this sword to your bag pack? ")
    if getSword  == 'Y':
        bagPack.append(roomAndWeapons["Room1"])
        print(f"Your bag pack now has {bagPack}")
        print()
    
    print("You can go east or you can go south. I'll recommend going east first ;)")
    enterDirection = input("What direction would you like to go? ")
    if enterDirection == "go east":
        return roomSeven()
    elif enterDirection == "go south":
        return roomThree()
    elif enterDirection == "go north" or "go west":
        print("You can't go that direction.")
    else:
        print("Enter a valid direction.")

def roomTwo():
    print('''Hi welcome to the hall of Faraday.''')
    #North and east
    return 0

def roomThree():
    count = 0
    print()
    print('''Welcome to the main room. In this room you can go in any direction.''')
    
    readyToPlay = input("Are you ready to play? ")
    while readyToPlay != 'no':
        enterDirection = input("Enter a direction ('go north', 'go east', 'go west', 'go south'): ")
        if enterDirection == 'go north':
            return roomOne()
        elif enterDirection == 'go south':
            return roomTwo()
        elif enterDirection == 'go west':
            return roomFour()
        elif enterDirection == 'go east':
            return roomFive()
        else:
            print("Enter a valid room")

def roomFour():
    print('''Hi welcome to the hall of Nikola Tesla.''')
    #east
    return 0

def roomFive():
    print('''Hi welcome to the wall of Mercedez.''')
    #west and north 
    return 0

def roomSix():
    print('''Hi welcome to the wall of Einstein.''')
    #west
    return 0

def roomSeven():
    print()
    print('''Hi welcome to the Hall of Dumbledore. In this room there is a Body Armor.''')
    getSword = input("Would you like to add this body armor to your bag pack? ")
    if getSword  == 'Y':
        bagPack.append(roomAndWeapons["Room7"])
        print(f"Your bag pack now has {bagPack}")
        print()
    
    print("Only way to go now is West. Back to Einstein hall.")
    enterDirection = input("What direction would you like to go? ")
    if enterDirection == "go west":
        return roomOne()
    else:
        print("There is no way or room to go except west")

    #west

def roomEight():
    print('''Hi welcome to the wall of Einstein.''')
    #monster room
    return 0

roomThree()


# for room in roomAndWeapons:
#     print(roomAndWeapons[room])