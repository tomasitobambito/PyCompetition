import pygame as pg
from player import Player
from enemy import Enemy
from textbox import TextBox
from inputbox import InputBox
from settings import *

class Level:
    def __init__(self):
        self.displaySurf = pg.display.get_surface()

        self.allSprites = pg.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), self.allSprites)
        self.enemy = Enemy((SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2), self.allSprites)
        # self.textbox = TextBox((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), self.allSprites, "Hello")
        self.inputbox = InputBox((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), self.allSprites, "Question", "Answer")

    def run(self, dt):
        self.displaySurf.fill('black')
        self.allSprites.draw(self.displaySurf)
        self.allSprites.update(dt)
        