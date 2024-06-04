from pygame import *
from pygame.locals import *
from constants import all_sprites, SCREEN_HEIGHT, SCREEN_WIDTH, WALL_THICKNESS, current_room
from room import Room
from passage import Exit

# init pygame, window, room
init()

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#define background color -- remove this later
background_color = (0,0,0)

# Room One
start_room = Room(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, (128, 128, 128))
start_room.build_border()
start_room.build_wall(500, 300, 30, 60) # pillar

# Room Two
room2 = Room(SCREEN_WIDTH - WALL_THICKNESS * 2, SCREEN_HEIGHT / 2, (128, 0, 228))
room2.build_border()
start_room.build_passage(Exit, room2, SCREEN_WIDTH - WALL_THICKNESS * 2, SCREEN_HEIGHT / 2)
room2.build_passage(Exit, start_room, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

current_room.append(start_room)
start_room.enter_room()
running = True

while running:   
    
    # Handles Quitting
    running = not any(event.type == QUIT for event in event.get())


    # Fill the screen with black
    window.fill(background_color)

    current_room[0].update_player_movement() # The outerlist is acting like a pointer (because there are none in python)

    all_sprites.draw(window)

    display.flip()

    time.Clock().tick(60)        

