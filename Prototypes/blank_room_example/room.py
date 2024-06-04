from typing import * # Used for fixed typing
from pygame import *
from sprite_groups import all_sprites
from Wall2 import Wall
from Square import Square
from main import WALL_THICKNESS

class Room:
    def __init__(
        self,
        start_x: int,
        start_y: int,
        wall_group: sprite.Group,
        default_wall_color: Tuple[int, int, int] = (128, 128, 128)
    ) -> None:
        
        self.player = Square(start_x, start_y, [all_sprites])

        # Wall Properties
        self.wall_group = wall_group
        self.default_wall_color = default_wall_color

    def build_wall(self, left: int, top: int, width: int = WALL_THICKNESS, height: int = WALL_THICKNESS, color: Tuple[int, int, int] = None) -> None:
        if color is None: # Neccessary because class properties can't be used as function parameter defaults
            color = self.default_wall_color

        Wall(color, left, top, width, height, [self.wall_group, all_sprites])
    
    def exit_room(self) -> None:
        # probs change this, but something will be neccessary
        for group in [all_sprites, self.wall_group]: group.empty()

    def update_player_movement(self) -> None:
        self.player.move()

