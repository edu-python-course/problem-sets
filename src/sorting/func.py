"""
Sorting functions implementations

"""

from typing import List


def bubble_sort(origin: List[int]) -> List[int]:
    """Return a sorted collection using the bubble sort algorithm

    :param origin: an original list to sort
    :type origin: list[int]

    :return: a sorted list
    :rtype: list[int]

    Bubble sort is a sorting algorithm that compares two adjacent
    elements and swaps them until they are not in the intended order.

    Just like the movement of air bubbles in the water that rise up to
    the surface, each element of the array move to the end in each
    iteration. Therefore, it is called a bubble sort.

    .. seealso:: https://www.programiz.com/dsa/bubble-sort

    Usage examples:

    >>> assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    >>> assert bubble_sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]

    """

    result = origin.copy()
    size: int = len(origin)

    for step in range(size):
        for idx in range(size - step - 1):
            if result[idx] > result[idx + 1]:
                result[idx], result[idx + 1] = result[idx + 1], result[idx]

    return result


def selection_sort(origin: List[int]) -> List[int]:
    """Return a sorted collection using the selection sort algorithm

    :param origin: an original list to sort
    :type origin: list[int]

    :return: a sorted list
    :rtype: list[int]


    Selection sort is a sorting algorithm that selects the smallest
    element from an unsorted list in each iteration and places that
    element at the beginning of the unsorted list.

    .. seealso:: https://www.programiz.com/dsa/selection-sort

    Usage examples:

    >>> assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    >>> assert selection_sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]

    """

    result = origin.copy()
    size: int = len(origin)

    for step in range(size):
        min_idx = step

        for idx in range(step + 1, size):
            if result[idx] < result[min_idx]:
                min_idx = idx

        result[step], result[min_idx] = result[min_idx], result[step]

    return result


def insertion_sort(origin: List[int]) -> List[int]:
    """Return a sorted collection using the insertion sort algorithm

    :param origin: an original list to sort
    :type origin: list[int]

    :return: a sorted list
    :rtype: list[int]

    Insertion sort is a sorting algorithm that places an unsorted
    element at its suitable place in each iteration.

    Insertion sort works similarly as we sort cards in out hand in a card
    game.

    We assume that the first card is already sorted then, we select
    an unsorted card. If the unsorted card is greater than the card in
    hand, it is places on the right otherwise, to the left. In the same
    way, other unsorted cards are taken and put in their right place.

    .. seealso:: https://www.programiz.com/dsa/insertion-sort

    Usage examples:

    >>> assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    >>> assert insertion_sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]

    """

    result = origin.copy()
    size: int = len(origin)

    for step in range(1, size):
        value = result[step]
        idx = step - 1

        while idx >= 0 and value < result[idx]:
            result[idx + 1] = result[idx]
            idx -= 1

        result[idx + 1] = value

    return result


def merge_lists(list_a: List[int], list_b: List[int]) -> List[int]:
    """Return a joined sorted list from two ordered lists

    :param list_a: first sorted list
    :type list_a: list[int]
    :param list_b: second sorted list
    :type list_b: list[int]

    :return: merged sorted list
    :rtype: list[int]

    Merge two lists that are already sorted into a new sorted list.

    Usage examples:

    >>> assert merge_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]

    """

    idx_a: int = 0
    size_a: int = len(list_a)
    idx_b: int = 0
    size_b: int = len(list_b)
    result: List[int] = []

    while idx_a < size_a and idx_b < size_b:
        if list_a[idx_a] < list_b[idx_b]:
            result.append(list_a[idx_a])
            idx_a += 1
        else:
            result.append(list_b[idx_b])
            idx_b += 1

    if idx_a < size_a:
        result += list_a[idx_a:]

    if idx_b < size_b:
        result += list_b[idx_b:]

    return result


