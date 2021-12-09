from typing import Dict, List, Set, Optional

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
            if point in checked:
                continue

            lowest_neighbour = True
            for adj_point in point.get_adjacent_points():
                if adj_point not in self.values:
                    continue

                if val >= self.values.get(adj_point):
                    lowest_neighbour = False
                    break

            checked.add(point)

            if lowest_neighbour:
                [checked.add(p) for p in point.get_adjacent_points()]
                lowest.append(point)

        return lowest

    def get_risk(self, point: Point) -> int:
        return self.values[point] + 1

    @property
    def values(self) -> Dict[Point, int]:
        return self._values

    def find_basins(self) -> List[Set[Point]]:
        return [basin for basin in [self.find_basin(low_point) for low_point in self.find_lowest_points()]]

    def find_basin(self, point: Point, checked: Set[Point] = None) -> Set[Point]:
        if checked is None:
            checked = set()

        checked.add(point)

        for adjacent in point.get_adjacent_points():
            if adjacent in checked:
                continue

            if adjacent in self.values and self.values.get(adjacent) < 9:
                checked.union(self.find_basin(adjacent, checked))

        return checked
