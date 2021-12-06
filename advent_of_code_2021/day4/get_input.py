from typing import Generator

from .board import Board


def get_numbers(filename: str) -> Generator[int, None, None]:
    with open(filename) as file:
        numbers = file.readline().strip()

        for number in numbers.split(','):
            yield int(number)


def get_boards(filename: str) -> Generator[Board, None, None]:
    with open(filename) as file:
        next(file)
        next(file)

        data = []
        for value in file:
            value = value.strip()
            if value == '':
                yield Board(data)
                data = []
                continue

            for num in value.replace('  ', ' ',).split(' '):
                data.append(int(num))

        yield Board(data)
