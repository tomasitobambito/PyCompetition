import pygame as pg
import time
from settings import *
from level import Level
class Game:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Game name (in the future)")
        self.clock = pg.time.Clock()
        self.level = Level()

    def run(self):
        prevTime = time.time()
        running = True

        while running:
            dt = time.time() - prevTime
            prevTime = time.time()

            # even loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.level.run(dt)

            pg.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()