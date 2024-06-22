from pygame import *
from typing import *
from constants import COLLECTABLE_PATHS
from player import PLAYER

class Collectable(sprite.Sprite):
    def __init__(
        self, 
        left: int, 
        top: int, 
        name: str,
        groups: List[sprite.Group] = None
    ) -> None:
        
        # Add the sprites to groups
        super().__init__(*groups if groups else [])

        # Init Properties
        self.name = name

        # Draw Image
        self.image = Surface((35, 35))
        tile_image = image.load(COLLECTABLE_PATHS[name])
        self.image.blit(tile_image, (0, 0))
        
        self.rect = self.image.get_rect(topleft=(left, top))

    def pickup(self):
        PLAYER.inventory[self.name] += 1
        sprite.Sprite.kill(self) # Remove from groups and delete