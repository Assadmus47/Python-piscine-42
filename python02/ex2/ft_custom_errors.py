
class GardenError(Exception):
    """
    Base exception class for all garden-related errors.

    This exception serves as the parent class for all
    custom garden errors. It allows grouping related
    exceptions and catching them with a single
    except GardenError block.
    """
    pass


class PlantError(GardenError):
    """
    Exception raised for plant-related problems.

    This error represents issues affecting plant health
    or plant conditions in the garden system.
    """
    def __init__(self):
        """
        Initialize the PlantError with a default error message.
        """
        super().__init__("The tomato plant is wilting!")


class WaterError(GardenError):
    """
    Exception raised for watering-related problems.

    This error is triggered when the irrigation system
    does not have sufficient water resources.
    """
    def __init__(self):
        """
        Initialize the WaterError with a default error message.
        """
        super().__init__("Not enough water in the tank!")


def test_error_types() -> None:
    """
    Demonstrate the use of custom exception types.

    This function:
        - Raises and catches a PlantError
        - Raises and catches a WaterError
        - Demonstrates that catching GardenError
          also catches its child exceptions

    It shows how inheritance helps organize
    related exception types and improves
    error handling clarity.
    """
    print("=== Custom Garden Errors Demo ===")
    print("")
    print("Testing PlantError...")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("")

    try:
        print("Testing WaterError...")
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
        print("")

    try:
        print("Testing catching all garden errors...")
        raise PlantError()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
        print("")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
