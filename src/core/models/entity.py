from dataclasses import dataclass
from typing import Tuple


@dataclass
class Entity:
    name: str
    team: str
    distance: float
    screen_x: float
    screen_y: float
    box: Tuple[int, int, int, int]
    visible: bool

    def to_dict(self) -> dict:
        return {
            "name": self.name, "team": self.team,
            "distance": self.distance,
            "screen_x": self.screen_x, "screen_y": self.screen_y,
            "box": self.box, "visible": self.visible,
        }