import pygame

# Screen Dimensions.
WIDTH = 800
HEIGHT = 600

# Save colors as variables for easy use.
green = (34, 139, 34)
white = (255,255,255)

# Create the game window.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set fps and clock speed.
clock = pygame.time.Clock()
fps = 60

# Set box dimensions.
box_width = 20
box_height = 40
box_x = WIDTH // 2 - box_width // 2
box_y = HEIGHT // 2 - box_height // 2
box = pygame.Rect(box_x, box_y, box_width, box_height)

running = True

while running:
    # Fill the screen with the color white.
    screen.fill(white)

    # Close the window if the user clicks the X button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the box on the screen.
    pygame.draw.rect(screen, green, box)

    # Stores the amount of time since the last time tick was called.
    time_passed = clock.tick(fps) / 1000

    pygame.display.flip()

    