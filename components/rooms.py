from components.constants import  SCREEN_HEIGHT, SCREEN_WIDTH, WALL_THICKNESS#, current_room, all_sprites
from components.room import Room
tutorial_room = Room(start_x = SCREEN_WIDTH // 2, start_y=SCREEN_HEIGHT - WALL_THICKNESS * 3)
start_room = Room(start_x = (SCREEN_WIDTH -35) // 2, start_y=SCREEN_HEIGHT - WALL_THICKNESS * 5, default_wall_color=(128, 128, 128))

def create_start_room():
    pass

def create_room_two():
    room2 = Room(start_x=WALL_THICKNESS, start_y= (SCREEN_HEIGHT -WALL_THICKNESS) // 2)
    start_room.build_passage(room2, SCREEN_WIDTH - WALL_THICKNESS * 2, SCREEN_HEIGHT / 2, "r")
    room2.build_passage(start_room, SCREEN_WIDTH // 2 + SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2, "u")

def create_scotts_room():
    scotts_room = Room(start_x=SCREEN_WIDTH - WALL_THICKNESS * 4, start_y=100 , default_wall_color=(190, 0, 0))
    scotts_room.build_passage(start_room,  2.5 * WALL_THICKNESS, SCREEN_HEIGHT - 2 * WALL_THICKNESS, "u")
    start_room.build_passage(scotts_room, SCREEN_WIDTH // 2 - WALL_THICKNESS // 2, WALL_THICKNESS)
    scotts_room.build_passage(start_room, SCREEN_WIDTH - WALL_THICKNESS * 3.5, 5, "u")

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


def create_tutorial_room():

    #create doorways
    start_room.build_passage(tutorial_room, (SCREEN_WIDTH-WALL_THICKNESS) // 2, SCREEN_HEIGHT - WALL_THICKNESS * 2, "u")
    tutorial_room.build_passage(start_room, (SCREEN_WIDTH -WALL_THICKNESS) // 2, WALL_THICKNESS, "u", True)

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

    #key example
    tutorial_room.build_collectable(35, 105, "key")
    tutorial_room.build_collectable(35, 175, "coin")
    
    room_name = tutorial_room
    
    #trigger example
    trigger1 = room_name.build_trigger(385, SCREEN_HEIGHT - WALL_THICKNESS * 5)
    trigger2 = room_name.build_trigger(455, SCREEN_HEIGHT - WALL_THICKNESS * 5)
    trigger3 = room_name.build_trigger(525, SCREEN_HEIGHT - WALL_THICKNESS * 5)
    trigger4 = room_name.build_trigger(595, SCREEN_HEIGHT - WALL_THICKNESS * 5)

    #trap example
    arrow_spitter1 = room_name.build_arrow_spitter(280, 0, rotation_degrees_ccw=180)
    arrow_spitter2 = room_name.build_arrow_spitter(350, SCREEN_HEIGHT - WALL_THICKNESS, rotation_degrees_ccw=0)
    arrow_spitter3 = room_name.build_arrow_spitter(0, SCREEN_HEIGHT - WALL_THICKNESS * 4, rotation_degrees_ccw=270)
    arrow_spitter4 = room_name.build_arrow_spitter(SCREEN_WIDTH - WALL_THICKNESS, SCREEN_HEIGHT - WALL_THICKNESS * 6, rotation_degrees_ccw=90)

    # connect trap and trigger
    trigger1.set_linked_trap(arrow_spitter1)
    trigger2.set_linked_trap(arrow_spitter2)
    trigger3.set_linked_trap(arrow_spitter3)
    trigger4.set_linked_trap(arrow_spitter4)

    arrow_spitter1.set_linked_trigger(trigger1)
    arrow_spitter2.set_linked_trigger(trigger2)
    arrow_spitter3.set_linked_trigger(trigger3)
    arrow_spitter4.set_linked_trigger(trigger4)