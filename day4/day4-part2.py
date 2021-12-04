from day4.get_input import get_numbers, get_boards


def solve(filename: str) -> None:
    boards = []
    for board in get_boards(filename):
        boards.append(board)

    print(boards)

    called = []
    for num in get_numbers(filename):
        called.append(num)

        print(f"Calling {num}")

        for index, board in enumerate(boards):
            if board.is_solved(called):
                if len(boards) > 1:
                    boards.remove(board)
                else:
                    print(f'Losing board finally won, score: {boards[0].get_score(called, num)}')
                    return

        print(f'Not found the losing board yet')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
