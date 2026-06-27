#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/darki_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(f"{dark_spell_record('Fantasy', 'Earth, wind and air')}")
