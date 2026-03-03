
def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients  # late import

    result: str = validate_ingredients(ingredients)  # appelle le validator

    if result.endswith("- VALID"):
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"
