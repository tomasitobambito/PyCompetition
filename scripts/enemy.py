import pygame as pg
from pygame.math import Vector2
from settings import *
from support import *
from timer import Timer
from character import Character

class Enemy(Character):
    def __init__(self, pos, group, collisionGroup):
        self.generate_directions()

        super().__init__(
            pos, 
            group, 
            collisionGroup,
            {
                'up': [],
                'down': [],
                'left': [], 
                'right': []
            },
            {
                'down': []
            }, 
            'enemy'
        )

        for sprite in group.sprites():
            if sprite.charType == 'player':
                self.player = sprite

        self.speed = 150
        self.maxSpeed = 330
        self.speedMultiplier = 10
        self.forbiddenDirection = Vector2()

        self.timers = {
            'grace period': Timer(3000),
            'change mistakes': Timer(200)
        }

        self.z = LAYERS['enemy']

        self.timers['grace period'].activate()

    def generate_directions(self):
        vect = Vector2((1, 0))
        self.directions = [vect]
        for i in range(7):
            vect = vect.rotate(45)
            self.directions.append(vect)

    def accelerate(self, dt):
        if self.speed < self.maxSpeed:
            self.speed += self.speedMultiplier * dt

    def get_status(self):
        if self.direction.y == -1:
            self.status = 'up'
        elif self.direction.y == 1:
            self.status = 'down'
        elif self.direction.x > 0: 
            self.status = 'right'
        elif self.direction.x < 0:
            self.status = 'left'
            pass

    def calc_direction(self, dt):
        obstruction = False
        playerDir = (self.player.pos - self.pos).normalize()
        bestFitAngle = 360
        for direction in self.directions:
            if self.try_move(direction, dt):
                obstruction = True
                continue
            angle = abs(playerDir.angle_to(direction))
            if angle <= bestFitAngle: 
                self.direction = direction
                bestFitAngle = angle

        if obstruction and (self.direction == self.forbiddenDirection):
            self.direction = self.direction.rotate(180)
        

    def try_move(self, moveDir, dt):
        hitboxCopy = self.hitbox.copy()
        rectCopy = self.rect.copy()
        posCopy = Vector2(self.pos.x, self.pos.y)

        # 
        posCopy.x += moveDir.x * self.speed * dt
        rectCopy.centerx = round(posCopy.x)
        hitboxCopy.bottomleft = rectCopy.bottomleft
        xCollision = self.collision('horizontal', moveDir, hitboxCopy, rectCopy, posCopy)

        posCopy.y += moveDir.y * self.speed * dt
        rectCopy.centery = round(posCopy.y)
        hitboxCopy.bottomleft = rectCopy.bottomleft
        yCollision = self.collision('vertical', moveDir, hitboxCopy, rectCopy, posCopy)

        return xCollision or yCollision
        
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update_hitbox(self):
        self.hitbox.bottomleft = self.rect.bottomleft

    def reset(self):
        self.speed = 150
        self.forbiddenDirection = Vector2()
        self.timers['grace period'].activate()
        self.image = self.idleSurfs['down']

    def update(self, dt):
        self.update_timers()
        self.get_status()

        if not self.timers['grace period'].active:
            self.accelerate(dt)
            self.calc_direction(dt)
            self.move(dt)

            self.forbiddenDirection = Vector2(self.direction.x, self.direction.y).rotate(180)
            if self.direction.x == 0:
                self.forbiddenDirection.x = 0
            elif self.direction.y == 0:
                self.forbiddenDirection.y = 0

            self.animate(dt)
        
        self.update_hitbox()
    