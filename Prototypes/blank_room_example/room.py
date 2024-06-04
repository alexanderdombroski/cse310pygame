from typing import * # Used for fixed typing
from pygame import *
from Wall2 import Wall
from Square import Square
from constants import all_sprites, all_walls, all_exits, WALL_THICKNESS, SCREEN_HEIGHT, SCREEN_WIDTH, current_room
from passage import Exit

class Room:
    def __init__(
        self,
        start_x: int,
        start_y: int,
        default_wall_color: Tuple[int, int, int] = (128, 128, 128)
    ) -> None:
        
        self.room_sprites = sprite.Group()
        self.room_walls = sprite.Group()
        self.room_exits = sprite.Group()
        self.player = Square(start_x, start_y, [self.room_sprites])

        self.start_x = start_x
        self.start_y = start_y

        # Wall Properties
        self.default_wall_color = default_wall_color

    
    def enter_room(self) -> None:
        # Makes a room visible
        global all_sprites, all_walls, all_exits, current_room
        all_sprites.empty()
        all_walls.empty()
        all_exits.empty()
        all_sprites.add(self.room_sprites.copy())
        all_walls.add(self.room_walls.copy())
        all_exits.add(self.room_exits.copy())
        
        # Reset movement
        current_room[0] = self
        self.player.rect.x = self.start_x
        self.player.rect.y = self.start_y

    def update_player_movement(self) -> None:
        self.player.move()

    # --------- Add Room Features ---------
    def build_wall(self, left: int, top: int, width: int = WALL_THICKNESS, height: int = WALL_THICKNESS, color: Tuple[int, int, int] = None) -> None:
        if color is None: # Neccessary because class properties can't be used as function parameter defaults
            color = self.default_wall_color

        Wall(color, left, top, width, height, [self.room_walls, self.room_sprites])

    def build_border(self) -> None:
        self.build_wall(0, 0, height=SCREEN_HEIGHT) # Left
        self.build_wall(0, 0, width=SCREEN_WIDTH) # Top
        self.build_wall(SCREEN_WIDTH - WALL_THICKNESS, 0, height=SCREEN_HEIGHT) # Right
        self.build_wall(0, SCREEN_HEIGHT - WALL_THICKNESS, width=SCREEN_WIDTH) # Bottom

    def build_passage(self, exit_type: Type[Exit], *args: Tuple, **kwargs: Dict[str, Any]) -> None:
        exit = exit_type(*args, **kwargs)
        self.room_sprites.add(exit)
        self.room_exits.add(exit)
        # Creates an exit of the specified type
        # *args is for required arguments
        # **kwargs is for optional arguments