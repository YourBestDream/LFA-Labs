from .TokenType import TokenType
from .AST import Number, BinaryOperator

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception('Unexpected token type')

    def factor(self):
        token = self.current_token
        if token.type == TokenType.INTEGER:
            self.eat(TokenType.INTEGER)
            return Number(token.value)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node

    def term(self):
        node = self.factor()
        while self.current_token.type in (TokenType.MULT, TokenType.DIV):
            token = self.current_token
            if token.type == TokenType.MULT:
                self.eat(TokenType.MULT)
            elif token.type == TokenType.DIV:
                self.eat(TokenType.DIV)
            node = BinaryOperator(left=node, operator=token.type, right=self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
            node = BinaryOperator(left=node, operator=token.type, right=self.term())
        return node
