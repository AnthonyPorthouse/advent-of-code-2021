from typing import List


class Board:
    board_width = 5
    board_height = 5
    data: List[int]

    def __init__(self, data: List[int]):
        self.data = data

    def is_solved(self, called: List[int]) -> bool:
        if self.__check_rows(called):
            return True

        return self.__check_columns(called)

    def __check_rows(self, called: List[int]) -> bool:
        for x in range(5):
            check = []
            for y in range(5):
                x_offset = x * self.board_width
                check.append(self.data[x_offset + y])

            win = True
            for val in check:
                if val not in called:
                    win = False

            if win:
                return True

        return False

    def __check_columns(self, called: List[int]) -> bool:
        for x in range(5):
            check = []
            for y in range(5):
                y_offset = y * self.board_height
                check.append(self.data[y_offset + x])

            win = True
            for val in check:
                if val not in called:
                    win = False

            if win:
                return True

        return False

    def get_score(self, called: List[int], multiplier: int) -> int:
        remaining = []

        for val in self.data:
            if val not in called:
                remaining.append(val)

        return sum(remaining) * multiplier

    def __repr__(self) -> str:
        out = "Board Layout: \n"


        for i, val in enumerate(self.data):
            if i % 5 == 0:
                out += '\n'
            out += str(val).rjust(2) + " "

        return out.rstrip()
