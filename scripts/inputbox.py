import pygame as pg
from dialog import Dialog
from support import draw_text
from settings import FONT

class InputBox(Dialog):
    def __init__(self, pos, group, question, answer):
        super().__init__(pos, group, 'input')

        self.question = question
        self.answer = answer
        self.enteredAnswer = ''

        self.correctAnswer = False
        self.closed = False

        self.questionFont = pg.font.Font(FONT, 80)

        self.acceptButtonRect = pg.Rect(self.rect.bottomright[0] - 210, 550, 85, 85)
        self.inputRect = pg.Rect(self.rect.bottomleft[0]+125, 550, 930, 85)
        self.inputRect = self.inputRect.inflate(-30, -40)
        self.questionTextRect = pg.Rect(self.rect.topleft[0], self.rect.topleft[1], self.rect.width, self.rect.height-110)
        self.questionTextRect = self.questionTextRect.inflate(-180, -180)

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
        if self.enteredAnswer.lower() == self.answer.lower():
            self.correctAnswer = True

    def updateText(self, inputText, backspace):
        self.enteredAnswer += inputText
        
        if backspace:
            self.enteredAnswer = self.enteredAnswer[:-1]


    def update(self, inputText, backspace):
        self.close()
        self.confirm()
        self.updateText(inputText, backspace)
        draw_text(pg.display.get_surface(), self.question, self.textColor, self.questionTextRect, self.questionFont)
        draw_text(pg.display.get_surface(), self.enteredAnswer, self.textColor, self.inputRect, self.font)