"""
Game engine

"""

import logging

from wrw_game.exceptions import EnemyDown, GameOver
from wrw_game.loggers import stream_handler
from wrw_game.models import Enemy, Player

logger = logging.getLogger("engine")
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)


def get_player_name() -> str:
    """Return a player's name from the user prompt"""

    player_name: str = ""

    while not player_name:
        player_name = input("ENTER YOUR NAME: ").strip()

    return player_name


def play() -> None:
    """Play the game"""

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
            msg_score_points = f"SCORE POINTS: {player.score}"
            logger.info(exc)
            logger.info(msg_score_points)
            break


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        pass
