
class Plant:
    """
    Represent a plant with name , height and age.
    """
    def __init__(self, name: str, height: int, day: int):
        self.height = height
        self.name = name
        self.day = day

    def get_info(self) -> None:
        """
        Display formatted info about the plants
        """
        print(f"{self.name}: {self.height}cm, {self.day} days old")

    def age(self) -> None:
        """
        increment age of plants by one day
        """
        self.day += 1

    def grow(self) -> None:
        """
        increment height of plants by one cm
        """
        self.height += 1


def main() -> None:
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    init_height: int = plants[0].height
    print("=== Day 1 ===")

    plants[0].get_info()
    for day in range(1, 7):
        for plant in plants:
            plant.age()
            plant.grow()

    print("=== Day 7 ===")
    plants[0].get_info()
    print(f"Growth this week: +{plants[0].height - init_height}cm")


if __name__ == "__main__":
    main()
