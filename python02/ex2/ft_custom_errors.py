
class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self):
        super().__init__("The tomato plant is wilting!")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("")
    try:
        print("Testing PlantError...")
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
