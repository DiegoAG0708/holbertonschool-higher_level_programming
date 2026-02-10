#!/usr/bin/python3
"""
Module that defines the Student class with serialization
and deserialization capabilities.
"""


class Student:
    """
    Class that defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes contained in
        this list are retrieved. Otherwise, all attributes are retrieved.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the Student.
        """
        if isinstance(attrs, list):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with values from the provided dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
