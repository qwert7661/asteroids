import pygame
import random
from circleshape import CircleShape
from powerup import PowerUp
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (130,100,50), (self.position.x, self.position.y), self.radius)
        pygame.draw.circle(screen, 'black', (self.position.x, self.position.y), self.radius, 1)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            spawn_powerup = random.choice(range(100))
            if spawn_powerup <= POWERUP_CHANCE:
                PowerUp(self.position.x, self.position.y)
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2 * 1.2