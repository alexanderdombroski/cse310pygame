from pygame import *
from typing import *
from constants import WALL_THICKNESS

class Trigger(sprite.Sprite):
    def __init__(
        self, 
        left: int, 
        top: int, 
        width: int = WALL_THICKNESS, 
        height: int = WALL_THICKNESS, 
        color: Tuple[int, int, int] = (0,255,0), 
        groups: List[sprite.Group] = None, 
    ) -> None:
        
        super().__init__()

        self.image = Surface((width, height))
        self.image.fill(Color(color))
        
        self.rect = self.image.get_rect(topleft=(left, top))

    def update(self):
        pass
