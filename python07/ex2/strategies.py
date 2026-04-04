
from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, crt: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, crt: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, crt: Creature) -> None:
        print(crt.attack())

    def is_valid(self, crt: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, crt: Creature) -> None:
        if not self.is_valid(crt):
            raise Exception(
                f"Invalid Creature '{crt.name}' for this aggressive strategy"
                )
        if isinstance(crt, TransformCapability):
            print(crt.transform())
            print(crt.attack())
            print(crt.revert())

    def is_valid(self, crt: Creature) -> bool:
        return isinstance(crt, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, crt: Creature) -> None:
        if not self.is_valid(crt):
            raise Exception(
                f"Invalid Creature '{crt.name}' for this defensive strategy"
                )
        if isinstance(crt, HealCapability):
            print(crt.attack())
            print(crt.heal())

    def is_valid(self, crt: Creature) -> bool:
        return isinstance(crt, HealCapability)
