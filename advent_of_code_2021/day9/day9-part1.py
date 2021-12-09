from advent_of_code_2021.day9.Heightmap import Heightmap
from advent_of_code_2021.day9.get_input import get_input


def solve(filename: str) -> None:
    raw = [list(line) for line in get_input(filename)]
    heightmap = Heightmap(raw)

    lowest_points = heightmap.find_lowest_points()
    print(lowest_points)

    total_risk = sum([risk for risk in [heightmap.get_risk(point) for point in lowest_points]])
    print(f'total risk: {total_risk}')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
