import pygame

# Screen Dimensions.
WIDTH = 800
HEIGHT = 600

# Create the game window.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set fps and clock speed.
clock = pygame.time.Clock()
fps = 60

running = True

while running:
    screen.fill((255,255,255))

    # Close the window if the user clicks the X button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Stores the amount of time since the last time tick was called.
    time_passed = clock.tick(fps) / 1000

    pygame.display.flip()

    