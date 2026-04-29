import copy

class Enemy:
    def __init__(self, name, description, health, defense, speed, attack, weapon, armor, items, xp_reward=10, loot_chance=0.3):
        self.name = name
        self.description = description
        self.health = health
        self.defense = defense
        self.speed = speed
        self.attack = attack
        self.weapon = weapon
        self.armor = armor
        self.items = items
        self.xp_reward = xp_reward
        self.loot_chance = loot_chance

    def get_status(self):
        """Returns a short status string for combat display"""
        return f"{self.name} | HP: {self.health} | ATK: {self.attack} | DEF: {self.defense}| ITEMS: {self.weapon, self.armor, self.items} | XP: {self.xp_reward}"


Skeleton = Enemy(
    name="Skeleton",
    description="A lifeless walking skeleton",
    health=35,
    defense=0,
    speed=10,
    attack=5,
    weapon="Wooden Bow",
    armor="Wooden Shield",
    items=["Weak Health Potion", "Rusty Helm"],
    xp_reward=15,
    loot_chance=0.9
)
Zombie = Enemy(
    name="Zombie",
    description="A reanimated decomposing human corpse",
    health=45,
    defense=8,
    speed=15,
    attack=15,
    weapon="Hands",
    armor="Cloth Sack",
    items=["Shield Potion", "Greater Health Potion"],
    xp_reward=15,
    loot_chance=0.95
)
Armored_Zombie = Enemy(
    name="Armored Zombie",
    description="A reanimated decomposing human corpse in armor!",
    health=75,
    defense=30,
    speed=10,
    attack=29,
    weapon="Iron Sword",
    armor= "Chainmail",
    items=["Poison Vial", "Greater Health Potion"],
    xp_reward=35,
    loot_chance=0.4
)
Rabid_Dog = Enemy(
    name="Rabid Dog",
    description="A vicious massive dog with rabies!",
    health=35,
    defense=3,
    speed=25,
    attack=9,
    weapon="Teeth",
    armor= "",
    items=["Weak Health Potion", "Basic Clothes"],
    xp_reward=10,
    loot_chance=0.97
)
Goblin = Enemy(
    name="Goblin",
    description="A sneaky green creature with a rusty dagger",
    health=25,
    defense=1,
    speed=14,
    attack=6,
    weapon="Steel Dagger",
    armor="Leather Armor",
    items=["Poison Vial", "Greater Health Potion", "Worn Boots"],
    xp_reward=10,
    loot_chance=0.5
)

Wolf = Enemy(
    name="Dire Wolf",
    description="A large feral wolf with glowing eyes",
    health=30,
    defense=3,
    speed=18,
    attack=8,
    weapon="Teeth",
    armor="",
    items=["Shield Potion", "Strength Elixir", "Weak Health Potion"],
    xp_reward=18,
    loot_chance=0.98
)

Bandit = Enemy(
    name="Bandit",
    description="A ragged highwayman looking for an easy target",
    health=45,
    defense=4,
    speed=12,
    attack=9,
    weapon="Iron Sword",
    armor="Iron Armor",
    items=["Strength Elixir", "Max Health Potion", "Leather Boots"],
    xp_reward=30,
    loot_chance=0.3
)

ENEMIES = {
    "Skeleton": Skeleton,
    "Zombie": Zombie,
    "Armored Zombie": Armored_Zombie,
    "Rabid Dog": Rabid_Dog,
    "Goblin": Goblin,
    "Dire Wolf": Wolf,
    "Bandit": Bandit,
}

def get_random_enemy():
    """Returns a random enemy object from the list.
    Used later for random encounters."""
    import random
    import copy
    if not ENEMIES:
        return None
    enemy_name = random.choice(list(ENEMIES.keys()))
    original = ENEMIES[enemy_name]
    return copy.deepcopy(original)