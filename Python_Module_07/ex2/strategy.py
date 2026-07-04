#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Any) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        """ Validate if a creature is suitable for the strategy."""
        pass


class InvalidStrategyError(Exception):
    pass


class NormalStrategy(BattleStrategy):
    """ Suitable for all creatures. Creature only uses its attack method. """
    def act(self, creature: Any) -> None:
        print(creature.attack())

    def is_valid(self, creature: Any) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    """ Suitable for creatures that can transform. """
    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "aggressive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature: Any) -> bool:
        return (hasattr(creature, 'transform') and
                hasattr(creature, 'revert') and
                hasattr(creature, 'attack'))


class DefensiveStrategy(BattleStrategy):
    """ Suitable for creatures that can heal. """
    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "defensive strategy")
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature: Any) -> bool:
        return (hasattr(creature, 'heal') and
                hasattr(creature, 'attack'))
