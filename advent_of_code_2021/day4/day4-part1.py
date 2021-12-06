from .get_input import get_numbers, get_boards


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
                print(f'Board {index + 1} wins, score: {board.get_score(called, num)}')
                return

        print(f'No Winners Yet')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
