
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
        print(
            f"- {self.name}: {self.height}cm"
            ", {self.color} flowers (blooming)"
            )


class PrizeFlower(FloweringPlant):
    """
    Represent a prizeFlower with name , height , age , color and prize points.
    """
    def __init__(self, name: str, height: int, color: str,  prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self) -> None:
        """
        Display detailed information about the flower
        """
        print(
            f"- {self.name}: {self.height}cm,"
            " {self.color} flowers (blooming),"
            " Prize points: {self.prize_points}"
            )


class GardenManager:
    total_gardens: int = 0
    all_gardens: list[GardenManager] = []

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        self.stats = GardenManager.GardenStats(self)
        GardenManager.all_gardens.append(self)
        GardenManager.total_gardens += 1

    class GardenStats:
        def __init__(self, manager):
            self.manager = manager

        def get_garden_report(self) -> None:
            print(f"=== {self.manager.owner}'s Garden Report ===")
            print("Plants in garden:")
            for plant in self.manager.plants:
                plant.get_info()
            print("")
            counts: int = self.count_plant_types()
            print(
                f"Plants added: {len(self.manager.plants)},"
                " Total growth: {self.manager.total_growth}cm"
            )
            print(
                f"Plant types: {counts['regular']} regular,"
                " {counts['flowering']} flowering,"
                " {counts['prize']} prize flowers"
                )

        def count_plant_types(self) -> dict:
            """Compte combien de chaque type de plante"""
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in self.manager.plants:
                if type(plant).__name__ == "Plant":
                    counts["regular"] += 1
                elif type(plant).__name__ == "FloweringPlant":
                    counts["flowering"] += 1
                elif type(plant).__name__ == "PrizeFlower":
                    counts["prize"] += 1
            return counts

        def calculate_score(self) -> int:
            """Calcule le score = somme de toutes les hauteurs"""
            total: int = 0
            for plant in self.manager.plants:
                total += plant.height
            return total

    @classmethod
    def create_garden_network(cls):
        return cls("new garden")

    def add_plant_to_garden(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grew_plant(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grew()
            self.total_growth += 1

    @staticmethod
    def validate_height(height: int) -> bool:
        """Valide qu'une hauteur est positive"""
        return height > 0

    @classmethod
    def display_all_garden_scores(cls) -> None:
        """Affiche les scores de tous les jardins"""
        print("Garden scores", end="")

        for i, garden in enumerate(cls.all_gardens):
            score: int = garden.stats.calculate_score()
            if i == 0:
                print(f" - {garden.owner}: {score}", end="")
            else:
                print(f", {garden.owner}: {score}", end="")

        print()  # retour à la ligne
        print(f"Total gardens managed: {cls.total_gardens}")


def main():
    print("=== Garden Management System Demo ===")
    print("")
    alice: GardenManager = GardenManager("Alice")

    oak: Plant = Plant("Oak Tree", 100)
    rose: FloweringPlant = FloweringPlant("Rose", 25, "red")
    sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant_to_garden(oak)
    alice.add_plant_to_garden(rose)
    alice.add_plant_to_garden(sunflower)

    print("")

    alice.grew_plant()

    print("")

    alice.stats.get_garden_report()

    print("")
    print(f"Height validation test: {GardenManager.validate_height(100)}")

    bob: GardenManager = GardenManager("Bob")
    oak = Plant("Oak Tree", 92)
    bob.add_plant_to_garden(oak)

    GardenManager.display_all_garden_scores()


if __name__ == "__main__":
    main()
