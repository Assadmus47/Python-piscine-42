from typing import List


class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when an operation fails due to plant-related problems."""
    pass


class WaterError(GardenError):
    """Raised when an operation fails due to watering-related problems."""
    pass


class GardenManager:
    """
    Simple garden management system demonstrating robust error handling.

    This class supports:
        - Adding plants to a garden list
        - Watering plants with guaranteed cleanup using finally
        - Validating plant health using custom exceptions

    The goal is to demonstrate defensive programming patterns where
    the system continues operating even when some operations fail.
    """

    def __init__(self):
        """Initialize an empty garden."""
        self.plants: List[str] = []

    def add_plant_to_garden(self, plant: str) -> None:
        """
        Add a plant to the garden.

        Args:
            plant (str): Plant name to add.

        Raises:
            PlantError: If the name is empty or already exists in the garden.
        """
        if (plant in self.plants):
            raise PlantError("Plant already exists in the garden!")
        if (not plant):
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant)
        print(f"Added {plant} successfully")

    def water_plants(self) -> None:
        """
        Water all plants in the garden.

        This method simulates opening a watering system, watering each plant,
        and always closing the system using a finally block.

        Raises:
            WaterError: If watering cannot be performed (invalid plant entry).
        """
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
        """
        Validate plant health conditions.

        Args:
            plant_name (str): Name of the plant to check.
            water_level (int): Water level between 1 and 10.
            sunlight_hours (int): Sunlight hours between 2 and 12.

        Raises:
            PlantError: If the plant name is invalid or not in the garden.
            WaterError: If the water level is invalid.
            PlantError: If sunlight hours
            are invalid (or use another custom error).
        """
        if (not plant_name):
            raise PlantError("Plant name cannot be empty!")

        if (plant_name not in self.plants):
            raise PlantError("This plant does not exist in the garden")

        if (water_level > 10):
            raise WaterError(
                f"Water level {water_level} is too high (max 10)"
                )

        elif (water_level < 1):
            raise WaterError(
                f"Water level {water_level} is too low (min 1)"
                )

        if (sunlight_hours > 12):
            raise PlantError(
                f"Sunlight hours {sunlight_hours} are too high (max 12)"
                )

        elif (sunlight_hours < 2):
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
                )

        print(
            f"{plant_name}: healthy "
            f"(water: {water_level}, sun: {sunlight_hours})"
            )


def test_garden_management() -> None:
    """
    Demonstrate the garden management system behavior.

    This function tests:
        - Adding valid plants
        - Handling invalid plant inputs
        - Watering plants with cleanup via finally
        - Checking plant health with both valid and invalid values
        - Error recovery using GardenError
    """
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

    try:
        garden.check_plant_health("tomato", 5, 8)
    except (PlantError, WaterError) as e:
        print("Error checking tomato:", e)

    try:
        garden.check_plant_health("lettuce", 15, 6)
    except (PlantError, WaterError) as e:
        print("Error checking lettuce:", e)

    print("")

    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except (GardenError, WaterError) as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")
    print("")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
