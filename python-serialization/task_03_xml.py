#!/usr/bin/python3
"""
Module that provides serialization and deserialization
of Python dictionaries using XML format.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML file to save to.
    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        with open(filename, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        return dictionary
    except Exception:
        return None
