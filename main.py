from pygame import *
from pygame.locals import *
import os
from components.constants import WINDOW, all_sprites, current_room
from components.player import PLAYER
from components.rooms import create_scotts_room, create_start_hub, create_room_two, create_tutorial_room, tutorial_room, create_bonus_room, start_hub, ice_room
from components.inventory import toggle_inventory

# init pygame, window, room
init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

background_image = image.load("components/images/test_background.png").convert()

#define background color -- remove this later
background_color = (0,0,0)

create_start_hub()

create_bonus_room()


# Room Two
create_room_two()

# Create scotts room
create_scotts_room()

# Create tutorial room
create_tutorial_room()

current_room.append(tutorial_room)
# tutorial_room.enter_room()
ice_room.enter_room()
running = True

created_you_win_text = False

while running:
    # Handles Quitting
    running = not any(event.type == QUIT for event in event.get())

    # GIVE KEYBOARD SHORTCUT to quit (hold `q` `u` `i` `t` simultaneously) or `R_ctrl` & `q`
    keys = key.get_pressed()
    if keys[K_q] and keys[K_u] and keys[K_i] and keys[K_t]:
        running = False
    elif keys[K_q] and keys[K_LCTRL]:
        running = False

    # Fill the screen with background image
    WINDOW.blit(background_image, (0,0))

    PLAYER.move()

    current_room[0].looped_updates()

    all_sprites.update()
    all_sprites.draw(WINDOW)

    toggle_inventory()

    if PLAYER.inventory["trophy"] >= 1 and not created_you_win_text:
        start_hub.build_text("YOU WON", 100, 100, (255,255,255), 90)
        created_you_win_text = True

    display.flip()

    time.Clock().tick(60)