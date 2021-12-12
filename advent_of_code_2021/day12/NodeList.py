from typing import Dict

from advent_of_code_2021.day12.Node import Node


class NodeList:
    nodes: Dict[str, Node]

    def __init__(self, nodes: Dict[str, Node]):
        self.nodes = nodes

    @property
    def start(self) -> Node:
        return self.nodes['start']

    @property
    def end(self) -> Node:
        return self.nodes['end']
