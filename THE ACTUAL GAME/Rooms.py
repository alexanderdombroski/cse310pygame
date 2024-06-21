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
    
    for i in range(1, 33):
        # Spikes on the left and right walls of the screen.
        scotts_room.build_spike((255,255,255), (WALL_THICKNESS, WALL_THICKNESS * i), "r")
        scotts_room.build_spike((255,255,255), (SCREEN_WIDTH - WALL_THICKNESS, WALL_THICKNESS * i), "l")

        # Left and right spikes on pillars from the bottom.
        if i > 4:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * 5, WALL_THICKNESS * i), "l")
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * 7, WALL_THICKNESS * i), "r")
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * 18, WALL_THICKNESS * i), "l")
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * 20, WALL_THICKNESS * i), "r")

        # First section of down spikes from ceiling.
        if i > 1 and i < 11:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * i, WALL_THICKNESS), "d")
        
        if i > 11 and i < 14:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * i, WALL_THICKNESS * 14), "d")
        if i > 24 and i < 27:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * i, WALL_THICKNESS * 14), "d")

        # Left and right spikes on first wall pillar from top.
        if i < 14:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * 12, WALL_THICKNESS * i), "l")
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * 14, WALL_THICKNESS * i), "r")
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * 25, WALL_THICKNESS * i), "l")
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * 27, WALL_THICKNESS * i), "r")
        
        # Second section of down spikes from ceiling.
        if i > 14 and i < 24:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * i, WALL_THICKNESS), "d")
        
        # First up spikes.
        if i > 4 and i < 7:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * i, WALL_THICKNESS * 5), "u")
        
        # Second up spikes.
        if i > 17 and i < 20:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * i, WALL_THICKNESS * 5), "u")
    scotts_room.build_spike((255,255,255), (0,0), "r")
    scotts_room.build_passage(Exit, tutorial_room, 100, 0)


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
    tutorial_room.build_spike((255,255,255), start_coordinate=(700, 300), direction= "l")

    # boulder example
    tutorial_room.build_boulder(35,35,300,300,500,200)