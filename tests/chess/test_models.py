import unittest

from chess import Bishop, King, Piece, Queen


class TestPieceModel(unittest.TestCase):
    """Abstract chess model test case"""

    def setUp(self) -> None:
        self.instance = Piece()

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

    def test_position_outside(self):
        position = 10, 10
        regex = r"^.*\:Position \(-?\d+, -?\d+\) is outside the board$"
        with self.assertLogs() as logger:
            self.instance.set_position(position)
            self.assertRegex(*logger.output, regex)

    def test_get_delta(self):
        self.instance.position = 5, 5
        position = 10, 3
        dx, dy = 10 - 5, 3 - 5
        self.assertTupleEqual((dx, dy), self.instance.get_delta(position))


class TestKingPiece(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = King()
        self.instance.set_position((5, 5))

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
        self.instance = Queen()
        self.instance.set_position((2, 3))

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
        self.instance = Bishop()
        self.instance.set_position((5, 5))

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


if __name__ == "__main__":
    unittest.main()
