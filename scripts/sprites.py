import pygame as pg
from settings import *

class Generic(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['background']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-15, -5)