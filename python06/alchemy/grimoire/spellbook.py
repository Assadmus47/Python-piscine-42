
def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients  # late import
    
    result = validate_ingredients(ingredients)  # appelle le validator
    
    if "VALID" in result:
        return "Spell recorded: ..."
    else:
        return "Spell rejected: ..."