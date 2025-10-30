import pygame as pg
from constants import *

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    print("Starting Asteroids!")
    
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return


        screen.fill((0,0,0))

        pg.display.flip()


if __name__ == "__main__":
    main()
