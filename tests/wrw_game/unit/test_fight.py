import unittest

from wrw_game.enums import FightChoice, FightResult


class TestFightChoice(unittest.TestCase):
    def test_warrior_str(self):
        self.assertEqual(str(FightChoice.WARRIOR), "WARRIOR")

    def test_robber_str(self):
        self.assertEqual(str(FightChoice.ROBBER), "ROBBER")

    def test_wizard_str(self):
        self.assertEqual(str(FightChoice.WIZARD), "WIZARD")

    def test_equality(self):
        self.assertNotEqual(FightChoice.WARRIOR, FightChoice.ROBBER)
        self.assertNotEqual(FightChoice.WARRIOR, FightChoice.WIZARD)
        self.assertNotEqual(FightChoice.ROBBER, FightChoice.WIZARD)


class TestFightResult(unittest.TestCase):
    def test_success_str(self):
        self.assertEqual(str(FightResult.SUCCESS), "SUCCESS")

    def test_failure_str(self):
        self.assertEqual(str(FightResult.FAILURE), "FAILURE")

    def test_draw_str(self):
        self.assertEqual(str(FightResult.DRAW), "DRAW")


class TestFights(unittest.TestCase):
    def test_draw_warrior(self):
        fight_result = FightChoice.WARRIOR - FightChoice.WARRIOR
        self.assertEqual(FightResult.DRAW, fight_result)

    def test_draw_robber(self):
        fight_result = FightChoice.ROBBER - FightChoice.ROBBER
        self.assertEqual(FightResult.DRAW, fight_result)

    def test_draw_wizard(self):
        fight_result = FightChoice.WIZARD - FightChoice.WIZARD
        self.assertEqual(FightResult.DRAW, fight_result)

    def test_success_warrior(self):
        fight_result = FightChoice.WARRIOR - FightChoice.ROBBER
        self.assertEqual(FightResult.SUCCESS, fight_result)

    def test_success_robber(self):
        fight_result = FightChoice.ROBBER - FightChoice.WIZARD
        self.assertEqual(FightResult.SUCCESS, fight_result)

    def test_success_wizard(self):
        fight_result = FightChoice.WIZARD - FightChoice.WARRIOR
        self.assertEqual(FightResult.SUCCESS, fight_result)

    def test_failure_warrior(self):
        fight_result = FightChoice.WARRIOR - FightChoice.WIZARD
        self.assertEqual(FightResult.FAILURE, fight_result)

    def test_failure_robber(self):
        fight_result = FightChoice.ROBBER - FightChoice.WARRIOR
        self.assertEqual(FightResult.FAILURE, fight_result)

    def test_failure_wizard(self):
        fight_result = FightChoice.WIZARD - FightChoice.ROBBER
        self.assertEqual(FightResult.FAILURE, fight_result)

    def test_exception(self):
        self.assertRaises(TypeError, FightChoice.WARRIOR.__sub__, 1)
        self.assertRaises(TypeError, FightChoice.WARRIOR.__sub__, "1")
        self.assertRaises(TypeError, FightChoice.WARRIOR.__sub__, None)


if __name__ == "__main__":
    unittest.main()
