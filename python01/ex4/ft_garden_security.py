
class SecurePlant():
    """
    Represent a SecurePlant with name , private height and private age.
    """
    def __init__(self, name: str, height: int, day: int):
        self.name = name
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(day)

    def set_height(self, height: int) -> None:
        """
        Update the value of the private attribute
        """
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        """
        Update the value of the private attribute
        """
        if (age < 0):
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Impossible ages rejected")
            return
        self.__day = age
        print(f"Age updated: {self.__day} days [OK]")

    def get_height(self) -> int:
        """
        Return the current height of the plant.

        Returns:
            int: height in cm
        """
        return self.__height

    def get_age(self) -> int:
        """
        Return the current age of the plant.

        Returns:
            int: age in days
        """
        return self.__day

    def get_info(self) -> None:
        """
        Display formatted info about the plants
        """
        print(
            f"Current plant: {self.name} "
            f"({self.__height}cm, {self.__day} days)"
            )


def main():
    print("=== Garden Security System ===")

    plant: SecurePlant = SecurePlant("Rose", 25, 30)
    print("")

    plant.set_height(-5)
    print("")

    plant.get_info()


if __name__ == "__main__":
    main()
