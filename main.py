import pygame
from constants import *
from player import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting Asteroids!")    
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Drawing
        screen.fill((0,0,0))
        player.draw(screen)

        # Display flip
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
