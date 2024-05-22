import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Move the Red Square')

# Square properties
SQUARE_SIZE = 50
square_x = SCREEN_WIDTH // 2
square_y = SCREEN_HEIGHT // 2
SQUARE_SPEED = 5

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys pressed
    keys = pygame.key.get_pressed()
    
    # Update square position based on key press
    if keys[pygame.K_LEFT]:
        square_x -= SQUARE_SPEED
    if keys[pygame.K_RIGHT]:
        square_x += SQUARE_SPEED
    if keys[pygame.K_UP]:
        square_y -= SQUARE_SPEED
    if keys[pygame.K_DOWN]:
        square_y += SQUARE_SPEED
    
    # Ensure the square stays within bounds of the screen
    square_x = max(0, min(square_x, SCREEN_WIDTH - SQUARE_SIZE))
    square_y = max(0, min(square_y, SCREEN_HEIGHT - SQUARE_SIZE))
    
    # Fill the screen with BLACK
    screen.fill(BLACK)
    
    # Draw the RED square
    pygame.draw.rect(screen, RED, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()