from typing import Generator


def get_input(filename: str) -> Generator[int, None, None]:
    with open(filename) as file:
        for num in file.readline().strip().split(','):
            yield int(num)

