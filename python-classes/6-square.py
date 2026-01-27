#!/usr/bin/python3
"""
This module defines a Square class with size and position validation,
a getter and setter for both, an area method, and a method to print
the square using the character '#', respecting its position.
"""


class Square:
    """
    This class defines a square by its size and position.
    The size and position attributes are private and validated
    during instantiation and when updated through property setters.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
            TypeError: if position is not a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: the current size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): new size of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: the current position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): new position of the square

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the character '#'.
        If size is 0, print an empty line.
        Position is respected: spaces for position[0], newlines for position[1].
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print("")

        # Print each row with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
