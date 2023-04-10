import unittest
from unittest import mock

from wtk import enums
from wtk import exceptions
from wtk import models
from wtk import settings


class TestEnemyModel(unittest.TestCase):
    ENEMY_LEVEL = 10

    def setUp(self) -> None:
        self.instance = models.Enemy(level=TestEnemyModel.ENEMY_LEVEL)

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
        choice = enums.FightChoice.WARRIOR
        with mock.patch("builtins.input", return_value=str(choice.value)):
            self.assertEqual(models.Player._select_fight_choice(), choice)

    def test_robber_selection(self):
        choice = enums.FightChoice.ROBBER
        with mock.patch("builtins.input", return_value=str(choice.value)):
            self.assertEqual(models.Player._select_fight_choice(), choice)

    def test_wizard_selection(self):
        choice = enums.FightChoice.WIZARD
        with mock.patch("builtins.input", return_value=str(choice.value)):
            self.assertEqual(models.Player._select_fight_choice(), choice)

    def test_success_fights(self):
        result = models.Player.fight(
            enums.FightChoice.WARRIOR, enums.FightChoice.ROBBER
        )
        self.assertEqual(result, enums.FightResult.SUCCESS)

        result = models.Player.fight(
            enums.FightChoice.ROBBER, enums.FightChoice.WIZARD
        )
        self.assertEqual(result, enums.FightResult.SUCCESS)

        result = models.Player.fight(
            enums.FightChoice.WIZARD, enums.FightChoice.WARRIOR
        )
        self.assertEqual(result, enums.FightResult.SUCCESS)

    def test_failure_fights(self):
        result = models.Player.fight(
            enums.FightChoice.WARRIOR, enums.FightChoice.WIZARD
        )
        self.assertEqual(result, enums.FightResult.FAILURE)

        result = models.Player.fight(
            enums.FightChoice.ROBBER, enums.FightChoice.WARRIOR
        )
        self.assertEqual(result, enums.FightResult.FAILURE)

        result = models.Player.fight(
            enums.FightChoice.WIZARD, enums.FightChoice.ROBBER
        )
        self.assertEqual(result, enums.FightResult.FAILURE)

    def test_draw_fights(self):
        result = models.Player.fight(
            enums.FightChoice.WARRIOR, enums.FightChoice.WARRIOR
        )
        self.assertEqual(result, enums.FightResult.DRAW)

        result = models.Player.fight(
            enums.FightChoice.ROBBER, enums.FightChoice.ROBBER
        )
        self.assertEqual(result, enums.FightResult.DRAW)

        result = models.Player.fight(
            enums.FightChoice.WIZARD, enums.FightChoice.WIZARD
        )
        self.assertEqual(result, enums.FightResult.DRAW)
