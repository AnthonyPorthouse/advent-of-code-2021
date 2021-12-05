from typing import Generator, Tuple

from day5.Point import Point


def get_points(filename: str) -> Generator[Tuple[Point, Point], None, None]:
    with open(filename) as file:
        for line in file:
            line = line.strip()

            point_vals = line.split(' -> ')

            a = point_vals[0].split(',')
            b = point_vals[1].split(',')

            yield Point(x=int(a[0]), y=int(a[1])), Point(x=int(b[0]), y=int(b[1]))


