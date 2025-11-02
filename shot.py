import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
        # Clearing when beyond screen limit
        if self.position.x < -100: self.kill()
        if self.position.x > SCREEN_WIDTH + 100: self.kill()
        if self.position.y < -100: self.kill()
        if self.position.y > SCREEN_HEIGHT + 100: self.kill()