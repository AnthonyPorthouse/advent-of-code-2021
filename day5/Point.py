from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def is_horizontal(self, other: Point) -> bool:
        return self.y == other.y

    def is_vertical(self, other: Point) -> bool:
        return self.x == other.x

    def is_diagonal(self, other: Point) -> bool:
        return self.x != other.x and self.y != other.y

    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y
