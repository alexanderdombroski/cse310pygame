from typing import * # Used for fixed typing
from pygame import *
from Wall2 import Wall
from Square import PLAYER
from constants import all_sprites, all_walls, all_exits, all_ice, all_mud, all_spikes, WALL_THICKNESS, SCREEN_HEIGHT, SCREEN_WIDTH, current_room
from passage import Exit
from ice import Ice
from mud import Mud
from spikes import Spike


class Room:
    def __init__(
        self,
        start_x: int = None,
        start_y: int = None,
        default_wall_color: Tuple[int, int, int] = (128, 128, 128),
        build_border: bool = True
    ) -> None:
        
        self.room_sprites = sprite.Group()
        self.room_walls = sprite.Group()
        self.room_exits = sprite.Group()
        self.room_ice = sprite.Group()
        self.room_mud = sprite.Group()
        self.room_spikes = sprite.Group()


        self.start_x = start_x
        self.start_y = start_y
        PLAYER.teleport(start_x, start_y)

        # Wall Properties
        self.default_wall_color = default_wall_color
        if build_border:
            self.build_border()

    
    def enter_room(self) -> None:
        # Makes a room visible
        global all_sprites, all_walls, all_exits, all_ice, all_mud, current_room
        all_sprites.empty()
        all_walls.empty()
        all_exits.empty()
        all_ice.empty()
        all_mud.empty()
        all_sprites.add(self.room_sprites.copy())
        all_sprites.add(PLAYER)
        all_walls.add(self.room_walls.copy())
        all_exits.add(self.room_exits.copy())
        all_ice.add(self.room_ice.copy())
        all_mud.add(self.room_mud.copy())
        all_spikes.add(self.room_spikes.copy())
        
        # Reset movement
        current_room[0] = self
        PLAYER.teleport(self.start_x, self.start_y)

        # color: Tuple[int, int, int], 
#         left: int, 
#         top: int, 
#         length: int,
#         is_horizontal: bool,
#         # width: int, 
#         # height: int, 
#         groups: List[sprite.Group] = None

    # --------- Add Room Features ---------
    def build_wall(self, left: int, top: int, length: int = WALL_THICKNESS, width: int = WALL_THICKNESS, color: Tuple[int, int, int] = None) -> None:
        if color is None: # Neccessary because class properties can't be used as function parameter defaults
            color = self.default_wall_color

        Wall(color, left, top, length, width, [self.room_walls, self.room_sprites])

    def build_border(self) -> None:
        self.build_wall(0, 0, length=SCREEN_HEIGHT) # Left
        self.build_wall(0, 0, width=SCREEN_WIDTH) # Top
        self.build_wall(SCREEN_WIDTH - WALL_THICKNESS, 0, length=SCREEN_HEIGHT) # Right
        self.build_wall(0, SCREEN_HEIGHT - WALL_THICKNESS, width=SCREEN_WIDTH) # Bottom

    def build_passage(self, exit_type: Type[Exit], *args: Tuple, **kwargs: Dict[str, Any]) -> None:
        exit = exit_type(*args, **kwargs)
        self.room_sprites.add(exit)
        self.room_exits.add(exit)
        # Creates an exit of the specified type
        # *args is for required arguments
        # **kwargs is for optional arguments
    
    def build_ice(self, left: int, top: int, width: int = WALL_THICKNESS, height: int = WALL_THICKNESS) -> None:
        Ice(left, top, width, height, [self.room_ice, self.room_sprites])
    
    def build_mud(self, left: int, top: int, width: int = WALL_THICKNESS, height: int = WALL_THICKNESS) -> None:
        Mud(left, top, width, height, [self.room_mud, self.room_sprites])

    def build_spike(self, color: tuple[int, int, int], start_coordinate: tuple[int, int], direction: str) -> None:
        # Spike(color, start_coordinate, [self.room_spikes, self.room_sprites], direction)
        Spike(color, start_coordinate, direction, [self.room_spikes, self.room_sprites])