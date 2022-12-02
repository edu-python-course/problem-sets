import logging

from wrw_game.exceptions import EnemyDown, GameOver
from wrw_game.loggers import stream_handler
from wrw_game.models import Enemy, Player

logger = logging.getLogger("engine")
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)


def get_player_name() -> str:
    player_name: str = ""

    while not player_name:
        player_name = input("ENTER YOUR NAME: ").strip()

    return player_name


def play() -> None:
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
            logger.info(f"SCORE POINTS: {player.score}")
            break


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        pass
