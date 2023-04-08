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
    :type position: bool

    """

    position: Tuple[int, int] = 0, 0
    is_white: bool = True
    name: str = "piece"

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

        logger.warning(f"Position {position} is outside the board")

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


class King(Piece):
    name = "king"

    def can_move(self, position: Tuple[int, int]) -> bool:
        dx, dy = self.get_delta(position)
        if not -1 <= dx <= 1 or not -1 <= dy <= 1:
            return False

        return within_board(position)


class Queen(Piece):
    name = "queen"

    def can_move(self, position: Tuple[int, int]) -> bool:
        dx, dy = self.get_delta(position)
        if abs(dx) != abs(dy) and dx != 0 and dy != 0:
            return False

        return within_board(position)


class Bishop(Piece):
    name = "bishop"

    def can_move(self, position: Tuple[int, int]) -> bool:
        dx, dy = self.get_delta(position)
        if abs(dx) != abs(dy):
            return False

        return within_board(position)


class Knight(Piece):
    name = "knight"

    def can_move(self, position: Tuple[int, int]) -> bool:
        dx, dy = self.get_delta(position)
        if (abs(dx), abs(dy)) not in ((2, 1), (1, 2)):
            return False

        return within_board(position)


class Rook(Piece):
    name = "rook"

    def can_move(self, position: Tuple[int, int]) -> bool:
        dx, dy = self.get_delta(position)
        if dx != 0 and dy != 0:
            return False

        return within_board(position)


class Pawn(Piece):
    ...  # TODO: add implementation


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
