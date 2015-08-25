"""
File: arraysortedlist.py

Project 9.2

Completes the sorted list implementation.
"""

from arrays import Array
from abstractlist import AbstractList

class ArraySortedList(AbstractList):
    """An array-based sorted list implementation."""

    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArraySortedList.DEFAULT_CAPACITY)
        AbstractList.__init__(self, sourceCollection)

    def _resize(self, array, logicalSize):
        """If the array needs resizing, resizes and returns
        the new array.  Otherwise, returns the olf array."""
        temp = None
        # If array is full
        if len(array) == logicalSize:
            temp = Array(2 * len(array))
        # If array is wasting space
        elif logicalSize < .25 * len(array) and \
             len(array) > ArraySortedList.DEFAULT_CAPACITY:
            temp = Array(round(.5 * len(array)))
        # None of the above
        else:
            return array
        # Copy items to new array
        for i in range(logicalSize):
            temp[i] = array[i]
        return temp

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self._items[i]

    def __index__(self, item):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        left = 0
        right = len(self) - 1
        while left <= right:
            midPoint = (left + right) // 2
            if self._items[midPoint] == item:
                return midpoint
            elif self._items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        # Item not in the list
        raise ValueError(str(item) + " not in list.")

    def __contains__(self, item):
        """Returns True if item is in the list,
        or False otherwise."""
        try:
            return self.index(item) < len(self)
        except:
            return False

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArraySortedList.DEFAULT_CAPACITY)

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self)
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        item = self._items[i]
        for j in range(i, len(self) - 1):
            self._items[j] = self._items[j + 1]
        self._size -= 1
        self.incModCount()
        self._items = self._resize(self._items, len(self))
        return item

    def add(self, item):
        """Adds item to self."""
        # Empty or last item, place at the end
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            self._items[len(self)] = item
        else:
            # Search for first item >= new item
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            # Open a hole for new item
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i - 1]
            # Insert item and update size
            self._items[targetIndex] = item
        self._size += 1
        self.incModCount()

    def listIterator(self):
        """Returns a list iterator."""
        raise Exception("List iterator for sorted lists not supported yet")

           


