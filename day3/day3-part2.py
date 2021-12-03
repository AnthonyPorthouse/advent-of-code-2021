import logging
from typing import List, Tuple

from day3.get_input import get_input, get_input_numbers


def solve(filename: str) -> None:
    values = [value for value in get_input_numbers(filename)]

    position_count = len(next(get_input(filename)))

    o2 = filter_o2(position_count, values)

    print(f"o2: {o2}")

    co2 = filter_co2(position_count, values)

    print(f"co2: {co2}")

    print(f"rating: {o2 * co2}")


def filter_o2(positions: int, values: List[int]) -> int:
    for index in range(positions):
        bitmask = calculate_bitmask(positions, index)

        high_totals = 0
        low_totals = 0

        for value in values:
            if value & bitmask == bitmask:
                high_totals += 1
            else:
                low_totals += 1

        if high_totals >= low_totals:
            values = list(filter(lambda v: v & bitmask == bitmask, values))
        else:
            values = list(filter(lambda v: v & bitmask == 0, values))

        if len(values) == 1:
            return values.pop()


def filter_co2(positions: int, values: List[int]) -> int:
    for index in range(positions):
        bitmask = calculate_bitmask(positions, index)

        high_totals = 0
        low_totals = 0

        for value in values:
            if value & bitmask == bitmask:
                high_totals += 1
            else:
                low_totals += 1

        if low_totals <= high_totals:
            values = list(filter(lambda v: v & bitmask == 0, values))
        else:
            values = list(filter(lambda v: v & bitmask == bitmask, values))

        if len(values) == 1:
            return values.pop()


def calculate_bitmask(length: int, index: int) -> int:
    bit_filter = ['0' for i in range(length)]
    bit_filter[index] = '1'
    return int(''.join(bit_filter), 2)





if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
