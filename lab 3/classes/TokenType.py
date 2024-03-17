from enum import Enum, auto

# Define the types of tokens that our lexer can recognize.
class TokenType(Enum):
    INTEGER = auto()  # Represents an integer
    PLUS = auto()    # Represents a plus sign '+'
    MINUS = auto()   # Represents a minus sign '-'
    LPAREN = auto()  # Represents a left parenthesis '('
    RPAREN = auto()  # Represents a right parenthesis ')'
    EOF = auto()     # Represents the end of the input