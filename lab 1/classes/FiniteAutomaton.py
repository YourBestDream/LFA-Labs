class FiniteAutomaton:
    def __init__(self):
        self.Q = ['q0','q1','q2']
        self.E = ['a','b']
        self.F = ['q2']
        self.sigma = {
            'q0': [['a','q0'],['b','q1']],
            'q1': [['b','q1'],['b','q2'],['a','q0']],
            'q2': [['b','q1']]
        }
    
    def set_automaton(self, Q, E, F, sigma):
        self.Q = Q
        self.E = E
        self.F = F
        self.sigma = sigma

    def from_automaton_to_grammar(self):
        self.VN = ['A'+str(i) for i in range(len(self.Q))]
        self.VT = self.E.copy()
        productions = []
        for state, transitions in self.sigma.items():
            index = self.Q.index(state)
            for transition in transitions:
                if len(transition) == 2:
                    letter, final_state = transition
                    productions.append(f"A{index} -> {letter}A{self.Q.index(final_state)}")

        for accept_state in self.F:
            productions.append(f"A{accept_state[1]} -> ε")

        return f"Vn = {self.VN}\nVt = {self.VT} \n" + "\n".join(productions)

    def is_dfa(self):
        for state in self.Q:
            transitions_for_state = self.sigma.get(state, [])
            symbols_seen = set()

            for transition in transitions_for_state:
                symbol = transition[0]

                if symbol == "ε" or symbol in symbols_seen:
                    return "NDFA"
                symbols_seen.add(symbol)
        return "DFA"

    # def conversion_ndfa_to_dfa(self):
    #     need_of_conv = self.is_dfa()
    #     if need_of_conv == "DFA":
    #         return "No need to convert. FA is already a DFA"
    #     else:
