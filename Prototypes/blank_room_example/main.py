from pygame import *
from pygame.locals import *
import os
import sys
from constants import all_sprites, SCREEN_HEIGHT, SCREEN_WIDTH, WALL_THICKNESS, current_room
from room import Room
from passage import Exit
from Square import PLAYER
from Rooms import create_scotts_room, create_start_room, start_room, scotts_room

# init pygame, window, room
init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), NOFRAME)

#define background color -- remove this later
background_color = (0,0,0)

create_start_room()

# Room Two
room2 = Room(default_wall_color=(128, 0, 228))
# room2.build_border()
start_room.build_passage(Exit, room2, SCREEN_WIDTH - WALL_THICKNESS * 2, SCREEN_HEIGHT / 2)
room2.build_passage(Exit, start_room, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

#create scotts room
create_scotts_room()

current_room.append(start_room)
start_room.enter_room()
running = True

while running:   
    
    # Handles Quitting
    running = not any(event.type == QUIT for event in event.get())

    #GIVE KEYBOARD SHORTCUT to quit (press `q` `u` `i` `t` simultaneously)
    keys = key.get_pressed()
    if keys[K_q] and keys[K_u] and keys[K_i] and keys[K_t]:
        running = False
    elif keys[K_q] and keys[K_LCTRL]:
        running = False


    # Fill the screen with black
    window.fill(background_color)

    PLAYER.move()

    all_sprites.draw(window)

    #once sprites has a .png, change to blit
    display.flip()

    time.Clock().tick(60)        

