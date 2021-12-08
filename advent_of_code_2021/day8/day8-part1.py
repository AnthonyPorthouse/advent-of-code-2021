from advent_of_code_2021.day8.decoder import detect_simple_digits
from advent_of_code_2021.day8.get_input import get_input


def solve(filename: str) -> None:
    total_simple_numbers = 0
    for _, output in get_input(filename):
        total_simple_numbers += detect_simple_digits(output)

    print(f'Detected {total_simple_numbers} instances of 2, 4, 7, 8')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
