from __future__ import annotations
from typing import List

from advent_of_code_2021.day12.NodeType import NodeType


class Node:
    _connections: List[Node]
    _name: str
    _type: NodeType

    def __init__(self, name: str, type: NodeType):
        self._connections = []
        self._name = name
        self._type = type

    def add_connection(self, other: Node) -> None:
        if other not in self._connections:
            self._connections.append(other)
            other.add_connection(self)

    @property
    def type(self) -> NodeType:
        return self._type

    @property
    def name(self) -> str:
        return self._name

    @property
    def connections(self) -> List[Node]:
        return self._connections

    def __repr__(self) -> str:
        return self._name
