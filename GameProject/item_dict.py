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
special_2 = {"name": "fire_dmg", "damage": 1}
special_3 = {"name": "Fire Slash", "damage": 6}
special_4 = {"name": "Wicked Slash", "damage": 8}

# all potion effects
effect_1 = {"name": "Lesser heal", "hp": 25}
effect_2 = {"name": "heal", "hp": 50}
effect_3 = {"name": "greater heal", "hp": 75}
effect_4 = {"name": "Max heal", "hp": 100}
effect_5 = {"name": "Defense Boost", "def_bonus": 8, "duration": 5}
effect_6 = {"name": "Strength Boost", "attack_bonus": 8, "duration": 5}
effect_7 = {"name": "Poison", "damage": 8, "duration": 3}
effect_8 = {"name": "Poison", "damage": 3}

# all weapons
item1 = Melee("Basic Sword", 4, 1)
item2 = Melee("Iron Greatsword", 15, 2, two_handed=True, **special_1)
item3 = Ranged("Wooden Bow", 2, 1, two_handed=True)
item4 = Melee("Torch", 1, 3,**special_2)
item18 = Melee("Iron Sword", 8, 1)
item19 = Melee("Steel Dagger", 6, 2, crit_chance=0.15)
item20 = Ranged("Hunter's Bow", 7, 1, two_handed=True)
item21 = Melee("Flame Sword", 12, 1, **special_3)
item35 = Melee("Diamond Sword", 20, 4,**special_4)

# all consumables
item5 = Consumables("Weak Health Potion", **effect_1)
item11 = Consumables("Health Potion", **effect_2)
item12 = Consumables("Greater Health Potion", **effect_3)
item13 = Consumables("Max Health Potion", **effect_4)
item22 = Consumables("Shield Potion", **effect_5)
item23 = Consumables("Strength Elixir", **effect_6)
item24 = Consumables("Poison Vial", **effect_7)
item36 = Consumables("Teeth", **effect_8)

## all armor
item6 = Armor("Wooden Shield", 3, equip_slot="left hand")
item7 = Armor("Rusty Helm", 2, equip_slot="head")
item8 = Armor("Worn Boots", 2, equip_slot="feet")
item9 = Armor("Cloth Sack", 1, equip_slot="armor")
item10 = Armor("Leather Armor", 8, equip_slot="armor")
item14 = Armor("Chainmail", 12, equip_slot="armor")
item15 = Armor("Basic Clothes", 3, equip_slot="armor")
item16 = Armor("Bone Armor", 10, equip_slot="armor")
item17 = Armor("Slate Armor", 15, equip_slot="armor")
item25 = Armor("Iron Armor", 18, equip_slot="armor")
item26 = Armor("Diamond Armor", 28, equip_slot="armor")
item27 = Armor("Cloth Shoes", 1, equip_slot="feet")
item28 = Armor("Leather Boots", 4, equip_slot="feet")
item29 = Armor("Diamond Boots", 15, equip_slot="feet")
item30 = Armor("Bone Helm", 8, equip_slot="head")
item31 = Armor("Iron Helm", 10, equip_slot="head")
item32 = Armor("Diamond Helm", 20, equip_slot="head")
item33 = Armor("Cloth Helm", 1, equip_slot="head")
item34 = Armor("Leather Helm", 4, equip_slot="head")


# all items dictionary - ADD THIS LINE
ITEMS = {
    # ====================== WEAPONS ======================
    "Basic Sword": item1,
    "Iron Greatsword": item2,
    "Wooden Bow": item3,
    "Torch": item4,
    "Iron Sword": item18,
    "Steel Dagger": item19,
    "Hunter's Bow": item20,
    "Flame Sword": item21,
    "Diamond Sword": item35,

    # ====================== CONSUMABLES ======================
    "Weak Health Potion": item5,
    "Health Potion": item11,
    "Greater Health Potion": item12,
    "Max Health Potion": item13,
    "Shield Potion": item22,
    "Strength Elixir": item23,
    "Poison Vial": item24,
    "Teeth": item36,

    # ====================== ARMOR ======================
    "Wooden Shield": item6,
    "Rusty Helm": item7,
    "Worn Boots": item8,
    "Cloth Sack": item9,
    "Leather Armor": item10,
    "Chainmail": item14,
    "Basic Clothes": item15,
    "Bone Armor": item16,
    "Slate Armor": item17,
    "Iron Armor": item25,
    "Diamond Armor": item26,
    "Cloth Shoes": item27,
    "Leather Boots": item28,
    "Diamond Boots": item29,
    "Bone Helm": item30,
    "Iron Helm": item31,
    "Diamond Helm": item32,
    "Cloth Helm": item33,
    "Leather Helm": item34,


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


