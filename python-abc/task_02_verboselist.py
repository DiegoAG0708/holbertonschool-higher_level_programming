#!/usr/bin/python3
"""
Module task_02_verboselist
Defines a VerboseList class that extends Python's built-in list
and prints notifications on modifications.
"""


class VerboseList(list):
    """
    A list subclass that prints notifications when modified.
    """

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
