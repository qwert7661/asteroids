import pygame
pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
FPS_MINIMUM = 20

FONT = pygame.font.Font(None, 30)
BIGFONT = pygame.font.Font(None, 100)
FONT_POWERUP = pygame.font.Font(None, 30)

ASTEROID_MIN_RADIUS = 10        # default 10
ASTEROID_KINDS = 0              # default 0
ASTEROID_KINDS_MAX = 20         # default 20
ASTEROID_SPAWN_RATE = 1       # seconds, default 1
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 15              # default 20
PLAYER_TURN_SPEED = 300         # default 300
PLAYER_SPEED = 200              # default 200
PLAYER_SLOW_SPEED_FACTOR = 0.3   # default 0.3
PLAYER_SLOW_TURN_FACTOR = 0.3   
PLAYER_SHOOT_SPEED = 500        # default 500
PLAYER_SHOOT_COOLDOWN = 0.5     # default 0.5

SHOT_RADIUS = 5                 # default 5

POWERUP_RADIUS = 15              # default 15
POWERUP_CHANCE = 20            # % of 100, default 20
POWERUP_LIFESPAN = 10           # seconds, default 10
POWERUP_SHIELD_COOLDOWN = 1     # seconds
POWERUP_INVINCIBILITY_TIME = 10 # seconds
POWERUP_FAST_FIRE_TIME = 10     # seconds
POWERUP_FAST_FIRE_RATE = PLAYER_SHOOT_COOLDOWN * 0.3
POWERUP_BACKWARD_SHOT_TIME = 10 # seconds
POWERUP_TRIPLE_SHOT_TIME = 10   # seconds
POWERUP_TRIPLE_SHOT_ANGLE = 20
POWERUP_PIERCING_SHOT_TIME = 10

# Difficulty Factors/Stage Times
SECONDS_TO_ENDGAME = 500
ASTEROID_SPAWN_RATE_FACTOR = -ASTEROID_SPAWN_RATE/SECONDS_TO_ENDGAME    # every second, decrease the spawn cooldown by default=0.002
ASTEROID_KINDS_TIME = SECONDS_TO_ENDGAME//ASTEROID_KINDS_MAX            # every default=25 seconds, increase the number of asteroid kinds
