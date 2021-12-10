import statistics
from typing import List

from advent_of_code_2021.day10.Token import Token


def score_tokens(tokens: List[Token]) -> int:
    total = 0
    for token in tokens:
        if token is Token.T_CLOSE_PAREN:
            total += 3
        elif token is Token.T_CLOSE_SQUARE:
            total += 57
        elif token is Token.T_CLOSE_BRACE:
            total += 1197
        elif token is Token.T_CLOSE_ANGLE:
            total += 25137

    return total


def score_incomplete_tokens(lines: List[List[Token]]) -> int:
    scores = []
    for tokens in lines:
        total = 0

        while len(tokens) > 0:
            total *= 5
            token = tokens.pop()
            end_token = Token.valid_end_token(token)
            if end_token is Token.T_CLOSE_PAREN:
                total += 1
            elif end_token is Token.T_CLOSE_SQUARE:
                total += 2
            elif end_token is Token.T_CLOSE_BRACE:
                total += 3
            elif end_token is Token.T_CLOSE_ANGLE:
                total += 4

        scores.append(total)

    return statistics.median(scores)
