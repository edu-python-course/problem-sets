from typing import List, Tuple


class Piece:
    """Chess piece model"""

    # TODO: add implementation


class King(Piece):
    """King piece model"""

    # TODO: add implementation


class Queen(Piece):
    """Queen piece model"""

    # TODO: add implementation


class Bishop(Piece):
    """Bishop piece model"""

    # TODO: add implementation


class Knight(Piece):
    """Knight piece model"""

    # TODO: add implementation


class Rook(Piece):
    """Rook piece model"""

    # TODO: add implementation


class Pawn(Piece):
    """Pawn piece model"""

    # TODO: add implementation


def within_board(position: Tuple[int, int]) -> bool:
    """Check if position is within a chess board

    :param position: a position to check
    :type position: tuple

    :return: True if position is within a chess board, otherwise False
    :rtype: bool

    """

    x, y = position

    return 0 <= x <= 7 and 0 <= y <= 7


def filter_can_move(pieces: List[Piece],
                    position: Tuple[int, int]) -> List[Piece]:
    """Filter the list of chess piece

    :param pieces: a list of chess pieces
    :type pieces: list
    :param position: a position to check piece move
    :type position: tuple

    :return: a list of pieces that can move to specified position
    :rtype: list

    """

    # TODO: add implementation
