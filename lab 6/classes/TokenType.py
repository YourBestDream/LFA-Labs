from enum import Enum

class TokenType(Enum):
    INTEGER = '0|[1-9][0-9]*'  # Regex format not used here but illustrates intent
    PLUS = '+'
    MINUS = '-'
    MULT = '*'
    DIV = '/'
    LPAREN = '('
    RPAREN = ')'
    EOF = '\0'
