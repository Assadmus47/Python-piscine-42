from typing import List


def water_plants(plant_list: List[str]):
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


def test_watering_system():
    print("=== Garden Watering System ===")
    print("")
    print("Testing normal watering...")
    plant_list: List[str] = [
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
