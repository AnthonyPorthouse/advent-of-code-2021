import functools

from advent_of_code_2021.day9.Heightmap import Heightmap
from advent_of_code_2021.day9.get_input import get_input


def solve(filename: str) -> None:
    raw = [list(line) for line in get_input(filename)]
    heightmap = Heightmap(raw)

    lowest_points = heightmap.find_lowest_points()
    print(lowest_points)

    basins = heightmap.find_basins()
    basins.sort(key=len, reverse=True)

    total = functools.reduce(lambda x, y: x * y, map(len, basins[:3]))

    print(f'Largest Basin total: {total}')

if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
