import pygame as pg
import random
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

        self.state = 'game'

        self.setup()

    def setup(self):
        self.player = Player((SPAWNPOINTX, SPAWNPOINTY), self.allSprites, self.collisionSprites)
        self.enemy = Enemy((SPAWNPOINTX + TILESIZE, SPAWNPOINTY), self.allSprites, self.collisionSprites)
    
        # self.textbox = TextBox((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), self.allSprites, "I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS I AM IN YOUR WALLS ")
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

        # player is running, regular game state
        if self.state == 'game':
            self.allSprites.update(dt)

            if self.player.hitbox.colliderect(self.enemy.hitbox):
                question = random.choice(self.questions)
                self.inputbox = InputBox((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), self.dialogs, question['question'], question['answer'])

                self.state = 'question_time'
            
                
        # question is being asked
        if self.state == 'question_time':
            self.dialogs.update(inputText, backspace)

            if self.inputbox.closed:
                # funy
                if self.inputbox.answer == "glare":
                    # play metal pipe falling sound
                    pass

                if self.inputbox.correctAnswer:
                    # play sound or something idgaf
                    pass
                else:
                    self.player.hp -= 1
                self.inputbox.kill()

                # reset to initial state
                self.player.pos = Vector2(SPAWNPOINTX, SPAWNPOINTY)
                self.enemy.pos = Vector2(SPAWNPOINTX + 3 * TILESIZE, SPAWNPOINTY)

                self.state = 'game'
                self.allSprites.update(dt)


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
