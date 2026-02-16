
class Plant:
    """
    Represent a plant with name and height.
    """
    def __init__(self, name: str, height: int):
        self.height = height
        self.name = name

    def get_info(self) -> None:
        """
        Display formatted info about the plants
        """
        print(f"- {self.name}: {self.height}cm")

    def grew(self) -> None:
        """
        Dsiplay that plant is grewing and increment height
        """
        print(f"{self.name} grew 1cm")
        self.height += 1

class FloweringPlant(Plant):
    """
    Represent a flower with name , height and color.
    """
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> None:
        """
        Display detailed information about the flower
        """
        print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """
    Represent a prizeFlower with name , height , age , color and prize points.
    """
    def __init__(self, name: str, height: int, color: str,  prize_points: int):
        super().__init__(name, height, color)
        self.prize_points =  prize_points

    def get_info(self) -> None:
        """
        Display detailed information about the flower
        """
        print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.prize_points}")


class GardenManager:
    total_gardens = 0
    def __init__(self, owner):
        self.owner = owner
        self.garden = []
    class GardenStats:
        @staticmethod
        def get_garden_stats():
            print("=== Alice's Garden Report ===")
            
    @classmethod
    def create_garden_network(cls):
        total_gardens += 1
        return cls("new garden")
    def add_plant_to_garden(self, plant:Plant):
        self.garden.append(plant)
        print(f"Added Oak Tree to {self.owner}'s garden")
    def grew_plant(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.garden:
            plant.grew()
    