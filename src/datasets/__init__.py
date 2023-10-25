"""
Dataset challenges
==================

Swap dictionary keys and values
-------------------------------

.. autofunction:: swap_dict_loop

.. autofunction:: swap_dict

"""

__all__ = [
    "get_bricks_count",
    "get_least_bricks_count",
    "get_least_bricks_position",
    "get_position_frequency",
    "filter_by_values",
    "flatten_list",
    "swap_dict",
    "swap_dict_loop",
    "get_avg_score",
    "get_both_top_low_students",
    "get_low_student",
    "get_top_student",
]

from datasets.bricks import (
    get_bricks_count,
    get_least_bricks_count,
    get_least_bricks_position,
    get_position_frequency
)
from datasets.filters import filter_by_values
from datasets.flatten import flatten_list
from datasets.func import swap_dict, swap_dict_loop
from datasets.students import (
    get_avg_score,
    get_both_top_low_students,
    get_low_student,
    get_top_student
)
