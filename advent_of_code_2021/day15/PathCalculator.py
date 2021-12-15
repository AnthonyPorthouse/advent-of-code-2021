from typing import List, Optional

from advent_of_code_2021.day15.Node import Node
from advent_of_code_2021.day15.NodeList import NodeList

class PathCalculator:
    nodes: NodeList
    start: Node
    end: Node

    def __init__(self, nodes: NodeList, start: Node, end: Node):
        self.nodes = nodes
        self.start = start
        self.end = end

    def find_paths(self, node: Node, current_steps: Optional[List[Node]] = None) -> List[List[Node]]:
        routes = []

        if current_steps is None:
            current_steps = [node]
        else:
            current_steps.append(node)

        for next_node in node.connections:
            if next_node.point is self.end:
                next_steps = current_steps.copy()
                next_steps.append(next_node)
                routes.append(next_steps)
                continue

            results = self.find_paths(next_node, current_steps.copy())

            for result in results:
                routes.append(result)

        return routes
