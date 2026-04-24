import item_dict


# test player class
class Player:
    def __init__(self, name, health, damage, defence, **item_equip):
        self.name = name
        self.hp = health
        self.dmg = damage
        self.defence = defence
        self.__dict__.update(item_equip)

P1 = Player("", 100, 1, 0)

# makes a backpack for player to use
backpack = []

def add_to_backpack(item_id):
    #adds an item to the backpack
    if len(backpack) >= 15:
        print(f'{item_id} cannot be added, backpack is full.')
        return False
    else:
        backpack.append(item_id)
        print(f"{item_id} added to backpack")
        return True


def remove_from_backpack(item_id):
    #removes one item from backpack
    if item_id in backpack:
        backpack.remove(item_id)
        print(f"{item_id} removed from backpack")
        return True
    else:
        print(f"{item_id} not in backpack")
        return False

def show_backpack():
    #displays everything in the backpack.
    if not backpack:
        print("Backpack is empty")
    else:
        print("\n  ── BACKPACK ────────────────")
        for i, item in enumerate(backpack, 1):
            print(f"    {i}. {item}")
        print("  ────────────────────────────\n")


# makes a player inv
player_inv = {
    "right hand": None, # Nothing equipped at start
    "left hand": None, # Nothing equipped at start
    "head": None, # Nothing equipped at start
    "armor": None, # Nothing equipped at start
    "feet": None, # Nothing equipped at start
    }

def equip_item(item_id): #Right now I don't think any of this works, so I'm going to rebuild it
    # Check if item is in backpack
    if item_id not in backpack:
        print(f" You do not have {item_id} in your backpack")
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
        backpack.append(old_item)
        print(f"↩ Unequipped '{old_item}' from {slot}")

    # Equip the new item
    player_inv[slot] = item_id
    backpack.remove(item_id)
    print(f"✓ Equipped '{item_id}' in {slot} slot")


def show_equipped():
    """Show all equipped items."""
    print("\n  ── EQUIPPED ────────────────")
    for slot, item_id in player_inv.items():
        display_name = item_id if item_id else "-- empty --"
        print(f"    {slot.capitalize():<12}: {display_name}")
    print("  ────────────────────────────")

    def inspect_item(item_name):
        """Show details about an item from backpack or equipped."""
        item_obj = item_dict.get_item(item_name)
        if item_obj:
            print(f"\n=== Inspecting: {item_name} ===")
            for attr, value in vars(item_obj).items():
                if not attr.startswith('_'):
                    print(f"  {attr}: {value}")
        else:
            print(f"Could not find item '{item_name}'.")