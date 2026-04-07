# todo, fix the inventory logic
# todo, make a working system that can add items to the inventory
# todo, get the held item to change the stats of the player
# todo, add the rest of the map to the game(50%)
# todo, get a enemy that can spawn during an interaction
# todo, make a shop interface and logic

import player
import item_dict
import world

game_running = True
inventory = player.backpack
player_inv = player.player_inv
world_map = world.world_map
current_room = "Town square"
inv_open = False

print("\n" + "="*50)
print("    Welcome to Averneth")
print("    The land of magic and monsters.")
print("="*50 + "\n")

print("Before you go exploring.... I'll need to know your name.",
      )
# Ask for name
while True:
    char_name = input("What is your character's name?>").strip()

    if not char_name:
        print("You have to enter something — even adventurers need names!")
        continue

    # Optional: very simple validation (you can make it stricter later)
    if any(c.isdigit() for c in char_name):
        print("Names can't contain numbers in this world. Try letters only.")
        continue

    # If we get here → name looks okay
    confirm = input(f"Is '{char_name}' correct? (y/n): ").lower()
    if confirm.startswith('y'):
        break
    else:
        print("Okay, let's try again.\n")

print(f"\nWelcome, brave {char_name}!\n")

player.P1 = player.Player(char_name, 100, 1, 0)  # defence=0

# ================SECTION 1================
# Main game logic functions

def show_status():
    """Reports the player's current location and the items in the area."""
    print("\n" + "=" * 30)
    print(f"Location: {current_room}")
    print(f"Description: {world_map[current_room]['description']}")
    print(f"items: {world_map[current_room]['item']}")
    print("=" * 30)


def move_player(direction):
    """Handles logic for moving between rooms."""
    global current_room  # We use 'global' because we are changing a variable outside the function

    # Check if the direction is a valid key in the current room's dictionary
    if direction in world_map[current_room]:
        current_room = world_map[current_room][direction]
        print(f"You walk to the {direction}...")
    else:
        print("You can't go that way!")


def pick_up_item():
    room_data = world_map[current_room]
    if "item" in room_data and room_data["item"]:
        item = room_data["item"]
        if player.add_to_backpack(item):
            room_data["item"] = ""   # remove from room
            print(f"You picked up the {item}!")
        else:
            print("But your backpack is full — you can't carry it.")
    else:
        print("There's nothing here to pick up.")


def player_swing():
    """allows the player the attack the space in front of them"""


def change_player_stats():
    """Makes outside input to change the state of the player"""


def player_has_died():
    """Ends the game if the player HP reaches 0"""
    if player.P1.HP >= 0:
        player_has_died = True
        print("You have died!")
        game_running = False


# ================SECTION 2================
            # Inventory logic

def equip_item(item_id):
    # Check if item is in backpack
    if item_id not in player.backpack:
        print(f" You do not have {item_dict.ITEMS} in your backpack")
        return
    # Look up the item in the item_dict
    item_obj = item_dict.get_item(item_id)

    if item_obj is None:
        print(f"✗ '{item_id}' is not a recognized item.")
        return

    # Check if this item CAN be equipped
    if not hasattr(item_obj, 'equip_slot'):
        print(f"✗ '{item_id}' cannot be equipped.")
        return

    slot = item_obj.equip_slot  # e.g. "right hand", "armor", etc.

    # Check if slot exists
    if slot not in player_inv:
        print(f"✗ '{slot}' is not a valid equipment slot.")
        return

    # If something already in that slot, swap it out
    if player_inv[slot] is not None:
        old_item = player_inv[slot]
        player.backpack.append(old_item)
        print(f"↩ Unequipped '{old_item}' from {slot}")

def select_item_in_inv(Items):
    """This checks the stats of the item you have selected"""
    
    if item_dict.ITEMS not in inventory:
        print("You don't have that item")
    else:
        item_dict.ITEMS.item_id in inventory
        print("What would you like to do with this item?")
        print("equip, drop, inspect")

def display_inv():
    print("Commands: 'select, exit'")
    print("You open your inventory")
    print(f"{player.P1.name} || HP: {player.P1.hp} | DMG: {player.P1.dmg} | DEF: {player.P1.defence}")
    player.show_backpack()
    player.show_equipped()
    input("What do you want to do? ")
    
def Equip_item(item_id):
    """Checks to see if there is anything you can equip"""
    if item_id not in inventory:
        print("You have nothing to equip")
    else:
        


def update_held_item():
    """Checks what item is in the player hand and updates the stats as needed"""


# ================SECTION 3================
# The actual running game


print("Commands: 'go [north/south/east/west]', 'get', 'inv', 'swing', 'exit', 'quit'")

while game_running:
    show_status()

    # creates an inventory interface when the game is running

    user_input = input("> ").lower().split()

    if not user_input:
        continue

    command = user_input[0]

    if command == "inv":
        inv_open = True
        display_inv()

        # goes to this loop if the inventory is open
        while inv_open:

            user_input = input("> ").lower().split()

            if not user_input:
                continue

            command = user_input[0]

            # allows player to choose an item in inventory
            if command == "select":
                if len(user_input) > 1:
                    select_item_in_inv(user_input[1])
                    
            elif command  == "equip":
                equip_item(item_dict.ITEMS)

                # allows to drop items from inventory
                # elif command == "drop":
                """remove_item()"""

            # allows the player to leave the inventory
            elif command == "exit":
                print("returning to game")
                inv_open = False

            # Command to inspect selected item in inventory
            elif command == "inspect":
                continue
            else:
                print("That is not a known command")

# ================SECTION 4================
# The commands that run in the game

    # Command Movement
    if command == "go":
        if len(user_input) > 1:
            move_player(user_input[1])
        else:
            print("Go where?")

    # Command Picking up items
    elif command == "get":
        pick_up_item()

    # Command Quit
    elif command == "quit":
        print("Thanks for playing!")
        game_running = False

    # Command Swing
    elif command == "swing":
        player_swing()

    elif command == "equip" and len(user_input) > 1:
        item_name = ' '.join(user_input[1:]).title()
        player.equip_item(item_name)

    elif command == "drop" and len(user_input) > 1:
        item_name = ' '.join(user_input[1:]).title()
        player.remove_from_backpack(item_name)

    elif command == "inspect" and len(user_input) > 1:
        item_name = ' '.join(user_input[1:]).title()
        # Add this function call - see #7 below
        player.inspect_item(item_name)


    #prevents this from running if you exit the inventory
    elif command == "exit":
        continue
    # If the command is an Unknown command
    else:
        print("I don't understand that command.")