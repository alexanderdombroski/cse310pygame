import pygame
from pygame.locals import *

class Impassable():
    def __init__(self, color):
        super(Impassable, self).__init__()

        self.image = pygame.Surface((50,500))
        self.image.fill(( 255, 87, 51 ))

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        pygame.draw.rect(self, color, pygame.Rect(30, 30, 60, 60))