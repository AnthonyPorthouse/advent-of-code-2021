from advent_of_code_2021.day10.Token import Token
from advent_of_code_2021.day10.TokenScorer import score_tokens, score_incomplete_tokens
from advent_of_code_2021.day10.get_input import get_input


def solve(filename: str):
    bad_tokens = []
    incomplete_lines = []
    for line in get_input(filename):
        tokens = []
        corrupted = False
        for t in line:
            t = Token(t)
            if t in Token.open_tokens():
                # Open token, append to stack
                tokens.append(t)
            elif t is Token.valid_end_token(tokens[-1:][0]):
                # Valid Close token, remove previous open
                tokens.pop()
            else:
                # Invalid End token, add to bad tokens list
                bad_tokens.append(t)
                corrupted = True
                break

        if not corrupted:
            incomplete_lines.append(tokens)

    print(f'Corrupted Score {score_tokens(bad_tokens)}')
    print(f'Incomplete Score {score_incomplete_tokens(incomplete_lines)}')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
