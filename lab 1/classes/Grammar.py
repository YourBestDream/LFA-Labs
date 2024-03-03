class Grammar:
    def __init__(self):
        # Type 2 grammar
        self.VN = ['S', 'B', 'C']
        self.VT = ['a', 'b', 'c']
        self.P = {
            'S': ['aB'],
            'B': ['aC', 'bB'],
            'C': ['bB', 'c', 'aS', 'ε']
        }
        #Type 3 grammar
        # self.VN = ['S', 'A', 'B']
        # self.VT = ['1', '0']
        # self.P = {
        #     'S': ['0A'],
        #     'A': ['1B', '0'],
        #     'B': ['0A', '1']
        # }
    def set_grammar(self, VN, VT, P):
        self.VN = VN
        self.VT = VT
        self.P = P

    def chomsky_check(self):
        is_type_3 = True
        is_type_2 = True

        for left, rights in self.P.items():
            # Type 2 checks: Left side must be a single non-terminal.
            if len(left) != 1 or left not in self.VN:
                is_type_2 = False

            for right in rights:
                # Modify Type 3 checks to accurately reflect Type 3 grammar constraints.
                # Specifically, ensure it does not classify grammars with recursive productions as Type 3.
                if len(right) > 2 or (len(right) == 2 and not(right[0] in self.VT and right[1] in self.VN)):
                    is_type_3 = False
                if len(right) == 1 and right not in self.VT:
                    is_type_3 = False
                if right == '':
                    is_type_3 = False  # Assuming epsilon productions are not allowed in our Type 3 definition.

        # After all checks, determine the type
        if is_type_3:
            return "Type 3 (Regular)"
        elif is_type_2:
            return "Type 2 (Context-Free)"
        else:
            return "Type 1 (Context-Sensitive)"  # Assuming no Type 0 grammars for simplicity
