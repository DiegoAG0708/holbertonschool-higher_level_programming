#!/usr/bin/python3
"""
Module that provides the from_json_string function.
It returns a Python object represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: The corresponding Python data structure.
    """
    return json.loads(my_str)
