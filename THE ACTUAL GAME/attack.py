from pygame import *
from typing import *
import time

class Projectile(sprite.Sprite):
    def __init__(
        self, 
        left: int, 
        top: int, 
        width: int = 35, 
        height: int = 35 * 2, 
        groups: List[sprite.Group] = None,
        speed:int = 6,
        rotation_degrees_ccw : int = 0 # 0:up, 90:left, 180:down, 270:right
    ) -> None:
        
        # Add the sprites to groups
        super().__init__(*groups if groups else [])

        self.start_x = left
        self.start_y = top
        self.width = width
        self.full_height = height
        self.rotation_degrees_ccw = rotation_degrees_ccw
        self.speed = speed
        self.lifespan = 1.5

        
        self.only_once:bool = True

        if self.rotation_degrees_ccw == 0 | self.rotation_degrees_ccw == 180:
            self.image = Surface((self.width, 1))
            self.image.fill(Color((255, 0, 255)))
            self.rect = self.image.get_rect(topleft=(self.start_x, self.start_y))

        else:
            self.image = Surface((1, self.width))
            self.image.fill(Color((255, 0, 255)))
            self.rect = self.image.get_rect(topleft=(self.start_x, self.start_y))

        


        self.attack_creation_time = time.time()
        self.delta_time = 0



    def move(self):
        if self.rotation_degrees_ccw == 0:
            # if only_once:
            #     self.rect.y -= 1
            #     only_once = False

            self.rect.y -= self.speed
            self.delta_y = self.start_y - self.rect.y
            

            if self.delta_y <= self.full_height:
                self.image = transform.scale(self.image, (self.width, self.delta_y))
                self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y)) #update the rect size
                self.image.fill(Color((255, 0, 255)))

        if self.rotation_degrees_ccw == 90:
            self.rect.x -= self.speed
            self.delta_x = self.start_x - self.rect.x
            
            if self.delta_x <= self.full_height:
                self.image = transform.scale(self.image, (self.delta_x, self.width))
                self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y)) #update the rect size
                self.image.fill(Color((255, 0, 255)))

        if self.rotation_degrees_ccw == 180:
            
            self.delta_y = self.rect.bottom - self.start_y
            if self.delta_y <= self.full_height:

                self.image = transform.scale(self.image, (self.width, self.delta_y + self.speed))
                self.rect = self.image.get_rect(topleft = (self.start_x, self.start_y)) #update the rect size
                self.image.fill(Color((255, 0, 255)))
            else: 
                self.rect.y += self.speed

        if self.rotation_degrees_ccw == 270:
            self.delta_x = self.rect.right - self.start_x
            if self.delta_x + self.speed < self.full_height:

                self.image = transform.scale(self.image, (self.delta_x + self.speed, self.width))
                self.rect = self.image.get_rect(topleft = (self.start_x, self.start_y)) #update the rect size
                self.image.fill(Color((255, 0, 255)))
            else: 
                self.rect.x += self.speed
        


    def update(self):
        self.delta_time = time.time() - self.attack_creation_time # find how many seconds ago attack was created
        if self.delta_time >= self.lifespan: # check if lifespan is over
            
            self.kill() # kill sprite if lifespan over
        else:
            self.move()





# print("\n\n\n\nProjectile After Initialization:")
# print(f"top: {self.rect.top}")
# print(f"bottom: {self.rect.bottom}")
# print(f"left: {self.rect.left}")
# print(f"right: {self.rect.right}")
# print(f"x: {self.rect.x}")
# print(f"y: {self.rect.y}")