from components.collectable import COLLECTABLE_DATA
from components.player import PLAYER
from components.text.text import Text
from pygame import Surface, SRCALPHA, key, K_e, image
from components.constants import WINDOW, SCREEN_HEIGHT, SCREEN_WIDTH
from datetime import datetime, timedelta

# Create a surface for the inventory with a transparent background
inventory_surface = Surface((800, 400), SRCALPHA)
showing = False  # Inventory visibility flag
toggle_time = datetime.now()  # Last time the inventory was toggled
DELAY_TIME = timedelta(seconds=0.25)  # Delay between toggles


def toggle_inventory():
    global showing, toggle_time
    keys = key.get_pressed()  # Get the current state of all keyboard buttons
    # Check if 'E' key is pressed and the delay time has passed since the last toggle
    if keys[K_e] and datetime.now() - toggle_time > DELAY_TIME:
        toggle_time = datetime.now()  # Update the toggle time
        showing = not showing  # Toggle the visibility of the inventory
    if showing:
        render_inventory()  # Render the inventory if it is visible
        WINDOW.blit(inventory_surface, (SCREEN_WIDTH // 2 - 400, SCREEN_HEIGHT // 2 - 200))  # Display the inventory in the center of the screen


def render_inventory():
    # Fill the inventory surface with a semi-transparent dark color
    inventory_surface.fill((50, 50, 50, 240))
    # Iterate through the collectable items and render them in the inventory
    for i, (name, (path, _)) in enumerate(COLLECTABLE_DATA.items(), 1):
        inventory_surface.blit(image.load(path), (10, i*40))  # Draw the collectable image
        inventory_surface.blit(Text(name, 0, 0).image, (55, i*40))  # Draw the collectable name
        inventory_surface.blit(Text(f"{PLAYER.inventory[name]}", 0, 0).image, (200, i*40))  # Draw the quantity of the collectable item
