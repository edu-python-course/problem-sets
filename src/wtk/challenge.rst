###############################################################################
                         Wizards, Thieves and Knights
###############################################################################

"Wizards, Thieves and Knights" (:abbr:`WTK (Wizards, Thieves and Knights)`)
game is a "Paper, Rock and Scissors" clone but in a fantasy setting. It comes
with a simple command line interface where the use must type in his or her
choice. The enemy is controlled by the script. The player's goal is to gain
as many score points, as it possible.

*****************
Code organization
*****************

Use separate modules to maintain your code base. For example:

::

    /
    |-- engine.py
    |-- exceptions.py
    |-- models.py
    |-- settings.py

******************************
General playground description
******************************

The game process is divided into rounds. Each round consists of **attack** and
**defence** stages. Rounds are repeated, until player is defeated.

Fight rules
===========

It's simple...

- **Wizard** beats **Knight**
- **Thief** beats **Wizard**
- **Knight** beats **Thief**

Attack stage
============

Player selects the choice to attack from **wizard**, **thief** or **knight**,
enemy selects the choice for defence from the same options by random. If the
attack is successful:

- enemy health is decreased
- player gains score points

In case enemy is defeated:

- a new enemy instance is initialized using higher level
- player gains some extra score points
- next defence stage is skipped, and player attacks again

Defence stage
=============

Player selects the choice to defend from **wizard**, **thief** or **knight**,
enemy selects the choice to attack from the same options by random. If the
attack is successful:

- player health is decreased

If player is defeated:

- report the message about gained score points to the terminal
- write down player's name and score points to "scores.txt" file

**********
Exceptions
**********

Enemy down
==========

This is an exceptional scenario when enemy is defeated. A custom exception
``EnemyDown`` should be used to track these cases. Exception should provide
the details on the enemy's instance, especially its level.

.. autoclass:: wtk.exceptions.EnemyDown

Game over
=========

This is an exceptional scenario when player is defeated. A custom exception
``GameOver`` should be used to track these cases. Exception should provide
the details on the player's instance, especially its score points.

.. autoclass:: wtk.exceptions.GameOver

******
Models
******

Enemy
=====

.. autoclass:: wtk.models.Enemy
    :members: decrease_health, select_attack, select_defence
    :special-members: __init__

You are free to implement other methods you like, if needed.

Player
======

.. autoclass:: wtk.models.Player
    :members: decrease_health, select_attack, select_defence,
              fight, attack, defence
    :special-members: __init__

********
Settings
********

Settings module contains constants values for the game.

For example,

.. autodata:: wtk.settings.INITIAL_PLAYER_HEALTH
    :no-value:
.. autodata:: wtk.settings.INITIAL_ENEMY_LEVEL
    :no-value:
.. autodata:: wtk.settings.SCORE_SUCCESS_ATTACK
    :no-value:
.. autodata:: wtk.settings.SCORE_ENEMY_DOWN
    :no-value:

You may also define messages with this module, for example:

.. autodata:: wtk.settings.MSG_SUCCESS_ATTACK
.. autodata:: wtk.settings.MSG_SUCCESS_DEFENCE
.. autodata:: wtk.settings.MSG_FAILURE_ATTACK
.. autodata:: wtk.settings.MSG_FAILURE_DEFENCE
.. autodata:: wtk.settings.MSG_DRAW

******
Engine
******

Engine module should provide two functions:

- ``get_player_name``
- ``play``

Player name getter
==================

Asks the user to type in his or her name and return it back.
Leading and trailing whitespaces are to be trimmed.
Name should contain at least one character.

.. autofunction:: wtk.engine.get_player_name

Play
====

This function initializes player and enemy instance.
It processes game rounds inside of an endless loop stage by stage.
If an enemy is defeated - a new one should be initialized with level increased
by 1 (one). This case should be reported to the terminal.
If a player is defeated - the "Game Over" message should be reported to the
terminal.
``KeyboardInterrupt`` should be handled as well - it's behavior is similar
to "Game Over" event, but "game over" message should be omitted.

.. autofunction:: wtk.engine.play

*********************
Optional Enhancements
*********************

#.  Add scores processor to show top-10 scores from a record table.
#.  Create game menu, for example:
    ::

        AVAILABLE MENU CHOICES: PLAY, SCORES, EXIT
        TYPE YOUR CHOICE HERE:

#.  Store score table to the database instead of using text file.
