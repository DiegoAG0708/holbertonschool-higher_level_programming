#!/usr/bin/python3
"""
Module task_00_abc
Defines an abstract Animal class and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.
    """

    def sound(self):
        return "Meow"
