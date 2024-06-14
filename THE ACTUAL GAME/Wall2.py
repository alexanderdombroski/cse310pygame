from pygame import *
from typing import *

class Wall(sprite.Sprite):
    def __init__(
        self, 
        color: Tuple[int, int, int], 
        left: int, 
        top: int, 
        height: int,
        # is_horizontal: bool = True,
        # print_postion:bool = False,
        width: int, 
        groups: List[sprite.Group] = None
    ) -> None:
        
        # Add the sprites to groups
        super().__init__(*groups if groups else [])


        tile_image = image.load("images/wall_tile.png")
        tile_width, tile_height = tile_image.get_size()
        
        # Generate Image Tiles
        self.image = Surface((width, height))
        for x in range(left, width+left, tile_width):
            for y in range(top, height+top, tile_height):
                self.image.blit(tile_image, (x, y))
        
        image.save(self.image, "images/wall_tile.png")
            
        
        # Set the position
        self.rect = self.image.get_rect(topleft=(left, top))

        # if print_postion:
        #     print(f" I'm a wall with info: [top:{self.rect.top}, bottom:{self.rect.bottom}, left:{self.rect.left}, right:{self.rect.right}]")


        # self.image = Surface((width, height))
        # self.image.fill(Color(color))
        
        # self.rect = self.image.get_rect(topleft=(left, top))

    # def print_self_coordinates(self) -> None:
        # print(f"top:{self.rect.top}, bottom:{self.rect.bottom}, left:{self.rect.left}, right:{self.rect.right} ")

    
    def is_vertically_aligned(self, x_left: int, x_right: int) -> bool:
        x_midpoint = (x_left + x_right) / 2
        if x_left >= self.rect.left and x_left < self.rect.right:
            return True
        elif x_right <= self.rect.right and x_right > self.rect.left:
            return True
        elif x_midpoint >=self.rect.left and x_midpoint <=self.rect.right:
            return True
        else:
            return False

        
    def is_horizontally_aligned(self, y_left: int, y_right: int) -> bool:
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
    #   if self.rect.top <= wall.rect.bottom and self.rect.bottom > wall.rect.bottom:

    def collide_bottom(self, y_top: int, y_bottom: int) -> bool:
        return y_bottom >= self.rect.top and y_top < self.rect.top
    

    