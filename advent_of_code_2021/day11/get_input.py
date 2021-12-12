from typing import Generator


def get_input(filename: str) -> Generator[int, None, None]:
    with open(filename) as file:
        for line in file:
            for value in line.strip():
                yield int(value)
