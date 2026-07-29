from collections.abc import Callable

Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]


def spell_combiner(spell1: Spell, spell2: Spell
                   ) -> Callable[[str, int], tuple[str, str]]:
    """Return a spell that casts both spells."""

    def combined(target: str, power: int) -> tuple[str, str]:
        return (
            spell1(target, power),
            spell2(target, power),
        )

    return combined


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    """Return a spell with amplified power."""

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Condition, spell: Spell) -> Spell:
    """Return a spell that is only cast if the condition is met."""

    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    """Return a spell that casts every spell in order."""

    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power)for spell in spells]

    return sequence


if __name__ == "__main__":

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def enough_power(target: str, power: int) -> bool:
        return power >= 10

    print()
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print()
    print("Testing power amplifier...")
    original_power = 10
    multiplier = 3
    amplified_fireball = power_amplifier(fireball, multiplier)
    print(
        f"Original: {original_power}, "
        f"Amplified: {original_power * multiplier}"
    )

    # print(amplified_fireball("Dragon", original_power))

    # print()
    # print("Testing conditional caster...")
    # conditional_fireball = conditional_caster(
    #     enough_power,
    #     fireball,
    # )
    # print(conditional_fireball("Dragon", 5))
    # print(conditional_fireball("Dragon", 15))

    # print()
    # print("Testing spell sequence...")
    # sequence = spell_sequence(
    #     [
    #         fireball,
    #         heal,
    #     ]
    # )

    # for spell in sequence("Dragon", 10):
    #     print(spell)
