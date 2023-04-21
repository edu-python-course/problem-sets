"""
Chess board functions

"""

from __future__ import annotations

from typing import List, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from chess.piece import Piece


def within_board(position: Tuple[int, int]) -> bool:
    """
    Check if position is within a chess board

    :param position: a position to check
    :type position: tuple

    :return: True if position is within a chess board, otherwise False
    :rtype: bool

    Usage:

    >>> assert within_board((2, 2)) is True
    >>> assert within_board((3, 3)) is True
    >>> assert within_board((4, 4)) is True
    >>> assert within_board((5, -5)) is False
    >>> assert within_board((-5, 5)) is False
    >>> assert within_board((5, 50)) is False

    """

    position_x, position_y = position

    return 0 <= position_x <= 7 and 0 <= position_y <= 7


def filter_can_move(pieces: List[Piece],
                    position: Tuple[int, int]) -> List[Piece]:
    """
    Filter the list of chess piece

    :param pieces: a list of chess pieces
    :type pieces: list
    :param position: a position to check piece move
    :type position: tuple

    :return: a list of pieces that can move to specified position
    :rtype: list

    """

    return [piece for piece in pieces if piece.can_move(position)]
