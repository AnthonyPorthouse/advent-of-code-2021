from advent_of_code_2021.day11.Board import Board


def solve(filename: str) -> None:
    board = Board(filename)
    print(board)

    flashes = 0
    tick = 0
    while flashes < 100:
        print(f'tick: {tick + 1}')
        flashes = board.tick()
        print(board)
        tick += 1

    print(f'Ticks to synchronise: {tick}')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
