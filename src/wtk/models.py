"""
Game models

"""

import logging
import random
from abc import ABC, abstractmethod
from functools import wraps

from wtk import settings
from wtk.enums import FightChoice, FightResult, get_fight_result
from wtk.exceptions import EnemyDown, GameOver
from wtk.loggers import stream_handler

__all__ = ["Enemy", "Player"]


class _AbstractModel(ABC):
    """Abstract game model"""

    @abstractmethod
    def select_attack(self) -> FightChoice:
        """Return a selected attack choice"""

    @abstractmethod
    def select_defence(self) -> FightChoice:
        """Return a selected defence choice"""

    @abstractmethod
    def decrease_health(self) -> None:
        """Decrease instance health points"""


class Enemy(_AbstractModel):
    """
    Enemy model

    Represents the playing enemy-bot.

    :ivar level: enemy's level value
    :type level: int
    :ivar health: enemy's instance health points
    :type health: int

    """

    def __init__(self, level: int = settings.INITIAL_ENEMY_LEVEL) -> None:
        """
        Initialize instance

        :param level: an enemy's level indicator
        :type level: int

        """

        self.health = level
        self.level = level

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return f"Enemy(level={self.level})"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return f"Enemy level {self.level}"

    def decrease_health(self) -> None:
        """
        Decrease health points

        This method decreases the health meter value. When it comes to be
        less than 1 (one) an ``EnemyDown`` exception is raised.

        :raise: EnemyDown

        """

        self.health -= 1
        if self.health < 1:
            raise EnemyDown(self)

    @staticmethod
    def _select_fight_choice() -> FightChoice:  # pragma: no cover
        """
        Return a random fight choice

        Choices made by an enemy are random.

        :return: a fight choice

        """

        return random.choice(tuple(FightChoice))

    @wraps(_select_fight_choice, ("__annotations__", "__doc__"))
    def select_attack(self) -> FightChoice:  # pragma: no cover
        return self._select_fight_choice()

    @wraps(_select_fight_choice, ("__annotations__", "__doc__"))
    def select_defence(self) -> FightChoice:  # pragma: no cover
        return self._select_fight_choice()


class Player(_AbstractModel):
    """
    Player model

    This model is controlled by the player.

    :ivar name: player's name
    :type name: str
    :ivar health: player's instance health points
    :type health: int
    :ivar score: player's instance gained score points
    :type score: int

    """

    logger = logging.getLogger("PlayerModel")
    logger.setLevel(logging.INFO)
    logger.addHandler(stream_handler)

    def __init__(self, name: str) -> None:
        """
        Initialize instance

        This method performs player instance initialization. It set instance
        name, initial score points value and health.

        :param name: a player's name
        :type name: str

        """

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
        """
        Decrease health points

        This method decreases the health meter value. When it comes to be
        less than 1 (one) an ``GameOver`` exception is raised.

        :raise: GameOver

        """

        self.health -= 1
        if self.health < 1:
            raise GameOver(self)

    @staticmethod
    def _select_fight_choice() -> FightChoice:
        """
        Return fight choice from the user's prompt

        The player is asked to make their decision for the upcoming fight.
        The chosen value is validated and if it is invalid the question is
        repeated.

        :return: a fight choice

        """

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

    @wraps(_select_fight_choice, ("__annotations__", "__doc__"))
    def select_attack(self) -> FightChoice:  # pragma: no cover
        return self._select_fight_choice()

    @wraps(_select_fight_choice, ("__annotations__", "__doc__"))
    def select_defence(self) -> FightChoice:  # pragma: no cover
        return self._select_fight_choice()

    @staticmethod
    def fight(attack: FightChoice, defence: FightChoice) -> FightResult:
        """
        Fight result calculation interface

        The method calculates the fight result based on the game rules:

        - **knight** beats **thief**
        - **thief** beats **wizard**
        - **wizard** beats **knight**

        """

        return get_fight_result(attack, defence)

    def add_score_points(self, score_points: int) -> None:
        """Add score points to the player instance"""

        self.score += score_points

    def attack(self, enemy: Enemy) -> None:
        """
        Attack an enemy

        Perform attack on an enemy instance. This method takes an enemy
        instance as an argument. After that, it takes attack choice from
        the player model and the defence choice from an enemy model.
        After fight result calculation required operation are to be
        performed (decrease enemy health, assign score points etc.).
        Based on fight result should print out a message:

        - "YOUR ATTACK IS SUCCESSFUL!"
        - "YOUR ATTACK IS FAILED!"
        - "IT'S A DRAW!"

        """

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
        """
        Defend from an enemy's attack

        Perform defence from an enemy attack. This method takes an enemy
        instance as an argument. After that, it takes defence choice from
        the player model and the attack choice from an enemy model.
        After fight result calculation required operation are to be
        performed (decrease player health).
        Based on fight result should print out a message:

        - "YOUR DEFENCE IS SUCCESSFUL!"
        - "YOUR DEFENCE IS FAILED!"
        - "IT'S A DRAW!"

        """

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
