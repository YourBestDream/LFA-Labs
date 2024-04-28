from enum import Enum

class TokenType(Enum):
    INTEGER = '0|[1-9][0-9]*'  # This will not match correctly as intended in your lexer without real regex
    PLUS = r'\+'               # Correct for '+'
    MINUS = r'\-'              # Correct for '-'
    LPAREN = r'\('             # Correct for '('
    RPAREN = r'\)'             # Correct for ')'
    EOF = r'\0'                # Typically not needed in this form