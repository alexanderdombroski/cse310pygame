from pygame import *
from pygame.locals import *
import os
from constants import all_sprites, SCREEN_HEIGHT, SCREEN_WIDTH, WALL_THICKNESS, current_room, all_spikes
from room import Room
from passage import Exit
from player import PLAYER
from rooms import create_scotts_room, create_start_room, create_room_two, create_tutorial_room, start_room, tutorial_room
from attack import Projectile

# init pygame, window, room
init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), NOFRAME)
background_image = image.load("THE ACTUAL GAME/images/test_background.png").convert()

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

frozen_state = False

while running:   
    
    # Handles Quitting
    # running = not any(event.type == QUIT for event in event.get())
    # frozen_state = not any (event.type == KEYDOWN for event in event.get()) and not any (event.key == K_SPACE for event in event.get())

    for evan in event.get():
        if evan.type == QUIT:
            quit()

        if evan.type == KEYDOWN:
            if evan.key == K_SPACE:
                frozen_state = not frozen_state
                # print(frozen_state)

    #GIVE KEYBOARD SHORTCUT to quit (hold `q` `u` `i` `t` simultaneously) or `R_ctrl` & `q`
    keys = key.get_pressed()
    if keys[K_q] and keys[K_u] and keys[K_i] and keys[K_t]:
        running = False
    elif keys[K_q] and keys[K_LCTRL]:
        running = False
        


    if not frozen_state:
        # Fill the screen with background image
        window.blit(background_image, (0,0))

        PLAYER.move()

        all_sprites.update()
        all_sprites.draw(window)

        display.flip()


            

        time.Clock().tick(60)        


    # # Handles Quitting
    # running = not any(event.type == QUIT for event in event.get())

    # #GIVE KEYBOARD SHORTCUT to quit (hold `q` `u` `i` `t` simultaneously) or `R_ctrl` & `q`
    # for event in event.get():

    #     keys = key.get_pressed()
    #     if keys[K_q] and keys[K_u] and keys[K_i] and keys[K_t]:
    #         running = False
    #     elif keys[K_q] and keys[K_LCTRL]:
    #         running = False
    #         if event.type == KEYDOWN:
    #             if event.key == K_SPACE:
    #                 frozen_state = not frozen_state
    #                 print(frozen_state)

    # if not frozen_state: