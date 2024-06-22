from pygame import *
from typing import *
from constants import WALL_THICKNESS

class Trigger(sprite.Sprite):
    def __init__(
        self, 
        left: int, 
        top: int, 
        width: int = WALL_THICKNESS, 
        height: int = WALL_THICKNESS, 
        color: Tuple[int, int, int] = (0,255,0), 
        groups: List[sprite.Group] = None, 
        linked_trap = "",
    ) -> None:
        
        super().__init__(*groups if groups else [])

        self.image = image.load("THE ACTUAL GAME/images/button_unpressed.png")
        
        self.rect = self.image.get_rect(topleft=(left, top))

        self.linked_trap = linked_trap

        self.last_contact_bool = False
        self.current_contact_bool = False

        self.send_signal = False    

    def set_linked_trap(self, trap):
        self.linked_trap = trap

    def update(self):
        if self.current_contact_bool and not self.last_contact_bool:
            self.image = image.load("THE ACTUAL GAME/images/button_pressed.png")

        elif not self.current_contact_bool and self.last_contact_bool:
            self.image = image.load("THE ACTUAL GAME/images/button_unpressed.png")
