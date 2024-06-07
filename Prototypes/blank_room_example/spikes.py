from pygame import *
from typing import *

class Spike(sprite.Sprite):
    def __init__(
        self, 
        color: tuple[int, int, int],
        point_one: tuple[int, int],
        point_two: tuple[int, int],
        point_three: tuple[int, int],
        groups: List[sprite.Group] = None
            ) -> None:
        super.__init__(*groups if groups else [])

        points = []
        width = 0
        points.add(point_one, point_two, point_three)
        for i, point in points.enumerate():
            if i == 0:
                width = 0
            else: 
                point[0] - point[0]

        # self.image = Surface()
        # draw.polygon(screen, color, (point_one, point_two, point_three))

        
        # pass