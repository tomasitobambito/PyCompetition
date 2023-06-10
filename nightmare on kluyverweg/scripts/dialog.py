import pygame as pg
from settings import FONT

class Dialog(pg.sprite.Sprite):
    def __init__(self, pos, group, type):
        super().__init__(group)

        if type == 'text':
            self.image = pg.image.load('../graphics/misc/textbox.png').convert_alpha()
        elif type == 'input':
            self.image = pg.image.load('../graphics/misc/inputbox.png').convert_alpha()

        self.rect = self.image.get_rect(center = pos)

        # this position was found using trial and error, do not touch it, it will break
        self.closeButtonRect = pg.Rect(self.rect.topright[0] - 80, 30, 45, 45)

        self.font = pg.font.Font(FONT, 48)

        self.textColor = (0, 0, 0)

    # for safety
    def update(self, dt):
        pass
        