import pygame as pg
from pygame.math import Vector2
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # replace with importing assets
        
        # general setup
        self.image = pg.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']

        # # movement
        self.direction = Vector2()
        self.pos = Vector2(self.rect.center)
        self.speed = 300

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] or keys[pg.K_w]:
            self.direction.y = -1
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction.x = -1
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, dt):
        if self.direction.length() == 0:
            return
        self.direction = self.direction.normalize()

        # horizontal
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)
