"""
File: sort.py
Author: Zachary King
Credit: Ken Lambert
A module that defines some sorting algorithms
"""

from arrays import Array

def swap(lyst, i, j):
    """
    Exchanges the items at positions i and j.
    """
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

def selectionSort(lyst):
    """
    Complexity Analysis:
    Best Case: O(n^2)
    Average Case: O(n^2)
    Worst Case: O(n^2)
    """
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
    """
    Complexity Analysis:
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)
    """
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
    """
    Complexity Analysis:
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)
    """
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
    """
    Complexity Analysis:
    Best Case: O(nlogn)
    Average Case: O(nlogn)
    Worst Case: O(n^2)
    """
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
    """
    Complexity Analysis:
    Best Case: O(nlogn)
    Average Case: O(nlogn)
    Worst Case: O(nlogn)
    """
    _mergeSort(lyst, 0, len(lyst) - 1)

def _mergeSort(lyst, first, last):
    # Break problem into smaller structurally identical pieces
    mid = (first + last) // 2
    if first < last:
        _mergeSort(lyst, first, mid)
        _mergeSort(lyst, mid + 1, last)

    # Merge solved pieces to get solution to original problem
    a, f, l = 0, first, mid + 1
    tmp = [None] * (last - first + 1)

    while f <= mid and l <= last:
        if lyst[f] < lyst[l]:
            tmp[a] = lyst[f]
            f += 1
        else:
            tmp[a] = lyst[l]
            l += 1
        a += 1

    if f <= mid:
        tmp[a:] = lyst[f:mid + 1]

    if l <= last:
        tmp[a:] = lyst[l:last + 1]

    a = 0
    while first <= last:
        lyst[first] = tmp[a]
        first += 1
        a += 1
