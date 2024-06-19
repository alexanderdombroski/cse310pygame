from pygame import *
from typing import *

class Collectable(sprite.Sprite):
    def __init__(
        self, 
        left: int, 
        top: int, 
        image_path: str,
        groups: List[sprite.Group] = None
    ) -> None:
        pass