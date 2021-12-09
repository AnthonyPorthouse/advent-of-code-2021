from typing import Dict, List

from advent_of_code_2021.day9.Point import Point


class Heightmap:
    _values: Dict[Point, int]

    def __init__(self, heightmap: List[List[int]]):
        values = {}
        for y, row in enumerate(heightmap):
            for x, height in enumerate(row):
                values[Point(x, y)] = height

        self._values = values

    def find_lowest_points(self) -> List[Point]:
        lowest = []
        checked = set()

        for point, val in self.values.items():
            print(f'checking for {point}')
            if point in checked:
                continue

            lowest_neighbour = True
            for adj_point in point.get_adjacent_points():
                if adj_point not in self.values:
                    print(f'{adj_point} not valid, skipping')
                    continue

                if val >= self.values.get(adj_point):
                    print(f'{point} >= {adj_point}, stopping checking')
                    lowest_neighbour = False
                    break

            print(f'marking {point} as checked')
            checked.add(point)

            if lowest_neighbour:
                print(f'{point} is the lowest neighbor, also marking adjacent points as checked')
                [checked.add(p) for p in point.get_adjacent_points()]
                lowest.append(point)

        return lowest

    def get_risk(self, point: Point) -> int:
        return self.values[point] + 1

    @property
    def values(self) -> Dict[Point, int]:
        return self._values
