from pygame import *
from typing import *

class Spike(sprite.Sprite):
    def __init__(
        self, 
        color: tuple[int, int, int],
        start_coordinate: tuple[int, int],
        groups: List[sprite.Group] = None
            ) -> None:
        super.__init__(*groups if groups else [])

        width = 50

        start_x = start_coordinate[0]
        start_y = start_coordinate[1]

        point_1 = start_coordinate
        point_2 = (start_x, start_y + width)
        point_3 = (start_x + width, (start_y + width))

        self.image = Surface(width, width)
        # draw.polygon(screen, color, (point_one, point_two, point_three))

        
        # pass