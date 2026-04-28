# item class for all items

#group together all the different item classes into one so the game can search for everything at once

# Parent class for all items
# This exists so all item types can inherit from it
# Child classes define their own __init__ methods
class Items:
    def __init__(self, item_id, item_type):
        self.item_id = item_id
        self.item_type = item_type

class Melee(Items):
    def __init__(self, item_id, attack, attack_speed, equip_slot="right hand", **special):
        super().__init__(item_id, "weapon")  # Call parent's __init__
        self.equip_slot = equip_slot
        self.attack = attack
        self.atkspd = attack_speed
        self.__dict__.update(special)

class Ranged(Items):
    def __init__(self, item_id, attack, attack_speed, equip_slot="right hand", **special):
        super().__init__(item_id, "weapon")  # Call parent's __init__
        self.equip_slot = equip_slot
        self.attack = attack
        self.atkspd = attack_speed
        self.__dict__.update(special)

class Armor(Items):
    def __init__(self, item_id, defense, equip_slot="armor", **special):
        super().__init__(item_id, "armor")  # Call parent's __init__
        self.equip_slot = equip_slot  # Could be "head", "armor", "feet"
        self.defense = defense
        self.__dict__.update(special)

class Consumables(Items):
    # def for normal item like food and potions
    def __init__(self, item_id, **effect):
        super().__init__(item_id, "potion")  # Call parent's __init__
        self.__dict__.update(effect)


class Holdables(Items):
    # pretty much everything else
    def __init__(self, item_id, tooltip):
        super().__init__(item_id, "tool")  # Call parent's __init__
        self.tooltip = tooltip


# all special abilities
special_1 = {"name": "heavy_slash", "damage": 15}
special_2 = {"name": "fire_dmg", "damage": 4}

# all potion effects
effect_1 = {"name": "Lesser heal", "hp": 25}

# all weapons
item1 = Melee("Basic Sword", 5, 1)
item2 = Melee("Iron Greatsword", 15, 2, **special_1)
item3 = Ranged("Wooden Bow", 2, 1)
item4 = Melee("Torch", 1, 3,**special_2)

# all consumables
item5 = Consumables("Weak Health Potion", **effect_1)

## all armor
item6 = Armor("Shield", 3, equip_slot="left hand")
item7 = Armor("Rusty Helm", 2, equip_slot="head")
item8 = Armor("Worn Boots", 1, equip_slot="feet")
item9 = Armor("Cloth Sack", 2, equip_slot="armor")
item10 = Armor("Leather Armor", 8, equip_slot="armor")

# all items dictionary - ADD THIS LINE
ITEMS = {
    "Basic sword": item1,
    "Iron Greatsword": item2,
    "Wooden Bow": item3,
    "Torch": item4,
    "Health Potion": item5,
    "Shield": item6,
    "Rusty Helm": item7,
    "Feet": item8,
    "Cloth Sack": item9,
    "Leather Armor": item10,
}

def get_item(item_name):
    """Look up an item by its name. Returns the item object or None."""
    if not item_name:
        return None
    item_name = item_name.strip()
    #try exact match first
    if item_name in ITEMS:
        return ITEMS[item_name]
    #try lower case
    title_name = item_name.title()
    if title_name in ITEMS:
        return ITEMS[title_name]
    #case-insensitive backup
    for k, v in ITEMS.items():
        if k.lower() == title_name.lower():
            return v
    return None


