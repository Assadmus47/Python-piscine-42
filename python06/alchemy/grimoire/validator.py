
def validate_ingredients(ingredients: str) -> str:
    valid_elements: list[str] = ["fire", "water", "earth", "air"]

    if any(element in ingredients for element in valid_elements):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
