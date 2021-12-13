from typing import Set

from advent_of_code_2021.day13.Point import Point
from advent_of_code_2021.day13.get_input import get_points


class Board:
    board: Set[Point]

    width: int
    height: int

    def __init__(self, filename: str):
        self.board = set()
        self.width, self.height = 0, 0

        self.__init_board(filename)

    def __init_board(self, filename: str) -> None:
        for point in get_points(filename):
            self.width = max(self.width, point.x)
            self.height = max(self.height, point.y)

            self.board.add(point)

    def fold_at_y(self, y: int) -> None:
        self.height = y - 1

        new_board = set()

        for point in self.board:
            if point.y > y:
                new_y = y - (point.y - y)
                new_board.add(Point(point.x, new_y))
            else:
                new_board.add(point)

        self.board = new_board

    def fold_at_x(self, x: int) -> None:
        self.width = x - 1

        new_board = set()

        for point in self.board:
            if point.x > x:
                new_x = x - (point.x - x)
                new_board.add(Point(new_x, point.y))
            else:
                new_board.add(point)

        self.board = new_board

    def __repr__(self) -> str:
        out = ''
        for y in range(self.height + 1):
            for x in range(self.width + 1):
                point = Point(x, y)
                if point in self.board:
                    out += '#'
                else:
                    out += '.'

            out += '\n'
        return out
