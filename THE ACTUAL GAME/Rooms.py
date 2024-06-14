from constants import all_sprites, SCREEN_HEIGHT, SCREEN_WIDTH, WALL_THICKNESS, current_room
from room import Room, Exit

start_room = Room(start_x = SCREEN_WIDTH // 2, start_y=SCREEN_HEIGHT - 105, default_wall_color=(128, 128, 128))

def create_start_room():

    # Room One
    start_room.build_wall(500, 300, 70) # pillar

    # Ice Test
    start_room.build_ice(105, 105, 300, 100)
    start_room.build_mud(105, 305, 300, 100)


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
