import item_dict

world_map = {
    "Town square": {
        "description": "A great bustling central location",
        "north": "Great Hall",
        "south": "Blacksmith shop",
        "east": "Merchant",
        "west": "Town gate",
        "item": item_dict.item4.item_id

    },

    "Great Hall": {
        "description": "A vast room with stone walls and flickering torches.",
        "north": "Library",
        "east": "Armory",
        "south": "Town square",
        "item": item_dict.item1.item_id
    },
    "Library": {
        "description": "Shelves of dusty books reach the ceiling. It's quiet.",
        "south": "Great Hall",
        "item": "Ancient Scroll"
    },
    "Armory": {
        "description": "Racks of rusty swords and shields line the walls.",
        "west": "Great Hall",
        "item": "Shield"
    },

    "Merchant": {
        "description": "The shop of the town",
        "west": "Town square",
        "east": "shopkeep",
        "item": "",
    },

    "Blacksmith shop": {
        "description": "A quaint family run shop that sells basic tools",
        "north": "Town square",
        "item": "",

    },

    "Town gate": {
        "description": "A gate with walls on both sides protecting from outside harm",
        "east": "Town square",
        "west": "Whispering meadows",
        "item": ""

    },

    "Whispering meadows": {
        "description": "An enchanted forest near the town, there might be monsters here",
        "east": "Town square",
        "item": "",
    },
}