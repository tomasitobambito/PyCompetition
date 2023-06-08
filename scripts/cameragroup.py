import pygame as pg
from pygame.math import Vector2
from settings import *

class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurf = pg.display.get_surface()
        self.offset = Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layerIndex in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layerIndex:
                    offsetRect = sprite.rect.copy()
                    offsetRect.center -= self.offset
                    self.displaySurf.blit(sprite.image, offsetRect)