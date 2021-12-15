from typing import Tuple

from advent_of_code_2021.day14.Pair import Pair


class Rule:
    _pair: str
    _insert: str

    def __init__(self, pair: str, insert: str):
        self._pair = pair
        self._insert = insert

    @property
    def pair(self) -> str:
        return self._pair

    @property
    def insert(self) -> str:
        return self._insert

    @property
    def pair_as_pair(self) -> Pair:
        return Pair(self.pair[0], self.pair[1])

    @property
    def new_pairs(self) -> Tuple[Pair, Pair]:
        return Pair(self.pair[0], self.insert), Pair(self.insert, self.pair[1])

    @property
    def new_value(self) -> str:
        return f'{self.pair[0]}{self.insert}{self.pair[1]}'

    def __repr__(self) -> str:
        return f'{self.pair} -> {self.insert}'
