from pygame import *
from room import Room
from abc import ABC, abstractmethod


class Exit(ABC):
    def __init__(self, destination: Room) -> None:
        self.destination = destination
    
    @abstractmethod
    def change_room() -> None:
        pass




class Door(Exit):
    pass

class Ladder(Exit):
    pass