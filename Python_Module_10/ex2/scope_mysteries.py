#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any

Counter = Callable[[], int]
Accumulator = Callable[[int], int]
Enchantment = Callable[[str], str]


def mage_counter() -> Counter:
    """Return a closure that counts how many times it has been called."""
    count = 0

    def increase() -> int:
        nonlocal count
        count += 1
        return count

    return increase


def spell_accumulator(initial_power: int) -> Accumulator:
    """Return a closure that accumulates power starting from a value."""
    power_count = initial_power

    def accumulate(power: int) -> int:
        nonlocal power_count
        power_count += power
        return power_count
    return accumulate


def enchantment_factory(enchantment_type: str) -> Enchantment:
    """Return a closure that applies a fixed enchantment type to an item."""

    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    """Return a private memory system with store and recall
    functions implemented as closures.
    """
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        if key in vault:
            return vault[key]
        return "Memory not found"
    return {
        "store": store,
        "recall": recall,
    }


def main() -> None:
    print("Testing mage counter...")
    a = mage_counter()
    b = mage_counter()
    print(f"counter_a call 1: {a()}")
    print(f"counter_a call 2: {a()}")
    print(f"counter_b call 1: {b()}")

    print("\nTesting spell accumulator...")
    initial_power = 100
    c = spell_accumulator(initial_power)
    add1 = 20
    add2 = 30
    print(f"Base {initial_power}, add {add1}:"
          f" {c(add1)}")
    print(f"Base {initial_power}, add {add2}:"
          f" {c(add2)}")

    print("\nTesting enchantment factory...")
    fire = enchantment_factory("Flaming")
    ice = enchantment_factory("Frozen")
    print(fire("Sword"))
    print(ice("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    secret = 42
    print(f"Store 'secret' = {secret}")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
