
def ft_garden_intro() -> None:
    """
    Display introductory information about a plant in the garden.

    Prints the plant's name, height, and age in a formatted way,
    surrounded by a welcome header and an end message.
    """
    color: str = "Rose"
    height: int = 25
    age: int = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {color}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("")
    print("=== End of Program ===")


def main() -> None:
    ft_garden_intro()


if __name__ == "__main__":
    main()
