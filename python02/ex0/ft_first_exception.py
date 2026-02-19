
def check_temperature(temp_str: str) -> int | None:
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
