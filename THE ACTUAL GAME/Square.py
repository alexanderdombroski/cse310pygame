from typing import * # Used for fixed typing
from pygame import *
from constants import all_sprites, all_walls, all_exits, all_ice, all_mud, all_spikes, SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_SPEED, current_room

class Square(sprite.Sprite):
    def __init__(
        self, 
        start_x: int, 
        start_y: int, 
        groups: List[sprite.Group] = None
    ) -> None:
        
        super().__init__(*groups if groups else [])
        
        # self.width = 35
        # self.color = (100, 200, 0)
        self.facing = "right"
        self.speed = PLAYER_SPEED

        #change Surface((w, w)) to a png
        # self.image = Surface((self.width,self.width))
        # self.image.fill(self.color)
        # self.image = image.load("player_sprite_big.png")
        # self.image = image.load("entity70px.png")
        self.image = image.load("THE ACTUAL GAME/images/antler_blob.png")
        

        # Center the square in the screen
        self.rect = self.image.get_rect(center=(start_x, start_y))



        self.inventory = {
            "keys": 0
        }

    def print_direction(self) -> None:
        print(self.facing)

    def print_self_coordinates(self) -> None:
        print(f"top:{self.rect.top}, bottom:{self.rect.bottom}, left:{self.rect.left}, right:{self.rect.right} ")

    def change_color(self, new_color: Tuple[int, int, int]) -> None:
        self.image.fill(new_color)

    def update_collisions(self, walls: sprite.Group) -> None:
        for spike in all_spikes:
            if self.rect.colliderect(spike.rect):
                self.teleport(current_room[0].start_x, current_room[0].start_y)
                

        for exit in all_exits:
            if self.rect.colliderect(exit.rect):
                exit.change_room()
                return None # End the function early cause new room
        
        self.__change_speed(sprite.spritecollideany(self, all_ice), 2)
        self.__change_speed(sprite.spritecollideany(self, all_mud), 0.5)

        self.collisions = {
            "left": False,
            "top": False,
            "right": False,
            "bottom": False
        }

        for wall in walls:
            if wall.is_vertically_aligned(self.rect.left, self.rect.right):
                if self.rect.top <= wall.rect.bottom and self.rect.bottom > wall.rect.bottom:
                    self.collisions["top"] = wall.collide_top(self.rect.top, self.rect.bottom)
                if self.rect.bottom >= wall.rect.top and self.rect.top < wall.rect.top:
                    self.collisions["bottom"] = wall.collide_bottom(self.rect.top, self.rect.bottom)
            if wall.is_horizontally_aligned(self.rect.top, self.rect.bottom):    
                if self.rect.left <= wall.rect.right and self.rect.right > wall.rect.right:
                    self.collisions["left"] = wall.collide_left(self.rect.left, self.rect.right)
                if self.rect.right >= wall.rect.left and self.rect.left < wall.rect.left:
                    self.collisions["right"] = wall.collide_right(self.rect.left, self.rect.right)

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
    
    def teleport(self, x: int = None, y: int = None) -> None:
        # Allows player to teleport to a new x/y value(s) if provided
        if x != None:
            self.rect.x = x
        if y != None:
            self.rect.y = y

    def __change_speed(self, condition: bool, speed_modifier: int) -> None:
        new_speed = PLAYER_SPEED * speed_modifier
        if condition:
            self.speed = new_speed
        elif (self.speed == new_speed):
            # Leaves other speed modifiers alone
            self.speed = PLAYER_SPEED
            # Snap back to grid
            self.__snap_to_grid()
    
    def __snap_to_grid(self) -> None:
        # Align the player relative to speed
        self.teleport(
            round(self.rect.x / self.speed) * self.speed,
            round(self.rect.y / self.speed) * self.speed
        )

    

PLAYER = Square(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, all_sprites)