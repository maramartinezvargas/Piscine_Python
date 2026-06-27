#!/usr/bin/env python3

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    """Return a list of ingredients allowed for light spells."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a light spell with its ingredients and validation status."""

    validation_status: str = validate_ingredients(ingredients)

    return f"Spell recorded: {spell_name} ({validation_status})"
