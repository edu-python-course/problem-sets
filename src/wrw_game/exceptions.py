"""
Game exception

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wrw_game.models import Enemy, Player


class EnemyDown(Exception):
    """Raised when an enemy is defeated"""

    def __init__(self, model: Enemy) -> None:
        self.model = model

    def __str__(self) -> str:
        return f"{self.model} is defeated"


class GameOver(Exception):
    """Raised when a player is defeated"""

    def __init__(self, model: Player) -> None:
        self.model = model

    def __str__(self) -> str:
        return f"{self.model} is defeated"
