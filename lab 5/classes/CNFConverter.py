import string

class CNFConverter:
    def __init__(self, grammar):
        # grammar is expected to be a dictionary where keys are non-terminals and values are a set of possible productions
        self.grammar = grammar
        self.start_symbol = next(iter(grammar))  # Assume the first key as start symbol
        self.terminals = set()
        self.non_terminals = set(grammar.keys())
        self.update_terminals_and_non_terminals()

    def update_terminals_and_non_terminals(self):
        for productions in self.grammar.values():
            for production in productions:
                for symbol in production:
                    if symbol.islower():  # Assuming all terminals are lowercase
                        self.terminals.add(symbol)
                    elif symbol.isupper():
                        self.non_terminals.add(symbol)

    def eliminate_start_symbol_from_rhs(self):
        if any(self.start_symbol in production for productions in self.grammar.values() for production in productions):
            # Create a new start symbol
            new_start = self.start_symbol + "'"
            self.grammar[new_start] = {self.start_symbol}
            self.start_symbol = new_start
            self.non_terminals.add(new_start)

    def eliminate_non_solitary_terminals(self):
        replacements = {}
        for non_terminal, productions in list(self.grammar.items()):
            new_productions = set()
            for production in productions:
                modified_production = ""
                for symbol in production:
                    if symbol in self.terminals:
                        # Create a new non-terminal for the solitary terminal if not already created
                        if symbol not in replacements:
                            new_non_terminal = symbol.upper() + "_"
                            replacements[symbol] = new_non_terminal
                            self.grammar[new_non_terminal] = {symbol}
                            self.non_terminals.add(new_non_terminal)
                        modified_production += replacements[symbol]
                    else:
                        modified_production += symbol
                new_productions.add(modified_production)
            self.grammar[non_terminal] = new_productions

    def to_binary(self):
        non_terminal_map = {}
        new_name_suffix = 1  # Start a suffix for new non-terminals
        for non_terminal, productions in list(self.grammar.items()):
            new_productions = set()
            for production in productions:
                production = list(production)  # Make sure production is a list of symbols
                while len(production) > 2:
                    first, second, *rest = production
                    pair = first + second
                    # Check if we have already created a non-terminal for this pair
                    if pair not in non_terminal_map:
                        # Create a new name for a non-terminal
                        new_non_terminal = f'N{new_name_suffix}_'
                        new_name_suffix += 1
                        self.non_terminals.add(new_non_terminal)
                        non_terminal_map[pair] = new_non_terminal
                        self.grammar[new_non_terminal] = {pair}
                    # Replace the first two symbols with the new non-terminal
                    production = [non_terminal_map[pair]] + rest
                new_productions.add(''.join(production))
            self.grammar[non_terminal] = new_productions



    def eliminate_epsilon_productions(self):
        epsilon_producing_non_terminals = {nt for nt, prods in self.grammar.items() if '' in prods}
        changed = True

        while changed:
            changed = False
            new_productions = {}

            for non_terminal, productions in self.grammar.items():
                new_productions[non_terminal] = productions.copy()

                if non_terminal in epsilon_producing_non_terminals:
                    continue

                for production in productions:
                    positions = [i for i, symbol in enumerate(production) if symbol in epsilon_producing_non_terminals]
                    # Generate all combinations of productions that exclude each epsilon-producing non-terminal one at a time
                    for i in range(1, 1 << len(positions)):
                        new_prod = list(production)
                        for j in range(len(positions)):
                            if i & (1 << j):
                                new_prod[positions[j]] = None
                        new_prod = ''.join(filter(None, new_prod))

                        if new_prod and new_prod != production:
                            new_productions[non_terminal].add(new_prod)
                            changed = True

            self.grammar = new_productions

        # Finally, remove all epsilon productions except from the start symbol
        for non_terminal in list(epsilon_producing_non_terminals):
            if non_terminal == self.start_symbol:
                self.grammar[non_terminal].add('')
            else:
                self.grammar[non_terminal].discard('')



    def eliminate_unit_productions(self):
        # Mapping from non-terminals to the set of non-terminals they can reach via unit productions
        unit_closure = {nt: {nt} for nt in self.non_terminals}

        # Compute the closure of unit productions
        for non_terminal in self.non_terminals:
            for production in list(self.grammar[non_terminal]):
                if production in self.non_terminals and production != non_terminal:
                    unit_closure[non_terminal].add(production)

        # Use the Floyd-Warshall algorithm to compute the transitive closure
        for k in self.non_terminals:
            for i in self.non_terminals:
                if k in unit_closure[i]:
                    for j in unit_closure[k]:
                        unit_closure[i].add(j)

        # Replace unit productions
        new_grammar = {}
        for non_terminal in self.non_terminals:
            new_productions = set()
            for reachable in unit_closure[non_terminal]:
                for production in self.grammar[reachable]:
                    if production not in self.non_terminals:
                        new_productions.add(production)
            new_grammar[non_terminal] = new_productions

        self.grammar = new_grammar


    def convert_to_cnf(self):
        self.eliminate_start_symbol_from_rhs()
        print("Eliminated start symbol form rhs\n", self.grammar, "\n")
        self.eliminate_non_solitary_terminals()
        print("Eliminated non-solitary terminals\n", self.grammar, "\n")
        self.to_binary()
        print("Converted to binary\n", self.grammar, "\n")
        self.eliminate_epsilon_productions()
        print("Eliminated epsilon productions\n", self.grammar, "\n")
        self.eliminate_unit_productions()
        return self.grammar