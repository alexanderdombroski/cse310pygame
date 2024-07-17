from pygame import *
import pygame as pyg
from typing import *
from components.constants import WALL_THICKNESS, all_attacks
from components.trigger import Trigger
from components.attack import Fire
import time
# from room import Room

class Fire_Breather(sprite.Sprite):
    def __init__(
        self, 
        left: int, 
        top: int, 
        width: int = WALL_THICKNESS, 
        height: int = WALL_THICKNESS, 
        color: Tuple[int, int, int] = (0,0,225), 
        second_color: Tuple[int, int, int] = (255,0,255),
        groups: List[sprite.Group] = None, 
        attack_groups: List[sprite.Group] = None,
        rotation_degrees_ccw:int = 0, # 0:up, 90:left, 180:down, 270:right
        proj_h:int = 3 * 35,

    ) -> None:
        
        super().__init__(*groups if groups else [])

        # Load an image file named "arrow.png" located in the "components/images" directory,
        # convert it for optimal display, and enable per-pixel transparency.
        self.png = image.load("components/images/arrow.png").convert_alpha()

        # Create a new Surface for this sprite
        self.image = Surface((width, height))

        self.attack_groups = attack_groups
        self.rotation_degrees_ccw = rotation_degrees_ccw

        self.normal_color = Color(color)
        self.second_color = second_color

        # Draw the initial image with the normal color
        self.draw_image(self.normal_color)

        # Define the position and size of the sprite
        self.rect = self.image.get_rect(topleft=(left, top))
        
        self.last_fire_time = 0
        self.delta_time = 0

        self.fade_time = 1

        # Load the sound effect for the laser cannon
        self.lazer_sound = mixer.Sound("components/sounds/lazer-cannon.mp3")

        # Set the cooldown period for firing
        self.cooldown = 2
        
        self.pattern=1
        self.attack_count=0
        self.long_cd =2
        self.proj_h = proj_h

    def draw_image(self, color):
        # Fill the sprite's surface with the given color and draw the arrow image
        self.image.fill(color)
        self.image.blit(self.png, (0,0))
        if self.rotation_degrees_ccw != 0:
            self.image = transform.rotate(self.image, self.rotation_degrees_ccw)

    def spit_arrow(self, attack_groups):
        left_param = self.rect.x
        top_param=self.rect.y

        # Adjust the starting position of the projectile based on the rotation
        if self.rotation_degrees_ccw == 180:
            top_param = self.rect.bottom
        elif self.rotation_degrees_ccw == 270:
            left_param = self.rect.right

        # Create a new projectile (Fire) instance
        self.latest_projectile = Fire(left=left_param, top=top_param, groups = attack_groups, speed=7, lifespan=.75, rotation_degrees_ccw=self.rotation_degrees_ccw, max_height=self.proj_h)

        # Change the sprite's color to indicate it has fired
        self.draw_image(self.second_color)
        self.last_fire_time = time.time()

        # Play the laser sound effect
        # self.lazer_sound.play()
    
    def update(self):
        if self.pattern==1:
            self.delta_time = time.time() - self.last_fire_time
            if self.delta_time > self.cooldown:
                self.spit_arrow(self.attack_groups)
            
            progress = 1 - (self.delta_time / self.fade_time)
            r_value = int(255 * progress)

            if r_value >= 0:
                if r_value > 255:
                    r_value = 255
                self.draw_image((r_value, 0, 225))
