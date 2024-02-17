import random as rn

from .Grammar import Grammar

class Automata:
    def __init__(self, grammar = Grammar()):
        self.grammar = grammar
    
    def generating_strings(self):
        for i in range(5):
            self.start = self.grammar.VN[0]
            self.progression = "S"
            while self.start[-1] not in self.grammar.VT:
                temp = self.start[-1]
                self.start = self.start[:-1]
                self.start += rn.choice(self.grammar.P[temp])
                self.progression += f"-> {self.start}"
            print(f"\nProgression: \n{self.progression}")
            print(f"Result: {self.start}")
    
    def check_string(self, input_string):
        current_strings = [input_string]
        steps = 0
        max_steps = 100

        while steps < max_steps:
            next_strings = []
            for s in current_strings:
                if s == self.grammar.VN[0]:
                    print("String can be obtained from the grammar.")
                    return True
                
                for non_terminal, productions in self.grammar.P.items():
                    for prod in productions:
                        if prod in s:
                            next_state = s.replace(prod, non_terminal, 1)
                            next_strings.append(next_state)
            
            if not next_strings:
                break

            current_strings = list(set(next_strings))
            steps += 1

        print("String cannot be obtained from the grammar.")
        return False