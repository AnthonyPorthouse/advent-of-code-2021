from typing import Generator

from advent_of_code_2021.day13.Point import Point


def get_points(filename: str) -> Generator[Point, None, None]:
    with open(filename) as file:
        for line in file:

            if line.strip() == '':
                return

            points = line.strip().split(',')
            yield Point(int(points[0]), int(points[1]))


def get_folds(filename: str) -> Generator[list[str], None, None]:
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line[0:11] == 'fold along ':
                fold = line[11:]
                yield fold.split('=')
