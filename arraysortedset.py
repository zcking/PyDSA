"""
File: arraysortedset.py
Author: Zachary King
"""

from arraysortedbag import ArraySortedBag

class ArraySortedSet(ArraySortedBag):
    """A sorted array set implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ArraySortedBag.__init__(self, sourceCollection)

    # Accessor methods
    def add(self, item):
        """Adds item to self."""
        if not item in self:
            ArraySortedBag.add(self, item)
