import pygame as pg
from dialog import Dialog
from support import draw_text

class InputBox(Dialog):
    def __init__(self, pos, group, question, answer):
        super().__init__(pos, group, 'input')

        self.question = question
        self.answer = answer
        self.enteredAnswer = ''

        self.correctAnswer = False
        self.closed = False
        self.active = True

        self.acceptButtonRect = pg.Rect(self.rect.bottomright[0] - 210, 550, 85, 85)
        self.inputRect = pg.Rect(self.rect.bottomleft[0]+125, 550, 930, 85)

    def close(self):
        if pg.mouse.get_pressed()[0]: 
            if self.closeButtonRect.collidepoint(pg.mouse.get_pos()):
                self.closed = True

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            self.closed = True

    def confirm(self):
        if pg.mouse.get_pressed()[0]:
            if self.acceptButtonRect.collidepoint(pg.mouse.get_pos()):
                self.closed = True
                self.checkAnswer()

        if pg.key.get_pressed()[pg.K_RETURN]:
            self.closed = True
            self.checkAnswer()

    def checkAnswer(self):
        if self.enteredAnswer.lower() == self.answer:
            self.correctAnswer = True

    def updateText(self):
        if active:
            keys = pg.key.get_pressed()
            for key in keys.keys():
                if keys[key]:
                    self.userText += key.unicode

    def update(self, dt):
        self.close()
        self.confirm()
        pg.draw.rect(self.image, 'green', self.inputRect)

        print(self.enteredAnswer)