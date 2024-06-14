from constants import all_sprites, SCREEN_HEIGHT, SCREEN_WIDTH, WALL_THICKNESS, current_room
from room import Room, Exit

tutorial_room = Room(start_x = SCREEN_WIDTH // 2, start_y=SCREEN_HEIGHT - 105)
start_room = Room(start_x = SCREEN_WIDTH // 2, start_y=SCREEN_HEIGHT - 105, default_wall_color=(128, 128, 128))

def create_start_room():
    pass

def create_room_two():
    room2 = Room(default_wall_color=(128, 0, 228))
    start_room.build_passage(Exit, room2, SCREEN_WIDTH - WALL_THICKNESS * 2, SCREEN_HEIGHT / 2)
    room2.build_passage(Exit, start_room, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


def create_scotts_room():
    # Room 3 (scotts_room)

    scotts_room = Room(start_x=SCREEN_WIDTH - WALL_THICKNESS * 4, start_y=50 , default_wall_color=(190, 0, 0))
    scotts_room.build_passage(Exit, start_room,  2.5 * WALL_THICKNESS, SCREEN_HEIGHT - 2 * WALL_THICKNESS)
    start_room.build_passage(Exit, scotts_room, SCREEN_WIDTH // 2 - WALL_THICKNESS // 2, WALL_THICKNESS)

    scotts_room.build_wall(5*35,5*35,14*35)
    scotts_room.build_wall(6*35,5*35,14*35)
    
    scotts_room.build_wall(13*35,0,14*35)
    scotts_room.build_wall(12*35,0,14*35)
    
    scotts_room.build_wall(19*35,5*35,14*35)
    scotts_room.build_wall(18*35,5*35,14*35)
    
    scotts_room.build_wall(25*35,0,14*35)
    scotts_room.build_wall(26*35,0,14*35)

    scotts_room.build_spike((255,255,255), (WALL_THICKNESS,100))


    # # X, Y, Width, Height
    # for i in range(3, 34, 2):
    #     thickness_factor = 2 if i % 4 == 3 else 1
    #     scotts_room.build_wall(SCREEN_WIDTH - WALL_THICKNESS * i, WALL_THICKNESS * thickness_factor, WALL_THICKNESS, SCREEN_HEIGHT - (35*3))


def create_tutorial_room():

    #create doorways
    start_room.build_passage(Exit, tutorial_room, WALL_THICKNESS, SCREEN_HEIGHT // 2 - WALL_THICKNESS // 2)
    tutorial_room.build_passage(Exit, start_room, SCREEN_WIDTH // 2 - WALL_THICKNESS // 2, WALL_THICKNESS)

    # TODO add text to explain how to play and describe objects 

    # wall example
    tutorial_room.build_wall(700, 500, 70, 210) # pillar

    # Ice / Mud example
    tutorial_room.build_ice(105, 105, 300, 100)
    tutorial_room.build_mud(105, 305, 300, 100)

    # spike example
    tutorial_room.build_spike((255,255,255), start_coordinate=(700, 300))
