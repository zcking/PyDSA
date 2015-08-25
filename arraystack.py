"""
File: arraystack.py
Author: Zachary King
"""

from arrays import Array
from abstractstack import AbstractStack

class ArrayStack(AbstractStack):
    """An array-based stack implementation."""

    DEFAULT_CAPACITY = 10 # For all array stacks

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)

    # Accessors
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises KeyError if stack is empty."""
        if self.isEmpty(): raise KeyError ("Stack is empty")
        return self._items[len(self) - 1]

    # Mutators
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        """Inserts item at top of the stack."""
        # Resize array here if necessary
        if self._size == len(self._items):
            self._items.grow()
        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises KeyError if stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty(): raise KeyError ("Stack is empty")
        oldItem = self._items[len(self)-1]
        self._items[len(self)-1] = self._items._fillValue
        self._size -= 1
        # Resize array here if necessary
        if len(self) <= len(self._items) // 4 and \
           len(self._items) >= 2 * ArrayStack.DEFAULT_CAPACITY:
            # Shrink the size by half but not below default capacity
            # and remove those garbage cells from the underlying list
            # self._items.shrink()
            temp = Array(len(self._items) // 2) # Create a new array
            for i in range(len(self)):      # Copy data from old array
                temp[i] = self._items[i]    # to new array
            self._items = temp # Reset old array variable to new array
        return oldItem
