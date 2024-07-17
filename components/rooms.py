from components.constants import  SCREEN_HEIGHT, SCREEN_WIDTH, WALL_THICKNESS#, current_room, all_sprites
from components.room import Room
from components.timed_room import Timed_Room


tutorial_room = Room(start_x = SCREEN_WIDTH // 2 - (35*.75), start_y=SCREEN_HEIGHT - WALL_THICKNESS * 3 -(35*.5), music_path="components/sounds/tutorial-room-sound.mp3")
start_hub = Room(start_x = (SCREEN_WIDTH -35) // 2, start_y=SCREEN_HEIGHT // 2, default_wall_color=(128, 128, 128), music_path = "components/sounds/itty-bitty-8-bit.mp3")


def create_start_hub():
    font_size = 100
    start_hub.build_collectable(90, SCREEN_HEIGHT - 115, "key")
    start_hub.build_text("Main Hub", 365, 280, (255,255,255), font_size)

def create_room_two():
    room2 = Room(start_x=3 * WALL_THICKNESS, start_y= (SCREEN_HEIGHT -WALL_THICKNESS) // 2)
    start_hub.build_passage(room2, SCREEN_WIDTH - WALL_THICKNESS * 2, SCREEN_HEIGHT / 2, "r")
    room2.build_passage(start_hub, SCREEN_WIDTH // 2 + SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2, "u")

def create_scotts_room():
    scotts_room = Room(start_x=SCREEN_WIDTH - WALL_THICKNESS * 4, start_y=100 , default_wall_color=(190, 0, 0))
    scotts_room.build_passage(start_hub,  2.5 * WALL_THICKNESS, SCREEN_HEIGHT - 2 * WALL_THICKNESS, "u")
    start_hub.build_passage(scotts_room, SCREEN_WIDTH // 2 - WALL_THICKNESS // 2, WALL_THICKNESS)
    scotts_room.build_passage(start_hub, SCREEN_WIDTH - WALL_THICKNESS * 3.5, 5, "u")

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
        if i < 19:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS, WALL_THICKNESS * i), "r")
            scotts_room.build_spike((255,255,255), (SCREEN_WIDTH - WALL_THICKNESS, WALL_THICKNESS * i), "l")

        # Left and right spikes on pillars from the bottom.
        if i > 4 and i < 19:
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

        # First spikes on floor
        if i > 7 and i < 17:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * i, SCREEN_HEIGHT - WALL_THICKNESS), "u")

        if i > 20 and i < 30:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * i, SCREEN_HEIGHT - WALL_THICKNESS), "u")

        # First up spikes.
        if i > 4 and i < 7:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * i, WALL_THICKNESS * 5), "u")
        
        # Second up spikes.
        if i > 17 and i < 20:
            scotts_room.build_spike((255,255,255), (WALL_THICKNESS * i, WALL_THICKNESS * 5), "u")

    scotts_room.build_collectable(400, SCREEN_HEIGHT - 115, "key", callback= lambda: start_hub.build_passage(bonus_room, 700,35, locked=True, max_entries=1))

