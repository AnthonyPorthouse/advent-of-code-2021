from typing import Tuple, Dict

from advent_of_code_2021.day11.Point import Point
from advent_of_code_2021.day11.State import State
from advent_of_code_2021.day11.get_input import get_input


class Board:
    board: Dict[Point, State]

    width: int
    height: int

    def __init__(self, filename: str):
        self.board = {}
        self.width = 10
        self.height = 10

        self.__init_board(filename)

    def __init_board(self, filename: str) -> None:
        pos = 0
        for val in get_input(filename):
            x = pos % self.width
            y = int(pos / self.width)

            self.board[Point(x, y)] = State(val, False)

            pos += 1

    def tick(self) -> int:
        flashes = 0
        for pos, _ in self.board.items():
            flashes += self.increase_point(pos)

        for pos, state in self.board.items():
            state.reset()

        return flashes

    # Increase the value for a given point
    # If that point gets to be 9, then increase the value of all surrounding points
    # Finally returns the number of times a value has increased to 9
    def increase_point(self, point: Point) -> int:
        flashes = 0
        state = self.board.get(point)
        state.value += 1
        if state.value == 10:
            state.flash = True
            flashes += 1
            for p in point.get_surrounding_points():
                if p in self.board:
                    flashes += self.increase_point(p)

        return flashes

    def __repr__(self):
        out = ''
        for point, val in self.board.items():
            value = min(val.value, 10)
            out += str(value)

            if point.x == 9:
                out += '\n'

        return out
