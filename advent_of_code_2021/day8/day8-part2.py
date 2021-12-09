from advent_of_code_2021.day8.decoder import detect_simple_digits, decode_number
from advent_of_code_2021.day8.get_input import get_input


def solve(filename: str) -> None:
    total = 0
    for signal, output in get_input(filename):
        number = decode_number(signal, output)
        print(f'decoded: {number}')
        total += number

    print(f'total: {total}')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
