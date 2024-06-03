import pygame
from pygame.locals import *
from Square import *
from Wall2 import *
from sprite_groups import all_walls, all_sprites

# init pygame, window, square1
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_character = Square(SCREEN_WIDTH, SCREEN_HEIGHT)

WALL_THICKNESS = 35
wall_groups = [all_sprites, all_walls] # list of sprite group refereces
left_wall = Wall((128, 128, 128), 0, 0, WALL_THICKNESS, SCREEN_HEIGHT, wall_groups)
top_wall = Wall((128, 128, 128), 0, 0, SCREEN_WIDTH, WALL_THICKNESS, wall_groups)
right_wall = Wall((128, 128, 128), SCREEN_WIDTH - WALL_THICKNESS, 0, WALL_THICKNESS, SCREEN_HEIGHT, wall_groups)
bottom_wall = Wall((128, 128, 128), 0, SCREEN_HEIGHT - WALL_THICKNESS, SCREEN_WIDTH, WALL_THICKNESS, wall_groups)

exit = False


#define background color -- remove this later
background_color = (0,0,0)



while not exit:
    
    # Reset collision bools
    left_collide = False
    top_collide = False
    right_collide = False
    bottom_collide = False

    if player_character.rect.colliderect(left_wall.rect):
        left_collide = True
    if player_character.rect.colliderect(top_wall.rect):
        top_collide = True
    if player_character.rect.colliderect(right_wall.rect):
        right_collide = True
    if player_character.rect.colliderect(bottom_wall.rect):
        bottom_collide = True

   

    #handles quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True


    keys = pygame.key.get_pressed()

    #moves the player
    if keys[pygame.K_w] and not top_collide:
        player_character.rect.y -= player_character.speed
        player_character.facing = "top"
        if keys[pygame.K_a]:
            player_character.facing = "left"
        if keys[pygame.K_d]:
            player_character.facing = "right"

    if keys[pygame.K_a] and not left_collide:
        player_character.rect.x -= player_character.speed
        player_character.facing = "left"

    if keys[pygame.K_s] and not bottom_collide:
        player_character.rect.y += player_character.speed
        player_character.facing = "bottom"
        if keys[pygame.K_a]:
            player_character.facing = "left"
        if keys[pygame.K_d]:
            player_character.facing = "right"

    if keys[pygame.K_d] and not right_collide:
        player_character.rect.x += player_character.speed
        player_character.facing = "right"



    # Fill the screen with black
    window.fill(background_color)

    all_sprites.draw(window)
   
    pygame.display.flip()

    pygame.time.Clock().tick(60)        

        


    

