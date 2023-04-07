import unittest

from chess import Piece


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


if __name__ == "__main__":
    unittest.main()
