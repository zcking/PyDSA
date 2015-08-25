"""
File: linkedlist.py
Author: Zachary King
"""

from node import TwoWayNode
from abstractlist import AbstractList

class LinkedList(AbstractList):
    """A link-based list implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Uses a circular linked structure with a dummy header node
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head
        AbstractList.__init__(self, sourceCollection)

    # Helper method returns node at position i
    def _getNode(self, i):
        """Helper method: returns a pointer to the node at position i."""
        if i == len(self):
            return self._head
        elif i == len(self) - 1:
            return self._head.previous
        probe = self._head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    #Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._head.next
        while cursor != self._head:
            yield cursor.data
            cursor = cursor.next

    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self._getNode(i).data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head
        
    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self._getNode(i).data = item

    def insert(self, i, item):
        """Inserts the item at position i."""
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        theNode = self._getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous.next = newNode
        theNode.previous = newNode
        self._size += 1
        self.incModCount()

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        theNode = self._getNode(i)
        item = theNode.data
        theNode.previous.next = theNode.next
        theNode.next.previous = theNode.previous
        self._size -= 1
        self.incModCount()
        return item

    def listIterator(self):
        """Returns a list iterator."""
        return LinkedList.ListIterator(self)

    class ListIterator(object):
        """Represents the list iterator for linked list."""

        def __init__(self, backingStore):
            self._backingStore = backingStore
            self._modCount = backingStore.getModCount()
            self.first()

        def first(self):
            """Returns the cursor to the beginning of the backing store."""
            self._cursor = self._backingStore._head.next
            self._lastItemPos = None

        def hasNext(self):
            """Returns True if the iterator has a next item or False otherwise."""
            return self._cursor != self._backingStore._head

        def next(self):
            """Preconditions: hasNext returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and advances the cursor to the next item.
            Postcondition: lastItemPos is now defined.
            Raises: ValueError if no next item.
            AttributeError if illegal mutation of backing store."""
            if not self.hasNext():
                raise ValueError("No next item in list iterator")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("Illegal modification of backing store")
            self._lastItemPos = self._cursor
            self._cursor = self._cursor.next
            return self._lastItemPos.data

        def last(self):
            """Moves the cursor to the end of the backing store."""
            self._cursor = self._backingStore._head
            self._lastItemPos = -1

        def hasPrevious(self):
            """Returns True if the iterator has a previous item or False otherwise."""
            return self._cursor.previous != self._backingStore._head

        def previous(self):
            """Preconditions: hasPrevious returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and moves the cursor to the previous item.
            Postcondition: lastItemPos is now defined.
            Raises: ValueError if no next item.
            AttributeError if illegal mutation of backing store."""
            if not self.hasPrevious():
                raise ValueError("No previous item in list iterator")
            self._cursor = self._cursor.previous
            self._lastItemPos = self._cursor
            return self._lastItemPos.data

        def replace(self, item):
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Replaces the items at the current position with item."""
            if self._lastItemPos == None:
                raise AttributeError("The current position is undefined.")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            self._lastItemPos.data = item
            self._lastItemPos = None

        def insert(self, item):         
            """Preconditions:
            The list has not been modified except by this iterator's mutators.
            Adds item to the end if the current position is undefined, or
            inserts it at that position."""
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            if self._lastItemPos is None:
                self._backingStore.add(item)
            else:
                newNode = TwoWayNode(item, self._lastItemPos.previous, self._lastItemPos)
                self._lastItemPos.previous.next = newNode
                self._lastItemPos.previous = newNode
                self._backingStore.incModCount()
                self._backingStore._size += 1
                self._lastItemPos = None
            self._modCount += 1

        def remove(self):         
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Pops the item at the current position."""
            if self._lastItemPos == None:
                raise AttributeError("The current position is undefined.")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            item = self._lastItemPos.data
            # If the item removed was obtained via previous, move cursor ahead
            if self._lastItemPos == self._cursor:
                self._cursor = self._cursor.next
            self._lastItemPos.previous.next = self._lastItemPos.next
            self._lastItemPos.next.previous = self._lastItemPos.previous
            self._backingStore._size -= 1
            self._backingStore.incModCount()
            self._modCount += 1
            self._lastItemPos = None
           





