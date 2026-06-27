#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validate the ingredients for a dark spell.
    and check if the provided ingredients are valid.
    This explote for circle dependency"""

    status: str = "INVALID"
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()

    for allowed_ingredient in allowed_ingredients:
        if allowed_ingredient in ingredients.lower():
            status = "VALID"
            break

    return f"{ingredients} - {status}"
