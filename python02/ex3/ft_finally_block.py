from typing import List


def water_plants(plant_list: List[str | None]) -> None:
    """
    Simulate watering a list of plants in the garden.

    This function:
        - Opens the watering system (simulated with a print)
        - Iterates through each plant in the list
        - Waters each valid plant
        - Raises a ValueError if a plant is invalid (None)
        - Always closes the watering system using a finally block

    Args:
        plant_list (list[str | None]): A list of plant names.
        The list may contain invalid entries (None) to simulate
        corrupted or bad input data.

    Raises:
        ValueError: If a plant entry is None.

    The finally block ensures that cleanup always happens,
    even if an error occurs during watering.
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Demonstrate the watering system behavior.

    This function tests:
        - Normal watering with valid plant names
        - Watering with an invalid plant (None)
        - That the watering system is always closed
          thanks to the finally block

    It shows how try/except/finally guarantees
    proper cleanup even when errors occur.
    """
    print("=== Garden Watering System ===")
    print("")
    print("Testing normal watering...")
    plant_list: List[str | None] = [
        "tomato", "lettuce", "carrots"
    ]
    water_plants(plant_list)
    print("Watering completed successfully!")

    print("")

    print("Testing with error...")
    plant_list = [
        "tomato", None
    ]
    water_plants(plant_list)
    print("")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
