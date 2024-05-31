import pygame
from pygame.locals import *
from Square import *
from Wall import *

# init pygame, window, square1
pygame.init()

screen_width = 1200
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))

player_character = Square(screen_width, screen_height)

wall_thickness = 35
left_wall = Wall((128, 128, 128), 0, 0, wall_thickness, screen_height)
top_wall = Wall((128, 128, 128), 0, 0, screen_width, wall_thickness)
right_wall = Wall((128, 128, 128), screen_width - wall_thickness, 0, wall_thickness, screen_height)
bottom_wall = Wall((128, 128, 128), 0, screen_height - wall_thickness, screen_width, wall_thickness)

exit = False

# Create a sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player_character)
all_sprites.add(left_wall)
all_sprites.add(top_wall)
all_sprites.add(right_wall)
all_sprites.add(bottom_wall)



#define background color -- remove this later
background_color = (0,0,0)



while not exit:
    
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

        


    

