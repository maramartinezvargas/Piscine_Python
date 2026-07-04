#!/usr/bin/env python3

from ex1.factories import HealingCreatureFactory, TransformCreatureFactory


def test_healing_capbility(heal_factory: HealingCreatureFactory) -> None:
    base_creature = heal_factory.create_base()
    evolved_creature = heal_factory.create_evolved()

    print("Testing Creature with healing capability")
    print(" base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal())

    print(" evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal())


def test_transform_capability(
    transform_factory: TransformCreatureFactory
) -> None:
    base_creature = transform_factory.create_base()
    evolved_creature = transform_factory.create_evolved()

    print("Testing Creature with transform capability")
    print(" base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())

    print(" evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())


if __name__ == "__main__":
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing_capbility(heal_factory)
    print()
    test_transform_capability(transform_factory)
