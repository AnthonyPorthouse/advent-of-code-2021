from typing import Generator, Tuple, List


def get_input(filename: str) -> Generator[Tuple[List[str], List[str]], None, None]:
    with open(filename) as file:
        for line in file:
            line = line.strip()
            parts = line.split(' | ')
            signal = parts[0].split(' ')
            output = parts[1].split(' ')

            yield signal, output
