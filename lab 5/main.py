from classes.CNFConverter import CNFConverter

Vn = ['S', 'A', 'B', 'C', 'E']  # Non-terminal symbols
Vt = ['a', 'b']  # Terminal symbols
P = {
    'S': {'aB', 'AC'},
    'A': {'a', 'ACSC', 'BC'},
    'B': {'b', 'aA'},
    'C': {'', 'BA'},  # The empty string representing an epsilon production
    'E': {'bB'}
}

chomsky_grammar = CNFConverter(Vn, Vt, P)

chomsky_grammar.normalize_grammar()