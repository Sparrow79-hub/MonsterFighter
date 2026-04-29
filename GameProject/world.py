import item_dict

world_map = {
    "Town square": {
        "description": "A great bustling central location",
        "north": "Great Hall",
        "south": "Blacksmith shop",
        "east": "Merchant",
        "west": "Town gate",
        "item": item_dict.item4.item_id,
        "Safety": 100

    },

    "Great Hall": {
        "description": "A vast room with stone walls and flickering torches.",
        "north": "Library",
        "east": "Armory",
        "south": "Town square",
        "item": item_dict.item1.item_id,
        "Safety": 100
    },
    "Library": {
        "description": "Shelves of dusty books reach the ceiling. It's quiet.",
        "south": "Great Hall",
        "item": " ",
        "Safety": 100
    },
    "Armory": {
        "description": "Racks of rusty swords and shields line the walls.",
        "west": "Great Hall",
        "item": "Shield",
        "Safety": 100
    },

    "Merchant": {
        "description": "The shop of the town. There's nothing here right now.",
        "west": "Town square",
        "east": "Shopkeep",
        "item": "",
        "Safety": 100
    },
    "Shopkeep": {
        "description": "A place you weren't meant to see, everything around you fades away.",
        "west": "Merchant",
        "item": "",
        "Safety": 100
    },
    "Blacksmith shop": {
        "description": "A quaint family run shop that sells basic tools",
        "north": "Town square",
        "item": "",
        "Safety": 100

    },

    "Town gate": {
        "description": "A gate with walls on both sides protecting from outside harm",
        "east": "Town square",
        "west": "Whispering meadows",
        "item": "",
        "Safety": 80
    },

    "Whispering meadows": {
        "description": "An enchanted grassland near the town, there might be monsters here",
        "east": "Town square",
        "west": "Whispering Forest",
        "item": "",
        "Safety": 30
    },

    "Whispering Forest": {
        "description": "",
        "east": "Whispering meadows",
        "north": "Screaming Hills",
        "item": "",
        "Safety": 10
    },

    "Screaming Hills": {
        "description": "",
        "south": "Whispering Forest",
        # "west": "",
        "item": "",
        "Safety": 0
    }

}

test_map = {
    "Testing place":{
        "description": "Test place",
        "item": item_dict.item1.item_id #change this to whatever you need to
    }
}