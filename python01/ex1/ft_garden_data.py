
class Plant:
    """
    Represent a plant with name , height and age.
    """
    def __init__(self, name: str, height: int, age: int):
        self.height = height
        self.name = name
        self.age = age

    def get_info(self) -> None:
        """
        Display formatted info about the plants.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")

    for plant in plants:
        plant.get_info()


if __name__ == "__main__":
    main()
