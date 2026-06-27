#!/usr/bin/env python3

# Absolute import
from elements import create_fire

# Relative imports
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: "
            f"brew '{create_air()}' "
            f"and '{strength_potion()}' "
            f"mixed withn '{create_fire()}'"
            )
