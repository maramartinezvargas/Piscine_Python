#!/usr/bin/env python3

from ex0.factories import CreatureFactory
from ex1.capabilities import Bloomelle, Sproutling, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    """ Factory class to create creatures that can heal themselves. """
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """ Factory class to create creatures that can transform into other
    creatures. """
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
