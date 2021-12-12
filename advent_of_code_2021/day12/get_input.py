from advent_of_code_2021.day12.Node import Node
from advent_of_code_2021.day12.NodeList import NodeList
from advent_of_code_2021.day12.NodeType import NodeType


def get_input(filename: str) -> NodeList:

    nodes = {}

    with open(filename) as file:
        for value in file:
            vals = value.strip().split('-')
            a = vals[0]
            b = vals[1]
            if a not in nodes:
                nodes[a] = __build_node(a)

            if b not in nodes:
                nodes[b] = __build_node(b)

            nodes[a].add_connection(nodes[b])

    return NodeList(nodes)


def __build_node(raw: str) -> Node:
    if raw == 'start':
        return Node('start', NodeType.START)
    if raw == 'end':
        return Node('end', NodeType.END)
    if raw.isupper():
        return Node(raw, NodeType.BIG)

    return Node(raw, NodeType.SMALL)
