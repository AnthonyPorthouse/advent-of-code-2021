from __future__ import annotations
from enum import Enum
from typing import List


class Token(Enum):
    T_OPEN_PAREN = '('
    T_CLOSE_PAREN = ')'
    T_OPEN_SQUARE = '['
    T_CLOSE_SQUARE = ']'
    T_OPEN_ANGLE = '<'
    T_CLOSE_ANGLE = '>'
    T_OPEN_BRACE = '{'
    T_CLOSE_BRACE = '}'

    @staticmethod
    def open_tokens() -> List[Token]:
        return [Token.T_OPEN_SQUARE, Token.T_OPEN_ANGLE, Token.T_OPEN_PAREN, Token.T_OPEN_BRACE]

    @staticmethod
    def valid_end_token(token: Token) -> Token:
        if token is Token.T_OPEN_ANGLE:
            return Token.T_CLOSE_ANGLE
        if token is Token.T_OPEN_SQUARE:
            return Token.T_CLOSE_SQUARE
        if token is Token.T_OPEN_PAREN:
            return Token.T_CLOSE_PAREN
        if token is Token.T_OPEN_BRACE:
            return Token.T_CLOSE_BRACE
