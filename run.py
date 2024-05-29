import pygame
from Wall import Wall, BreakableWall
from globals import all_sprites, all_walls

# Screen Dimensions.
WIDTH = 800
HEIGHT = 600

FPS = 60

# Save colors as variables for easy use.
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)    



def main():
    # Create the game window.
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Set fps and clock speed.
    clock = pygame.time.Clock()


    # Set box dimensions.
    box_width = 20
    box_height = 40

    # Put the box's starting position at the center  of the screen.
    box_x = WIDTH // 2 - box_width // 2
    box_y = HEIGHT // 2 - box_height // 2

    running = True

    # Build Walls
    wall1 = Wall(100, 100, 50, 50)
    # wall2 = Wall(200, 100, 50, 50)
    # wall3 = BreakableWall(400, 300, 50, 100, 2, GREEN)

    while running:
        # Fill the screen with the color WHITE.
        screen.fill(WHITE)

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
        pygame.draw.rect(screen, GREEN, box)

        # Stores the amount of time since the last time tick was called.
        time_passed = clock.tick(FPS) / 1000

        # Set the speed in relation to the time passed.
        speed = time_passed * 200

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()

        

if __name__ == "__main__":
    main()