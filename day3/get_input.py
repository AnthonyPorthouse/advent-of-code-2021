from typing import Generator, List


def get_input(filename: str) -> Generator[List[bool], None, None]:
    with open(filename) as file:
        for value in file:
            value = value.strip()

            output = []

            for char in value:
                if char == '1':
                    output.append(True)
                else:
                    output.append(False)

            yield output
