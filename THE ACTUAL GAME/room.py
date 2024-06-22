from typing import * # Used for fixed typing
from pygame import *
from wall import Wall
from player import PLAYER
from constants import all_sprites, all_walls, all_exits, all_ice, all_mud, all_spikes, all_text, all_collectables, all_triggers, all_arrow_spitters, all_attacks, WALL_THICKNESS, SCREEN_HEIGHT, SCREEN_WIDTH, DEFAULT_FONT_COLOR, DEFAULT_FONT_SIZE, current_room
from passage import Exit
from ice import Ice
from mud import Mud
from spikes import Spike
from boulder import Boulder
from text.text import Text
from collectable import Collectable
from trigger import Trigger
from arrow_spitter import Arrow_Spitter


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
        self.room_text = sprite.Group()
        self.room_boulder = sprite.Group()
        self.room_collectables = sprite.Group()        
        self.room_triggers =  sprite.Group()
        self.room_arrow_spitters = sprite.Group()
        self.room_attacks = sprite.Group()

        self.start_x = start_x
        self.start_y = start_y
        PLAYER.teleport(start_x, start_y)
        #small bug where defining a room without start x/y makes player unkillable (unable to be teleported to start of room)

        # Wall Properties
        self.default_wall_color = default_wall_color
        if build_border:
            self.build_border()        
    

    def enter_room(self) -> None:
        # Makes a room visible
        all_sprites.empty()

        all_walls.empty()
        all_exits.empty()
        all_ice.empty()
        all_mud.empty()
        all_spikes.empty()
        all_text.empty()
        all_collectables.empty()
        all_triggers.empty()
        all_arrow_spitters.empty()
        all_attacks.empty()

        all_sprites.add(self.room_sprites.copy())
        all_sprites.add(PLAYER)
        
        all_walls.add(self.room_walls.copy())
        all_exits.add(self.room_exits.copy())
        all_ice.add(self.room_ice.copy())
        all_mud.add(self.room_mud.copy())
        all_spikes.add(self.room_spikes.copy())
        all_text.add(self.room_text.copy())
        all_collectables.add(self.room_collectables.copy())
        all_triggers.add(self.room_triggers.copy())
        all_arrow_spitters.add(self.room_arrow_spitters.copy())
        all_attacks.add(self.room_attacks)
        
        # Reset movement
        current_room[0] = self
        PLAYER.teleport(self.start_x, self.start_y)

#         color: Tuple[int, int, int], 
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
        Spike(color, start_coordinate, direction, [self.room_spikes, self.room_sprites])


    def build_text(self, text: str, left: int, top: int, color: tuple[int, int, int] = DEFAULT_FONT_COLOR, size = DEFAULT_FONT_SIZE):
        Text(text, left, top, color, size, [self.room_text, self.room_sprites])


    def build_boulder(self, left, top, width, height, boulder_x, boulder_y) -> None:
        Boulder(left, top, width, height, boulder_x, boulder_y, [self.room_boulder, self.room_sprites])


    def build_collectable(self, left: int, top: int, name: str):
        Collectable(left, top, name, [self.room_collectables, self.room_sprites])


    def build_trigger(
            self,
            left: int, 
            top: int, 
            width: int = WALL_THICKNESS, 
            height: int = WALL_THICKNESS, 
            color: Tuple[int, int, int] = (0,255,0), 
            groups: List[sprite.Group] = None, 
            linked_trap = "",):
        return Trigger(left, top, width, height, color, [self.room_triggers, self.room_sprites], linked_trap)


    def build_arrow_spitter(
            self, 
            left: int, 
            top: int, 
            width: int = WALL_THICKNESS, 
            height: int = WALL_THICKNESS, 
            color: Tuple[int, int, int] = (0,0,255), 
            second_color: Tuple[int, int, int] = (255, 0, 255),
            groups: List[sprite.Group] = None, 
            attack_groups: List[sprite.Group] = None,
            linked_trigger = "",
            rotation_degrees_ccw:int = 0 # 0:up, 90:left, 180:down, 270:right
    ):
        return Arrow_Spitter(left=left, top=top, width=width, height=height, color=color, groups=[self.room_arrow_spitters, self.room_sprites], attack_groups= [all_attacks, self.room_sprites, all_sprites], linked_trigger=linked_trigger, second_color=second_color, rotation_degrees_ccw=rotation_degrees_ccw)