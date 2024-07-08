from typing import Tuple, Callable
from components.room import Room
from datetime import datetime, timedelta

class Timed_Room(Room):
    def __init__(
        self, 
        previous_room: Room,
        room_duration: int,
        start_x: int = None, 
        start_y: int = None, 
        default_wall_color: Tuple[int, int, int] = (128, 128, 128), 
        build_border: bool = True,
        timeout_callback: Callable = None
    ) -> None:
        
        super().__init__(start_x, start_y, default_wall_color, build_border = build_border)
        self.previous_room = previous_room
        self.timeout_callback = timeout_callback
        self.room_duration = timedelta(seconds=room_duration)

    def enter_room(self) -> None:
        super().enter_room()
        self.start_time = datetime.now()

    def looped_updates(self) -> None:
        super().looped_updates()
        if datetime.now() - self.start_time > self.room_duration:
            if self.timeout_callback != None:
                self.timeout_callback()
            for spr in self.room_sprites:
                spr.kill()
            self.previous_room.enter_room()
    