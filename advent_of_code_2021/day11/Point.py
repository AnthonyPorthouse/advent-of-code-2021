from __future__ import annotations
from dataclasses import dataclass
from typing import Generator


@dataclass
class Point:
    x: int
    y: int

    def get_surrounding_points(self) -> Generator[Point, None, None]:
        for x in range(self.x-1, self.x+2):
            for y in range(self.y-1, self.y+2):
                if x == self.x and y == self.y:
                    continue

                yield Point(x, y)

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f'{self.x},{self.y}'
