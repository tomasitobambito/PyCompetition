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

        self.setup()

    def setup(self):
        self.player = Player(PLAYERSPAWN, self.allSprites, self.collisionSprites)
        self.enemy = Enemy(random.choice(ENEMYSPAWNS), self.allSprites, self.collisionSprites)
    
        Generic(
            pos = (0, 0),
            surf = pg.image.load('../graphics/map/background.png').convert_alpha(),
            groups = self.allSprites,
            z = LAYERS['background']
        )

        tileImages = create_map(TILESET)
        self.create_tiles(tileImages)

        self.questions = import_questions('../data/questions.txt')

        self.state = 'restart'
        self.lastTime = pg.time.get_ticks()
        self.timeAlive = 0

        # reset screen
        self.gameFont = pg.font.Font(FONT, 80)

        self.playerStandSurf = pg.image.load('../graphics/player/idle/down.png')
        self.playerStandSurf = pg.transform.scale_by(self.playerStandSurf, 2.5)
        self.playerStandRect = self.playerStandSurf.get_rect(center = (SCREEN_WIDTH / 2, 350))
        
        self.gameNameSurf = self.gameFont.render('Game Name', False, (0, 0, 0)) # color is subject to change
        self.gameNameRect = self.gameNameSurf.get_rect(center = (SCREEN_WIDTH / 2, 80))
    

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
        
            self.timeAlive += pg.time.get_ticks() - self.lastTime
            self.lastTime = pg.time.get_ticks()
            
        # question is being asked
        if self.state == 'question_time':
            self.dialogs.update(inputText, backspace)

            if self.inputbox.closed:

                # funy
                if self.inputbox.answer == "glare":
                    # play metal pipe falling sound
                    pass

                if self.inputbox.correctAnswer:
                    # play sound or something
                    pass
                else:
                    self.player.hp -= 1
                self.inputbox.kill()

                # reset to initial state
                self.reset_characters(dt)

                self.state = 'game' if self.player.hp > 0 else 'restart'

        
        if self.state == 'restart':
            self.displaySurf.fill('lightgray')

            if self.timeAlive == 0:
                message = "Press space to play, don't get caught!"
            else:
                message = f"Your Score: {int(self.timeAlive / 1000)} Press space to retry!"
            messageSurf = self.gameFont.render(message, False, (0, 0, 0))
            messageRect = messageSurf.get_rect(center = (SCREEN_WIDTH / 2, 600))

            self.displaySurf.blit(self.playerStandSurf, self.playerStandRect)
            self.displaySurf.blit(self.gameNameSurf, self.gameNameRect)
            self.displaySurf.blit(messageSurf, messageRect)

            keys = pg.key.get_pressed()

            if keys[pg.K_SPACE]:
                self.state = 'game'
                self.timeAlive = 0
                self.reset_characters(dt)

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

    def reset_characters(self, dt):
        self.player.pos = Vector2(PLAYERSPAWN)
        self.enemy.pos = Vector2(random.choice(ENEMYSPAWNS))
        self.allSprites.update(dt)
        self.enemy.reset()
        self.player.status = 'down'
        self.lastTime = pg.time.get_ticks()