def merge_sort(origin: List[int]) -> List[int]:
    """Return a sorted collection using the merge sort algorithm

    :param origin: an original list to sort
    :type origin: list[int]

    :return: a sorted list
    :rtype: list[int]


    Merge sort is one of the most popular sorting algorithms that is
    based on the principle of "Divide and Conquer Algorithm".

    Here, a problem is divided into multiple sub-problems.
    Each sub-problem is solved individually. Finally, sub-problems are
    combined to form the final solution.

    .. seealso:: https://www.programiz.com/dsa/merge-sort

    Usage examples:

    >>> merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    >>> merge_sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]

    """

    size: int = len(origin)
    if size <= 1:
        return origin

    mid_idx: int = size // 2
    left_portion = merge_sort(origin[:mid_idx])
    right_portion = merge_sort(origin[mid_idx:])

    return merge_lists(left_portion, right_portion)


def quick_sort(origin: List[int]) -> List[int]:
    """Return a sorted collection using the quick sort algorithm

    :param origin: an original list to sort
    :type origin: list[int]

    :return: a sorted list
    :rtype: list[int]

    Quicksort is a sorting algorithm based on the **divide and conquer
    approach** where:

    #. A list is divided into sub-lists by selection a **pivot element**.
       While dividing the list, the pivot element should be positioned
       in suc a way that elements less than pivot are kept on the left
       side and elements greater than pivot are on the right side of
       the pivot.
    #. The left and right sub-lists are also divided using the same
       approach. This process continues until each sublist contains
       a single element (or no elements at all).
    #. At this point, elements are already sorted. Finally, elements are
       combined to form a sorted list.

    .. seealso:: https://www.programiz.com/dsa/quick-sort

    Usage examples:

    >>> quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    >>> quick_sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]

    """

    size: int = len(origin)
    if size <= 1:
        return origin

    sorting_base: int = origin[0]
    less_than: List[int] = [val for val in origin if val < sorting_base]
    equal_to: List[int] = [val for val in origin if val == sorting_base]
    greater_than: List[int] = [val for val in origin if val > sorting_base]

    return quick_sort(less_than) + equal_to + quick_sort(greater_than)


def counting_sort(origin: List[int]) -> List[int]:
    """Return a sorted collection using the counting sort algorithm

    :param origin: an original list to sort
    :type origin: list[int]

    :return: a sorted list
    :rtype: list[int]

    Counting sort is a sorting algorithm that sorts the elements of
    a list by counting the number of occurrences of each unique element
    in a list. The count is stored in an auxiliary list and the sorting
    is done by mapping the count as an index of the auxiliary list.

    .. seealso:: https://www.programiz.com/dsa/counting-sort

    Usage examples:

    >>> counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    >>> counting_sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]

    """

    size: int = len(origin)
    max_value: int = max(origin)
    count: List[int] = [0] * (max_value + 1)
    result: List[int] = [0] * size

    for value in origin:
        count[value] += 1

    for idx in range(1, max_value + 1):
        count[idx] += count[idx - 1]

    idx = size - 1
    while idx >= 0:
        count_idx = origin[idx]
        result_idx = count[count_idx] - 1
        result[result_idx] = origin[idx]
        count[count_idx] -= 1
        idx -= 1

    return result


