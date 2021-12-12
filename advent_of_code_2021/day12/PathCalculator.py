from typing import List, Optional

from advent_of_code_2021.day12.Node import Node
from advent_of_code_2021.day12.NodeList import NodeList
from advent_of_code_2021.day12.NodeType import NodeType


class PathCalculator:
    nodes: NodeList

    def __init__(self, nodes: NodeList):
        self.nodes = nodes

    def find_paths(self, node: Node, current_steps: Optional[List[Node]] = None) -> List[List[Node]]:
        routes = []

        if current_steps is None:
            current_steps = [node]
        else:
            current_steps.append(node)

        for next_node in node.connections:
            if next_node.type is NodeType.START:
                continue

            if next_node.type is NodeType.SMALL and next_node in current_steps:
                continue

            if next_node.type is NodeType.END:
                next_steps = current_steps.copy()
                next_steps.append(next_node)
                routes.append(next_steps)
                continue

            results = self.find_paths(next_node, current_steps.copy())

            for result in results:
                routes.append(result)

        return routes

    def find_paths_with_backtracking(self, node: Node, backtracked_node: Optional[Node] = None, current_steps: Optional[List[Node]] = None) -> List[List[Node]]:
        routes = []

        if current_steps is None:
            current_steps = [node]
        else:
            current_steps.append(node)

        for next_node in node.connections:
            if next_node.type is NodeType.START:
                continue

            if next_node.type is NodeType.SMALL and next_node in current_steps:
                if backtracked_node is not None:
                    continue
                else:
                    backtracked_node = next_node

            if next_node.type is NodeType.END:
                next_steps = current_steps.copy()
                next_steps.append(next_node)
                routes.append(next_steps)
                continue

            results = self.find_paths_with_backtracking(next_node, backtracked_node, current_steps.copy())

            for result in results:
                routes.append(result)

        return routes
