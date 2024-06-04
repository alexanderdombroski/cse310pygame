import pygame
from pygame.locals import *
from typing import *

class Wall(pygame.sprite.Sprite):
    def __init__(
        self, 
        color: Tuple[int, int, int], 
        left: int, 
        top: int, 
        width: int, 
        height: int, 
        groups: List[pygame.sprite.Group] = None
    ):
        
        # Add the sprites to groups
        super().__init__(*groups if groups else [])

        self.image = pygame.Surface((width, height))
        self.image.fill(pygame.Color(color))
        
        self.rect = self.image.get_rect(topleft=(left, top))
