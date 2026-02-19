from typing import List


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:

    def __init__(self):
        self.plants: List[str] = []

    def add_plant_to_garden(self, plant: str) -> None:
        if (plant in self.plants):
            raise PlantError("Plant already exist in the garden!")
        if (not plant):
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant)
        print(f"Added {plant} successfully")

    def water_plants(self) -> None:
        try:
            print("Opening watering system")
            for plant in self.plants:
                if plant is None:
                    raise WaterError(
                        "Error: Cannot water None - invalid plant!"
                        )
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self, plant_name: str, water_level: int, sunlight_hours: int
    ) -> None:
        try:
            if (plant_name not in self.plants):
                raise PlantError("Plant these not exist in the garden")

            if (not plant_name):
                raise PlantError("Plant name cannot be empty!")

            if (water_level > 10):
                raise PlantError(
                    f"Water level {water_level} is too high (max 10)"
                    )

            elif (water_level < 1):
                raise PlantError(
                    f"Water level {water_level} is too low (min 1)"
                    )

            if (sunlight_hours > 12):
                raise PlantError(
                    f"Sunlight hours {sunlight_hours} is too high (max 12)"
                    )

            elif (sunlight_hours < 2):
                raise PlantError(
                    f"Sunlight hours {sunlight_hours} is too low (min 2)"
                    )

            print(
                f"{plant_name}: healthy "
                f"(water: {water_level}, sun: {sunlight_hours})"
                )

        except PlantError as e:
            print(f"Error checking {plant_name}:", e)


def test_garden_management():
    print("=== Garden Management System ===")
    garden: GardenManager = GardenManager()
    print("")

    print("Adding plants to garden...")
    try:
        garden.add_plant_to_garden("tomato")
    except PlantError as e:
        print("Error adding plant:", e)
    try:
        garden.add_plant_to_garden("lettuce")
    except PlantError as e:
        print("Error adding plant:", e)
    try:
        garden.add_plant_to_garden("")
    except PlantError as e:
        print("Error adding plant:", e)

    print("")

    print("Watering plants...")
    garden.water_plants()

    print("")

    print("Checking plant health...")
    garden.check_plant_health("tomato", 5, 8)
    garden.check_plant_health("lettuce", 15, 6)

    print("")

    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")
    print("")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
