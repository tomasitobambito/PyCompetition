import pygame as pg
from pygame.math import Vector2
from settings import *
from support import *
from character import Character

class Player(Character):
    def __init__(self, pos, group):
        super().__init__(
            pos, 
            group, 
            {
                'up': [],
                'down': [],
                'left': [], 
                'right': []
            },
            {
                'up': [],
                'down': [],
                'left': [],
                'right': []
            },
            'player'
        )

        self.speed = 300

        self.hp = 3

        self.z = LAYERS['player']

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] or keys[pg.K_w]:
            self.status = 'up'
            self.direction.y = -1
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.status = 'down'
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.status = 'left'
            self.direction.x = -1
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.status = 'right'
            self.direction.x = 1
        else:
            self.direction.x = 0

    def update(self, dt):
        self.input()
        self.move(dt)
        self.handle_idle()
        print(self.hitbox.x)
        if not self.idle:
            self.animate(dt)
