#!/usr/bin/python3
"""
This module defines a Square class with size validation,
a getter and setter for size, an area method, and a method
to print the square using the character '#'.
"""


class Square:
    """
    This class defines a square by its size.
    The size attribute is private and validated during instantiation
    and when updated through the property setter.
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
        self.size = size  # use property setter for validation

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
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
