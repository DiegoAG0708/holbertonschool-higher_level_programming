#!/usr/bin/python3
"""
Module 0-lookup
Defines a function that returns the list of attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attributes and methods.
    """
    return dir(obj)
