import pygame as pg
from settings import *
from support import draw_text
from dialog import Dialog

class TextBox(Dialog):
    def __init__(self, pos, group, text):
        super().__init__(pos, group, 'text')
        
        self.text = text

        self.textRect = self.rect.inflate(-180, -180)

    def close(self):
        if pg.mouse.get_pressed()[0]:
            if self.closeButtonRect.collidepoint(pg.mouse.get_pos()):
                self.kill()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            self.kill()

    def update(self, dt):
        self.display_text()
        self.close()

    def display_text(self):
        draw_text(self.image, self.text, self.textColor, textRect, self.font)
