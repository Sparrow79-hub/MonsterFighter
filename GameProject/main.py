# ============================================================
#  main.py
#  The entry point for the game.
#  This file's job is to tie everything together.
#  It should stay clean and readable — the heavy lifting
#  happens in the other files.
#
#  IMPORTS FROM:
#    player.py  →  the Player class
#    items.py   →  all the item instances
#
#  HOW TO RUN:
#    Open this file in PyCharm and press the green Run button.
#    All other files will be loaded automatically.
# ============================================================

from player import Player
from items  import (
    basic_sword,
    iron_sword,
    iron_greatsword,
    poison_dagger,
    basic_armor,
    iron_chestplate,
    health_potion,
)


def main():
    print("\n" + "="*48)
    print("   MINI TERRARIA  —  Player System Test")
    print("="*48)

    # ── Create the player ──────────────────────────────
    # Player only needs a name — everything else starts
    # at default values defined in player.py
    chara = Player("Chara")

    # ── Add items to the backpack ──────────────────────
    print("\n>>> Picking up some starting items...")
    chara.inventory.add_item("Health Potion", 3)
    chara.inventory.add_item("Bread",         5)

    # ── Show starting stats ────────────────────────────
    print("\n>>> Starting stats (no gear equipped):")
    chara.stats()

    # ── Equip starting gear ────────────────────────────
    print(">>> Equipping starting gear...")
    chara.equip(basic_sword)
    chara.equip(basic_armor)
    chara.stats()

    # ── Upgrade weapon ─────────────────────────────────
    print(">>> Upgrading to Iron Greatsword...")
    chara.equip(iron_greatsword)
    chara.stats()

    # ── Simulate taking damage ─────────────────────────
    print(">>> Taking damage in a battle...")
    chara.take_damage(12)   # armor should absorb some
    chara.take_damage(5)
    chara.take_damage(3)    # small hit — defense might absorb most of it

    # ── Use a health potion ────────────────────────────
    print("\n>>> Using a Health Potion...")
    if chara.inventory.has_item("Health Potion"):
        chara.heal(30)
        chara.inventory.drop_item("Health Potion", 1)
    else:
        print("  ✗  No potions left!")

    # ── Gain EXP and level up ──────────────────────────
    print("\n>>> Winning a battle — gaining EXP...")
    chara.gain_exp(60)
    chara.gain_exp(55)   # this pushes over 100 → triggers level up!

    # ── Unequip a slot ─────────────────────────────────
    print(">>> Taking armor off...")
    chara.unequip("armor")

    # ── Final stats ────────────────────────────────────
    print(">>> Final stats:")
    chara.stats()


# ── This block means: only run main() if you run THIS file directly.
#    If another file imports main.py, main() won't run automatically.
#    This is a standard Python best practice.
if __name__ == "__main__":
    main()
