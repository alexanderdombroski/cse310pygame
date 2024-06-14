from pygame import *
from typing import *

class Mud(sprite.Sprite):
    def __init__(
        self, 
        left: int, 
        top: int, 
        width: int, 
        height: int, 
        groups: List[sprite.Group] = None
    ) -> None:
        
        # Add the sprites to groups
        super().__init__(*groups if groups else [])

        self.image = Surface((width, height))
        self.image.fill(Color((101, 67, 33)))
        
        tile_image = image.load("images/mud.png")
        tile_width, tile_height = tile_image.get_size()
        
        # Generate Image Tiles
        self.image = Surface((width, height))
        for x in range(0, width, tile_width):
            for y in range(0, height, tile_height):
                self.image.blit(tile_image, (x, y))

        self.rect = self.image.get_rect(topleft=(left, top))