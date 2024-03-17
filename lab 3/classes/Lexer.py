from .Token import Token
from .TokenType import TokenType

class Lexer:
    # Initialize the lexer with the input text.
    def __init__(self, text):
        self.text = text  # The string input to tokenize
        self.pos = 0  # The current position in the text
        self.current_char = self.text[self.pos]  # The current character

    def advance(self):
        """Advance the `pos` pointer and update the `current_char`."""
        self.pos += 1
        # Check if we've reached the end of the text
        if self.pos > len(self.text) - 1:
            self.current_char = None  # EOF
        else:
            self.current_char = self.text[self.pos]

    def integer(self):
        """Handle multi-digit integers by aggregating until a non-digit is found."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Tokenize the input text by recognizing tokens one at a time."""
        while self.current_char is not None:
            if self.current_char.isspace():  # Skip whitespace
                self.advance()
                continue

            if self.current_char.isdigit():  # Handle integers
                return Token(TokenType.INTEGER, self.integer())

            if self.current_char == '+':  # Plus token
                self.advance()
                return Token(TokenType.PLUS)

            if self.current_char == '-':  # Minus token
                self.advance()
                return Token(TokenType.MINUS)

            if self.current_char == '(':  # Left parenthesis
                self.advance()
                return Token(TokenType.LPAREN)

            if self.current_char == ')':  # Right parenthesis
                self.advance()
                return Token(TokenType.RPAREN)

            self.error()  # If none match, raise an error

        # Once we're done with all characters, return an EOF token
        return Token(TokenType.EOF)

    def error(self):
        """Raise an exception if an invalid character is encountered."""
        raise Exception('Invalid character')
