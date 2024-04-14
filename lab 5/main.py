from classes.CNFConverter import CNFConverter

grammar_22 = {
    'S': {'aB', 'AC'},
    'A': {'a', 'ACSC', 'BC'},
    'B': {'b', 'aA'},
    'C': {'', 'BA'},
    'E': {'bB'}
}

converter = CNFConverter(grammar_22)
cnf_grammar = converter.convert_to_cnf()
print(cnf_grammar)