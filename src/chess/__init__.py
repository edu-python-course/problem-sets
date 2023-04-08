"""
Chess challenge

"""

import logging
from typing import List, Tuple

logger = logging.getLogger(__name__)


class Piece:
    """Chess piece model

    :ivar name: the name of a piece (e.g. "king", "pawn")
    :type name: str
    :ivar position: the position on a chess board
    :type position: tuple
    :ivar is_white: a flag indicating if a chess piece is white
    :type is_white: bool

    """

    name: str = "piece"

    def __init__(self,
                 is_white: bool = True,
                 position: Tuple[int, int] = (0, 0)) -> None:
        """Initialize instance

        :param is_white: indicating if a piece is white. Defaults to True.
        :type is_white: bool
        :param position: initial piece position. Defaults to (0, 0).
        :type position: tuple

        """

        self.is_white = is_white
        self.position = position

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return f"{self.__class__.__name__}({self.is_white}, {self.position})"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        color = "white" if self.is_white else "black"

        return f"{color} {self.name} at {self.position}"

    def swap_color(self) -> None:
        """Change the piece color to the opposite one"""

        self.is_white = not self.is_white

    def set_position(self, position: Tuple[int, int]) -> None:
        """Change piece position to a specified one

        :param position: new position for a piece
        :type position: tuple

        """

        if within_board(position):
            self.position = position
            return

        logger.warning("Position %s is outside the board", position)

    def can_move(self, position: Tuple[int, int]) -> bool:
        """Check if a move to a specified position is valid

        :param position: a position to check
        :type position: tuple

        :return: True if move is valid, otherwise False
        :rtype: bool

        """

        raise NotImplementedError

    def get_delta(self, position: Tuple[int, int]) -> Tuple[int, int]:
        """Return the deltas between current position and the specified one

        :param position: a position to calculate delta with
        :type position: tuple
        :return: a pair of delta x and delta y values
        :rtype: tuple

        """

        position_x, position_y = position
        current_x, current_y = self.position

        return position_x - current_x, position_y - current_y


class King(Piece):  # pylint: disable=C0115
    name = "king"

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if not -1 <= delta_x <= 1 or not -1 <= delta_y <= 1:
            return False

        return within_board(position)


class Queen(Piece):  # pylint: disable=C0115
    name = "queen"

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if abs(delta_x) != abs(delta_y) and delta_x != 0 and delta_y != 0:
            return False

        return within_board(position)


class Bishop(Piece):  # pylint: disable=C0115
    name = "bishop"

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if abs(delta_x) != abs(delta_y):
            return False

        return within_board(position)


class Knight(Piece):  # pylint: disable=C0115
    name = "knight"

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if (abs(delta_x), abs(delta_y)) not in ((2, 1), (1, 2)):
            return False

        return within_board(position)


class Rook(Piece):  # pylint: disable=C0115
    name = "rook"

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if delta_x != 0 and delta_y != 0:
            return False

        return within_board(position)


class Pawn(Piece):  # pylint: disable=C0115
    name = "pawn"

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if delta_x != 0:
            return False
        if self.is_white and delta_y != 1:
            return False
        if not self.is_white and delta_y != -1:
            return False

        return within_board(position)


def within_board(position: Tuple[int, int]) -> bool:
    """Check if position is within a chess board

    :param position: a position to check
    :type position: tuple

    :return: True if position is within a chess board, otherwise False
    :rtype: bool

    """

    position_x, position_y = position

    return 0 <= position_x <= 7 and 0 <= position_y <= 7


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

    return [piece for piece in pieces if piece.can_move(position)]
