import unittest
from unittest import mock

from wrw_game import exceptions
from wrw_game import models


class TestSuccessAttack(unittest.TestCase):
    def setUp(self) -> None:
        self.player = models.Player("player")
        self.enemy = models.Enemy(10)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=2
    )
    def test_decrease_health(self, *mocks):
        self.enemy.decrease_health = mock.Mock()
        self.player.attack(self.enemy)
        self.enemy.decrease_health.assert_called_once()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=2
    )
    def test_score_assignment(self, *mocks):
        self.player.add_score_points = mock.Mock()
        self.player.attack(self.enemy)
        self.player.add_score_points.assert_called_once_with(1)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=2
    )
    def test_score_assignment_enemy_down(self, *mocks):
        self.player.add_score_points = mock.Mock()
        self.enemy.health = 0
        self.assertRaises(exceptions.EnemyDown, self.player.attack, self.enemy)
        self.player.add_score_points.assert_called_once_with(5)

    # noinspection PyUnusedLocal
    @unittest.skip(reason="Logger is not implemented")
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=2
    )
    def test_messages(self, *mocks):
        message = "INFO:player:YOUR ATTACK IS SUCCESSFUL!"
        with self.assertLogs("player", "INFO") as logger:
            self.player.attack(self.enemy)
            self.assertEqual(logger.output, [message])


class TestFailureAttack(unittest.TestCase):
    def setUp(self) -> None:
        self.player = models.Player("player")
        self.enemy = models.Enemy(10)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=3
    )
    def test_decrease_health(self, *mocks):
        self.enemy.decrease_health = mock.MagicMock()
        self.player.attack(self.enemy)
        self.enemy.decrease_health.assert_not_called()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=3
    )
    def test_score_assignment(self, *mocks):
        self.player.add_score_points = mock.Mock()
        self.player.attack(self.enemy)
        self.player.add_score_points.assert_not_called()

    # noinspection PyUnusedLocal
    @unittest.skip(reason="Logger is not implemented")
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=3
    )
    def test_messages(self, *mocks):
        message = "INFO:player:YOUR ATTACK IS FAILED!"
        with self.assertLogs("player", "INFO") as logger:
            self.player.attack(self.enemy)
            self.assertEqual(logger.output, [message])


class TestSuccessDefence(unittest.TestCase):
    def setUp(self) -> None:
        self.player = models.Player("player")
        self.enemy = models.Enemy(10)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=2
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=1
    )
    def test_decrease_health(self, *mocks):
        self.player.decrease_health = mock.MagicMock()
        self.player.defence(self.enemy)
        self.player.decrease_health.assert_not_called()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=2
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=1
    )
    def test_score_assignment(self, *mocks):
        self.player.add_score_points = mock.Mock()
        self.player.defence(self.enemy)
        self.player.add_score_points.assert_not_called()

    # noinspection PyUnusedLocal
    @unittest.skip(reason="Logger is not implemented")
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=2
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=1
    )
    def test_messages(self, mock_print, *mocks):
        message = "INFO:player:YOUR DEFENCE IS SUCCESSFUL!"
        with self.assertLogs("player", "INFO") as logger:
            self.player.defence(self.enemy)
            self.assertEqual(logger.output, [message])


class TestFailureDefence(unittest.TestCase):
    def setUp(self) -> None:
        self.player = models.Player("player")
        self.enemy = models.Enemy(10)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=3
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=1
    )
    def test_decrease_health(self, *mocks):
        self.player.decrease_health = mock.MagicMock()
        self.player.defence(self.enemy)
        self.player.decrease_health.assert_called_once()

    # noinspection PyUnusedLocal
    @unittest.skip(reason="Logger is not implemented")
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=3
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=1
    )
    def test_messages(self, *mocks):
        message = "INFO:player:ENEMY ATTACK IS SUCCESSFUL!"
        with self.assertLogs() as logger:
            self.player.defence(self.enemy)
            self.assertEqual(logger.output, [message])


class TestDrawFight(unittest.TestCase):
    def setUp(self) -> None:
        self.player = models.Player("player")
        self.enemy = models.Enemy(10)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=1
    )
    def test_player_decrease_health(self, *mocks):
        self.player.decrease_health = mock.Mock()
        self.player.defence(self.enemy)
        self.player.decrease_health.assert_not_called()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=1
    )
    def test_enemy_decrease_health(self, *mocks):
        self.enemy.decrease_health = mock.Mock()
        self.player.attack(self.enemy)
        self.enemy.decrease_health.assert_not_called()

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=1
    )
    def test_score_assignment_attack(self, *mocks):
        self.player.attack(self.enemy)
        self.assertEqual(0, self.player.score)

    # noinspection PyUnusedLocal
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=1
    )
    def test_score_assignment_defence(self, *mocks):
        self.player.defence(self.enemy)
        self.assertEqual(0, self.player.score)

    # noinspection PyUnusedLocal
    @unittest.skip(reason="Logger is not implemented yet")
    @mock.patch(
        "wrw_game.models.Player.select_attack",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_defence",
        return_value=1
    )
    def test_attack_message(self, *mocks):
        message = "INFO:player:IT'S A DRAW!"
        with self.assertLogs("player", "INFO") as logger:
            self.player.attack(self.enemy)
            self.assertEqual(logger.output, [message])

    # noinspection PyUnusedLocal
    @unittest.skip(reason="Logger is not implemented")
    @mock.patch(
        "wrw_game.models.Player.select_defence",
        return_value=1
    )
    @mock.patch(
        "wrw_game.models.Enemy.select_attack",
        return_value=1
    )
    def test_defence_message(self, *mocks):
        message = "INFO:player:IT'S A DRAW!"
        with self.assertLogs("player", "INFO") as logger:
            self.player.defence(self.enemy)
            self.assertEqual(logger.output, [message])
