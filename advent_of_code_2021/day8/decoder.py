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

    out = ''
    for val in map(set, number):
        if val == decoder.one:
            out += '1'
        elif val == decoder.two:
            out += '2'
        elif val == decoder.three:
            out += '3'
        elif val == decoder.four:
            out += '4'
        elif val == decoder.five:
            out += '5'
        elif val == decoder.six:
            out += '6'
        elif val == decoder.seven:
            out += '7'
        elif val == decoder.eight:
            out += '8'
        elif val == decoder.nine:
            out += '9'
        else:
            out += '0'
    return int(out)


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

    def __init__(self, signal: List[str]):
        self.raw = signal
        self.one = set()
        self.two = set()
        self.three = set()
        self.four = set()
        self.five = set()
        self.six = set()
        self.seven = set()
        self.eight = set()
        self.nine = set()
        self.zero = set()

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

        # 6/9/0 have 6 segments lit
        set_690 = filter(lambda v: len(v) == 6, self.raw)
        for value in set_690:

            # 6 has all but one of 1's segments
            done = False
            for pos in self.one:
                if pos not in value:
                    self.six = set(value)
                    done = True
                    break
            if done:
                continue

            # 9 is 7+4, but zero doesn't have the middle segment
            match = True
            for pos in self.seven.union(self.four):
                if pos not in value:
                    # 0 doesn't have the middle segment
                    match = False
                    break
            if match:
                self.nine = set(value)
                continue
            else:
                self.zero = set(value)
                continue

        # 2/3/5 have 5 segments lit
        set_235 = filter(lambda v: len(v) == 5, self.raw)
        for value in set_235:

            # 3 has both of 1s segments
            match = all(v in value for v in self.one)
            if match:
                self.three = set(value)
                continue

            # 5 has all but one of 6s segments
            # if it doesn't match, then its 2
            match = all(v in self.six for v in value)
            if match:
                self.five = set(value)
            else:
                self.two = set(value)

    def __repr__(self) -> str:
        return f'1: {self.one}\n' \
               f'2: {self.two}\n' \
               f'3: {self.three}\n' \
               f'4: {self.four}\n' \
               f'5: {self.five}\n' \
               f'6: {self.six}\n' \
               f'7: {self.seven}\n' \
               f'8: {self.eight}\n' \
               f'9: {self.nine}\n' \
               f'0: {self.zero}\n' \
