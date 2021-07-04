import pygame
import os
from .config import *

class Wall(pygame.sprite.Sprite):

    def __init__(self,left,bottom,dir_images):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(dir_images,'wall.png'))
        self.image = pygame.transform.scale(self.image,(40,80))

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
        self.speedX = SPEED

        self.rect_top = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,1)

    def update(self):
        self.rect.left -= self.speedX
        self.rect_top.left = self.rect.left

    def stop(self):
        self.speedX = 0