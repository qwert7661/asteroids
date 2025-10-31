import pygame
pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

ASTEROID_MIN_RADIUS = 10        # default 20
ASTEROID_KINDS = 5              # default 3
ASTEROID_SPAWN_RATE = 1       # seconds, default 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 13              # default 20
PLAYER_TURN_SPEED = 300         # default 300
PLAYER_SPEED = 200              # default 200
PLAYER_SLOW_SPEED_FACTOR = 0.3   # default 0.2
PLAYER_SLOW_TURN_FACTOR = 0.3   
PLAYER_SHOOT_SPEED = 500        # default 500
PLAYER_SHOOT_COOLDOWN = 0     # default 0.3

SHOT_RADIUS = 5                 # default 5

POWERUP_RADIUS = 15              # 
POWERUP_CHANCE = 100            # % of 100
POWERUP_LIFESPAN = 10           # seconds
FONT_POWERUP = pygame.font.Font(None, POWERUP_RADIUS*3)
FONT_POWERUP_OUTLINE = pygame.font.Font(None,(POWERUP_RADIUS*3) + 4)