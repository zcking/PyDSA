"""
File: arrayset.py
Author: Zachary King
"""

from arraybag import ArrayBag

class ArraySet(ArrayBag):
    """An arraybag implementation that does
    not allow duplicate items."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, it it's present."""
        # Nothing different about the initialization from the parent's
        ArrayBag.__init__(self, sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self if not already in bag."""
        if not item in self:
            ArrayBag.add(self, item)

    
