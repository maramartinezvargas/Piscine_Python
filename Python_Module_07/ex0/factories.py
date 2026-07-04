#!/usr/bin/env python3

from abc import ABC, abstractmethod
from .creatures import Creature
from .creatures import Flameling, Aquabub, Pyrodon, Torragon


class CreatureFactory(ABC):
    """ Factory class to create creatures. This class is intended to be
    subclassed for specific creature types. """
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    """ Factory class to create fire-type creatures.
    (Flameling evolves into Pyrodon.) """
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """ Factory class to create water-type creatures.
    (Aquabub evolves into Torragon.) """
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
