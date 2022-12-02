import unittest
from unittest import mock

from wrw_game import exceptions
from wrw_game import models
from wrw_game import settings


class TestEnemyModel(unittest.TestCase):
    ENEMY_LEVEL = 10

    def setUp(self) -> None:
        self.instance = models.Enemy(level=TestEnemyModel.ENEMY_LEVEL)

    @unittest.skip(reason="Defaults are not implemented yet")
    def test_defaults(self):
        instance = models.Enemy()
        self.assertEqual(instance.level, settings.INITIAL_ENEMY_LEVEL)

    def test_initializer(self):
        self.assertEqual(self.instance.level, TestEnemyModel.ENEMY_LEVEL)
        self.assertEqual(self.instance.health, TestEnemyModel.ENEMY_LEVEL)

    def test_stringify(self):
        self.assertRegex(str(self.instance), r"Enemy level \d+")

    def test_decrease_health(self):
        test_value = self.instance.health - 1
        self.instance.decrease_health()
        self.assertEqual(self.instance.health, test_value)

    def test_enemy_down(self):
        self.instance.health = 1
        self.assertRaises(exceptions.EnemyDown, self.instance.decrease_health)

    def test_decrease_healths_side_effects(self):
        try:
            self.instance.decrease_health()
        except exceptions.EnemyDown:
            pass
        self.assertEqual(self.instance.level, TestEnemyModel.ENEMY_LEVEL)


class TestPlayerModel(unittest.TestCase):
    PLAYER_NAME = "Bosco Longhole"

    def setUp(self) -> None:
        self.instance = models.Player(name=TestPlayerModel.PLAYER_NAME)

    @unittest.skip(reason="Defaults are not implemented yet")
    def test_defaults(self):
        self.assertEqual(self.instance.health, settings.INITIAL_PLAYER_HEALTH)

    def test_initializer(self):
        self.assertEqual(self.instance.name, TestPlayerModel.PLAYER_NAME)

    def test_stringify(self):
        self.assertEqual(str(self.instance), TestPlayerModel.PLAYER_NAME)

    def test_decrease_health(self):
        test_value = self.instance.health - 1
        self.instance.decrease_health()
        self.assertEqual(self.instance.health, test_value)

    def test_game_over(self):
        self.instance.health = 1
        self.assertRaises(exceptions.GameOver, self.instance.decrease_health)

    def test_score_assignment(self):
        self.instance.score = 5
        self.instance.add_score_points(10)
        self.assertEqual(self.instance.score, 15)

    @mock.patch("builtins.input", side_effect=["-1", "f", "0", "1"])
    def test_invalid_fight_choice(self, mock_input):
        models.Player._select_fight_choice()
        self.assertEqual(mock_input.call_count, 4)

    def test_warrior_selection(self):
        choice = settings.WARRIOR
        with mock.patch("builtins.input", return_value=str(choice)):
            self.assertEqual(models.Player._select_fight_choice(), choice)

    def test_robber_selection(self):
        choice = settings.ROBBER
        with mock.patch("builtins.input", return_value=str(choice)):
            self.assertEqual(models.Player._select_fight_choice(), choice)

    def test_wizard_selection(self):
        choice = settings.WIZARD
        with mock.patch("builtins.input", return_value=str(choice)):
            self.assertEqual(models.Player._select_fight_choice(), choice)

    def test_success_fights(self):
        result = models.Player.fight(settings.WARRIOR, settings.ROBBER)
        self.assertEqual(result, settings.SUCCESS)

        result = models.Player.fight(settings.ROBBER, settings.WIZARD)
        self.assertEqual(result, settings.SUCCESS)

        result = models.Player.fight(settings.WIZARD, settings.WARRIOR)
        self.assertEqual(result, settings.SUCCESS)

    def test_failure_fights(self):
        result = models.Player.fight(settings.WARRIOR, settings.WIZARD)
        self.assertEqual(result, settings.FAILURE)

        result = models.Player.fight(settings.ROBBER, settings.WARRIOR)
        self.assertEqual(result, settings.FAILURE)

        result = models.Player.fight(3, settings.ROBBER)
        self.assertEqual(result, settings.FAILURE)

    def test_draw_fights(self):
        result = models.Player.fight(settings.WARRIOR, settings.WARRIOR)
        self.assertEqual(result, settings.DRAW)

        result = models.Player.fight(settings.ROBBER, settings.ROBBER)
        self.assertEqual(result, settings.DRAW)

        result = models.Player.fight(settings.WIZARD, settings.WIZARD)
        self.assertEqual(result, settings.DRAW)
