import pygame as pg
from pygame.math import Vector2
from settings import *
from support import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # general setup
        self.load_animations()
        self.load_idle()

        self.frameIndex = 0
        self.status = 'down'
        self.idle = True
        self.image = self.animations[self.status][self.frameIndex]
        self.rect = self.image.get_rect(center = pos)
        
        self.z = LAYERS['main']

        # # movement
        self.direction = Vector2()
        self.pos = Vector2(self.rect.center)
        self.speed = 300

    def load_idle(self):
        self.idleSurfs = {
            # 'up': [],
            'down': []
            # 'left': [],
            # 'right': []
        }

        for surf in self.idleSurfs.keys():
            path = '../graphics/player/idle/' + surf + ".png"
            self.idleSurfs[surf] = pg.image.load(path).convert_alpha()

    def load_animations(self):
        self.animations = {
            # 'up': [], 
            'down': []
            # 'left': [], 
            # 'right': []
        }

        for animation in self.animations.keys():
            path = '../graphics/player/' + animation
            self.animations[animation] = import_folder(path)

    def animate(self, dt):
        self.frameIndex += 3 * dt
        if self.frameIndex >= len(self.animations[self.status]):
            self.frameIndex = 0
        self.image = self.animations[self.status][int(self.frameIndex)]

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] or keys[pg.K_w]:
            # self.status = 'up'
            self.direction.y = -1
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.status = 'down'
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            # self.status = 'left'
            self.direction.x = -1
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            # self.status = 'right'
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

    def handle_idle(self):
        if self.direction.length() == 0:
            self.idle = True
            self.image = self.idleSurfs[self.status]
            self.frameIndex = 0
        else:
            self.idle = False

    def update(self, dt):
        self.input()
        self.move(dt)
        self.handle_idle()
        if not self.idle:
            self.animate(dt)
