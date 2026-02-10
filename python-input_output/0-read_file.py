#!/usr/bin/python3
"""
This module defines the read_file function.
It reads a UTF-8 text file and prints its contents to stdout.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
