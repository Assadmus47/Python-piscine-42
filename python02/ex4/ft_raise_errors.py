
def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> str:
    """
    Validate the health conditions of a plant.

    This function checks:
        - The plant name is not empty
        - The water level is between 1 and 10
        - The sunlight hours are between 2 and 12

    Args:
        plant_name (str): Name of the plant.
        water_level (int): Water level measurement.
        sunlight_hours (int): Number of sunlight hours.

    Raises:
        ValueError: If any parameter is outside
        the acceptable range.

    Returns:
    str: A success message if all values are valid.
    """
    if (not plant_name):
        raise ValueError("Plant name cannot be empty!")

    if (water_level > 10):
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif (water_level < 1):
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    if (sunlight_hours > 12):
        raise ValueError(
            f"Sunlight hours {sunlight_hours} are too high (max 12)"
            )
    elif (sunlight_hours < 2):
        raise ValueError(
            f"Sunlight hours {sunlight_hours} are too low (min 2)"
            )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """
    Demonstrate validation and error raising
    for plant health checks.

    This function tests:
        - Valid input values
        - Empty plant name
        - Invalid water level
        - Invalid sunlight hours

    It shows how ValueError is raised
    and handled properly without crashing
    the program.
    """
    print("=== Garden Plant Health Checker ===")
    print("")
    try:
        print("Testing good values...")
        print(check_plant_health("tomato", 5, 5))
        print("")
    except ValueError as e:
        print("Error: ", e)
        print("")

    try:
        print("Testing empty plant name...")
        check_plant_health("", 5, 5)
    except ValueError as e:
        print("Error:", e)
        print("")

    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print("Error:", e)
        print("")
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print("Error:", e)
        print("")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
