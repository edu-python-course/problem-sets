"""
Game runner

"""

import logging

from wrw_game import engine
from wrw_game.loggers import stream_handler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)


def run() -> None:
    """Run the game"""

    try:
        engine.play()
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("\nGOOD BYE!")


if __name__ == "__main__":
    run()
