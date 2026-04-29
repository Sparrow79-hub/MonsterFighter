# todo, fix the inventory logic-done
# todo, make a working system that can add items to the inventory-done
# todo, get the held item to change the stats of the player-done
# todo, add the rest of the map to the game(50%)
# todo, get a enemy that can spawn during an interaction
# todo, make a shop interface and logic
# todo, build the inventory logic so you can use items and select things-done
# TODO: Add combat instead of just printing
# TODO: Game over screen later
# TODO: Add leveling system later

import player
# import item_dict
import world
import enemy
from typing import Optional

P1 = player.Player("TempName", 100, 1, 0)

game_running = True
Name = True
inventory = player.backpack
player_inv = player.player_inv
world_map = world.world_map
current_room = "Town square"
current_enemy: Optional["enemy.Enemy"] = None
in_combat = False
player_has_died = False
selected_item = "None"
inv_open = False
inv_exited = False # Added this to try and fix the exit inv issue
char_name = ""   # Global variable to hold player's name


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

P1.name = char_name
print(f"\nWelcome, brave {char_name}!\n")

# Initialize stats with any starting equipment (currently none)
P1.update_stats_from_equipment()


# ================SECTION 1================
# Main game logic functions

def show_status():
    """Reports the player's current location and the items in the area."""
    print("\n" + "=" * 30)
    print(f"Location: {current_room}")
    print(f"Description: {world_map[current_room]['description']}")
    print(f"items: {world_map[current_room]['item']}")
    print("=" * 30)

def trigger_random_encounter():
    """Chance to spawn an enemy and start combat."""
    import random
    global current_enemy, in_combat

    if random.random() > 0.4:  # 40% chance
        return False

    enemy_obj = enemy.get_random_enemy()
    if enemy_obj:
        current_enemy = enemy_obj
        in_combat = True
        print("\n" + "=" * 50)
        print(f"⚔️  A wild {enemy_obj.name} appears!")
        print(enemy_obj.get_status())
        print("You are now in combat!")
        print("Commands: swing, run, inv, status")
        print("=" * 50)
        return True
    return False


def move_player(direction):
    """Handles moving + possible enemy encounter in the new room."""
    global current_room

    if direction in world_map[current_room]:
        current_room = world_map[current_room][direction]
        print(f"You walk to the {direction}...")

        # ====================== ENCOUNTER LOGIC ======================
        # Get safety of the NEW room we just entered
        safety = world_map[current_room].get("Safety", 100)  # default = safe

        if safety <= 95:  # dangerous room
            print("This area feels dangerous...")
            trigger_random_encounter()  # This will start combat if it triggers
        # ============================================================

    else:
        print("You can't go that way!")


def pick_up_item():
    """Attempt to pick up item. Triggers combat in dangerous rooms."""
    global in_combat, current_enemy

    room_data = world_map[current_room]

    if "item" not in room_data or not room_data["item"]:
        print("There's nothing here to pick up.")
        return

    item = room_data["item"]

    # ====================== SAFETY CHECK ======================
    # Only trigger combat in dangerous areas
    if "Safety" in room_data and room_data["Safety"] <= 95:
        print("This area feels dangerous...")
        trigger_random_encounter()

        # If combat started, player must win first
        if in_combat:
            print(f"You must defeat the enemy before claiming the {item}!")
            return  # Exit without giving the item
    # ==========================================================

    # If we reach here → either safe room OR you already won the fight
    if player.add_to_backpack(item):
        room_data["item"] = ""  # remove from room
        print(f"You picked up the {item}!")
    else:
        print("But your backpack is full — you can't carry it.")

def player_death():
    """Ends the game if the player HP reaches 0"""
    global player_has_died, game_running, P1

    if P1.hp >= 0:
        player_has_died = True
        print("You have died!")
        game_running = False

def enemy_attack():
    """Enemy attacks the player."""
    global in_combat, P1
    if not current_enemy:
        return
    damage = max(1, current_enemy.attack - P1.defence // 2)
    P1.hp -= damage
    print(f"The {current_enemy.name} hits you for {damage} damage!")

    if P1.hp <= 0:
        player_death()


def player_swing():
    """allows the player the attack the space in front of them if combat is initiated"""
    global current_enemy, in_combat, P1

    if not current_enemy:
        return

    damage = P1.dmg  # Use your current equipped damage
    # Simple damage calculation (can improve later)
    actual_damage = max(1, damage - current_enemy.defence // 2)

    current_enemy.health -= actual_damage
    print(f"You hit the {current_enemy.name} for {actual_damage} damage!")

    if current_enemy.health <= 0:
        print(f"You defeated the {current_enemy.name}!")
        P1.gain_exp(current_enemy.xp_reward)

        # ====================== LOOT DROP ======================
        # Drop ALL items the enemy has (weapon + armor + items list)
        loot_list = []

        if current_enemy.weapon:
            loot_list.append(current_enemy.weapon)
        if current_enemy.armor:
            loot_list.append(current_enemy.armor)
        if current_enemy.items:  # this is already a list
            loot_list.extend(current_enemy.items)

        # Try to add each item to backpack
        for items in loot_list:
            if player.add_to_backpack(items):
                print(f"The {current_enemy.name} dropped {items}!")
            else:
                print(f"The {current_enemy.name} dropped {items}, but your backpack is full!")
        # ======================================================

        in_combat = False
        current_enemy = None
        return

    # Enemy attacks back
    enemy_attack()

def attempt_run():
    """Try to flee from combat."""
    import random
    global in_combat, current_enemy, P1
    if not current_enemy:
        return
    if random.random() > 0.5:   # 50% chance to escape
        print("You successfully ran away!")
        in_combat = False
        current_enemy = None
    else:
        print("Couldn't escape!")
        enemy_attack()

def show_combat_status():
    """allows the player to check the status of player and enemy to keep an eye on health."""
    global in_combat, current_enemy, P1
    if not current_enemy:
        return
    print("\n" + "=" * 30)
    print(f"Player HP: {P1.hp} | DMG: {P1.dmg}")
    if current_enemy:
        print(current_enemy.get_status())
    print("=" * 30)

# ================SECTION 2================
            # Inventory logic

def display_inv():
    print("\n" + "=" * 30)
    print("You open your inventory")
    print(f"{P1.name} || HP: {P1.hp} | DMG: {P1.dmg} | DEF: {P1.defence}")
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

    # ====================== COMBAT HANDLING ======================
    while in_combat:  # Changed to while so it keeps asking for combat commands
        if command == "swing":
            player_swing()
        elif command == "run":
            attempt_run()
        elif command == "status":
            show_combat_status()
        elif command == "inv":
            display_inv()
        else:
            print("In combat! Use: swing, run, inv, status")

        # Get next input while still in combat
        user_input = input("> ").lower().split()
        if not user_input:
            continue
        command = user_input[0]
    # ============================================================

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


            # FIXED: Now passes P1 so equip_item can update stats
            elif cmd == "equip" and len(user_input) > 1:

                item_name = ' '.join(user_input[1:]).title()

                # Call the version in player.py and pass the player object

                player.equip_item(item_name, P1)

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