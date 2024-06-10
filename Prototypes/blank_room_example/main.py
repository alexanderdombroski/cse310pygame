from pygame import *
from pygame.locals import *
from constants import all_sprites, SCREEN_HEIGHT, SCREEN_WIDTH, WALL_THICKNESS, current_room
from room import Room
from passage import Exit
from Square import PLAYER

# init pygame, window, room
init()

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#define background color -- remove this later
background_color = (0,0,0)

# Room One
start_room = Room(default_wall_color=(128, 128, 128))
start_room.build_border()
start_room.build_wall(500, 300, 30, 60) # pillar

# Ice Test
start_room.build_ice(100, 100, 100, 100)
start_room.build_mud(200, 100, 100, 100)

# Room Two
room2 = Room(default_wall_color=(128, 0, 228))
room2.build_border()
start_room.build_passage(Exit, room2, SCREEN_WIDTH - WALL_THICKNESS * 2, SCREEN_HEIGHT / 2)
room2.build_passage(Exit, start_room, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Room 3 (scotts_room)
scotts_room = Room(SCREEN_WIDTH - WALL_THICKNESS * 2, SCREEN_HEIGHT - WALL_THICKNESS * 2, (190, 0, 0))
scotts_room.build_border()
scotts_room.build_passage(Exit, start_room,  1.66 * WALL_THICKNESS, SCREEN_HEIGHT - 2 * WALL_THICKNESS)
start_room.build_passage(Exit, scotts_room, SCREEN_WIDTH // 2 - WALL_THICKNESS // 2, WALL_THICKNESS)
# X, Y, Width, Height
for i in range(3, 33, 2):
    thickness_factor = 1 if i % 4 == 1 else 2
    scotts_room.build_wall(SCREEN_WIDTH - WALL_THICKNESS * i, WALL_THICKNESS * thickness_factor, WALL_THICKNESS, SCREEN_HEIGHT - (3 - thickness_factor) * WALL_THICKNESS)

current_room.append(start_room)
start_room.enter_room()
running = True

while running:   
    
    # Handles Quitting
    running = not any(event.type == QUIT for event in event.get())


    # Fill the screen with black
    window.fill(background_color)

    PLAYER.move()

    all_sprites.draw(window)

    #once sprites has a .png, change to blit
    display.flip()

    time.Clock().tick(60)        

