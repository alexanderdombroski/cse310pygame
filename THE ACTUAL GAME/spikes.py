from pygame import *
from typing import *

class Spike(sprite.Sprite):
    def __init__(
        self, 
        color: tuple[int, int, int],
        start_coordinate: tuple[int, int],
        groups: List[sprite.Group] = None
    ) -> None:
        super().__init__(*groups if groups else [])

        width = 50
        height = 50

        point_1 = (0, 0)
        point_2 = (0, width)
        point_3 = (width, height // 2)

        self.image = Surface((width, height))
        self.rect = self.image.get_rect(topleft=start_coordinate)
        draw.polygon(self.image, color, (point_1, point_2, point_3))
