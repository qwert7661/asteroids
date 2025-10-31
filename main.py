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

    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update
        # player.update(dt)
        for item in updatable:
            item.update(dt)
        for ast in asteroids:
            if ast.check_collision(player):
                print("Game over!")
                return
        for ast in asteroids:
            for shot in shots:
                if ast.check_collision(shot):
                    ast.kill()
                    shot.kill()

        

        # Render
        screen.fill((0,0,0))
        for item in drawable:
            item.draw(screen)

        # Display flip
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
