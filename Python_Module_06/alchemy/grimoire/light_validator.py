#!/usr/bin/env python3


def validate_ingredients(ingredients: str) -> str:
    """Validate the ingredients for a light spell.
    Import the allowed ingredients from light_spellbook.py
    and check if the provided ingredients are valid."""
    from .light_spellbook import light_spell_allowed_ingredients

    status: str = "INVALID"
    allowed_ingredients: list[str] = light_spell_allowed_ingredients()

    for allowed_ingredient in allowed_ingredients:
        if allowed_ingredient in ingredients.lower():
            status = "VALID"
            break

    return f"{ingredients} - {status}"
