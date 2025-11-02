import pygame
import random
from circleshape import CircleShape
from powerup import PowerUp
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (150,80,80), (self.position.x, self.position.y), self.radius)
        pygame.draw.circle(screen, 'black', (self.position.x, self.position.y), self.radius, 1)
    
    def update(self, dt):
        global fps
        if dt != 0:
            fps = int(1/dt)
        self.position += self.velocity * dt



        # Clear when beyond screen limits
        if self.position.x < -100: self.kill()
        if self.position.x > SCREEN_WIDTH + 100: self.kill()
        if self.position.y < -100: self.kill()
        if self.position.y > SCREEN_HEIGHT + 100: self.kill()

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS and fps > FPS_MINIMUM:
            spawn_powerup = random.choice(range(100))
            if spawn_powerup <= POWERUP_CHANCE:
                PowerUp(self.position.x, self.position.y)
        else:
            new_radius = max(min((self.radius - ASTEROID_MIN_RADIUS), self.radius//1.8), ASTEROID_MIN_RADIUS)
            angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2 * 1.2