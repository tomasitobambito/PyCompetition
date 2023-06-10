import pygame as pg
import time
from settings import *
from level import Level
class Game:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_NAME)
        self.clock = pg.time.Clock()
        self.level = Level()

    def run(self):
        prevTime = time.time()
        running = True

        while running:
            dt = time.time() - prevTime
            prevTime = time.time()

            currentInput = ""
            backspace = False

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        backspace = True
                    elif event.key == pg.K_RETURN:
                        pass
                    else:
                        currentInput += event.unicode


            self.level.run(dt, currentInput, backspace)

            pg.display.update() 

if __name__ == '__main__':
    game = Game()
    game.run()