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

        self.png = image.load("components/images/arrow.png").convert_alpha()

        self.image = Surface((width, height))

        self.attack_groups = attack_groups
        self.rotation_degrees_ccw = rotation_degrees_ccw

        self.normal_color = Color(color)
        self.second_color = second_color

        self.draw_image(self.normal_color)

        self.rect = self.image.get_rect(topleft=(left, top))
        
        self.last_fire_time = 0
        self.delta_time = 0

        self.fade_time = 1

        self.lazer_sound = mixer.Sound("components/sounds/lazer-cannon.mp3")

        # self.latest_projectile=True
        self.cooldown = 2
        # self.pattern=1
        self.pattern=1
        self.attack_count=0
        self.long_cd =2
        self.proj_h = proj_h

    def draw_image(self, color):
        self.image.fill(color)
        self.image.blit(self.png, (0,0))
        if self.rotation_degrees_ccw != 0:
            self.image = transform.rotate(self.image, self.rotation_degrees_ccw)

    def spit_arrow(self, attack_groups):
        left_param = self.rect.x
        top_param=self.rect.y

        if self.rotation_degrees_ccw == 180:
            top_param = self.rect.bottom
        elif self.rotation_degrees_ccw == 270:
            left_param = self.rect.right

        self.latest_projectile = Fire(left=left_param, top=top_param, groups = attack_groups, speed=7, lifespan=.75, rotation_degrees_ccw=self.rotation_degrees_ccw, max_height=self.proj_h)

        self.draw_image(self.second_color)
        self.last_fire_time = time.time()

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

