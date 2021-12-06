from __future__ import annotations
from typing import List


class School:
    fish: List[int]

    def __init__(self, state: List[int]):
        self.fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for val in state:
            self.fish[val] += 1

    def tick(self) -> None:
        fish = self.fish[:]

        fish[0], fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7], fish[8] = fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[0] + fish[7], fish[8], fish[0]

        self.fish = fish

    def count_fish(self):
        return sum(self.fish)
