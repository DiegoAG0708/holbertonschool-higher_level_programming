#!/usr/bin/python3
"""
Module 4-inherits_from
Defines a function that checks if an object is an instance of a subclass.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class.
    Returns False if obj is exactly an instance of a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
