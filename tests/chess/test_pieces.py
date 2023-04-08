import sys
import unittest

from chess.piece import Bishop, King, Knight, Pawn, Piece, Queen, Rook


class TestPieceModel(unittest.TestCase):
    """Abstract chess model test case"""

    def setUp(self) -> None:
        self.instance = Piece()

    def test_default_initializer(self):
        self.assertIs(True, self.instance.is_white)
        self.assertTupleEqual((0, 0), self.instance.position)

    def test_initializer(self):
        instance = Piece(False, (7, 6))
        self.assertIs(False, instance.is_white)
        self.assertTupleEqual((7, 6), instance.position)

    def test_swap_color(self):
        self.instance.is_white = True
        self.instance.swap_color()
        self.assertFalse(self.instance.is_white)
        self.instance.swap_color()
        self.assertTrue(self.instance.is_white)

    def test_set_position(self):
        position = 2, 5
        self.instance.set_position(position)
        self.assertTupleEqual(position, self.instance.position)

    @unittest.skipIf(sys.version_info < (3, 10),
                     "Test requires Python3.10 or higher")
    def test_no_log(self):
        with self.assertNoLogs():
            self.instance.set_position((1, 1))

    def test_position_outside(self):
        position = 10, 10
        regex = r"^.*\:Position \(-?\d+, -?\d+\) is outside the board$"
        with self.assertLogs() as logger:
            self.instance.set_position(position)
            self.assertRegex(*logger.output, regex)

    def test_position_unchanged(self):
        initial = self.instance.position
        position = 8, 8
        self.instance.set_position(position)
        self.assertTupleEqual(initial, self.instance.position)

    def test_get_delta(self):
        self.instance.position = 5, 5
        position = 10, 3
        dx, dy = 10 - 5, 3 - 5
        self.assertTupleEqual((dx, dy), self.instance.get_delta(position))


class TestKingPiece(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = King(True)
        self.instance.set_position((5, 5))

    def test_str(self):
        self.assertEqual("white king at (5, 5)", str(self.instance))

    def test_can_move(self):
        positions = ((5, 6), (6, 6), (6, 5), (6, 4),
                     (5, 4), (4, 4), (4, 5), (4, 6))
        self.assertTrue(
            all(self.instance.can_move(position) for position in positions)
        )

    def test_cannot_move(self):
        self.instance.set_position((0, 0))
        positions = ((-1, -1), (2, 8), (3, 7), (0, 7))
        self.assertTrue(
            all(not self.instance.can_move(position) for position in positions)
        )


class TestQueenPiece(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = Queen(False)
        self.instance.set_position((2, 3))

    def test_str(self):
        self.assertEqual("black queen at (2, 3)", str(self.instance))

    def test_can_move(self):
        positions = ((2, 5), (4, 5), (7, 3), (3, 2),
                     (2, 2), (0, 1), (1, 3), (1, 4))
        self.assertTrue(
            all(self.instance.can_move(position) for position in positions)
        )

    def test_cannot_move(self):
        positions = ((1, 1), (-3, 3), (0, 4), (6, 1))
        self.assertTrue(
            all(not self.instance.can_move(position) for position in positions)
        )


class TestBishopPiece(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = Bishop(True)
        self.instance.set_position((5, 5))

    def test_str(self):
        self.assertEqual("white bishop at (5, 5)", str(self.instance))

    def test_can_move(self):
        positions = ((6, 6), (7, 3), (2, 2), (3, 7))
        self.assertTrue(
            all(self.instance.can_move(position) for position in positions)
        )

    def test_cannot_move(self):
        positions = ((8, 8), (6, 3), (0, 6), (3, 4))
        self.assertTrue(
            all(not self.instance.can_move(position) for position in positions)
        )


class TestKnightPiece(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = Knight(False)
        self.instance.set_position((3, 4))

    def test_str(self):
        self.assertEqual("black knight at (3, 4)", str(self.instance))

    def test_can_move(self):
        positions = ((4, 6), (5, 5), (5, 3), (4, 2),
                     (2, 2), (1, 3), (1, 5), (2, 6))
        self.assertTrue(
            all(self.instance.can_move(position) for position in positions)
        )

    def test_cannot_move(self):
        self.instance.set_position((6, 2))
        positions = ((6, 4), (8, 3), (4, 0), (0, 7), (5, 3))
        self.assertTrue(
            all(not self.instance.can_move(position) for position in positions)
        )


class TestRookPiece(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = Rook(True)
        self.instance.set_position((5, 2))

    def test_str(self):
        self.assertEqual("white rook at (5, 2)", str(self.instance))

    def test_can_move(self):
        positions = ((5, 4), (7, 2), (5, 1), (2, 2))
        self.assertTrue(
            all(self.instance.can_move(position) for position in positions)
        )

    def test_cannot_move(self):
        positions = ((3, 4), (4, 6), (8, 2), (3, 1))
        self.assertTrue(
            all(not self.instance.can_move(position) for position in positions)
        )


class TestPawnPiece(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = Pawn(False)
        self.instance.set_position((6, 5))

    def test_str(self):
        self.assertEqual("black pawn at (6, 5)", str(self.instance))

    def test_can_move(self):
        self.instance.is_white = False
        self.assertTrue(self.instance.can_move((6, 4)))

        self.instance.is_white = True
        self.assertTrue(self.instance.can_move((6, 6)))

    def test_cannot_move(self):
        self.instance.is_white = False
        self.assertFalse(self.instance.can_move((6, 6)))
        self.assertFalse(self.instance.can_move((6, 3)))
        self.assertFalse(self.instance.can_move((5, 5)))

        self.instance.is_white = True
        self.assertFalse(self.instance.can_move((6, 4)))


if __name__ == "__main__":
    unittest.main()
