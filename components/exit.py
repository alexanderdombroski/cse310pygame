from pygame import *
from typing import *
import time
from components.constants import WALL_THICKNESS, all_sprites
from components.player import PLAYER
from components.constants import WINDOW

class Exit(sprite.Sprite):
    def __init__(
        self, 
        destination, # Needs to be a room, but cannot specify cause circular imports :(
        left: int, 
        top: int,
        direction: str = "u", # Left means you enter from the left (it is facing left).
        color: Tuple[int, int, int] = (0, 0, 0),
        locked: bool = False,
        max_entries = None
    ) -> None:
        super().__init__()

        self.image = Surface((WALL_THICKNESS, WALL_THICKNESS), SRCALPHA)
        
        self.rect = self.image.get_rect(topleft=(left, top))
        self.destination = destination

        self.locked = locked

        self.direction = direction
        self.__change_image("components/images/locked.png" if locked else "components/images/gate.png", render=False)
        
        self.max_entries = max_entries

        # Sounds
        self.unlock_sound = mixer.Sound("components/sounds/unlock-door.mp3")
        self.door_sound = mixer.Sound("components/sounds/open-door.mp3")
        
    def change_room(self) -> None:
        if self.locked:
            if (PLAYER.inventory["key"]):
                self.unlock()
        else:
            self.door_sound.play()
            self.__change_image("components/images/gate_open.png")
            time.sleep(0.5)
            self.destination.enter_room()
            self.__change_image("components/images/gate.png", render=False)
            if self.max_entries != None:
                if (self.max_entries - 1):
                    self.max_entries -= 1
                else:
                    self.kill()

    def unlock(self) -> None:
        # Unlock door
        self.__change_image("components/images/gate.png")

        self.locked = False
        PLAYER.inventory["key"] -= 1
        
        # Wait for sound to finish
        self.unlock_sound.play()
        time.sleep(1)

        # Enter Room
        self.change_room()

    def __change_image(self, path: str, render: bool = True):
        self.tile_image = image.load(path)
        if self.direction == "l":
            self.tile_image = transform.rotate(self.tile_image, 90)
        elif self.direction == "d":
            self.tile_image = transform.rotate(self.tile_image, 180)
        elif self.direction == "r":
            self.tile_image = transform.rotate(self.tile_image, 270)
        self.image.blit(self.tile_image, (0, 0))
        if render:
            all_sprites.update()
            all_sprites.draw(WINDOW)
            display.flip()
        
        