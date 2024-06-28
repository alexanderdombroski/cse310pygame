# File that holds a list of all constants
# This is good codding practice for orginaztion and prevents circular imports
from pygame.sprite import Group
from pygame import display, NOFRAME

# Global Sprite Groups
all_sprites = Group()
all_walls = Group()
all_exits = Group()
all_ice = Group()
all_mud = Group()
all_spikes = Group()
all_text = Group()
all_collectables = Group()
all_triggers = Group()
all_arrow_spitters = Group()
all_attacks = Group()

# Constants
SCREEN_WIDTH = 1050 + 70
SCREEN_HEIGHT = 630 + 70
WALL_THICKNESS = 35

PLAYER_SPEED = 5

DEFAULT_FONT_SIZE = 32
DEFAULT_FONT_COLOR = (255, 255, 255)


# Pointers
current_room = [] # Theres no pointers in python, so were using a list lol


WINDOW = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), NOFRAME)
