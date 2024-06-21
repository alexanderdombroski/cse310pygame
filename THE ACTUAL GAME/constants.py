# File that holds a list of all constants
# This is good codding practice for orginaztion and prevents circular imports
from pygame.sprite import Group

# Global Sprite Groups
all_sprites = Group()
all_walls = Group()
all_exits = Group()
all_ice = Group()
all_mud = Group()
all_spikes = Group()
all_text = Group()
all_collectables = Group()

# Constants
SCREEN_WIDTH = 1050 + 70
SCREEN_HEIGHT = 630 + 70
WALL_THICKNESS = 35

PLAYER_SPEED = 5

DEFAULT_FONT_SIZE = 32
DEFAULT_FONT_COLOR = (255, 255, 255)

COLLECTABLE_PATHS = {
    "key": "THE ACTUAL GAME/images/key.png"
}

# Pointers
current_room = [] # Theres no pointers in python, so were using a list lol