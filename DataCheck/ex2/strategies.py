from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategy(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategy("Invalid AggresiveStrategy for "
                                  f"{creature.creature_name}")

        if not isinstance(creature, TransformCapability):
            raise InvalidStrategy(
                f"Invalid AggressiveStrategy for {creature.creature_name}"
            )

        return [creature.transform(), creature.attack()]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategy("Invalid DefensiveStrategy for "
                                  f"{creature.creature_name}")

        if not isinstance(creature, HealCapability):
            raise InvalidStrategy(
                f"Invalid DefensiveStrategy for {creature.creature_name}"
            )

        return [creature.attack(), creature.heal()]
