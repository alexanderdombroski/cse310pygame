from pygame import *
from pygame.locals import *
import os
from components.constants import WINDOW, all_sprites, current_room
from components.player import PLAYER
from components.rooms import create_scotts_room, create_start_room, create_room_two, create_tutorial_room, start_room, tutorial_room

# init pygame, window, room
init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

background_image = image.load("components/images/test_background.png").convert()

#define background color -- remove this later
background_color = (0,0,0)

create_start_room()

# Main game sound
game_sound = mixer.Sound("components/sounds/tutorial-room-sound.mp3")
game_sound.play(loops=-1) # Makes the program loop indefinitely.

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
    WINDOW.blit(background_image, (0,0))

    PLAYER.move()

    all_sprites.update()
    all_sprites.draw(WINDOW)

    display.flip()

    time.Clock().tick(60)