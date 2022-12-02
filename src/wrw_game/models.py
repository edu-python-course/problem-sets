"""
Game models

"""
import random

from wrw_game.exceptions import EnemyDown, GameOver


class Enemy:
    """Enemy model

    :ivar level: enemy's level
    :type level: int
    :ivar health: enemy's instance health points
    :type health: int

    """

    def __init__(self, level: int) -> None:
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
    def _select_fight_choice() -> int:
        """Return a random fight choice"""

        return random.choice((1, 2, 3))

    def select_attack(self) -> int:
        return self._select_fight_choice()

    def select_defence(self) -> int:
        return self._select_fight_choice()


class Player:
    """Player model

    :ivar name: player's name
    :type name: str
    :ivar health: player's instance health points
    :type health: int
    :ivar score: player's instance gained score points
    :type score: int

    """

    def __init__(self, name: str) -> None:
        """Initialize instance"""

        self.name = name
        self.health = 5
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
    def _select_fight_choice() -> int:
        """Return fight choice from the user's prompt"""

        choice: int = 0
        valid_choices = 1, 2, 3

        while choice not in valid_choices:
            try:
                choice = int(input("MAKE YOUR CHOICE (1, 2, 3): "))
            except ValueError:
                pass

        return choice

    def select_attack(self) -> int:
        return self._select_fight_choice()

    def select_defence(self) -> int:
        return self._select_fight_choice()

    @staticmethod
    def fight(attack: int, defence: int) -> int:
        """Return a fight result"""

        # warrior - 1, robber - 2, wizard - 3
        success_attacks = 1 - 2, 2 - 3, 3 - 1
        failure_attacks = 1 - 3, 2 - 1, 3 - 2

        if attack == defence:
            return 0  # it's a draw

        if attack - defence in success_attacks:
            return 1

        if attack - defence in failure_attacks:
            return -1

    def attack(self, enemy: Enemy) -> None:
        """Attack an enemy"""

        attack = self.select_attack()
        defence = enemy.select_defence()
        fight_result = self.fight(attack, defence)

        if fight_result == 1:
            print("YOUR ATTACK IS SUCCESSFUL!")
            try:
                enemy.decrease_health()
                self.score += 1
            except EnemyDown:
                self.score += 5
                raise

        elif fight_result == -1:
            print("YOUR ATTACK IS FAILED!")

        elif fight_result == 0:
            print("IT'S A DRAW!")

    def defence(self, enemy: Enemy) -> None:
        """Defend from an enemy's attack"""

        attack = enemy.select_attack()
        defence = self.select_defence()
        fight_result = self.fight(attack, defence)

        if fight_result == 1:
            print("YOUR DEFENCE IS FAILED!")
            self.decrease_health()

        elif fight_result == -1:
            print("YOUR DEFENCE IS SUCCESSFUL!")

        elif fight_result == 0:
            print("IT'S A DRAW!")
