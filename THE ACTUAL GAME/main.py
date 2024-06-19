from pygame import *
from pygame.locals import *
import os
from constants import all_sprites, SCREEN_HEIGHT, SCREEN_WIDTH, WALL_THICKNESS, current_room, all_spikes
from room import Room
from passage import Exit
from Square import PLAYER
from Rooms import create_scotts_room, create_start_room, create_room_two, create_tutorial_room, start_room, tutorial_room

# init pygame, window, room
init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), NOFRAME)
background_image = image.load("images/test_background.png").convert()

#define background color -- remove this later
background_color = (0,0,0)

create_start_room()

# Room Two
create_room_two()

#create scotts room
create_scotts_room()

#create tutorial room
create_tutorial_room()

current_room.append(tutorial_room)
tutorial_room.enter_room()
running = True

while running:   
    
    # Handles Quitting
    running = not any(event.type == QUIT for event in event.get())

    #GIVE KEYBOARD SHORTCUT to quit (hold `q` `u` `i` `t` simultaneously) or `R_ctrl` & `q`
    keys = key.get_pressed()
    if keys[K_q] and keys[K_u] and keys[K_i] and keys[K_t]:
        running = False
    elif keys[K_q] and keys[K_LCTRL]:
        running = False


    # Fill the screen with background image
    window.blit(background_image, (0,0))

    PLAYER.move()
    # PLAYER.print_self_coordinates()



    all_sprites.draw(window)

    display.flip()

    time.Clock().tick(60)        


