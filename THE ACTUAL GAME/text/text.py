from constants import DEFAULT_FONT_SIZE, DEFAULT_FONT_COLOR
from pygame import sprite, font
from typing import *

class Text(sprite.Sprite):
    def __init__(self, 
        text: str,
        left: int, 
        top: int,
        color: Tuple[int, int, int] = DEFAULT_FONT_COLOR,
        size: int = DEFAULT_FONT_SIZE,
        groups = None
    ) -> None:
        
        # Add to groups
        super().__init__(*groups if groups else [])

        # Configure text
        self.text = text
        self.font = font.Font("text/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf", size)
        self.color = color

        # Call Pygame Constructors
        self.position = (left, top)
        self.display()
        
    def change_text(self, new_text: str = None, new_color: Tuple[int, int, int] = None):
        self.text = new_text or self.text
        self.color = new_color or self.color
        self.display()

    def display(self):
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(topleft=self.position)
    