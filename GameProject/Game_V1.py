# todo, fix the inventory logic-done
# todo, make a working system that can add items to the inventory-done
# todo, get the held item to change the stats of the player-done
# todo, add the rest of the map to the game(50%)
# todo, get a enemy that can spawn during an interaction
# todo, make a shop interface and logic
# todo, build the inventory logic so you can use items and select things-done
# TODO: Add combat instead of just printing

import player
import item_dict
import world
import enemy
P1 = player.Player("TempName", 100, 1, 0)

game_running = True
Name = True
inventory = player.backpack
player_inv = player.player_inv
world_map = world.world_map
current_room = "Town square"
selected_item = "None"
inv_open = False
inv_exited = False # Added this to try and fix the exit inv issue
char_name = ""   # Global variable to hold player's name
player.P1 = P1

print("\n" + "="*50)
print("    Welcome to Averneth")
print("    The land of magic and monsters.")
print("="*50 + "\n")

print("Before you go exploring.... I'll need to know your name.",
      )
# Ask for name
while Name:
    char_name = input("What is your character's name?>").strip()
    if char_name == "test":
        break

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
        char_name = char_name  # assign to global variable
        break
    else:
        print("Okay, let's try again.\n")

player.P1.name = char_name
print(f"\nWelcome, brave {char_name}!\n")

# Initialize stats with any starting equipment (currently none)
player.P1.update_stats_from_equipment()


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


def trigger_random_encounter():
    """Chance to spawn an enemy when moving or picking up items in dangerous areas."""
    import random

    # Only 40% chance of encounter (you can adjust this)
    if random.random() > 0.4:
        return False  # no encounter

    enemy_obj = enemy.get_random_enemy()
    if enemy_obj:
        print("\n" + "=" * 40)
        print(f"⚔️  A wild {enemy_obj.name} appears!")
        print(enemy_obj.get_status())
        print("=" * 40)
        return True
    return False

def player_swing():
    """allows the player the attack the space in front of them if combat is initiated"""



def player_has_died():
    """Ends the game if the player HP reaches 0"""
    if player.P1.HP >= 0:
        player_has_died = True
        print("You have died!")
        game_running = False


# ================SECTION 2================
            # Inventory logic

def display_inv():
    print("\n" + "=" * 30)
    print("You open your inventory")
    print(f"{player.P1.name} || HP: {player.P1.hp} | DMG: {player.P1.dmg} | DEF: {player.P1.defence}")
    player.show_backpack()
    player.show_equipped()
    print("\nInventory commands: equip <name>, drop <name>, inspect <name>, exit")
    



#def update_held_item():
#   """Checks what item is in the player hand and updates the stats as needed"""
    

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
        # FIXED: Simplified inventory sub-loop.
        # Used 'cmd' instead of 'command' to avoid overwriting main loop variable.
        # Now equip/drop/inspect work inside inventory.
        while inv_open:
            user_input = input("> ").lower().split()
            if not user_input:
                continue

            cmd = user_input[0]  # using cmd so it doesn't overwrite main command

            if cmd == "exit":
                print("Returning to game...")
                inv_open = False
                inv_exited = True # This should tell the main loop we just exited inv
                # Added 'break' when exiting inventory This stops the main loop from seeing
                # "exit" and stop printing "I don't understand"
                break

            elif cmd == "inv":
                display_inv()  # refresh the inventory display to prevent error


            # FIXED: Now passes player.P1 so equip_item can update stats
            elif cmd == "equip" and len(user_input) > 1:

                item_name = ' '.join(user_input[1:]).title()

                # Call the version in player.py and pass the player object

                player.equip_item(item_name, player.P1)

            elif cmd == "drop" and len(user_input) > 1:
                item_name = ' '.join(user_input[1:]).title()
                player.remove_from_backpack(item_name)

            elif cmd == "inspect" and len(user_input) > 1:
                item_name = ' '.join(user_input[1:]).title()
                player.inspect_item(item_name)

            else:
                print("Unknown inventory command. Try: equip <Item>, drop <Item>, inspect <Item>, or exit")

# ================SECTION 4================
# The commands that run in the game
    if inv_exited:
        inv_exited = False   # reset the flag
        # skip the rest of this loop iteration
    elif command == "go":
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

    #prevents this from running if you exit the inventory
    elif command == "exit":
       continue  # exit from inventory sub-loop - skip unknown command message
    # If the command is an Unknown command
    else:
        print("I don't understand that command.")