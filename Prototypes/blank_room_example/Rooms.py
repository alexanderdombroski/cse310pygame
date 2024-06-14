from constants import all_sprites, SCREEN_HEIGHT, SCREEN_WIDTH, WALL_THICKNESS, current_room
from room import Room, Exit

start_room = Room(default_wall_color=(128, 128, 128))
scotts_room = Room(SCREEN_WIDTH - WALL_THICKNESS * 2, SCREEN_HEIGHT - WALL_THICKNESS * 2, (190, 0, 0))

def create_start_room():
    # Room One
    start_room.build_wall(500, 300, 70, is_horizontal=False) # pillar

    # Ice Test
    start_room.build_ice(100, 100, 100, 100)
    start_room.build_mud(200, 100, 100, 100)


def create_scotts_room():
    # Room 3 (scotts_room)
    scotts_room.build_passage(Exit, start_room,  1.66 * WALL_THICKNESS, SCREEN_HEIGHT - 2 * WALL_THICKNESS)
    scotts_room.build_spike((255,255,255), (50,100))
    start_room.build_passage(Exit, scotts_room, SCREEN_WIDTH // 2 - WALL_THICKNESS // 2, WALL_THICKNESS)
    # X, Y, Width, Height
    for i in range(3, 34, 2):
        thickness_factor = 2 if i % 4 == 3 else 1
        scotts_room.build_wall(SCREEN_WIDTH - WALL_THICKNESS * i, WALL_THICKNESS * thickness_factor, WALL_THICKNESS, SCREEN_HEIGHT - (35*3))
