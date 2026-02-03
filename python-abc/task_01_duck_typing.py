#!/usr/bin/python3
"""
Module task_01_duck_typing
Defines an abstract Shape class and concrete Circle and Rectangle classes.
Demonstrates duck typing with shape_info function.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a Shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to compute area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to compute perimeter.
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
