"""
File: searches.py
Author: Zachary King
Credit: Ken Lambert
A module defining some search algorithms
"""

def indexOfMin(lyst):
    """Returns the index of the minimum item."""
    minIndex = 0
    currentIndex = 0
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex

def sequentialSearch(target, lyst):
    """Returns the index of the target item if found,
    or -1 otherwise."""
    position = 0
    while position < len(lyst):
        if target == lyst(position):
            return position
        position += 1
    return -1

def binarySearch(target, sortedLyst):
    """Returns the index of the target item if found,
    or -1 otherwise."""
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left+right) // 2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1
