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


def main() -> None:
    plants: List[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        for plant in plants:
            plant.age()
            plant.grow()
            plant.get_info()


if __name__ == "__main__":
    main()
