import pygame as pg
from player import Player
from enemy import Enemy
from textbox import TextBox
from inputbox import InputBox
from cameragroup import CameraGroup
from sprites import Generic
from support import create_map
from support import import_questions
from settings import *

class Level:
    def __init__(self):
        self.displaySurf = pg.display.get_surface()

        self.allSprites = CameraGroup()
        self.collisionSprites = pg.sprite.Group()
        self.dialogs = pg.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player((SPAWNPOINTX, SPAWNPOINTY), self.allSprites, self.collisionSprites)
        self.enemy = Enemy((SPAWNPOINTX + TILESIZE, SPAWNPOINTY), self.allSprites, self.collisionSprites)
        # self.textbox = TextBox((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), self.allSprites, "I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS ")
        # self.inputbox = InputBox((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), self.dialogs, "Question", "Answer")
        Generic(
            pos = (0, 0),
            surf = pg.image.load('../graphics/map/background.png').convert_alpha(),
            groups = self.allSprites,
            z = LAYERS['background']
        )

        tileImages = create_map(TILESET)
        self.create_tiles(tileImages)

        self.questions = import_questions('../data/questions.txt')
        
    def run(self, dt, inputText, backspace):
        self.displaySurf.fill('black')

        self.allSprites.custom_draw(self.player)
        self.dialogs.draw(self.displaySurf)

        self.allSprites.update(dt)
        
        # if self.inputbox.closed:
        #     if self.inputbox.correctAnswer:
        #         print('answer was right')
        #     else:
        #         print('fucking dimwit')
        #     self.inputbox.kill()
        #     self.inputbox.closed = False

        # if len(self.inputbox.groups()):
        #     self.dialogs.update(inputText, backspace)
        # else:
        #     self.allSprites.update(dt)
        
    def create_tiles(self, images):
        currentPos = Vector2(FIRSTTILEX, FIRSTTILEY)
        for i in range(len(TILESET)):
            for j in range(len(TILESET[i])):
                newSprite = Generic(currentPos, images[i][j], self.allSprites)
                if COLLISION[i][j]:
                    self.collisionSprites.add(newSprite)
                currentPos.x += TILESIZE
            currentPos.y += TILESIZE
            currentPos.x = FIRSTTILEX
