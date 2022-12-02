"""
Game models

"""

import logging
import random

from wrw_game import settings
from wrw_game.enums import FightChoice, FightResult
from wrw_game.exceptions import EnemyDown, GameOver
from wrw_game.loggers import stream_handler


class Enemy:
    """Enemy model

    :ivar level: enemy's level
    :type level: int
    :ivar health: enemy's instance health points
    :type health: int

    """

    def __init__(self, level: int = settings.INITIAL_ENEMY_LEVEL) -> None:
        """Initialize instance"""

        self.health = level
        self.level = level

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return f"Enemy(level={self.level})"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return f"Enemy level {self.level}"

    def decrease_health(self) -> None:
        """Decrease health points

        :raise: EnemyDown

        """

        self.health -= 1
        if self.health < 1:
            raise EnemyDown(self)

    @staticmethod
    def _select_fight_choice() -> FightChoice:  # pragma: no cover
        """Return a random fight choice"""

        return random.choice(tuple(FightChoice))

    def select_attack(self) -> FightChoice:  # pragma: no cover
        return self._select_fight_choice()

    def select_defence(self) -> FightChoice:  # pragma: no cover
        return self._select_fight_choice()


class Player:
    """Player model

    :ivar name: player's name
    :type name: str
    :ivar health: player's instance health points
    :type health: int
    :ivar score: player's instance gained score points
    :type score: int
    :cvar logger: class based message logger
    :type logger: :class: `logging.Logger`

    """

    logger = logging.getLogger("PlayerModel")
    logger.setLevel(logging.INFO)
    logger.addHandler(stream_handler)

    def __init__(self, name: str) -> None:
        """Initialize instance"""

        self.name = name
        self.health = settings.INITIAL_PLAYER_HEALTH
        self.score = 0

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return f"Player(name={self.name}"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.name

    def decrease_health(self) -> None:
        """Decrease instance health points

        :raise: GameOver

        """

        self.health -= 1
        if self.health < 1:
            raise GameOver(self)

    @staticmethod
    def _select_fight_choice() -> FightChoice:
        """Return fight choice from the user's prompt"""

        choices = ", ".join(
            f"{choice.name} - {choice.value}" for choice in FightChoice
        )
        msg = f"MAKE A FIGHT CHOICE FROM ({choices}): "
        while True:
            try:
                choice = int(input(msg))
                return FightChoice(choice)
            except ValueError:
                pass

    def select_attack(self) -> FightChoice:  # pragma: no cover
        return self._select_fight_choice()

    def select_defence(self) -> FightChoice:  # pragma: no cover
        return self._select_fight_choice()

    @staticmethod
    def fight(attack: FightChoice, defence: FightChoice) -> FightResult:
        """Return a fight result"""

        return attack - defence

    def add_score_points(self, score_points: int) -> None:
        """Add score points"""

        self.score += score_points

    def attack(self, enemy: Enemy) -> None:
        """Attack an enemy"""

        attack = self.select_attack()
        defence = enemy.select_defence()
        fight_result = self.fight(attack, defence)

        if fight_result == FightResult.SUCCESS:
            self.logger.info(settings.MSG_SUCCESS_ATTACK)
            try:
                enemy.decrease_health()
                self.add_score_points(settings.SCORE_SUCCESS_ATTACK)
            except EnemyDown:
                self.add_score_points(settings.SCORE_ENEMY_DOWN)
                raise

        elif fight_result == FightResult.FAILURE:
            self.logger.info(settings.MSG_FAILURE_ATTACK)

        elif fight_result == FightResult.DRAW:
            self.logger.info(settings.MSG_DRAW)

    def defence(self, enemy: Enemy) -> None:
        """Defend from an enemy's attack"""

        attack = enemy.select_attack()
        defence = self.select_defence()
        fight_result = self.fight(attack, defence)

        if fight_result == FightResult.SUCCESS:
            self.logger.info(settings.MSG_FAILURE_DEFENCE)
            self.decrease_health()

        elif fight_result == FightResult.FAILURE:
            self.logger.info(settings.MSG_SUCCESS_DEFENCE)
        elif fight_result == FightResult.DRAW:
            self.logger.info(settings.MSG_DRAW)
