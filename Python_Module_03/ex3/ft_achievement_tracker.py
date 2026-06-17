#!/usr/bin/env python3

import random


achievements: list[str] = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner", "Survivor",
    "Treasure Hunter", "First Steps", "Sharp Mind", "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    num_achievements: int = random.randint(5, 10)
    chosen: list[str] = random.sample(achievements, num_achievements)
    return set(chosen)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    # All player achievements
    all_distinct: set[str] = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_distinct}")

    # Common achievement
    common: set[str] = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common}\n")

    # Unique achievements for each player
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print("")

    # Missing achievements
    master_set: set[str] = set(achievements)
    print(f"Alice is missing: {master_set.difference(alice)}")
    print(f"Bob is missing: {master_set.difference(bob)}")
    print(f"Charlie is missing: {master_set.difference(charlie)}")
    print(f"Dylan is missing: {master_set.difference(dylan)}")


if __name__ == "__main__":
    main()
