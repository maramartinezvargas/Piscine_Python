#!/usr/bin/env python3

from typing import Any
from ex0.factories import FlameFactory, AquaFactory


def test_factory(factory: Any) -> None:
    """Test the given factory by creating base and evolved creatures and
    printing their descriptions and attacks."""
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print("Testing factory")
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def battle(factory1: Any, factory2: Any) -> None:
    """Simulate a battle between two creatures created by the given
    factories."""
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print("Testing battle")
    print(f"{creature1.describe()} "
          "\n vs.\n"
          f"{creature2.describe()}"
          "\n fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    print()

    test_factory(aqua_factory)
    print()

    battle(flame_factory, aqua_factory)
