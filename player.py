import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.thrusting = False
        self.low_thrusting = False

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def triangle_flame_outer(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        if self.thrusting:
            a = self.position - forward * (self.radius + (self.radius * 1.6))
            b = self.position - forward * self.radius - right
            c = self.position - forward * self.radius + right
        elif self.low_thrusting:
            a = self.position - forward * (self.radius + (self.radius * 0.9))
            b = self.position - forward * self.radius - right
            c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def triangle_flame_inner(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        if self.thrusting:
            a = self.position - forward * (self.radius + (self.radius * 1.2))
            b = self.position - forward * self.radius - right * 0.6
            c = self.position - forward * self.radius + right * 0.6
        elif self.low_thrusting:
            a = self.position - forward * (self.radius + (self.radius * 0.6))
            b = self.position - forward * self.radius - right * 0.6
            c = self.position - forward * self.radius + right * 0.6
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle())
        if self.thrusting or self.low_thrusting:
            self.draw_flame(screen)

    def draw_flame(self, screen):
        pygame.draw.polygon(screen, 'red', self.triangle_flame_outer())
        pygame.draw.polygon(screen, 'orange', self.triangle_flame_inner())

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_timer <= 0:
            bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOOT_COOLDOWN


    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:    # Turn left
            self.rotate(-dt)
        elif keys[pygame.K_LEFT]:
            self.rotate(-dt * PLAYER_SLOW_TURN_FACTOR)
        
        if keys[pygame.K_d]:    # Turn right
            self.rotate(dt)
        elif keys[pygame.K_RIGHT]:
            self.rotate(dt * PLAYER_SLOW_TURN_FACTOR)
        
        if keys[pygame.K_w]:    # Move forward
            self.move(dt)
            self.thrusting = True
            self.low_thrusting = False
        elif keys[pygame.K_UP]:
            self.move(dt * PLAYER_SLOW_SPEED_FACTOR)
            self.low_thrusting = True
            self.thrusting = False
        else: 
            self.thrusting = False
            self.low_thrusting = False
        
        if keys[pygame.K_s]:    # Move backward, slow speed only
            self.move(-dt * PLAYER_SLOW_SPEED_FACTOR)
        
        if keys[pygame.K_SPACE]:# Shoot
            self.shoot()
        self.shot_timer -= dt   # Decrease shot cooldown