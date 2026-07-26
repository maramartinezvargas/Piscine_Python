#!/usr/bin/env python3
import operator
from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any

Enchantment = Callable[[int, str, str], str]
PartialEnchantment = Callable[[str], str]


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers into a single value using the specified op."""

    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
        }
    if operation not in operations:
        raise ValueError("Unknown operation")

    func = operations[operation]
    return reduce(func, spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    """Apply an elemental enchantment with a given power to a target."""
    return f"{element} enchantment hits {target} with {power} power"


def partial_enchanter(enchantment: Enchantment
                      ) -> dict[str, PartialEnchantment]:
    """Create specialized enchantment functions with fixed power
    and element values."""

    holy = partial(enchantment, 50, "Holy")
    poison = partial(enchantment, 50, "Poison")
    earth = partial(enchantment, 50, "Earth")

    return {
        "holy": holy,
        "poison": poison,
        "earth": earth,
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using memoization
    to cache previous results."""

    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Create a single-dispatch spell handler based on the input type."""

    @singledispatch
    def base_spell(spell: Any) -> str:
        return "Unknown spell type"

    @base_spell.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @base_spell.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @base_spell.register(list)
    def _(spells: list[str]) -> str:
        return f"Multi-cast: {len(spells)} spells"

    return base_spell


def main() -> None:

    # Data for testing
    spell_powers: list[int] = [10, 20, 30, 40]
    labels: dict[str, str] = {
        "add": "Sum",
        "multiply": "Product",
        "max": "Max"
    }
    operations: list[str] = ["add", "multiply", "max"]
    elements: list[str] = ["holy", "poison", "earth"]
    targets: list[str] = ["Jenova", "Sephirot", "Aeris"]
    fibonacci_tests: list[int] = [0, 1, 10, 15]

    print("\nTesting spell reducer...")
    for op in operations:
        try:
            print(f"{labels[op]}: {spell_reducer(spell_powers, op)}")
        except ValueError as e:
            print(f"Error: {e}")

    print("\nTesting memoized fibonacci...")
    for n in fibonacci_tests:
        print(f"Fib({n}): {memoized_fibonacci(n)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["heal", "shield", "fireball"]))
    print(dispatcher(3.14))

    print("\nTesting partial enchanter...")
    enchants = partial_enchanter(base_enchantment)
    for element, target in zip(elements, targets):
        print(f"{enchants[element](target)}")


if __name__ == "__main__":
    main()
