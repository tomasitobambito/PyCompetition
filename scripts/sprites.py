import pygame as pg
from settings import *

class Generic(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['background']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z

class Tile(Generic):
    def __init__(self, pos, type, groups):
        surf = pg.image.load(f'../graphics/map/{type}').convert()

        super().__init__(pos, surf, groups, LAYERS['tile'])