
def check_temperature(temp_str: str) -> int | None:
    """
    Validate and process a temperature reading for garden plants.

    This function attempts to convert a string input into an integer
    temperature value. It checks whether the temperature is within the
    acceptable range for plants (0 to 40 degrees Celsius).

    Args:
        temp_str (str): The temperature value provided as a string.

    Returns:
        int | None: The valid temperature if within range,
        otherwise None if an error occurs.

    Raises:
        ValueError: If the temperature is outside the valid range.
    """
    try:
        temperature: int = int(temp_str)
        if temperature > 40:
            raise ValueError(
                f"{temperature}°C is too hot for plants (max 40°C)"
                )
        if temperature < 0:
            raise ValueError(
                f"Error: {temperature}°C is too cold for plants (min 0°C)"
                )
        print(f"Temperature {temperature}°C is perfect for plants!")
        return temperature

    except ValueError as error:
        print("Error:", error)


def test_temperature_input() -> None:
    """
    Demonstrate temperature validation with different test cases.

    This function tests:
        - A valid temperature ("25")
        - A non-numeric input ("abc")
        - A temperature that is too high ("100")
        - A temperature that is too low ("-50")

    It shows that the program continues running even when
    errors occur.
    """
    print("=== Garden Temperature Checker ===")
    print("")
    print("Testing temperature: 25")
    check_temperature("25")
    print("")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("")
    print("Testing temperature: 100")
    check_temperature("100")
    print("")
    print("Testing temperature: -50")
    check_temperature("-50")
    print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
