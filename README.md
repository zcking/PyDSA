# Python-Data-Structures
Simple data structures implemented in Python 3.

These implementations are based off of those written by Ken Lambert in his book, "Fundamental of Python: Data Structures."
Most of them have been modified to an extent, and a couple may not be completely functional. There are also
"interfaces" implemented to better utilize the heirarchial approach of object-orientation.

## Heirarchy of Data Structures
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
