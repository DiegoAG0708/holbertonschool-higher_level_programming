#!/usr/bin/python3
"""
Module 2-is_same_class
Defines a function that checks if an object is exactly an instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
