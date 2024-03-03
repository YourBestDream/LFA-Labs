import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

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

    def conversion_ndfa_to_dfa(self):
            if self.is_dfa() == "DFA":
                return "No need to convert. FA is already a DFA"
            
            dfa_states = [frozenset([self.Q[0]])]
            dfa_transitions = {}
            dfa_final_states = set()

            while len(dfa_states) > len(dfa_transitions):
                for state_set in dfa_states:
                    if state_set not in dfa_transitions:
                        dfa_transitions[state_set] = {}
                        for symbol in self.E:
                            next_state = frozenset(sum([self._get_next_states(s, symbol) for s in state_set], []))
                            if next_state not in dfa_states:
                                dfa_states.append(next_state)
                            dfa_transitions[state_set][symbol] = next_state

                            if not dfa_final_states.intersection(state_set) and any(s in self.F for s in state_set):
                                dfa_final_states.add(state_set)

            # Convert frozensets to more readable state names
            state_names = {state: f"D{index}" for index, state in enumerate(dfa_states)}
            dfa_final_states_names = [state_names[state] for state in dfa_final_states]

            # Convert transitions to use the new state names
            dfa_transitions_named = {state_names[state]: {symbol: state_names[next_state] for symbol, next_state in transitions.items()} for state, transitions in dfa_transitions.items()}
            self.draw_dfa(dfa_transitions_named, dfa_final_states_names)
            return f"Transitions in the form [State: [transition : state]]:{dfa_transitions_named}\nFinal state : {dfa_final_states_names}"

    def _get_next_states(self, current_state, symbol):
        return [transition[1] for transition in self.sigma.get(current_state, []) if transition[0] == symbol]
    
    def draw_dfa(self, dfa_transitions_named, dfa_final_states_names):
        G = nx.DiGraph()
        # Add nodes with their labels
        for state in dfa_transitions_named:
            G.add_node(state)
        
        # Add edges with their labels
        for state, transitions in dfa_transitions_named.items():
            for symbol, next_state in transitions.items():
                G.add_edge(state, next_state, label=symbol)
        
        pos = nx.circular_layout(G)  # Using circular layout for clearer structure
        
        # Draw the graph
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', edgecolors='black')
        nx.draw_networkx_labels(G, pos)
        edges = nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, connectionstyle='arc3,rad=0.2')
        
        # Handle self-loops after drawing other edges to avoid overlap issues
        for state, transitions in dfa_transitions_named.items():
            for symbol, next_state in transitions.items():
                if state == next_state:  # Identify self-loops
                    loop_pos = np.array(pos[state])
                    # Drawing self-loop with an arc away from the node
                    plt.annotate("", xy=loop_pos, xycoords='data',
                                 xytext=loop_pos + np.array([0, 0.4]), textcoords='data',
                                 arrowprops=dict(arrowstyle="->", color="red",
                                                 shrinkA=15, shrinkB=15,
                                                 patchA=None, patchB=None,
                                                 connectionstyle="arc3,rad=0.3"))
                    # Placing text for self-loop
                    plt.text(loop_pos[0], loop_pos[1] + 0.5, symbol, ha='center', color="red")
        
        # Highlight final states
        nx.draw_networkx_nodes(G, pos, nodelist=dfa_final_states_names, node_color='lightgreen', edgecolors='black')
        
        # Edge labels, avoiding self-loop edges since they're handled separately
        edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True) if u != v}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3)
        
        plt.title('DFA Visualization')
        plt.axis('off')
        plt.show()