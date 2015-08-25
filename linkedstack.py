"""
File: linkedstack.py
Author: Zachary King
"""

from node import Node
from abstractstack import AbstractStack

class LinkedStack(AbstractStack):
    """A link-based stack implementation."""

    def __init__(self, sourceCollection=None):
        self._items = None
        AbstractStack.__init__(self, sourceCollection)

    # Accessors
    def __iter__(self):
        """Iterates over a view of self.
        Visits items from bottom to top of stack."""
        def visitNodes(node):
            if not node is None:
                visitNodes(node.next)
                tempList.append(node.data)
        tempList = list()
        visitNodes(self._items)
        return iter(tempList)

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty(): raise KeyError("The stack is empty")
        return self._items.data

    # Mutators
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = None

    def push(self, item):
        """Inserts item at top of the stack."""
        self._items = Node(item, self._items)
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty(): raise KeyError("The stack is empty.")
        oldItem = self._items.data
        self._items = self._items.next
        self._size -= 1
        return oldItem
