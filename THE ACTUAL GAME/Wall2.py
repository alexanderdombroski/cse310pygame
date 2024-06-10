from pygame import *
from typing import *

class Wall(sprite.Sprite):
    def __init__(
        self, 
        color: Tuple[int, int, int], 
        left: int, 
        top: int, 
        width: int, 
        height: int, 
        groups: List[sprite.Group] = None
    ) -> None:
        
        # Add the sprites to groups
        super().__init__(*groups if groups else [])

        self.image = Surface((width, height))
        self.image.fill(Color(color))
        
        self.rect = self.image.get_rect(topleft=(left, top))
    
    def vertically_aligned(self, x_left: int, x_right: int) -> bool:
        if x_left >= self.rect.left and x_left < self.rect.right:
            return True
        elif x_right <= self.rect.right and x_right > self.rect.left:
            return True
        else:
            return False
        
    def horizontally_aligned(self, y_left: int, y_right: int) -> bool:
        if y_left >= self.rect.top and y_left < self.rect.bottom:
            return True
        elif y_right <= self.rect.bottom and y_right > self.rect.top:
            return True
        else:
            return False
    

    # Collision Detection
    def collide_left(self, x_left: int, x_right: int) -> bool:
        return x_left <= self.rect.right and x_right > self.rect.right

    def collide_right(self, x_left: int, x_right: int) -> bool:
        return x_right >= self.rect.left and x_left < self.rect.left

    def collide_top(self, y_top: int, y_bottom: int) -> bool:
        return y_top <= self.rect.bottom and y_bottom > self.rect.bottom

    def collide_bottom(self, y_top: int, y_bottom: int) -> bool:
        return y_bottom >= self.rect.top and y_top < self.rect.top