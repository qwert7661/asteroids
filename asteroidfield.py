import pygame
import random
from asteroid import Asteroid
from constants import *
from settings import *


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.total_time = 0
        self.time_track_cooldown = 0
        self.ASTEROID_SPAWN_RATE = ASTEROID_SPAWN_RATE
        self.ASTEROID_KINDS = ASTEROID_KINDS
        

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > self.ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, self.ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)

        # Track total time for scaling
        self.total_time += dt
        int_time = int(self.total_time)
        # Scale difficulty over time
        if self.ASTEROID_SPAWN_RATE > 0:
            self.ASTEROID_SPAWN_RATE += (ASTEROID_SPAWN_RATE_FACTOR * dt)
        if int_time % ASTEROID_KINDS_TIME == 0: 
            if self.time_track_cooldown == 0:
                self.time_track_cooldown = 1
                self.ASTEROID_KINDS += 1
                print(self.ASTEROID_KINDS)
        if int_time % ASTEROID_KINDS_TIME == 1:
            self.time_track_cooldown = 0
        # ASTEROID_KINDS += 1
        