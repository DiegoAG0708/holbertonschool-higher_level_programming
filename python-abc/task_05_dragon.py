#!/usr/bin/python3
"""
Module task_05_dragon
Demonstrates mixins with SwimMixin, FlyMixin, and Dragon class.
"""


class SwimMixin:
    """
    Mixin providing swimming ability.
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin providing flying ability.
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from SwimMixin and FlyMixin.
    Gains both swimming and flying abilities.
    """

    def roar(self):
        print("The dragon roars!")
