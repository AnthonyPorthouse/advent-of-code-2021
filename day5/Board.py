from typing import List

from day5.Point import Point


class Board:
    board: List[List[int]]

    width: int
    height: int

    def __init__(self, x: int = 5, y: int = 5):
        self.board = []
        self.width = x + 1
        self.height = y + 1

        self.__init_board()

    def __init_board(self) -> None:
        for _ in range(self.height):
            self.board.append([0 for _ in range(self.width)])

    def mark_points(self, a: Point, b: Point, include_diagonals: bool = False) -> None:
        if a == b:
            return

        if include_diagonals and a.is_diagonal(b):
            if a.x > b.x:
                b, a = a, b

            count = b.x - a.x

            if a.y < b.y:
                # diagonal down
                for i in range(count + 1):
                    self.board[a.y + i][a.x + i] += 1

            else:
                # diagonal up
                for i in range(count + 1):
                    self.board[a.y - i][a.x + i] += 1

            return

        if a.is_horizontal(b):
            if a.x > b.x:
                b, a = a, b

            for x in range(a.x, b.x + 1):
                self.board[a.y][x] += 1
            return

        if a.is_vertical(b):
            if a.y > b.y:
                b, a = a, b
            for y in range(a.y, b.y + 1):
                self.board[y][a.x] += 1
            return


    def count_points_above(self, num: int) -> int:
        total = 0

        for y in self.board:
            for x in y:
                if x >= num:
                    total += 1

        return total

    def __repr__(self) -> str:
        return '\n'.join([' '.join([str(val).rjust(2, ' ') for val in row]) for row in self.board])
