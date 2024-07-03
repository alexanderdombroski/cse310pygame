from pygame import *
from typing import *
import pygame

class Boulder(sprite.Sprite):
    def __init__(self, left: int, top: int, width: int, height: int, boulder_x: int, boulder_y: int, groups: List[sprite.Group] = None) -> None:
        # Initialize the parent class (sprite.Sprite)
        super().__init__(*groups if groups else [])

        # Assign the positions and dimensions
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        # Create a surface for the sprite
        self.image = Surface((width, height), flags=pygame.SRCALPHA)

        # Load the image
        boulder_image = image.load("THE ACTUAL GAME/images/boulder.png").convert_alpha()

        self.image.blit(boulder_image, (0, 0))

        # Create a rectangle object for positioning
        self.rect = self.image.get_rect(topleft=(left, top))

        def collide_left(self, sprite_group):
            if pygame.sprite.spritecollide(self, sprite_group, False):
                return

        def collide_bottom(self, sprite_group):
            if pygame.sprite.spritecollide(self, sprite_group, False):
                return

        def collide_right(self, sprite_group):
            if pygame.sprite.spritecollide(self, sprite_group, False):
                return

        def collide_top(self, sprite_group):
            if pygame.sprite.spritecollide(self, sprite_group, False):
                return
