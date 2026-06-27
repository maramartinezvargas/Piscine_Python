#!/usr/bin/env python3

from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return a list of ingredients allowed for dark spells."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a dark spell with its ingredients and validation status."""

    validation_status: str = validate_ingredients(ingredients)

    return f"Spell recorded: {spell_name} ({validation_status})"
