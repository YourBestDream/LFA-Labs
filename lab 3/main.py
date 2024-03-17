from classes.Lexer import Lexer
from classes.Token import Token
from classes.TokenType import TokenType

def main():
    # Input text for the lexer to tokenize
    text = "3 + 5 - ( 7 - 2 )"
    lexer = Lexer(text)  # Create a lexer instance with the input
    token = lexer.get_next_token()  # Start tokenizing
    while token.type != TokenType.EOF:  # Continue until EOF token is reached
        print(token)  # Print each token
        token = lexer.get_next_token()  # Move to the next token

if __name__ == "__main__":
    main()