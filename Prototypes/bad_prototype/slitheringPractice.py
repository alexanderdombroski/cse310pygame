import pygame
from pygame.locals import *
from Square import *
from Impassable import *

# init pygame, window, square1
pygame.init()
window = pygame.display.set_mode((1100, 500))
square1 = Square()
wall1 = Impassable()


# Create a sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(square1)


#define colors
background_color = (0,0,0)
rect_color = (0, 255, 0)

#define exit condition
exit = False

while not exit:

    #handles events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    # Update the position of the square
    all_sprites.update()

    # Fill the screen with black
    window.fill(background_color)

    #draw square1
    all_sprites.draw(window)
   
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.Clock().tick(60)        

        


    

