"""
File: grid.py
Author: Zachary King
Credit: Ken Lambert

A 2-D array implementation.
"""

from arrays import Array

class Grid(object):
    """Represents a two-dimensional array."""

    def __init__(self, rows, columns, fillValue=None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fillValue)

    def getHeight(self):
        """Returns the number of rows."""
        return self._data.size()

    def getWidth(self):
        """Returns the number of columns."""
        return len(self._data[0])

    def __getitem__(self, index):
        """Supports two-dimensional indexing
        with [row][column]."""
        return self._data[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self._data[row][col]) + " "
            result += "\n"
        return result
