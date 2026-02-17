
class Plant:
    """
    Represent a plant with name , height and age.
    """
    def __init__(self, name: str, height: int, day: int):
        self.height = height
        self.name = name
        self.day = day


class Flower(Plant):
    """
    Represent a flower with name , height , age and color.
    """
    def __init__(self, name: str, height: int, day: int, color: str):
        super().__init__(name, height, day)
        self.color = color

    def bloom(self) -> None:
        """
        Display that flower is blooming
        """
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        """
        Display detailed information about the flower
        """
        print(f"{self.name} ({type(self).__name__}): {self.height}cm, "
              f"{self.day} days, {self.color} color")


class Tree(Plant):
    """
    Represent a tree with name , height , age and trunk_diameter.
    """
    def __init__(self, name: str, height: int, day: int, trunk_diameter: int):
        super().__init__(name, height, day)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        Calculate shade produced by the tree and idsplay it
        """
        print(
            f"{self.name} provides "
            "{self.trunk_diameter * 1.56:g} square meters of shade"
            )

    def get_info(self) -> None:
        """
        Display detailed information about the tree
        """
        print(f"{self.name} ({type(self).__name__}): {self.height}cm, "
              f"{self.day} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represent a vegetable with name , height , age ,
    harvest_season and nutritional_value.
    """
    def __init__(
        self, name: str, height: int, day: int,
        harvest_season: str, nutritional_value: str
    ):
        super().__init__(name, height, day)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional(self) -> None:
        """
        Display nutritional information about the vegetable
        """
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")

    def get_info(self) -> None:
        """
        Display detailed information about the vegetable.
        """
        print(f"{self.name} ({type(self).__name__}): {self.height}cm "
              f"{self.day} days, {self.harvest_season} harvest")


def main():
    print("=== Garden Plant Types ===")
    print("")
    flower: Flower = Flower("Rose", 25, 30, "red")
    flower.get_info()
    flower.bloom()
    print("")
    tree: Tree = Tree("Oak", 500, 1825, 50)
    tree.get_info()
    tree.produce_shade()
    print("")
    tomato: Vegetable = Vegetable(
        "Tomato", 80, 90, "summer harvest", "vitamine c"
        )
    tomato.get_info()
    tomato.nutritional()


if __name__ == "__main__":
    main()
