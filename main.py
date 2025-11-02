import pygame
from constants import *
from settings import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerup import PowerUp


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




def main():
    print("Starting Asteroids!")
    print("Level 1")

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    PowerUp.containers = (powerups, updatable, drawable)

    difficulty = Difficulty(ASTEROID_KINDS, ASTEROID_SPAWN_RATE)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    

    dt = 0
    score = 0
    time_in_seconds = 0
    shield_cooldown = 0
    level = 1
    block_levelup = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        # Timetracking
        time_in_seconds += dt
        int_time = int(time_in_seconds)
        shield_cooldown -= dt


        # Update
        for item in updatable:
            item.update(dt)
        for ast in asteroids:
            if ast.check_collision(player):
                if player.invincible == False and shield_cooldown <= 0:
                    player.lives -= 1
                    shield_cooldown = POWERUP_SHIELD_COOLDOWN
                    if player.lives == 1:
                        player.shielded = False
                    if player.lives == 0:
                        print("Game over!")
                        print("Score:", score)
                        print("Time:",int_time)
                        return
                    else:
                        ast.split()
            if ((ast.position.x < -100 or ast.position.x > SCREEN_WIDTH + 100) 
            or (ast.position.y < -100 or ast.position.y > SCREEN_HEIGHT + 100)):
                ast.kill()

        for ast in asteroids:
            for shot in shots:
                if ast.check_collision(shot):
                    ast.split()
                    if not player.piercing_shot:
                        shot.kill()
                    score += 1
        for pow in powerups:
            if pow.check_collision(player):
                player.apply_powerup(pow)
                if pow.type == "nuke":
                    for ast in asteroids:
                        ast.split()
                pow.kill()

        # Render
        screen.fill((0,0,0))
        for item in drawable:
            item.draw(screen)

        # Display flip
        pygame.display.flip()
        dt = clock.tick(120) / 1000


if __name__ == "__main__":
    main()
