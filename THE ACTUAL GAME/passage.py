from pygame import *
from typing import *
from constants import WALL_THICKNESS
from player import PLAYER

class Exit(sprite.Sprite):
    def __init__(
        self, 
        destination, # Needs to be a room, but cannot specify cause circular imports :(
        left: int, 
        top: int,
        direction: str = "u", # Left means you enter from the left (it is facing left).
        width: int = WALL_THICKNESS,
        color: Tuple[int, int, int] = (0, 0, 0),
        locked: bool = False
    ) -> None:
        super().__init__()

        self.image = Surface((width, width), SRCALPHA)
        
        self.rect = self.image.get_rect(topleft=(left, top))
        self.destination = destination

        self.locked = locked

        tile_image = image.load("THE ACTUAL GAME/images/locked.png" if locked else "THE ACTUAL GAME/images/gate.png")

        if direction == "l":
            tile_image = transform.rotate(tile_image, 90)
        elif direction == "d":
            tile_image = transform.rotate(tile_image, 180)
        elif direction == "r":
            tile_image = transform.rotate(tile_image, 270)
        
        self.image.blit(tile_image, (0, 0))

        # Sounds
        self.unlock_sound = mixer.Sound("THE ACTUAL GAME/sounds/unlock-door.mp3")
        
    def change_room(self) -> None:
        if self.locked:
            if (PLAYER.inventory["key"]):
                self.unlock()
                self.destination.enter_room()
        else:
            self.destination.enter_room()

    def unlock(self) -> None:
        self.image.blit(image.load("THE ACTUAL GAME/images/gate.png"), (0, 0))
        self.unlock_sound.play()
        self.locked = False
        PLAYER.inventory["key"] -= 1




# class Switch



# class Door(Exit):
#     pass

# class Ladder(Exit):
#     pass