def radix_counting(origin: List[int], places: int) -> List[int]:
    """Return a list sorted by significant place digit

    :param origin: an original unsorted list
    :type origin: list[int]
    :param places: a significant digits places
    :type places: int

    :return: a sorted list, by digits at the significant place
    :rtype: list[int]

    """

    size: int = len(origin)
    count: List[int] = [0] * 10
    result: List[int] = [0] * size

    for value in origin:
        idx = value // places
        count[idx % 10] += 1

    for idx in range(1, 10):
        count[idx] += count[idx - 1]

    idx = size - 1
    while idx >= 0:
        count_idx = (origin[idx] // places) % 10
        result_idx = count[count_idx] - 1
        result[result_idx] = origin[idx]
        count[count_idx] -= 1
        idx -= 1

    return result


def radix_sort(origin: List[int]) -> List[int]:
    """Return a sorted collection using the radix sort algorithm

    :param origin: an original list to sort
    :type origin: list[int]

    :return: a sorted list
    :rtype: list[int]

    Radix sort is a sorting algorithm that sorts the elements by first
    grouping the individual digits of the same **place value**. Then,
    sort the elements according to their increasing/decreasing order.

    First, we will sort elements based on the value of the unit place.
    Then, we will sort elements based on the value of the tenth place.
    This process goes on until the last significant place.

    Usage examples:

    >>> assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    >>> assert radix_sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]

    """

    max_value: int = max(origin)
    result: List[int] = origin.copy()

    places = 1
    while max_value // places > 0:
        result = radix_counting(result, places)
        places *= 10

    return result


def bucket_sort(origin: List[int]) -> List[int]:
    """Return a sorted collection using the bucket sort algorithm

    :param origin: an original list to sort
    :type origin: list[int]

    :return: a sorted list
    :rtype: list[int]

    Bucket sort is a sorting algorithm that divides the unsorted list
    elements into several groups called buckets. Each bucket is then
    sorted by using any of the suitable sorting algorithms or
    recursively applying the same bucket algorithms.

    Finally, the sorted buckets are combined to form a final sorted
    list.

    .. seealso:: https://www.programiz.com/dsa/bucket-sort

    Usage examples:

    >>> assert bucket_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    >>> assert bubble_sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]

    """

    size: int = len(origin)
    result: List[int] = []
    bucket: List[List[int]] = [[] for _ in range(size)]

    for value in origin:
        bucket_idx = value // size
        if bucket_idx != size:
            bucket[bucket_idx].append(value)
        else:
            bucket[size - 1].append(value)

    for idx in range(size):
        # this implementation uses heap sort algorithm
        # for individual buckets
        bucket[idx] = heap_sort(bucket[idx])

    for idx in range(size):
        result += bucket[idx]

    return result


def heap_sort(origin: List[int]) -> List[int]:
    """Return a sorted collection using the heap sort algorithm

    :param origin: an original list to sort
    :type origin: list[int]

    :return: a sorted list
    :rtype: list[int]

    Heap sort is a popular and efficient sorting algorithm in computer
    programming. Learning how to write the heap sort algorithm requires
    knowledge of two types of data structures - arrays and trees.

    Heap sort works by visualizing the elements of the array as
    a special kind of computer binary tree called a heap.

    .. seealso:: https://www.programiz.com/dsa/heap-sort

    Usage examples:

    >>> heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    >>> heap_sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]

    """

    def heapify(_ds: List[int], _size: int, _idx: int) -> List[int]:
        left_idx = 2 * _idx + 1
        right_idx = 2 * _idx + 2

        if left_idx < _size and _ds[left_idx] > _ds[_idx]:
            largest_idx = left_idx
        else:
            largest_idx = _idx

        if right_idx < _size and _ds[right_idx] > _ds[largest_idx]:
            largest_idx = right_idx

        if largest_idx != _idx:
            _ds[_idx], _ds[largest_idx] = _ds[largest_idx], _ds[_idx]
            _ds = heapify(_ds, _size, largest_idx)

        return _ds

    size: int = len(origin)
    result: List[int] = origin.copy()

    for idx in range(size, -1, -1):
        heapify(result, size, idx)

    for idx in range(size - 1, 0, -1):
        result[0], result[idx] = result[idx], result[0]
        heapify(result, idx, 0)

    return result


def shell_sort(origin: List[int]) -> List[int]:
    """Return a sorted collection using the shell sort algorithm

    :param origin: an original list to sort
    :type origin: list[int]

    :return: a sorted list
    :rtype: list[int]

    Shell sort is a generalized version of the insertion sort algorithm.
    It first sorts elements that are far apart from each other and
    successively reduces the interval between the elements to be sorted.

    .. seealso:: https://www.programiz.com/dsa/shell-sort

    Usage examples:

    >>> assert shell_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    >>> assert shell_sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]

    """

    size: int = len(origin)
    result: List[int] = origin.copy()

    interval = size // 2
    while interval > 0:
        for step in range(interval, size):
            store = result[step]
            idx = step
            while idx >= interval and result[idx - interval] > store:
                result[idx] = result[idx - interval]
                idx -= interval

            result[idx] = store

        interval //= 2

    return result
