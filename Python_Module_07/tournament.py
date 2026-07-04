#!/usr/bin/env python3

from typing import Any
from ex0.factories import AquaFactory, FlameFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import (NormalStrategy, AggressiveStrategy,
                          DefensiveStrategy)
from ex2.strategy import InvalidStrategyError


def battle(opponents: list[tuple[Any, Any]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    # Simulate battles between all pairs of opponents
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            # Show battle creatures
            print("\n* Battle *")
            print(f"{creature1.describe()} "
                  "\n vs.\n"
                  f"{creature2.describe()}"
                  "\n now fight!")

            # Try strategy with each creature (handling invalid strategies)
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def display_opponents(opponents: list[tuple[Any, Any]]) -> str:
    # Create a list to hold the formatted names of the opponents
    names = []

    # Loop through each opponent and format their names
    for factory, strategy in opponents:
        creature = factory.create_base()

        creature_name = creature.name
        strategy_name = strategy.__class__.__name__.replace("Strategy", "")

        names.append(f"({creature_name}+{strategy_name})")
    # Return the formatted list of names as a string
    return "[ " + ", ".join(names) + " ]"


if __name__ == "__main__":
    # Initialize factories
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    # Initialize strategies
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    # Tournament 0: Basic --------------------------------------
    print("Tournament 0: (basic)")
    opponents = [(flame_factory, normal), (heal_factory, defensive)]
    print(display_opponents(opponents))
    battle(opponents)

    # Tournament 1: Error handling -----------------------------
    print("\nTournament 1: (error)")
    opponents1 = [(flame_factory, aggressive), (heal_factory, defensive)]
    print(display_opponents(opponents1))
    battle(opponents1)

    # Tournament 2: multiple -----------------------------
    print("\nTournament 2: (multiple)")
    opponents2 = [(aqua_factory, normal),
                  (heal_factory, defensive),
                  (transform_factory, aggressive)]
    print(display_opponents(opponents2))
    battle(opponents2)
