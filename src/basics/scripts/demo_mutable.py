"""
This module demonstrates the mutable nature of objects

"""

import logging
from typing import Any, List, Optional

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def change_mutable_v1(value: Any, mutable: List[Any]) -> List[Any]:
    """This function will change mutable argument"""

    mutable.append(value)
    return mutable


# noinspection PyDefaultArgument
def change_mutable_v2(value: Any,
                      mutable: Optional[List[Any]] = []) -> List[Any]:
    """This function will change default mutable object"""

    mutable.append(value)
    return mutable


def change_valid(value: Any,
                 mutable: Optional[List[Any]] = None) -> List[Any]:
    """
    This function wouldn't change defaults,
    but will change mutable argument.
    """

    mutable = mutable or []
    mutable.append(value)

    return mutable


if __name__ == "__main__":
    mutable_obj1 = []
    change_mutable_v1(1, mutable_obj1)
    mutable_obj1 += [2]  # [1, 2], because it was changed by "change_mutable"

    logger.info(f"{mutable_obj1 = }")

    mutable_obj2 = change_mutable_v2(10)  # expected: [10]
    mutable_obj3 = change_mutable_v2(20)  # expected: [20], but [10, 20]

    logger.info(f"{mutable_obj2 = }")
    logger.info(f"{mutable_obj3 = }")

    mutable_obj4 = change_valid(100)  # expected: [100]
    mutable_obj5 = change_valid(200)  # expected: [200]
    mutable_obj6 = change_valid(3, mutable_obj1)  # expected: [1, 2, 3]

    logger.info(f"{mutable_obj4 = }")
    logger.info(f"{mutable_obj5 = }")
    logger.info(f"{mutable_obj6 = }")
