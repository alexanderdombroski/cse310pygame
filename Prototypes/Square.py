import pygame
from pygame.locals import *

#square class. currently dependant on Coordinate
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()

        self.image = pygame.Surface((50,50))
        self.image.fill((0,200,0))

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.speed = 5

    def update(self):
        #when we press the key move in that direction by the speed amount
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

    