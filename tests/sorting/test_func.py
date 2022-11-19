import sorting


def test_bubble_sort(unsorted_list, reversed_list, sorted_list):
    assert sorting.bubble_sort(unsorted_list) == sorted_list
    assert sorting.bubble_sort(reversed_list) == sorted_list


def test_selection_sort(unsorted_list, reversed_list, sorted_list):
    assert sorting.selection_sort(unsorted_list) == sorted_list
    assert sorting.selection_sort(reversed_list) == sorted_list


def test_insertion_sort(unsorted_list, reversed_list, sorted_list):
    assert sorting.insertion_sort(unsorted_list) == sorted_list
    assert sorting.insertion_sort(reversed_list) == sorted_list


def test_merge_two_lists(sorted_list_a, sorted_list_b, sorted_merged_list):
    assert sorting.merge_lists(sorted_list_a, sorted_list_b) == \
           sorted_merged_list


def test_merge_sort(unsorted_list, reversed_list, sorted_list):
    assert sorting.merge_sort(unsorted_list) == sorted_list
    assert sorting.merge_sort(reversed_list) == sorted_list


def test_quick_sort(unsorted_list, reversed_list, sorted_list):
    assert sorting.quick_sort(unsorted_list) == sorted_list
    assert sorting.quick_sort(reversed_list) == sorted_list


def test_counting_sort(unsorted_list, reversed_list, sorted_list):
    assert sorting.counting_sort(unsorted_list) == sorted_list
    assert sorting.counting_sort(reversed_list) == sorted_list


def test_radix_sort(unsorted_list, reversed_list, sorted_list):
    assert sorting.radix_sort(unsorted_list) == sorted_list
    assert sorting.radix_sort(reversed_list) == sorted_list


def test_bucket_sort(unsorted_list, reversed_list, sorted_list):
    assert sorting.bucket_sort(unsorted_list) == sorted_list
    assert sorting.bucket_sort(reversed_list) == sorted_list


def test_heap_sort(unsorted_list, reversed_list, sorted_list):
    assert sorting.heap_sort(unsorted_list) == sorted_list
    assert sorting.heap_sort(reversed_list) == sorted_list


def test_shell_sort(unsorted_list, reversed_list, sorted_list):
    assert sorting.shell_sort(unsorted_list) == sorted_list
    assert sorting.shell_sort(reversed_list) == sorted_list
