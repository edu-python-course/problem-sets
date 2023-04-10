"""
Game runner

"""

import logging

from wtk import engine
from wtk.loggers import stream_handler

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
