#!/usr/bin/python3
"""
This module provides a function to read a UTF-8 text file
and print its contents to standard output.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The path to the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
