import pygame as pg
import random
from player import Player
from enemy import Enemy
from textbox import TextBox
from inputbox import InputBox
from cameragroup import CameraGroup
from soundmixer import SoundMixer
from sprites import Generic
from support import create_map
from support import import_questions
from settings import *

class Level:
    def __init__(self):
        self.displaySurf = pg.display.get_surface()

        # create groups
        self.allSprites = CameraGroup()
        self.collisionSprites = pg.sprite.Group()
        self.dialogs = pg.sprite.Group()

        self.setup()

    def setup(self):
        # create characters
        self.player = Player(PLAYERSPAWN, self.allSprites, self.collisionSprites)
        self.enemy = Enemy(random.choice(ENEMYSPAWNS), self.allSprites, self.collisionSprites)
    
        # create map
        tileImages = create_map(TILESET)
        self.create_tiles(tileImages)

        # import questions
        self.questions = import_questions('../data/questions.txt')

        # set initial state
        self.state = 'restart'
        self.lastTime = pg.time.get_ticks()
        self.timeAlive = 0

        # import sounds 
        self.soundMixer = SoundMixer('../sounds')
        self.soundMixer.sounds['music'].play(loops= -1)
        
        # reset screen
        self.gameFont = pg.font.Font(FONT, 80)

        self.playerStandSurf = pg.image.load('../graphics/player/idle/down.png')
        self.playerStandSurf = pg.transform.scale_by(self.playerStandSurf, 2.5)
        self.playerStandRect = self.playerStandSurf.get_rect(center = (SCREEN_WIDTH / 2, 350))
        
        self.gameNameSurf = self.gameFont.render(GAME_NAME, False, (0, 0, 0)) # color is subject to change
        self.gameNameRect = self.gameNameSurf.get_rect(center = (SCREEN_WIDTH / 2, 80))
    
    def show_score(self):
        scoreSurf = self.gameFont.render(f'Score: {int(self.timeAlive // 1000)}', False, 'darkred')
        scoreRect = scoreSurf.get_rect(center = (0, 40))
        scoreRect.centerx = SCREEN_WIDTH - scoreRect.width / 1.5
        self.displaySurf.blit(scoreSurf, scoreRect)
    
    def show_health(self):
        healthSurf = self.gameFont.render(f'HP: {self.player.hp}', False, 'darkred')
        healthRect = healthSurf.get_rect(center = (0, 40))
        healthRect.centerx = healthRect.width * 0.8
        self.displaySurf.blit(healthSurf, healthRect)

    def run(self, dt, inputText, backspace):
        self.displaySurf.fill('black')

        self.allSprites.custom_draw(self.player)
        self.dialogs.draw(self.displaySurf)

        # player is running, regular game state
        if self.state == 'game':
            self.allSprites.update(dt)
            self.show_score()
            self.show_health()

            if self.player.hitbox.colliderect(self.enemy.hitbox):
                self.soundMixer.sounds['caught'].play()
                
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
                if self.inputbox.enteredAnswer.lower() == "glare":
                    print('hello')
                    self.soundMixer.sounds['metal_pipe_falling'].play()
                    self.player.hp -= 1
                elif self.inputbox.correctAnswer:
                    self.soundMixer.sounds['question_correct'].play()
                else:
                    self.soundMixer.sounds['question_wrong'].play()
                    self.player.hp -= 1
                self.inputbox.kill()

                # reset to initial state
                self.reset_characters(dt)

                self.state = 'game' if self.player.hp > 0 else 'restart'

        
        if self.state == 'restart':
            self.displaySurf.fill((144, 161, 171))

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
                self.player.hp = 3
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
        self.enemy.move(dt)
        self.player.status = 'down'
        self.lastTime = pg.time.get_ticks()
