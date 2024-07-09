from components.collectable import COLLECTABLE_DATA
from components.player import PLAYER
from components.text.text import Text
from pygame import Surface, SRCALPHA, key, K_e, image
from components.constants import WINDOW, SCREEN_HEIGHT, SCREEN_WIDTH
from datetime import datetime, timedelta

inventory_surface = Surface((800, 400), SRCALPHA)
showing = False
toggle_time = datetime.now()
DELAY_TIME = timedelta(seconds=0.25)


def toggle_inventory():
    global showing, toggle_time
    keys = key.get_pressed()
    if keys[K_e] and datetime.now() - toggle_time > DELAY_TIME:
        toggle_time = datetime.now()
        showing = not showing
    if showing:
        render_inventory()
        WINDOW.blit(inventory_surface, (SCREEN_WIDTH // 2 - 400, SCREEN_HEIGHT // 2 - 200))
        

def render_inventory():
    inventory_surface.fill((50, 50, 50, 240))
    for i, (name, (path, _)) in enumerate(COLLECTABLE_DATA.items(), 1):
        inventory_surface.blit(image.load(path), (10, i*40))
        inventory_surface.blit(Text(name, 0, 0).image, (55, i*40))
        inventory_surface.blit(Text(f"{PLAYER.inventory[name]}", 0, 0).image, (200, i*40))