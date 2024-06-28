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
        locked: bool = False
    ) -> None:
        super().__init__()

        self.image = Surface((WALL_THICKNESS, WALL_THICKNESS), SRCALPHA)
        
        self.rect = self.image.get_rect(topleft=(left, top))
        self.destination = destination

        self.locked = locked

        tile_image = image.load("components/images/locked.png" if locked else "components/images/gate.png")

        if direction == "l":
            tile_image = transform.rotate(tile_image, 90)
        elif direction == "d":
            tile_image = transform.rotate(tile_image, 180)
        elif direction == "r":
            tile_image = transform.rotate(tile_image, 270)
        
        self.image.blit(tile_image, (0, 0))

        # Sounds
        self.unlock_sound = mixer.Sound("components/sounds/unlock-door.mp3")
        self.door_sound = mixer.Sound("components\sounds\open-door.mp3")
        
    def change_room(self) -> None:
        if self.locked:
            if (PLAYER.inventory["key"]):
                self.unlock()
        else:
            self.destination.enter_room()
            self.door_sound.play()

    def unlock(self) -> None:
        # Unlock door
        self.image.blit(image.load("components/images/gate.png"), (0, 0))
        all_sprites.update()
        all_sprites.draw(WINDOW)
        display.flip()


        self.locked = False
        PLAYER.inventory["key"] -= 1
        
        # Wait for sound to finish
        self.unlock_sound.play()
        time.sleep(1)

        # Enter Room
        self.destination.enter_room()
