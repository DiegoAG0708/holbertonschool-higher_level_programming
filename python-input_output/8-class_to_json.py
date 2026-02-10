#!/usr/bin/python3
"""
Module that provides the class_to_json function.
It returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
