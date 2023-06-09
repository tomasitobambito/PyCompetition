import pygame as pg
from pygame.math import Vector2
from settings import *
from support import *

class Character(pg.sprite.Sprite):
    """Base class for characters, parent to both player and enemy.
    """    
    def __init__(self, pos, group, collisionGroup, animations, idleSurfs, charType):
        """
        Args:
            pos ((int, int) or  pg.math.Vector2): Position to place center at.
            group (pg.sprite.Group): Sprite group to assign to.
        """        
        super().__init__(group)

        self.charType = charType
        self.animations = animations
        self.idleSurfs = idleSurfs

        self.load_animations()
        self.load_idle()

        self.collisionSprites = collisionGroup

        # general setup
        self.frameIndex = 0
        self.status = 'down'
        self.idle = True
        self.image = self.animations[self.status][self.frameIndex]
        self.rect = self.image.get_rect(center = pos)
    

        # collision setup
        self.hitbox = pg.rect.Rect(self.rect.bottomleft[0], self.rect.bottomleft[1] - 35, self.rect.width, 35)
        
        self.z = LAYERS['main'] # failsafe

        # movement
        self.direction = Vector2()
        self.pos = Vector2(self.rect.center)

    def load_idle(self):
        for surf in self.idleSurfs.keys():
            path = f'../graphics/{self.charType}/idle/' + surf + ".png"
            self.idleSurfs[surf] = pg.image.load(path).convert_alpha()

    def load_animations(self):
        for animation in self.animations.keys():
            path = f'../graphics/{self.charType}/' + animation
            self.animations[animation] = import_folder(path)

    def animate(self, dt):
        self.frameIndex += 3 * dt
        if self.frameIndex >= len(self.animations[self.status]):
            self.frameIndex = 0
        self.image = self.animations[self.status][int(self.frameIndex)]

    def collision(self, dir):
        for sprite in self.collisionSprites.sprites():
            if hasattr(sprite, 'hitbox'): # failsafe
                if sprite.hitbox.colliderect(self.hitbox):
                    if dir == 'horizontal':
                        if self.direction.x > 0:
                            self.hitbox.right = sprite.hitbox.left
                        elif self.direction.x < 0:
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.rect.centerx

                    if dir == 'vertical':
                        if self.direction.y > 0:
                            self.hitbox.bottom = sprite.hitbox.top
                        elif self.direction.y < 0:
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.bottomleft = self.hitbox.bottomleft
                        self.pos.y = self.rect.centery
    
    def move(self, dt):
        if self.direction.length() == 0:
            return
        self.direction = self.direction.normalize()

        # horizontal
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = round(self.pos.x)
        self.hitbox.bottomleft = self.rect.bottomleft
        self.collision('horizontal')

        # vertical
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = round(self.pos.y)
        self.hitbox.bottomleft = self.rect.bottomleft
        self.collision('vertical')

    def handle_idle(self):
        if self.direction.length() == 0:
            self.idle = True
            self.image = self.idleSurfs[self.status]
            self.frameIndex = 0
        else:
            self.idle = False

    
