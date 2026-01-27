#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height validation,
methods to compute its area and perimeter, a string representation
that prints the rectangle using '#', a repr() method that allows
recreating the instance with eval(), and a destructor that prints
a message when the instance is deleted.
"""


class Rectangle:
    """
    This class defines a rectangle by its width and height.
    Both attributes are private and validated during instantiation
    and when updated through property setters.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Compute and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation of the rectangle
        using the character '#'. If width or height is 0,
        return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used with eval() to recreate the instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when the instance is deleted."""
        print("Bye rectangle...")
