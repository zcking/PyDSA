"""
File: sort.py
Author: Zachary King
Credit: Ken Lambert
A module that defines some sorting algorithms
"""

from arrays import Array

def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

def selectionSort(lyst):
    """Selection sort sorts a list with a complexity
    analysis of O(n^2) in all cases."""
    i = 0
    while i < len(lyst) - 1:            # Do n - 1 searches
        minIndex = i                    # for the smallest
        j = i + 1
        while j < len(lyst):            # Start a search
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:               # Exchange if needed
            swap(lyst, minIndex, i)
        i += 1

def bubbleSort(lyst):
    """Bubble sort sorts a list with a complexity
    analysis of O(n^2) in the average case."""
    n = len(lyst)
    while n > 1:                        # Do n - 1 bubbles
        swapped = False
        i = 1                           # Start each bubble
        while i < n:
            if lyst[i] < lyst[i - 1]:   # Exchange if needed
                swap(lyst, i, i - 1)
                swapped = True
            i += 1
        if not swapped: return          # Returns if no swaps
        n -= 1

def insertionSort(lyst):
    """Insertion sort sorts a list with a complexity
    analysis of O(n^2) in the worst case."""
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i += 1

def quicksort(lyst):
    """Quick sort sorts a list with a complexity
    analysis of O(nlog(n)) in best case."""
    _quicksortHelper(lyst, 0, len(lyst) - 1)

def _quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = _partition(lyst, left, right)
        _quicksortHelper(lyst, left, pivotLocation - 1)
        _quicksortHelper(lyst, pivotLocation + 1, right)

def _partition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left+right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap(lyst, right, boundary)
    return boundary

def mergeSort(lyst):
    # lyst          list being sorted
    # copyBuffer    temporary space needed during merge
    copyBuffer = Array(len(lyst))
    _mergeSortHelper(lyst, copyBuffer, 0, len(lyst) - 1)

def _mergeSortHelper(lyst, copyBuffer, low, high):
    # lyst          list being sorted
    # copyBuffer    temp space for merging
    # low, high     bounds of sublist
    # middle        midpoint of sublist
    if low < high:
        middle = (low + high) // 2
        _mergeSortHelper(lyst, copyBuffer, low, middle)
        _mergeSortHelper(lyst, copyBuffer, middle + 1, high)
        _merge(lyst, copyBuffer, low, middle, high)

def _merge(lyst, copyBuffer, low, middle, high):
    # lyst          list that is being sorted
    # copyBuffer    temp space for merging
    # low           beginning of first sorted sublist
    # middle        end of first sorted sublist
    # middle + 1    beginning of second sorted sublist
    # high          end of second sorted sublist

    # Initialize i1 and i2 to the first items in each sublist
    i1 = low
    i2 = middle + 1

    # Interleave items from the sublists into the
    # copyBuffer in such a way that order is preserved.
    for i in range(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2] # First sublist exhausted
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1] # Second sublist exhausted
        elif lyst[i1] < lyst[i2]:
            copyBuffer[i] = lyst[i1] # Item in first sublist <
            i1 += 1
        else:
            copyBuffer[i] = lyst[i2] # Item in second sublist <
            i2 += 1

    for i in range(low, high + 1):      # Copy sorted items back to
        lyst[i] = copyBuffer[i]         # proper position in lyst
