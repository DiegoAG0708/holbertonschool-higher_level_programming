#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    Custom list class that inherits from Python's built-in list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
