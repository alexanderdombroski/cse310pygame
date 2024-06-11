from pygame import *
from typing import *

class Ice(sprite.Sprite):
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
        self.image.fill(Color((173, 216, 230)))
        
        self.rect = self.image.get_rect(topleft=(left, top))