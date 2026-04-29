import item_dict

# test player class
class Player:
    def __init__(self, name, health, damage, defence, **item_equip):
        self.name = name
        self.hp = health
        self.dmg = damage
        self.defence = defence
        self.__dict__.update(item_equip)

    def update_stats_from_equipment(self):
        """Recalculate DMG and DEF based on what is currently equipped.

        WHY: So that equipping a sword actually increases your damage.
        This runs every time you equip or unequip something.
        """
        # Reset to base stats first (prevents old bonuses from staying)
        self.dmg = 1        # your starting base damage
        self.defence = 0    # your starting base defense

        # Loop through every equipped slot
        for slot, item_id in player_inv.items():
            if item_id is None:
                continue  # nothing equipped here

            item_obj = item_dict.get_item(item_id)
            if item_obj is None:
                continue

            # Add weapon damage
            if hasattr(item_obj, 'attack'):
                self.dmg += item_obj.attack

            # Add armor defense
            if hasattr(item_obj, 'defense'):
                self.defence += item_obj.defense

        print(f"   → Stats updated | DMG: {self.dmg} | DEF: {self.defence}")  # temporary debug line
    def gain_exp(self, amount):
        """Gain experience - placeholder for leveling system"""
        print(f"You gained {amount} XP!")


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


def equip_item(item_id, player_obj):
    """Equip an item from backpack and update player stats.
        Better name matching so typing is more forgiving
    """
    item_id = item_id.strip().title()

    # Check backpack with case-insensitive match
    if item_id not in [item.title() for item in backpack]:
        print(f" You do not have '{item_id}' in your backpack")
        return

    # Find the exact name as stored in backpack
    for item in backpack:
        if item.title() == item_id:
            item_id = item
            break

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

    # ===================== IMPORTANT =====================
    # After equipping, update stats so gear actually works
    player_obj.update_stats_from_equipment()
    # ====================================================

def show_equipped():
    """Show all equipped items."""
    print("\n  ── EQUIPPED ────────────────")
    for slot, item_id in player_inv.items():
        display_name = item_id if item_id else "-- empty --"
        print(f"    {slot.capitalize():<12}: {display_name}")
    print("  ────────────────────────────")

    def inspect_item(item_name):
        # """Show details about an item from backpack or equipped."""
        item_obj = item_dict.get_item(item_name)
        if item_obj:
            print(f"\n=== Inspecting: {item_name} ===")
            for attr, value in vars(item_obj).items():
                if not attr.startswith('_'):
                    print(f"  {attr}: {value}")
        else:
            print(f"Could not find item '{item_name}'.")

# NEW FUNCTION: inspect_item()
# Allows player to see full details of any item (attack, defense, etc.)
# Uses the improved get_item() from item_dict.py
# Added because Game_V1.py calls player.inspect_item()
def inspect_item(item_name):
    # """Show details about an item from backpack or equipped."""
    # Make it case-insensitive
    item_obj = item_dict.get_item(item_name)

    if item_obj:
        print(f"\n=== Inspecting: {item_name} ===")
        for attr, value in vars(item_obj).items():
            if not attr.startswith('_'):
                print(f"  {attr}: {value}")
    else:
        print(f"Could not find item '{item_name}'. Try using the exact name shown in your backpack.")


def P1():
    return None