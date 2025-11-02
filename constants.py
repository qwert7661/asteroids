import pygame
pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

ASTEROID_MIN_RADIUS = 10        # default 20
ASTEROID_KINDS = 0              # default 3
ASTEROID_SPAWN_RATE = 1       # seconds, default 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 15              # default 20
PLAYER_TURN_SPEED = 300         # default 300
PLAYER_SPEED = 200              # default 200
PLAYER_SLOW_SPEED_FACTOR = 0.3   # default 0.2
PLAYER_SLOW_TURN_FACTOR = 0.3   
PLAYER_SHOOT_SPEED = 500        # default 500
PLAYER_SHOOT_COOLDOWN = 0.5     # default 0.3

SHOT_RADIUS = 5                 # default 5

POWERUP_RADIUS = 15              # 
POWERUP_CHANCE = 20            # % of 100, default 10
POWERUP_LIFESPAN = 10           # seconds, default 10
FONT_POWERUP = pygame.font.Font(None, POWERUP_RADIUS*3)
FONT_POWERUP_OUTLINE = pygame.font.Font(None,(POWERUP_RADIUS*3) + 4)

POWERUP_SHIELD_COOLDOWN = 1     # seconds
POWERUP_INVINCIBILITY_TIME = 10 # seconds
POWERUP_FAST_FIRE_TIME = 10     # seconds
POWERUP_FAST_FIRE_RATE = PLAYER_SHOOT_COOLDOWN * 0.3
POWERUP_BACKWARD_SHOT_TIME = 10 # seconds
POWERUP_TRIPLE_SHOT_TIME = 10   # seconds
POWERUP_TRIPLE_SHOT_ANGLE = 20
POWERUP_PIERCING_SHOT_TIME = 10

LEVEL2_TIME = 30                # seconds
LEVEL3_TIME = 60                # seconds


# Difficulty Factors/Stage Times
ASTEROID_SPAWN_RATE_FACTOR = -0.001  # every second, decrease the spawn cooldown by default=0.001
ASTEROID_KINDS_TIME = 20            # every default=20 seconds, increase the number of asteroid kinds
