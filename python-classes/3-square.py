#!/usr/bin/python3
"""
This module defines a Square class with size validation
and a method to compute its area.
"""


class Square:
    """
    This class defines a square by its size.
    The size attribute is private and validated during instantiation.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: the area of the square
        """
        return self.__size * self.__size
