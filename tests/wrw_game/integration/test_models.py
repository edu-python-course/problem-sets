import unittest
from unittest import mock

from wrw_game import enums
from wrw_game import exceptions
from wrw_game import models
from wrw_game import settings


class TestSuccessAttack(unittest.TestCase):
    def setUp(self) -> None:
        self.player = models.Player("player")
        self.enemy = models.Enemy(10)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=enums.FightChoice.ROBBER
    )
    def test_decrease_health(self, *mocks):
        self.enemy.decrease_health = mock.Mock()
        self.player.attack(self.enemy)
        self.enemy.decrease_health.assert_called_once()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=enums.FightChoice.ROBBER
    )
    def test_score_assignment(self, *mocks):
        self.player.add_score_points = mock.Mock()
        self.player.attack(self.enemy)
        self.player.add_score_points.assert_called_once_with(1)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=enums.FightChoice.ROBBER
    )
    def test_score_assignment_enemy_down(self, *mocks):
        self.player.add_score_points = mock.Mock()
        self.enemy.health = 0
        self.assertRaises(exceptions.EnemyDown, self.player.attack, self.enemy)
        self.player.add_score_points.assert_called_once_with(5)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=enums.FightChoice.ROBBER
    )
    def test_messages(self, *mocks):
        message = f"INFO:PlayerModel:{settings.MSG_SUCCESS_ATTACK}"
        with self.assertLogs() as logger:
            self.player.attack(self.enemy)
            self.assertEqual([message], logger.output)


class TestFailureAttack(unittest.TestCase):
    def setUp(self) -> None:
        self.player = models.Player("player")
        self.enemy = models.Enemy(10)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=enums.FightChoice.WIZARD
    )
    def test_decrease_health(self, *mocks):
        self.enemy.decrease_health = mock.MagicMock()
        self.player.attack(self.enemy)
        self.enemy.decrease_health.assert_not_called()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=enums.FightChoice.WIZARD
    )
    def test_score_assignment(self, *mocks):
        self.player.add_score_points = mock.Mock()
        self.player.attack(self.enemy)
        self.player.add_score_points.assert_not_called()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=enums.FightChoice.WIZARD
    )
    def test_messages(self, *mocks):
        message = f"INFO:PlayerModel:{settings.MSG_FAILURE_ATTACK}"
        with self.assertLogs() as logger:
            self.player.attack(self.enemy)
            self.assertEqual([message], logger.output)


class TestSuccessDefence(unittest.TestCase):
    def setUp(self) -> None:
        self.player = models.Player("player")
        self.enemy = models.Enemy(10)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=enums.FightChoice.ROBBER
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=enums.FightChoice.WARRIOR
    )
    def test_decrease_health(self, *mocks):
        self.player.decrease_health = mock.MagicMock()
        self.player.defence(self.enemy)
        self.player.decrease_health.assert_not_called()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=enums.FightChoice.ROBBER
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=enums.FightChoice.WARRIOR
    )
    def test_score_assignment(self, *mocks):
        self.player.add_score_points = mock.Mock()
        self.player.defence(self.enemy)
        self.player.add_score_points.assert_not_called()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=enums.FightChoice.ROBBER
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=enums.FightChoice.WARRIOR
    )
    def test_messages(self, mock_print, *mocks):
        message = f"INFO:PlayerModel:{settings.MSG_SUCCESS_DEFENCE}"
        with self.assertLogs() as logger:
            self.player.defence(self.enemy)
            self.assertEqual([message], logger.output)


class TestFailureDefence(unittest.TestCase):
    def setUp(self) -> None:
        self.player = models.Player("player")
        self.enemy = models.Enemy(10)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=enums.FightChoice.WIZARD
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=enums.FightChoice.WARRIOR
    )
    def test_decrease_health(self, *mocks):
        self.player.decrease_health = mock.MagicMock()
        self.player.defence(self.enemy)
        self.player.decrease_health.assert_called_once()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=enums.FightChoice.WIZARD
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=enums.FightChoice.WARRIOR
    )
    def test_messages(self, *mocks):
        message = f"INFO:PlayerModel:{settings.MSG_FAILURE_DEFENCE}"
        with self.assertLogs() as logger:
            self.player.defence(self.enemy)
            self.assertEqual([message], logger.output)


class TestDrawFight(unittest.TestCase):
    def setUp(self) -> None:
        self.player = models.Player("player")
        self.enemy = models.Enemy(10)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    def test_player_decrease_health(self, *mocks):
        self.player.decrease_health = mock.Mock()
        self.player.defence(self.enemy)
        self.player.decrease_health.assert_not_called()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=enums.FightChoice.WARRIOR
    )
    def test_enemy_decrease_health(self, *mocks):
        self.enemy.decrease_health = mock.Mock()
        self.player.attack(self.enemy)
        self.enemy.decrease_health.assert_not_called()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=enums.FightChoice.WARRIOR
    )
    def test_score_assignment_attack(self, *mocks):
        self.player.attack(self.enemy)
        self.assertEqual(0, self.player.score)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=enums.FightChoice.WARRIOR
    )
    def test_score_assignment_defence(self, *mocks):
        self.player.defence(self.enemy)
        self.assertEqual(0, self.player.score)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=enums.FightChoice.WARRIOR
    )
    def test_attack_message(self, *mocks):
        message = f"INFO:PlayerModel:{settings.MSG_DRAW}"
        with self.assertLogs() as logger:
            self.player.attack(self.enemy)
            self.assertEqual([message], logger.output)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=enums.FightChoice.WARRIOR
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=enums.FightChoice.WARRIOR
    )
    def test_defence_message(self, *mocks):
        message = f"INFO:PlayerModel:{settings.MSG_DRAW}"
        with self.assertLogs() as logger:
            self.player.defence(self.enemy)
            self.assertEqual([message], logger.output)
