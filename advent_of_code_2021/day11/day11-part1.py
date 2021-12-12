from advent_of_code_2021.day11.Board import Board


def solve(filename: str) -> None:
    board = Board(filename)
    print(board)

    total_flashes = 0
    for i in range(100):
        print(f'tick: {i + 1}')
        total_flashes += board.tick()
        print(board)

    print(f'total flashes: {total_flashes}')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
