from pygame import *
from typing import *
from constants import WALL_THICKNESS

class Exit(sprite.Sprite):
    def __init__(
        self, 
        destination, # Needs to be a room, but cannot specify cause circular imports :(
        left: int, 
        top: int, 
        width: int = WALL_THICKNESS,
        color: Tuple[int, int, int] = (0, 0, 0),
        locked: bool = False
    ) -> None:
        super().__init__()

        self.image = Surface((width, width), SRCALPHA)
        
        self.rect = self.image.get_rect(topleft=(left, top))
        self.destination = destination

        tile_image = image.load("THE ACTUAL GAME/images/locked.png" if locked else "THE ACTUAL GAME/images/gate.png")
        self.image.blit(tile_image, (0, 0))
        
    def change_room(self) -> None:
        self.destination.enter_room()

    def unlock(self) -> None:
        self.image.blit(image.load("images/gate.png"), (0, 0))




# class Switch



# class Door(Exit):
#     pass

# class Ladder(Exit):
#     pass