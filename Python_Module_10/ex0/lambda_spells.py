from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]],
                    ) -> list[dict[str, Any]]:
    """Sort artifacts by descending power."""
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(mages: list[dict[str, Any]], min_power: int,
                 ) -> list[dict[str, Any]]:
    """Filter mages with power greater than or equal to min_power."""
    return list(filter(lambda mage: mage["power"] >= min_power, mages,))


def spell_transformer(spells: list[str]) -> list[str]:
    """Decorate spell names."""
    return list(map(lambda spell: f"* {spell} *", spells,))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    """Calculate mage power statistics."""
    return {
        "max_power": max(mages, key=lambda mage: mage["power"],)["power"],
        "min_power": min(mages, key=lambda mage: mage["power"],)["power"],
        "avg_power": round(sum(mage["power"]
                               for mage in mages) / len(mages), 2,),
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
    ]

    spells = [
        "fireball",
        "heal",
        "shield",
    ]

    mages = [
        {"name": "Mara", "power": 120, "element": "water"},
        {"name": "Gandalf", "power": 90, "element": "light"},
        {"name": "Merlín", "power": 40, "element": "fire"},
    ]

    print()
    print("Testing artifact sorter...")
    artifacts = artifact_sorter(artifacts)
    print(
        f"{artifacts[0]['name']} ({artifacts[0]['power']} power) "
        f"comes before "
        f"{artifacts[1]['name']} ({artifacts[1]['power']} power)"
    )

    print()
    print("Testing spell transformer...")
    print(*spell_transformer(spells))

    """print("\nTesting power filter (min_power = 80)...")
    powerful_mages = power_filter(mages, min_power=80)
    for mage in powerful_mages:
        print(f" - {mage['name']} ({mage['element']}): {mage['power']} power")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f" Max Power : {stats['max_power']}")
    print(f" Min Power : {stats['min_power']}")
    print(f" Avg Power : {stats['avg_power']}")"""
