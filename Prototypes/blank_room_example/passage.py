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
        color: Tuple[int, int, int] = (200, 100, 25) 
    ) -> None:
        super().__init__()

        self.image = Surface((width, width))
        self.image.fill(Color(color))
        
        self.rect = self.image.get_rect(topleft=(left, top))
        self.destination = destination
        
    def change_room(self) -> None:
        self.destination.enter_room()


# class Door(Exit):
#     pass

# class Ladder(Exit):
#     pass