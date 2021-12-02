from enum import Enum


def solve(filename: str):
    horizontal = depth = aim = 0

    for command, count in get_command(filename):

        if command is Command.UP:
            aim -= count
        elif command is Command.DOWN:
            aim += count
        elif command is Command.FORWARD:
            horizontal += count
            depth += aim * count

    print(f"x: {horizontal} y: {depth} total: {horizontal * depth}")


class Command(Enum):
    UP = 'up'
    DOWN = 'down'
    FORWARD = 'forward'


def get_command(filename: str):
    with open(filename) as file:
        for value in file:
            value = value.strip()

            raw_command, count = value.split(' ')

            command = Command(raw_command)

            yield command, int(count)


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
