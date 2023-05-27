import pygame as pg
from player import Player
from settings import *

class Level:
    def __init__(self):
        self.displaySurf = pg.display.get_surface()

        self.allSprites = pg.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), self.allSprites)

    def run(self, dt):
        self.displaySurf.fill('black')
        self.allSprites.draw(self.displaySurf)
        self.allSprites.update(dt)