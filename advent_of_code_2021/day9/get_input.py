from typing import Generator, List


def get_input(filename: str) -> Generator[List[int], None, None]:
    with open(filename) as file:
        for line in file:
            yield map(int, line.strip())
