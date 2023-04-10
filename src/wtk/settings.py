"""
*************
Game settings
*************

This module contains game settings and constants.

.. py:data: INITIAL_PLAYER_NAME

    Initial health meter value for a player instance

    :type: int

.. py:data: INITIAL_ENEMY_LEVEL

    Indicates the level to initialize the first enemy instance.

    :type: int

.. py:data: SCORE_SUCCESS_ATTACK

    Set the score value to assign when an attack is successful

    :type: int

.. py:data: SCORE_ENEMY_DOWN

    Set the score value to assign when an enemy is defeated

    :type: int

"""

# general configuration
GAME_TITLE = "KNIGHT, THIEFS AND WIZARDS GAME"

# initial settings
INITIAL_PLAYER_HEALTH = 5
INITIAL_ENEMY_LEVEL = 1

# score assignment options
SCORE_SUCCESS_ATTACK = 1
SCORE_ENEMY_DOWN = 5

# messages
MSG_SUCCESS_ATTACK = "YOUR ATTACK IS SUCCESSFUL!"
MSG_SUCCESS_DEFENCE = "YOUR DEFENCE IS SUCCESSFUL!"
MSG_FAILURE_ATTACK = "YOUR ATTACK IS FAILED!"
MSG_FAILURE_DEFENCE = "YOUR DEFENCE HAS BEEN BREACHED!"
MSG_DRAW = "IT'S A DRAW!"
