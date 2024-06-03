import pygame
from pygame.locals import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, color, left, top, width, height, groups=None):
        # Add the sprites to groups
        if groups == None:
            super(Wall, self).__init__()
        else:
            super().__init__(self, groups)

        self.image = pygame.Surface((width,height))
        self.image.fill(pygame.Color(color))

        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top
        pygame.draw.rect(self.image, color, pygame.Rect(left, top, width, height))
