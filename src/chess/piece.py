"""
Chess pieces implementations

"""

import logging
from typing import Tuple

from chess import symbols
from chess.func import within_board

logger = logging.getLogger(__name__)


class Piece:
    """
    Chess piece model

    :ivar position: the position on a chess board
    :type position: tuple
    :ivar is_white: a flag indicating if a chess piece is white
    :type is_white: bool

    """

    def __init__(self,
                 is_white: bool = True,
                 position: Tuple[int, int] = (0, 0)) -> None:
        """
        Initialize instance

        :param is_white: indicating if a piece is white. Defaults to True.
        :type is_white: bool, optional
        :param position: initial piece position. Defaults to (0, 0).
        :type position: tuple, optional

        """

        self.is_white = is_white
        self.position = position

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return f"{self.__class__.__name__}({self.is_white}, {self.position})"

    def swap_color(self) -> None:
        """Change the piece color to the opposite one"""

        self.is_white = not self.is_white

    def set_position(self, position: Tuple[int, int]) -> None:
        """
        Change piece position to a specified one

        :param position: new position for a piece
        :type position: tuple

        """

        if within_board(position):
            self.position = position
            return

        logger.warning("Position %s is outside the board", position)

    def can_move(self, position: Tuple[int, int]) -> bool:
        """
        Check if a move to a specified position is valid

        :param position: a position to check
        :type position: tuple

        :return: True if move is valid, otherwise False
        :rtype: bool

        """

        raise NotImplementedError

    def get_delta(self, position: Tuple[int, int]) -> Tuple[int, int]:
        """
        Return the deltas between current position and the specified one

        :param position: a position to calculate delta with
        :type position: tuple
        :return: a pair of delta x and delta y values
        :rtype: tuple

        """

        position_x, position_y = position
        current_x, current_y = self.position

        return position_x - current_x, position_y - current_y


class King(Piece):  # pylint: disable=C0115
    def __str__(self) -> str:
        return symbols.WHITE_KING if self.is_white else symbols.BLACK_KING

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if not -1 <= delta_x <= 1 or not -1 <= delta_y <= 1:
            return False

        return within_board(position)


class Queen(Piece):  # pylint: disable=C0115
    def __str__(self) -> str:
        return symbols.WHITE_QUEEN if self.is_white else symbols.BLACK_QUEEN

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if abs(delta_x) != abs(delta_y) and delta_x != 0 and delta_y != 0:
            return False

        return within_board(position)


class Bishop(Piece):  # pylint: disable=C0115

    def __str__(self) -> str:
        return symbols.WHITE_BISHOP if self.is_white else symbols.BLACK_BISHOP

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if abs(delta_x) != abs(delta_y):
            return False

        return within_board(position)


class Knight(Piece):  # pylint: disable=C0115

    def __str__(self) -> str:
        return symbols.WHITE_KNIGHT if self.is_white else symbols.BLACK_KNIGHT

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if (abs(delta_x), abs(delta_y)) not in ((2, 1), (1, 2)):
            return False

        return within_board(position)


class Rook(Piece):  # pylint: disable=C0115

    def __str__(self) -> str:
        return symbols.WHITE_ROOK if self.is_white else symbols.BLACK_ROOK

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if delta_x != 0 and delta_y != 0:
            return False

        return within_board(position)


class Pawn(Piece):  # pylint: disable=C0115

    def __str__(self) -> str:
        return symbols.WHITE_PAWN if self.is_white else symbols.BLACK_PAWN

    def can_move(self, position: Tuple[int, int]) -> bool:
        delta_x, delta_y = self.get_delta(position)
        if delta_x != 0:
            return False
        if self.is_white and delta_y != 1:
            return False
        if not self.is_white and delta_y != -1:
            return False

        return within_board(position)
