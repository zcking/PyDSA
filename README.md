# Python-Data-Structures
Simple data structures and algorithms implemented in Python 3.

These implementations are based off of those written by Ken Lambert in his book, "Fundamental of Python: Data Structures."
Most of them have been modified to an extent, and a couple may not be completely functional. There are also
"interfaces" implemented to better utilize the heirarchial approach of object-orientation.

## Help with Individual Data Structures or Algorithms
To get help with individual data structures, their methods, complexity analysis, etc. please use the docstrings. An example would be as follows:
```python
import ArrayBag

print(help(ArrayBag))
```
or
```python
import ArrayBag

print(ArrayBag.__doc__)
```

## Heirarchy of Data Structures
```
AbstractCollection
|
|---->AbstractBag
|         |
|         |---->ArrayBag
|         |       |
|         |       |---->ArraySortedBag
|         |       |         |
|         |       |         |---->ArraySortedSet
|         |       |
|         |       |---->ArraySet
|         |
|         |---->HashBag
|         |        |
|         |        |---->HashSet
|         |
|         |---->LinkedBag
|         |        |
|         |        |---->LinkedSet
|         |
|         |---->TreeSortedBag
|                  |
|                  |---->TreeSortedSet
|
|---->AbstractDict
|         |
|         |---->ArrayDict
|         |        |
|         |        |---->ArraySortedDict
|         |
|         |---->HashDict
|         |---->LinkedDict
|         |---->TreeSortedDict
|
|---->AbstractList
|         |
|         |---->ArraySortedList
|         |        |
|         |        |---->ArrayList
|         |
|         |---->LinkedList
|
|---->AbstractStack
|         |
|         |---->ArrayStack
|         |---->LinkedStack
|
|---->ArrayQueue
|---->LinkedQueue
|         |
|         |---->LinkedPriorityQueue
|
|---->ArrayHeap
|---->HeapPriorityQueue
|---->LinkedBST
|---->LinkedDirectedGraph
```