def create_tutorial_room():

    # Split the screen into thirds for each tutorial room section.
    zone_1 = 0
    zone_2 = round(SCREEN_WIDTH * 1/3)
    zone_3 = round(SCREEN_WIDTH * 2/3)

    tutorial_room.build_collectable(SCREEN_WIDTH // 2 + 90, 385, "trophy")

    #create doorways
    start_hub.build_passage(tutorial_room, (SCREEN_WIDTH-WALL_THICKNESS) // 2, SCREEN_HEIGHT - WALL_THICKNESS * 2, "u")
    tutorial_room.build_passage(start_hub, (SCREEN_WIDTH -WALL_THICKNESS) // 2, WALL_THICKNESS, "u", True)
    
    room_name = tutorial_room
    
    #trap example
    arrow_spitter1 = room_name.build_arrow_spitter(280, 0, rotation_degrees_ccw=180)
    arrow_spitter2 = room_name.build_arrow_spitter(350, SCREEN_HEIGHT - WALL_THICKNESS, rotation_degrees_ccw=0)
    arrow_spitter3 = room_name.build_arrow_spitter(0, SCREEN_HEIGHT - WALL_THICKNESS * 4, rotation_degrees_ccw=270)
    arrow_spitter4 = room_name.build_arrow_spitter(SCREEN_WIDTH - WALL_THICKNESS, SCREEN_HEIGHT - WALL_THICKNESS * 6, rotation_degrees_ccw=90)

    # Main Title
    tutorial_room.build_text("Tutorial Room", 385, 100, (255,255,255), 50)

    # Collectable title
    tutorial_room.build_text("Collectables", zone_2 + 80, 200, (255,255,255), 30)

    # Key example
    tutorial_room.build_collectable(SCREEN_WIDTH // 2 + 90, 315, "key", callback=create_maze_room)

    # Coins example
    for x in range(zone_2 + 10, zone_3 - 35*4, 35):
        for y in range(315, 490, 70):
            tutorial_room.build_collectable(x, y, "coin")

    # Surface titles
    tutorial_room.build_text("Surfaces", zone_3 + 75, 200, (255,255,255), 30)
    tutorial_room.build_text("Ice", zone_3 + 130, 250, (255,255,255), 20)
    tutorial_room.build_text("Mud", zone_3 + 130, 400, (255,255,255), 20)

    # Ice / Mud example
    tutorial_room.build_ice(zone_3, 280, 300, 100)
    tutorial_room.build_mud(zone_3, 430, 300, 100)

    # Hazard Title
    tutorial_room.build_text("Hazards", zone_2 // 2 - 55, 200, (255,255,255), 30)

    # Spikes example
    for i in range(55, zone_2, 90):
        for j in range(300, 470, 70):
            tutorial_room.build_spike((255,255,255), (i, j), "u")

    # Trigger example
    trigger1 = room_name.build_trigger(55, 480)
    trigger2 = room_name.build_trigger(145, 480)
    trigger3 = room_name.build_trigger(235, 480)
    trigger4 = room_name.build_trigger(325, 480)

    # Connect trap and trigger
    trigger1.set_linked_trap(arrow_spitter1)
    trigger2.set_linked_trap(arrow_spitter2)
    trigger3.set_linked_trap(arrow_spitter3)
    trigger4.set_linked_trap(arrow_spitter4)

    arrow_spitter1.set_linked_trigger(trigger1)
    arrow_spitter2.set_linked_trigger(trigger2)
    arrow_spitter3.set_linked_trigger(trigger3)
    arrow_spitter4.set_linked_trigger(trigger4)


bonus_room = Timed_Room(start_hub, 10, 35, 35, build_border = True, music_path="components/sounds/bit-shift.mp3" )

def create_bonus_room():
    bonus_room.build_ice(90, 90, SCREEN_WIDTH - 180, SCREEN_HEIGHT - 180)
    for i in range(90, SCREEN_WIDTH - 180, 90):
        for j in range(90, SCREEN_HEIGHT - 180, 90):
            bonus_room.build_collectable(i, j, "coin")

    for i in range(90, SCREEN_HEIGHT - 90, 180):
        bonus_room.build_spike((255,255,255), (300, i), "u")
        bonus_room.build_spike((255,255,255), (600, i), "u")
        bonus_room.build_spike((255,255,255), (900, i), "u")


maze_room = Room(35, 70, build_border=True, music_path="components/sounds/maze-track.mp3")
maze_room2 = Room(SCREEN_WIDTH - 105, SCREEN_HEIGHT - 140, build_border=True)

def create_maze_room():
    start_hub.build_passage(maze_room, 50, 10, locked=True)
    maze_room.build_passage(start_hub, 50, 10)
    maze_room.build_collectable(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 70, "trophy", callback=reset_maze)
    
    # Left Walls
    maze_room.build_wall(105, 35, 35 * 4)
    maze_room.build_wall(105, 35 * 8, 35 * 4)
    maze_room.build_wall(105, 35 * 15, 35 * 4)

    # Second Left Walls
    maze_room.build_wall(210, 35 * 3, 35 * 4)
    maze_room.build_wall(245, 35 * 3, width=35 * 3)

    maze_room.build_wall(210, 35 * 9, 35 * 4)
    maze_room.build_wall(245, 35 * 9, width=35 * 4)
    maze_room.build_wall(350, 35 * 6, 35 * 3)


    maze_room.build_wall(210, 35 * 16, 35 * 3)
    
    # Bottom middle 
    maze_room.build_wall(315, 35 * 16, width=35 * 6)
    maze_room.build_wall(315, 35 * 16, width=35 * 6)
    maze_room.build_wall(315, 35 * 12, 35*4)
    maze_room.build_wall(420, 35 * 14, 35 * 2)

    # Middle Right (bottom to top)
    maze_room.build_wall(525, 35 * 12, 35 * 2)
    maze_room.build_wall(595, 35 * 16, 35 * 3)
    maze_room.build_wall(630, 35 * 11, 35 * 6)
    maze_room.build_wall(455, 35 * 11, width=35 * 5)
    maze_room.build_wall(455, 35 * 7, 35 * 4)

    # Top Middle
    maze_room.build_wall(35*9, 35, 70)
    maze_room.build_wall(35*12, 35, 35*3)
    maze_room.build_wall(35*15, 35*3, 35*2, 35*4) 
    maze_room.build_wall(35*19, 35, 35*4) 

    # Middle
    maze_room.build_wall(35*16, 35*5, 35*4)
    maze_room.build_wall(35*17, 35*8, width=35*2)

    # Second Right
    maze_room.build_wall(35*21, 35 * 11, 35 * 6)
    maze_room.build_wall(35*22, 35 * 16, width=35 * 6)

    maze_room.build_wall(35*21, 35*7, 35*2)
    
    
    # Right
    maze_room.build_wall(35*25, 35 * 6, 35 * 4)
    maze_room.build_wall(35*24, 35 * 10, width=35 * 5)
    maze_room.build_wall(35*24, 35 * 11, 35 * 3)
    maze_room.build_wall(35*25, 35 * 13, width=35 * 3)
    maze_room.build_wall(35*28, 35 * 13, 35 * 6)

    # Top Right
    maze_room.build_wall(35*28, 35, 35 * 7)
    maze_room.build_wall(35*22, 35*3, width=35*6)

def reset_maze():
    maze_room2.build_passage(start_hub, 50, 10)

    maze_room2.build_wall(35, 35*3, width=35*3)
    maze_room2.build_wall(35*3, 35*6, width=35*7)
    maze_room2.build_wall(35*10, 35*6, 35*7)

    # Long Top
    maze_room2.build_wall(35*10, 35, 35*3)
    maze_room2.build_wall(35*7, 35*3, width=35*22)
    maze_room2.build_wall(35*6, 35*3, 35*3)

    # Second Long Top
    maze_room2.build_wall(35*13, 35*6, 35*5)
    maze_room2.build_wall(35*14, 35*6, width=35*15)
    for x in range(35*16, 35*24, 35):
        maze_room2.build_collectable(x, 35*5, "coin")

    maze_room2.build_wall(35, 35*9, width=35*7)

    maze_room2.build_mud(35*17, 35*10, 35*11, 35*6)

    maze_room2.build_wall(35*13, 35*14, 35*6)

    # Bottom Left
    maze_room2.build_wall(35*4, 35*12, width=35*6)
    maze_room2.build_wall(35*3, 35*12, 35*5)

    maze_room2.build_ice(35*6, 35*15, 35*5, 35*2)

    maze_room2.enter_room()

trap_room = Room(start_x=35 * 3, start_y=35 * 3 / 2, music_path="components/sounds/cyborg-ninja.mp3")

def create_trap_room():

    room_name = trap_room

    room_name.build_passage(start_hub,35 * 1.5 / 2, 35 * 4 / 2, direction="l")
    start_hub.build_passage(room_name, WALL_THICKNESS, SCREEN_HEIGHT // 2 - WALL_THICKNESS // 2, direction="l")

    room_name.build_wall(left=1*WALL_THICKNESS, top=4 * WALL_THICKNESS, width=21* WALL_THICKNESS, length=2*WALL_THICKNESS)

    room_name.build_wall(left=21*WALL_THICKNESS, top=5 * WALL_THICKNESS, length=3* WALL_THICKNESS)
    room_name.build_wall(left=22*WALL_THICKNESS, top=7 * WALL_THICKNESS, width=5* WALL_THICKNESS)

    room_name.build_wall(left=26*WALL_THICKNESS, top=8*WALL_THICKNESS, length=8* WALL_THICKNESS)
    room_name.build_wall(left=25*WALL_THICKNESS, top=15*WALL_THICKNESS, width=2* WALL_THICKNESS)

    room_name.build_wall(left=17*WALL_THICKNESS, top=15*WALL_THICKNESS, length=5* WALL_THICKNESS)
    room_name.build_wall(left=17*WALL_THICKNESS, top=11*WALL_THICKNESS, width=9* WALL_THICKNESS)

    room_name.build_wall(left=17*WALL_THICKNESS, top=4* WALL_THICKNESS, length=4* WALL_THICKNESS, width=5*WALL_THICKNESS)
    room_name.build_wall(left=17*WALL_THICKNESS, top=7* WALL_THICKNESS, length=5* WALL_THICKNESS, width=9*WALL_THICKNESS)

    room_name.build_wall(left=4*WALL_THICKNESS, top=9* WALL_THICKNESS, length=7* WALL_THICKNESS, width=10*WALL_THICKNESS )
    room_name.build_wall(left=13*WALL_THICKNESS, top=15*WALL_THICKNESS, width=5* WALL_THICKNESS, length=4* WALL_THICKNESS)
    room_name.build_wall(left=7*WALL_THICKNESS, top=16* WALL_THICKNESS, length=4* WALL_THICKNESS, width=7*WALL_THICKNESS )

    room_name.build_passage(start_hub, 6.5*WALL_THICKNESS, 17*WALL_THICKNESS)
    room_name.build_collectable(5*WALL_THICKNESS, 17*WALL_THICKNESS, name="trophy")


    room_name.build_fire_breather(6*WALL_THICKNESS, 4 * WALL_THICKNESS, rotation_degrees_ccw=0)
    room_name.build_fire_breather(12*WALL_THICKNESS, 4 * WALL_THICKNESS, rotation_degrees_ccw=0)
    room_name.build_fire_breather(18*WALL_THICKNESS, 4 * WALL_THICKNESS, rotation_degrees_ccw=0)

    room_name.build_fire_breather(26*WALL_THICKNESS, 7 * WALL_THICKNESS, rotation_degrees_ccw=270, proj_max_height=4* WALL_THICKNESS)
    room_name.build_fire_breather(31*WALL_THICKNESS, 9 * WALL_THICKNESS, rotation_degrees_ccw=90, proj_max_height=4* WALL_THICKNESS)

    room_name.build_fire_breather(26*WALL_THICKNESS, 14 * WALL_THICKNESS, rotation_degrees_ccw=270, proj_max_height=4* WALL_THICKNESS)

    room_name.build_fire_breather(25*WALL_THICKNESS, 15 * WALL_THICKNESS, rotation_degrees_ccw=180, proj_max_height=3* WALL_THICKNESS)

    room_name.build_fire_breather(18*WALL_THICKNESS, 11 * WALL_THICKNESS, rotation_degrees_ccw=180, proj_max_height=4* WALL_THICKNESS)

    room_name.build_fire_breather(13*WALL_THICKNESS, 9 * WALL_THICKNESS, rotation_degrees_ccw=0)
    room_name.build_fire_breather(11*WALL_THICKNESS, 5 * WALL_THICKNESS, rotation_degrees_ccw=180)

    room_name.build_fire_breather(6*WALL_THICKNESS, 5 * WALL_THICKNESS, rotation_degrees_ccw=180)

    room_name.build_fire_breather(4*WALL_THICKNESS,13 * WALL_THICKNESS, rotation_degrees_ccw=90)


    arrow_spitter1 = room_name.build_arrow_spitter(31*WALL_THICKNESS, 2* WALL_THICKNESS, rotation_degrees_ccw=90)
    trigger1 = room_name.build_trigger(19*WALL_THICKNESS, 2 * WALL_THICKNESS)
    trigger1.set_linked_trap(arrow_spitter1)
    arrow_spitter1.set_linked_trigger(trigger1)

    arrow_spitter2 = room_name.build_arrow_spitter(31*WALL_THICKNESS, 15 * WALL_THICKNESS, rotation_degrees_ccw=90)
    trigger2 = room_name.build_trigger(28.5*WALL_THICKNESS, 13 * WALL_THICKNESS)
    trigger2.set_linked_trap(arrow_spitter2)
    arrow_spitter2.set_linked_trigger(trigger2)

    spitter3=room_name.build_arrow_spitter(left=17*WALL_THICKNESS, top=17*WALL_THICKNESS, rotation_degrees_ccw=270)
    spitter4=room_name.build_arrow_spitter(left=22*WALL_THICKNESS, top=9*WALL_THICKNESS, rotation_degrees_ccw=180)
    trigger4=room_name.build_trigger(22*WALL_THICKNESS, 17 * WALL_THICKNESS)
    trigger3=room_name.build_trigger(25*WALL_THICKNESS, 17* WALL_THICKNESS)

    trigger3.set_linked_trap(spitter3)
    spitter3.set_linked_trigger(trigger3)
    trigger4.set_linked_trap(spitter4)
    spitter4.set_linked_trigger(trigger4)

    trigger5 = room_name.build_trigger(left=15*WALL_THICKNESS, top=9* WALL_THICKNESS)
    spitter5 = room_name.build_arrow_spitter(left=15*WALL_THICKNESS, top=15* WALL_THICKNESS)
    trigger5.set_linked_trap(spitter5)
    spitter5.set_linked_trigger(trigger5)

    trigger6 = room_name.build_trigger(left=12*WALL_THICKNESS, top=7* WALL_THICKNESS)
    spitter6 = room_name.build_arrow_spitter(left=7*WALL_THICKNESS, top=15* WALL_THICKNESS)
    trigger6.set_linked_trap(spitter6)
    spitter6.set_linked_trigger(trigger6)

    trigger7 = room_name.build_trigger(left=2*WALL_THICKNESS,top=10 * WALL_THICKNESS)
    spitter7 = room_name.build_arrow_spitter(left=2*WALL_THICKNESS, top=5* WALL_THICKNESS, rotation_degrees_ccw=180)
    trigger7.set_linked_trap(spitter7)
    spitter7.set_linked_trigger(trigger7)

    trigger8 = room_name.build_trigger(left=2*WALL_THICKNESS,top=12 * WALL_THICKNESS)
    spitter8 = room_name.build_arrow_spitter(left=10*WALL_THICKNESS, top=14* WALL_THICKNESS, rotation_degrees_ccw=90)
    trigger8.set_linked_trap(spitter8)
    spitter8.set_linked_trigger(trigger8)
