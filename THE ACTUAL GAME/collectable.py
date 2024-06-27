from pygame import *
from typing import *
from player import PLAYER

COLLECTABLE_DATA = {
    "key": [
        "THE ACTUAL GAME/images/key.png",
        "THE ACTUAL GAME/sounds/key-get.mp3"
    ]
}

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
        tile_image = image.load(COLLECTABLE_DATA[name][0])
        self.image.blit(tile_image, (0, 0))
        
        self.rect = self.image.get_rect(topleft=(left, top))

        # Sounds
        self.pickup_sound = mixer.Sound(COLLECTABLE_DATA[name][1])

    def pickup(self):
        self.pickup_sound.play()
        PLAYER.inventory[self.name] += 1
        sprite.Sprite.kill(self) # Remove from groups and delete