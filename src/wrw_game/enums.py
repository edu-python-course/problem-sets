"""
Game enumerated types

"""

import enum


class FightResult(enum.Enum):
    """Fight result enumeration model"""

    SUCCESS = 1
    FAILURE = -1
    DRAW = 0

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.name


class FightChoice(enum.Enum):
    """Fight choice enumeration model"""

    WARRIOR = enum.auto()
    ROBBER = enum.auto()
    WIZARD = enum.auto()

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.name

    def __sub__(self, other) -> FightResult:
        """Return a fight result"""

        if not isinstance(other, FightChoice):
            raise TypeError(
                f"unsupported operand type(s) for -: "
                f"{self.__class__.__name__} and {other.__class__.__name__}"
            )

        if self == other:
            return FightResult.DRAW

        success_attacks = (
            FightChoice.WARRIOR.value - FightChoice.ROBBER.value,
            FightChoice.ROBBER.value - FightChoice.WIZARD.value,
            FightChoice.WIZARD.value - FightChoice.WARRIOR.value,
        )
        if self.value - other.value in success_attacks:
            return FightResult.SUCCESS

        return FightResult.FAILURE
