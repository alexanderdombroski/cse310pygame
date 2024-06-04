from typing import * # Used for fixed typing
from pygame import *
from pygame.locals import *
from sprite_groups import all_walls

class Square(sprite.Sprite):
    def __init__(
        self, 
        start_x: int, 
        start_y: int, 
        groups: List[sprite.Group] = None
    ) -> None:
        
        super().__init__(*groups if groups else [])
        
        self.width = 35
        self.color = (100, 200, 0)
        self.facing = "right"
        self.speed = 5

        self.image = Surface((self.width,self.width))
        self.image.fill(self.color)

        # Center the square in the screen
        self.rect = self.image.get_rect(center=(start_x, start_y))

        self.collisions = {
            "left": False,
            "top": False,
            "right": False,
            "bottom": False
        }

    def print_direction(self) -> None:
        print(self.facing)

    def change_color(self, new_color: Tuple[int, int, int]) -> None:
        self.image.fill(new_color)

    def update_collisions(self, walls: sprite.Group) -> None:
        self.collisions = {
            "left": False,
            "top": False,
            "right": False,
            "bottom": False
        }

        for wall in walls:
            if self.rect.colliderect(wall.rect): # Nesting this if statement prevents unnessessary checks
                if self.rect.left <= wall.rect.right and self.rect.right > wall.rect.right:
                    self.collisions["left"] = True
                if self.rect.top <= wall.rect.bottom and self.rect.bottom > wall.rect.bottom:
                    self.collisions["top"] = True
                if self.rect.right >= wall.rect.left and self.rect.left < wall.rect.left:
                    self.collisions["right"] = True
                if self.rect.bottom >= wall.rect.top and self.rect.top < wall.rect.top:
                    self.collisions["bottom"] = True

    def move(self) -> None:
        keys = key.get_pressed()
        self.update_collisions(all_walls)
        if (keys[K_w] or keys[K_UP]) and not self.collisions["top"]:
            self.rect.y -= self.speed
            self.facing = "top"
        if (keys[K_s] or keys[K_DOWN]) and not self.collisions["bottom"]:
            self.rect.y += self.speed
            self.facing = "bottom"
        if (keys[K_a] or keys[K_LEFT]) and not self.collisions["left"]:
            self.rect.x -= self.speed
            self.facing = "left"
        if (keys[K_d] or keys[K_RIGHT]) and not self.collisions["right"]:
            self.rect.x += self.speed
            self.facing = "right"