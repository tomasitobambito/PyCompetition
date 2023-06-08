import pygame as pg
from pygame.math import Vector2
from settings import *
from support import *
from timer import Timer
from character import Character

class Enemy(Character):
    def __init__(self, pos, group):
        self.generate_directions()

        super().__init__(
            pos, 
            group, 
            {
                'up': [],
                'down': [],
                # 'left': [], 
                'right': [],
                'up_bloody': [],
                'down_bloody': [],
                # 'left_bloody': [],
                'right_bloody': [],
                'up_bloodier': [],
                'down_bloodier': [],
                'right_bloodier': [],
                # 'left_bloodier': []
            },
            {
                # 'up': [],
                'down': [],
                # 'left': [], 
                # 'right': [],
                # 'up_bloody': [],
                'down_bloody': [],
                # 'left_bloody': [],
                # 'right_bloody': [],
                # 'up_bloodier': [],
                'down_bloodier': [],
                # 'right_bloodier': [],
                # 'left_bloodier': []
            }, 
            'enemy'
        )

        for sprite in group.sprites():
            if sprite.charType == 'player':
                self.player = sprite

        self.speed = 250
        self.mistakes = 0

        self.timers = {
            'change mistakes': Timer(200)
        }

        self.z = LAYERS['enemy']

    def generate_directions(self):
        vect = Vector2((1, 0))
        self.directions = [vect]
        for i in range(7):
            vect = vect.rotate(45)
            self.directions.append(vect)


    def get_mistakes(self):
        # temporary while question system not in place
        if not self.timers['change mistakes'].active:
            keys = pg.key.get_pressed()
    
            if keys[pg.K_e]:
                self.mistakes += 1
                self.timers['change mistakes'].activate()
                if self.mistakes >= 3:
                    self.mistakes = 0

    def get_status(self):
        if self.direction.y == -1:
            self.status = 'up'
        elif self.direction.y == 1:
            self.status = 'down'
        elif self.direction.x > 0: 
            self.status = 'right'
        elif self.direction.x < 0:
            # self.status = 'left'
            pass

    def add_blood(self):
        if self.mistakes == 0:
            self.status = self.status.split('_')[0]
        elif self.mistakes == 1:
            self.status = self.status.split('_')[0] + '_bloody'
        elif self.mistakes == 2:
            self.status = self.status.split('_')[0] + '_bloodier'

    def calc_direction(self):
        playerDir = (self.player.pos - self.pos).normalize()
        bestFitAngle = 360
        for direction in self.directions:
            angle = abs(playerDir.angle_to(direction))
            if angle <= bestFitAngle: 
                self.direction = direction
                bestFitAngle = angle


    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self, dt):
        self.get_mistakes()
        self.update_timers()
        self.get_status()
        self.add_blood()
        self.calc_direction()
        self.move(dt)

        self.handle_idle()
        if not self.idle:
            self.animate(dt)
