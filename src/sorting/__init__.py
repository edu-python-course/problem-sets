"""
Sorting Algorithms
==================

Bubble Sort
-----------

.. autofunction:: bubble_sort

Selection Sort
--------------

.. autofunction:: selection_sort

Insertion Sort
--------------

.. autofunction:: insertion_sort

Shell Sort
----------

.. autofunction:: shell_sort

Merge Sort
----------

.. autofunction:: merge_sort

Quick Sort
----------

.. autofunction:: quick_sort

Counting Sort
-------------

.. autofunction:: counting_sort

Radix Sort
----------

.. autofunction:: radix_sort

Bucket Sort
-----------

.. autofunction:: bucket_sort

Heap Sort
---------

.. autofunction:: heap_sort

"""

__all__ = [
    "bubble_sort",
    "bucket_sort",
    "counting_sort",
    "heap_sort",
    "insertion_sort",
    "merge_sort",
    "quick_sort",
    "radix_sort",
    "selection_sort",
    "shell_sort"
]

from sorting.func import (
    bubble_sort,
    bucket_sort,
    counting_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    radix_sort,
    selection_sort,
    shell_sort,
)
