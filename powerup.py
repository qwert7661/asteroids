import pygame
import random as rng
from constants import *
from circleshape import CircleShape

class PowerUp(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_RADIUS)
        self.lifespan = POWERUP_LIFESPAN
        self.type = self.determine_type()
        self.letter = self.assign_letter()
        self.letter_render = self.render_letter()
        self.letter_outline = self.render_letter_outline()

    def determine_type(self):
        types  = ["shield",
                  "fast_fire",
                  "piercing_shot",
                  "backward_shot",
                  "triple_shot",
                  "invincibility",
                  "nuke"]
        weight = [30, 20, 20, 15, 10, 4, 1]
        self.type = rng.choices(types, weights=weight, k=1)[0]
        return self.type

    def assign_letter(self):
        if self.type == "shield": self.letter = "S"
        if self.type == "fast_fire": self.letter = "F"
        if self.type == "piercing_shot": self.letter = "P"
        if self.type == "backward_shot": self.letter = "B"
        if self.type == "triple_shot": self.letter = "T"
        if self.type == "invincibility": self.letter = "I"
        if self.type == "nuke": self.letter = "N"
        return self.letter
    def render_letter(self):
        self.letter_render = FONT_POWERUP.render(self.letter,True,'green')
        return self.letter_render
    def render_letter_outline(self):
        self.letter_outline = FONT_POWERUP_OUTLINE.render(self.letter,True,'black')
        return self.letter_outline

    def draw(self, screen):
        screen.blit(self.letter_outline,(self.position.x - POWERUP_RADIUS + 2, self.position.y - POWERUP_RADIUS + 1))
        screen.blit(self.letter_render,(self.position.x - POWERUP_RADIUS + 3, self.position.y - POWERUP_RADIUS + 3))
        # pygame.draw.circle(screen, 'red', (self.position.x, self.position.y), self.radius, 1)

    def update(self, dt):
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()