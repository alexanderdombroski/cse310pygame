from pygame import *
from pygame.locals import *
from sprite_groups import all_walls, all_sprites
from room import Room

# init pygame, window, room
init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


WALL_THICKNESS = 35
start_room = Room(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, all_walls, (128, 128, 128))
start_room.build_wall(0, 0, height=SCREEN_HEIGHT) # Left
start_room.build_wall(0, 0, width=SCREEN_WIDTH) # Top
start_room.build_wall(SCREEN_WIDTH - WALL_THICKNESS, 0, height=SCREEN_HEIGHT) # Right
start_room.build_wall(0, SCREEN_HEIGHT - WALL_THICKNESS, width=SCREEN_WIDTH) # Bottom
start_room.build_wall(500, 300, 30, 60) # pillar


#define background color -- remove this later
background_color = (0,0,0)


running = True

while running:   
    
    # Handles Quitting
    running = not any(event.type == QUIT for event in event.get())


    # Fill the screen with black
    window.fill(background_color)

    start_room.update_player_movement()

    all_sprites.draw(window)

    display.flip()

    time.Clock().tick(60)        

