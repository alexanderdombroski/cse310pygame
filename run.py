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

# Put the box's starting position at the center  of the screen.
box_x = WIDTH // 2 - box_width // 2
box_y = HEIGHT // 2 - box_height // 2

running = True

while running:
    # Fill the screen with the color white.
    screen.fill(white)

    # Recreate the box object. This allows for the x and y coordinates to 
    # change when you press the arrow keys.
    box = pygame.Rect(box_x, box_y, box_width, box_height)

    # Close the window if the user clicks the X button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gets all of the keys pressed by the user.
    keys = pygame.key.get_pressed()

    # Moves the box around the screen.
    # The box cannot go outside of the screens borders.
    if keys[pygame.K_LEFT] and box_x >= 0:
        box_x -= speed
    if keys[pygame.K_RIGHT] and box_x <= WIDTH - box_width:
        box_x += speed
    if keys[pygame.K_UP] and box_y >= 0:
        box_y -= speed
    if keys[pygame.K_DOWN] and box_y <= HEIGHT - box_height:
        box_y += speed

    # Draw the box on the screen.
    pygame.draw.rect(screen, green, box)

    # Stores the amount of time since the last time tick was called.
    time_passed = clock.tick(fps) / 1000

    # Set the speed in relation to the time passed.
    speed = time_passed * 200

    pygame.display.flip()

    