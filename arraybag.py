"""
File: arraybag.py
Author: Zachary King
"""

from arrays import Array
from abstractbag import AbstractBag

class ArrayBag(AbstractBag):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        self._targetIndex = -1
        AbstractBag.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        self._items[len(self)] = item
        self._size += 1
        # Check array memory and increase it if necessary
        if self._size == len(self._items):
            self._items.grow()

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        Postcondition: item is removed from self."""
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for index of target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # If removing last item, set it to fillValue
        if targetIndex == len(self) - 1:
            self._items[targetIndex] = self._items._fillValue
        else:
            # Shift items to the left of target up by one position
            for i in range(targetIndex, len(self)-1):
                self._items[i] = self._items[i+1]
                self._items[i+1] = self._items._fillValue
        # Decrement logical size
        self._size -= 1
        # Check array memory and decrease it if necessary
        if self._size <= len(self._items) // 4 and len(self._items) > ArrayBag.DEFAULT_CAPACITY:
            self._items.shrink()
