from __future__ import annotations
from typing import List

from advent_of_code_2021.day15.NodeType import NodeType
from advent_of_code_2021.day15.Point import Point


class Node:
    _connections: List[Node]
    _point: Point
    _value: int

    def __init__(self, point: Point, value: int):
        self._connections = []
        self._point = point
        self._value = value

    def add_connection(self, other: Node) -> None:
        if other not in self._connections:
            self._connections.append(other)
            other.add_connection(self)

    @property
    def point(self) -> Point:
        return self._point

    @property
    def value(self) -> int:
        return self._value

    @property
    def connections(self) -> List[Node]:
        return self._connections

    def __repr__(self) -> str:
        return f'{self.point} {self.value}'
