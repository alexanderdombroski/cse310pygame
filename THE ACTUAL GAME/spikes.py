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

        start_x = start_coordinate[0]
        start_y = start_coordinate[1]

        point_1 = start_coordinate
        point_2 = (start_x, start_y + width)
        point_3 = (start_x + width, (start_y + width) / 2)

        self.image = Surface((width, height))
        self.rect = self.image.get_rect(topleft=(start_x, start_y))
        draw.polygon(self.image, color, (point_1, point_2, point_3))
