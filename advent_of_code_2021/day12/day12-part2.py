from advent_of_code_2021.day12.PathCalculator import PathCalculator
from advent_of_code_2021.day12.get_input import get_input


def solve(filename: str) -> None:
    nodes = get_input(filename)

    calculator = PathCalculator(nodes)
    routes = calculator.find_paths_with_backtracking(nodes.start)

    # print(routes)
    print(f'Route Count: {len(routes)}')


if __name__ == '__main__':
    solve('example1.txt')
    solve('example2.txt')
    solve('example3.txt')
    solve('input.txt')
