from .Board import Board
from .get_input import get_points


def solve(filename: str) -> None:
    max_x = 0
    max_y = 0

    for a, b in get_points(filename):
        max_x = max(max_x, a.x, b.x)
        max_y = max(max_y, a.y, b.y)

    board = Board(max_x, max_y)

    for a, b in get_points(filename):
        board.mark_points(a, b)

    print(board)
    print(f'board size: {board.width}x{board.height}')
    print(f'Number of points above 2: {board.count_points_above(2)}')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
