"""
Game exception

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # noinspection PyProtectedMember
    from wrw_game.models import _AbstractModel


class _GameModelException(Exception):
    """Base game model exception"""

    def __init__(self, model: _AbstractModel) -> None:
        """Initialize exception"""

        self.model = model

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return f"{self.model} is defeated"


class EnemyDown(_GameModelException):
    """Raised when an enemy is defeated"""


class GameOver(_GameModelException):
    """Raised when a player is defeated"""


__all__ = ["EnemyDown", "GameOver"]
