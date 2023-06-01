import pygame as pg

class Timer:
    def __init__(self, duration, func = None):
        self.duration = duration
        self.func = func
        self.startTime = 0
        self.active = False

    def activate(self):
        self.active = True
        self.startTime = pg.time.get_ticks()

    def deactivate(self):
        self.active = False

    def update(self):
        currentTime = pg.time.get_ticks()
        if currentTime - self.startTime >= self.duration:
            self.deactivate()
            if self.func:
                self.func()