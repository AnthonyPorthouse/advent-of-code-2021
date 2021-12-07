import math

from advent_of_code_2021.day7.get_input import get_input


def solve(filename: str) -> None:
    positions = {}
    for val in get_input(filename):
        if val in positions:
            positions[val] += 1
        else:
            positions[val] = 1

    min_pos = min(positions.keys())
    max_pos = max(positions.keys())

    best_pos = 0
    best_fuel = math.inf

    for target_pos in range(min_pos, max_pos + 1):
        fuel_use = 0
        for pos, count in positions.items():
            distance = abs(pos - target_pos)
            if distance == 0:
                continue
            current_fuel_use = int((distance * (distance + 1)) / 2) * count
            fuel_use += current_fuel_use

        print(f'space {target_pos} fuel use {fuel_use}')
        if fuel_use < best_fuel:
            best_pos = target_pos
            best_fuel = fuel_use

    print(f'Most efficient space is {best_pos} using {best_fuel} fuel')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
