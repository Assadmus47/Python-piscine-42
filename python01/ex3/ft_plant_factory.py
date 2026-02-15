from typing import List


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


class PlantFactory():
    def create_plant(
        self, info_plants: List[tuple[str, int, int]]
    ) -> List[Plant]:
        """
        Create liste of plants

        Return List of plants
        """
        plants: List[Plant] = []
        for name, height, day in info_plants:
            plants.append(Plant(name, height, day))
        return plants


def main() -> None:
    print("=== Plant Factory Output ===")
    info_plants: List[tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    factory: PlantFactory = PlantFactory()
    plants: List[Plant] = factory.create_plant(info_plants)

    for plant in plants:
        print("Created: ", end="")
        plant.get_info()

    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()
