"""
Game engine

"""

import logging

from wtk.exceptions import EnemyDown, GameOver
from wtk.loggers import stream_handler
from wtk.models import Enemy, Player

logger = logging.getLogger("engine")
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)


def get_player_name() -> str:
    """
    Return a player's name from the user prompt

    A validation process is performed as well. The player name cannot be
    an empty string.

    :return: a player defined name

    """

    player_name: str = ""

    while not player_name:
        player_name = input("ENTER YOUR NAME: ").strip()

    return player_name


def play() -> None:
    """
    Run the game

    The function initializes player and enemy instances.
    After that it runs the game process in an endless loop.
    Once the player is defeated - it stops the execution.

    """

    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy()

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown as exc:
            logger.info(exc)
            enemy = Enemy(enemy.level + 1)
        except GameOver as exc:
            logger.info(exc)
            logger.info("SCORE POINTS: %s", player.score)
            break


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        pass
