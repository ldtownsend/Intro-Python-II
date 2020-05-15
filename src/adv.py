from room import Room
from player import Player
from item import Item

items_dict = {
    'sword': Item("Sword","Sword of Ba'Heer: Good luck in battle!"),
    'book': Item("Book", "Anorak's Almanac: Probably want to study up."),
    'coin': Item("Coin", "Extra Life Quarter: Save for a rainy day..."),
    'grenade': Item("Grenade", "Holy Hand Grenade: Use it to zero out dozens of Sixers"),
    'no item': Item("No item", "There is nothing!")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items_dict['no item']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[items_dict['book']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[items_dict['grenade'], items_dict['book']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items_dict['coin']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items_dict['sword']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


player = Player(input("Ready Player One\n\nWhat is your name? \n\n"), room['outside'], [items_dict['sword']])

print(f"Hello, {player.name}.\n\n{player.current_room}\n\nYou have in your inventory: {[x.item_name for x in player.items]}")

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    cmd = input("--> ").lower()
    
    if cmd in ["n", "s", "e", "w"]:
        #Move to that room
        player.travel(cmd)
    
    elif cmd == "q":
        print("Goodbye!")
        exit()
    
    elif "get" or "take" in cmd:
        add_item = cmd.split(" ")[1]
        if items_dict[add_item] in player.current_room.items:
            player.items.append(items_dict[add_item])
            player.current_room.items.remove(items_dict[add_item])
            print(f"You added {add_item} to your inventory.")
            print([x.item_name for x in player.items])

    elif "drop" in cmd:
        drop_item = cmd.split(" ")[1]
        if items_dict[drop_item] in player.items:
            player.items.remove(items_dict[drop_item])
            player.current_room.items.append(items_dict[drop_item])
            print(f"You removed {drop_item} from your inventory.")
            print([x.item_name for x in player.items])

    else:
        print("I did not understand that command.")