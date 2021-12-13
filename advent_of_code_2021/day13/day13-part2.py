from advent_of_code_2021.day13.Board import Board
from advent_of_code_2021.day13.get_input import get_folds


def solve(filename: str) -> None:
    board = Board(filename)

    for fold in get_folds(filename):
        if fold[0] == 'x':
            board.fold_at_x(int(fold[1]))
        else:
            board.fold_at_y(int(fold[1]))

    print(board)
    print(f'Points on board: {len(board.board)}')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
