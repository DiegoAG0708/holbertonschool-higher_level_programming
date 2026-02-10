#!/usr/bin/python3
"""
Module that defines the CustomObject class with
serialization and deserialization using pickle.
"""

import pickle


class CustomObject:
    """
    A custom class that can be serialized and deserialized
    using the pickle module.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to a file.

        Args:
            filename (str): The name of the file to save to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file.

        Args:
            filename (str): The name of the file to load from.

        Returns:
            CustomObject: The deserialized object, or None if error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
