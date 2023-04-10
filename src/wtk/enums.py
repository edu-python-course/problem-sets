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

    KNIGHT = enum.auto()
    THIEF = enum.auto()
    WIZARD = enum.auto()

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.name


def get_fight_result(attack: FightChoice, defence: FightChoice) -> FightResult:
    """Return a fight result based on attack and defence choices

    This function performs argument types validation first and raises
    TypeError in case of failure. After that the attack choice is compared
    with the defence choice. The comparison rules are:

    - if attack and defence are the same - draw result is returned
    - if attack and defence pair is in successful attacks preset, the attack
      is considered to be successful
    - otherwise attack is considered to be failed

    :param attack: attack choice
    :type attack: :class: `FightChoice`
    :param defence: defence choice
    :type defence: :class: `FightChoice`

    :return:
    :rtype: :class: `FightResult`

    :raise: TypeError

    """

    # perform type validation
    if not isinstance(attack, FightChoice) or \
        not isinstance(defence, FightChoice):
        attack_cls = attack.__class__.__name__
        defence_cls = defence.__class__.__name__
        raise TypeError(
            f"unsupported argument type(s): '{attack_cls}' and '{defence_cls}'"
        )

    # calculate result
    if attack == defence:
        return FightResult.DRAW

    successful_attacks = (
        (FightChoice.KNIGHT, FightChoice.THIEF),
        (FightChoice.THIEF, FightChoice.WIZARD),
        (FightChoice.WIZARD, FightChoice.KNIGHT),
    )
    if (attack, defence) in successful_attacks:
        return FightResult.SUCCESS

    return FightResult.FAILURE
