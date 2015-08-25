"""
File: linkedset.py
Author: Zachary King
"""

from linkedbag import LinkedBag

class LinkedSet(LinkedBag):
    """A linked-bag implementation that does
    not allow duplicate items."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Nothing unique about init apart from parent's
        LinkedBag.__init__(self, sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self if not already in bag."""
        if not item in self:
            LinkedBag.add(self, item)
