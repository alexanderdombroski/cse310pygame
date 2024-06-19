from pygame import *
from typing import *

class Spike(sprite.Sprite):
    def __init__(
        self, 
        color: tuple[int, int, int],
        start_coordinate: tuple[int, int],
        direction: str,
        groups: List[sprite.Group] = None
    ) -> None:
        super().__init__(*groups if groups else [])

        long_side = 34
        short_side = 20

        match (direction):
            case "l": 
                point_1 = (short_side, 0)
                point_2 = (short_side, long_side)
                point_3 = (0, long_side // 2)
                self.image = Surface((short_side, long_side))
                self.rect = self.image.get_rect(topright=start_coordinate)
            case "r":
                point_1 = (0, 0)
                point_2 = (0, long_side)
                point_3 = (short_side, long_side // 2)
                self.image = Surface((short_side, long_side))
                self.rect = self.image.get_rect(topleft=start_coordinate)
            case "u":
                point_1 = (0, short_side)
                point_2 = (long_side, short_side)
                point_3 = (long_side // 2, 0)
                self.image = Surface((long_side, short_side))
                self.rect = self.image.get_rect(bottomleft=start_coordinate)
            case "d":
                point_1 = (0, 0)
                point_2 = (long_side, 0)
                point_3 = (long_side // 2, short_side)
                self.image = Surface((long_side, short_side))
                self.rect = self.image.get_rect(topleft=start_coordinate)


        draw.polygon(self.image, color, (point_1, point_2, point_3))   

    def move_spikes(self):
        keys = key.get_pressed()

        if keys[K_LEFT] or keys[K_RIGHT] or keys[K_UP] or keys[K_DOWN]:
            self.rect.x += 5             
