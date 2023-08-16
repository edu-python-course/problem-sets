"""
Game settings

"""

# general configuration
GAME_TITLE = "KNIGHT, THIEFS AND WIZARDS GAME"

# initial settings
INITIAL_PLAYER_HEALTH: int = 5
"""
Initial player health value

:type INITIAL_PLAYER_HEALTH: int
"""

INITIAL_ENEMY_LEVEL: int = 1
"""
Initial enemy level value

:type INITIAL_ENEMY_LEVEL: int
"""

# score assignment options
SCORE_SUCCESS_ATTACK: int = 1
"""
Score points value to assign when player's attack is successful

:type SCORE_SUCCESS_ATTACK: int
"""

SCORE_ENEMY_DOWN: int = 5
"""
Score points value to assign when enemy is defeated

:type SCORE_ENEMY_DOWN: int
"""

# messages
MSG_SUCCESS_ATTACK: str = "YOUR ATTACK IS SUCCESSFUL!"
"""
Successful attack message

:type MSG_SUCCESS_ATTACK: str
"""

MSG_SUCCESS_DEFENCE: str = "YOUR DEFENCE IS SUCCESSFUL!"
"""
Successful defence message

:type MSG_SUCCESS_DEFENCE: str
"""

MSG_FAILURE_ATTACK: str = "YOUR ATTACK IS FAILED!"
"""
Failed attack message

:type MSG_FAILURE_ATTACK: str
"""

MSG_FAILURE_DEFENCE: str = "YOUR DEFENCE HAS BEEN BREACHED!"
"""
Failed defence message

:type MSG_FAILURE_DEFENCE: str
"""

MSG_DRAW: str = "IT'S A DRAW!"
"""
Draw fight message

:type MSG_DRAW: str
"""
