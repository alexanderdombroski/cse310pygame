from typing import *
import pygame
from pygame.locals import *
from pygame.sprite import Group

class Square(pygame.sprite.Sprite):
    def __init__(self, screen_width: int, screen_height: int, groups: List[Group] = None):
        if groups == None:
            super(Square, self).__init__()
        else:
            super().__init__(self, groups)
        
        self.width = 35
        self.color = (0, 200, 0)

        self.facing = "right"

        self.image = pygame.Surface((self.width,self.width))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = (screen_width / 2) - (self.width / 2)
        self.rect.y = (screen_height / 2) - (self.width / 2)

        self.speed = 5

    def print_direction(self):
        print(self.facing)

    def change_color(self, new_color):
        self.image.fill(new_color)