from enum import Enum, auto
from typing import List, Dict, Set


def detect_simple_digits(raw: List[str]) -> int:
    count = 0

    for value in raw:
        if len(value) in [2,3,4,7]:
            count += 1

    return count


def decode_number(signal: List[str], number: List[str]) -> int:
    decoder = Decoder(signal)
    decoder.decode()


class Segment(Enum):
    TOP = auto
    TOP_LEFT = auto
    TOP_RIGHT = auto
    MIDDLE = auto
    BOTTOM_LEFT = auto
    BOTTOM_RIGHT = auto
    BOTTOM = auto


class Decoder:
    raw: List[str]

    one: Set[str]
    two: Set[str]
    three: Set[str]
    four: Set[str]
    five: Set[str]
    six: Set[str]
    seven: Set[str]
    eight: Set[str]
    nine: Set[str]
    zero: Set[str]

    segments: Dict[Segment, str]

    def __init__(self, signal: List[str]):
        self.raw = signal
        self.segments = {}

    def decode(self):
        for v in self.raw:
            if len(v) == 2:
                self.one = set(v)

            if len(v) == 3:
                self.seven = set(v)

            if len(v) == 4:
                self.four = set(v)

            if len(v) == 7:
                self.eight = set(v)

        # resolve top segment
        diff = self.one.symmetric_difference(self.seven)
        self.segments[Segment.TOP] = diff.pop()

        print(self.segments)
