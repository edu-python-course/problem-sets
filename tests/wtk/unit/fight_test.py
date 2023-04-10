import unittest

from wtk.enums import FightChoice, FightResult, get_fight_result


class TestFightChoice(unittest.TestCase):
    def test_warrior_str(self):
        self.assertEqual(str(FightChoice.KNIGHT), "KNIGHT")

    def test_robber_str(self):
        self.assertEqual(str(FightChoice.THIEF), "THIEF")

    def test_wizard_str(self):
        self.assertEqual(str(FightChoice.WIZARD), "WIZARD")

    def test_equality(self):
        self.assertNotEqual(FightChoice.KNIGHT, FightChoice.THIEF)
        self.assertNotEqual(FightChoice.KNIGHT, FightChoice.WIZARD)
        self.assertNotEqual(FightChoice.THIEF, FightChoice.WIZARD)


class TestFightResult(unittest.TestCase):
    def test_success_str(self):
        self.assertEqual(str(FightResult.SUCCESS), "SUCCESS")

    def test_failure_str(self):
        self.assertEqual(str(FightResult.FAILURE), "FAILURE")

    def test_draw_str(self):
        self.assertEqual(str(FightResult.DRAW), "DRAW")


class TestFights(unittest.TestCase):
    def test_draw_warrior(self):
        fight_result = get_fight_result(FightChoice.KNIGHT,
                                        FightChoice.KNIGHT)
        self.assertEqual(FightResult.DRAW, fight_result)

    def test_draw_robber(self):
        fight_result = get_fight_result(FightChoice.THIEF, FightChoice.THIEF)
        self.assertEqual(FightResult.DRAW, fight_result)

    def test_draw_wizard(self):
        fight_result = get_fight_result(FightChoice.WIZARD, FightChoice.WIZARD)
        self.assertEqual(FightResult.DRAW, fight_result)

    def test_success_warrior(self):
        fight_result = get_fight_result(FightChoice.KNIGHT, FightChoice.THIEF)
        self.assertEqual(FightResult.SUCCESS, fight_result)

    def test_success_robber(self):
        fight_result = get_fight_result(FightChoice.THIEF, FightChoice.WIZARD)
        self.assertEqual(FightResult.SUCCESS, fight_result)

    def test_success_wizard(self):
        fight_result = get_fight_result(FightChoice.WIZARD, FightChoice.KNIGHT)
        self.assertEqual(FightResult.SUCCESS, fight_result)

    def test_failure_warrior(self):
        fight_result = get_fight_result(FightChoice.KNIGHT, FightChoice.WIZARD)
        self.assertEqual(FightResult.FAILURE, fight_result)

    def test_failure_robber(self):
        fight_result = get_fight_result(FightChoice.THIEF, FightChoice.KNIGHT)
        self.assertEqual(FightResult.FAILURE, fight_result)

    def test_failure_wizard(self):
        fight_result = get_fight_result(FightChoice.WIZARD, FightChoice.THIEF)
        self.assertEqual(FightResult.FAILURE, fight_result)

    def test_exception(self):
        self.assertRaises(TypeError, get_fight_result, None, None)
        self.assertRaises(TypeError, get_fight_result, FightChoice.KNIGHT, 1)
        self.assertRaises(TypeError, get_fight_result, 1, FightChoice.KNIGHT)
