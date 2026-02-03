#!/usr/bin/python3
"""
Module task_03_countediterator
Defines a CountedIterator class that tracks iteration count.
"""


class CountedIterator:
    """
    An iterator wrapper that counts how many items have been iterated.
    """

    def __init__(self, iterable):
        # Wrap the iterable with Python's built-in iterator
        self.iterator = iter(iterable)
        # Counter to track how many items have been consumed
        self.count = 0

    def __next__(self):
        # Fetch next item from the underlying iterator
        item = next(self.iterator)  # raises StopIteration when exhausted
        # Increment counter
        self.count += 1
        return item

    def get_count(self):
        """
        Returns the number of items iterated so far.
        """
        return self.count

    def __iter__(self):
        # An iterator must return itself in __iter__
        return self
