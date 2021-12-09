from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int

    def get_adjacent_points(self) -> List[Point]:
        return [
            Point(self.x - 1, self.y),
            Point(self.x, self.y - 1),
            Point(self.x + 1, self.y),
            Point(self.x, self.y + 1),
        ]

    def __eq__(self, other: Point):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'{self.x},{self.y}'

    def __hash__(self):
        return hash(f'{self.x},{self.y}')
