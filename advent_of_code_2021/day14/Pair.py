from __future__ import annotations
from collections import namedtuple


class Pair(namedtuple('Pair', 'a b')):
    a: str
    b: str

    def __eq__(self, other: Pair) -> bool:
        return self.a == other.a and self.b == other.b

    def __hash__(self) -> int:
        return hash(f'{self.a}{self.b}')

    def __repr__(self) -> str:
        return f'{self.a}{self.b}'
