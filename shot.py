import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'yellow', (self.position.x, self.position.y), self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt