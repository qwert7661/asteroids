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
        if self.type == "shield": 
            self.letter = "S"
            self.letter_width, self.letter_height = FONT_POWERUP.size("S")
        if self.type == "fast_fire": 
            self.letter = "F"
            self.letter_width, self.letter_height = FONT_POWERUP.size("F")
        if self.type == "piercing_shot":
            self.letter = "P"
            self.letter_width, self.letter_height = FONT_POWERUP.size("P")
        if self.type == "backward_shot":
            self.letter = "B"
            self.letter_width, self.letter_height = FONT_POWERUP.size("B")
        if self.type == "triple_shot":
            self.letter = "T"
            self.letter_width, self.letter_height = FONT_POWERUP.size("T")
        if self.type == "invincibility":
            self.letter = "I"
            self.letter_width, self.letter_height = FONT_POWERUP.size("I")
        if self.type == "nuke":
            self.letter = "N"
            self.letter_width, self.letter_height = FONT_POWERUP.size("N")
        return self.letter
    
    def render_letter(self):
        if self.type == "shield": self.letter_render = FONT_POWERUP.render(self.letter,True,'cyan')
        if self.type == "fast_fire": self.letter_render = FONT_POWERUP.render(self.letter,True,'yellow')
        if self.type == "piercing_shot": self.letter_render = FONT_POWERUP.render(self.letter,True,'yellow')
        if self.type == "backward_shot": self.letter_render = FONT_POWERUP.render(self.letter,True,'yellow')
        if self.type == "triple_shot": self.letter_render = FONT_POWERUP.render(self.letter,True,'yellow')
        if self.type == "invincibility": self.letter_render = FONT_POWERUP.render(self.letter,True,'green')
        if self.type == "nuke": self.letter_render = FONT_POWERUP.render(self.letter,True,'red')
        return self.letter_render

    def draw(self, screen):
        screen.blit(self.letter_render,(self.position.x - (self.letter_width//2), self.position.y - (self.letter_height//2) + 1))
        pygame.draw.circle(screen, 'red', (self.position.x, self.position.y), self.radius, 1) # Draws hitbox

    def update(self, dt):
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()