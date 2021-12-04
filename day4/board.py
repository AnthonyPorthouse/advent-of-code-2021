from typing import List


class Board:
    board_width = 5
    board_height = 5
    data: List[int]

    def __init__(self, data: List[int]):
        self.data = data

    def is_solved(self, called: List[int]) -> bool:
        # Check Rows
        for x in range(5):
            check = []
            for y in range(5):
                check.append(self.data[(x*self.board_width) + y])

            win = True
            for val in check:
                if val not in called:
                    win = False

            if win:
                return True

        # Check Columns
        for y in range(5):
            check = []
            for x in range(5):
                check.append(self.data[(y * self.board_width) + x])

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
