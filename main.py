import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



def main():
    print("Starting Asteroids!")

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    dt = 0
    score = 0
    time_in_seconds = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update
        time_in_seconds += dt
        for item in updatable:
            item.update(dt)
        for ast in asteroids:
            if ast.check_collision(player):
                print("Game over!")
                print("Score:", score)
                print("Time:",int(time_in_seconds))
                return
        for ast in asteroids:
            for shot in shots:
                if ast.check_collision(shot):
                    ast.split()
                    shot.kill()
                    score += 1

        # Render
        screen.fill((0,0,0))
        for item in drawable:
            item.draw(screen)

        # Display flip
        pygame.display.flip()
        dt = clock.tick(120) / 1000
        print(dt)


if __name__ == "__main__":
    main()
