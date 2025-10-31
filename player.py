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

        self.lives = 1; self.shielded = False
        self.fast_fire = False; self.time_fast_fire = 0
        self.piercing_shot = False; self.time_piercing_shot = 0
        self.backward_shot = False; self.time_backward_shot = 0
        self.triple_shot = False; self.time_triple_shot = 0
        self.invincible = False; self.time_invincible = 0

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
        if not self.invincible and not self.shielded:
            pygame.draw.polygon(screen, 'grey', self.triangle())
        if self.shielded:
            pygame.draw.polygon(screen, (100,255,255), self.triangle())
        if self.invincible:
            pygame.draw.polygon(screen, 'green', self.triangle())

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
            if self.triple_shot:
                bullet_left = Shot(self.position.x, self.position.y, SHOT_RADIUS)
                bullet_left.velocity = pygame.Vector2(0,1).rotate(self.rotation - POWERUP_TRIPLE_SHOT_ANGLE) * PLAYER_SHOOT_SPEED
                bullet_right = Shot(self.position.x, self.position.y, SHOT_RADIUS)
                bullet_right.velocity = pygame.Vector2(0,1).rotate(self.rotation + POWERUP_TRIPLE_SHOT_ANGLE) * PLAYER_SHOOT_SPEED
            if self.backward_shot:
                bullet_back = Shot(self.position.x, self.position.y, SHOT_RADIUS)
                bullet_back.velocity = pygame.Vector2(0,1).rotate(self.rotation) * -PLAYER_SHOOT_SPEED
                if self.triple_shot:
                    bullet_back_left = Shot(self.position.x, self.position.y, SHOT_RADIUS)
                    bullet_back_left.velocity = pygame.Vector2(0,1).rotate(self.rotation - POWERUP_TRIPLE_SHOT_ANGLE) * -PLAYER_SHOOT_SPEED
                    bullet_back_right = Shot(self.position.x, self.position.y, SHOT_RADIUS)
                    bullet_back_right.velocity = pygame.Vector2(0,1).rotate(self.rotation + POWERUP_TRIPLE_SHOT_ANGLE) * -PLAYER_SHOOT_SPEED
            if not self.fast_fire: self.shot_timer = PLAYER_SHOOT_COOLDOWN
            if self.fast_fire: self.shot_timer = POWERUP_FAST_FIRE_RATE

    
    def apply_powerup(self, pow):
        if pow.type == "shield":
            self.lives += 1
            self.shielded = True
        if pow.type == "invincibility":
            self.invincible = True
            self.time_invincible = 0
        if pow.type == "fast_fire":
            self.fast_fire = True
            self.time_fast_fire = 0
        if pow.type == "backward_shot":
            self.backward_shot = True
            self.time_backward_shot = 0
        if pow.type == "triple_shot":
            self.triple_shot = True
            self.time_triple_shot = 0
        if pow.type == "piercing_shot":
            self.piercing_shot = True
            self.time_piercing_shot = 0


    def update(self, dt):
        # Player Input
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

        # Tracking powerups
        if self.invincible:
            self.time_invincible += dt
        if self.time_invincible >= POWERUP_INVINCIBILITY_TIME:
            self.invincible = False
            self.time_invincible = 0
        if self.fast_fire:
            self.time_fast_fire += dt
        if self.time_fast_fire >= POWERUP_FAST_FIRE_TIME:
            self.fast_fire = False
            self.time_fast_fire = 0
        if self.backward_shot:
            self.time_backward_shot += dt
        if self.time_backward_shot >= POWERUP_BACKWARD_SHOT_TIME:
            self.backward_shot = False
            self.time_backward_shot = 0
        if self.triple_shot:
            self.time_triple_shot += dt
        if self.time_triple_shot >= POWERUP_TRIPLE_SHOT_TIME:
            self.triple_shot = False
            self.time_triple_shot = 0
        if self.piercing_shot:
            self.time_piercing_shot += dt
        if self.time_piercing_shot >= POWERUP_PIERCING_SHOT_TIME:
            self.piercing_shot = False
            self.time_piercing_shot = 0
