import networkx as nx
import matplotlib.pyplot as plt

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
        
        # Add nodes
        for state in dfa_transitions_named:
            G.add_node(state, is_final=state in dfa_final_states_names)
        
        # Add edges
        for state, transitions in dfa_transitions_named.items():
            for input_symbol, next_state in transitions.items():
                G.add_edge(state, next_state, label=input_symbol)
        
        # Position nodes
        pos = nx.spring_layout(G, seed=42)  # Fixed seed for reproducible layout

        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', alpha=0.6)
        nx.draw_networkx_nodes(G, pos, nodelist=dfa_final_states_names, node_size=700, node_color='lightgreen', alpha=0.6)
        
        # Draw edges
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.1')
        nx.draw_networkx_labels(G, pos)

        # Draw edge labels
        edge_labels = nx.get_edge_attributes(G, 'label')
        edge_labels_pos = self._get_edge_label_pos(pos)
        nx.draw_networkx_edge_labels(G, edge_labels_pos, edge_labels=edge_labels)

        plt.axis('off')
        plt.show()

    def _get_edge_label_pos(self, pos):
        """Adjust edge label positions to reduce overlap and improve loop visibility."""
        edge_labels_pos = {}
        for edge in pos:
            # Shift edge labels towards the target node to reduce overlap with the node itself
            source_pos = np.array(pos[edge[0]])
            target_pos = np.array(pos[edge[1]])

            # For self-loops, position the label above the node
            if edge[0] == edge[1]:
                dx, dy = target_pos - source_pos
                dist = np.sqrt(dx ** 2 + dy ** 2)
                if dist == 0:  # Self-loop
                    # Adjust these values to change the loop label position
                    edge_labels_pos[edge] = target_pos + np.array([0, 0.1])
                continue

            # Adjust this value to move the label closer/further to the target node
            label_pos = source_pos * 0.6 + target_pos * 0.4
            edge_labels_pos[(edge[0], edge[1])] = label_pos

        return edge_labels_pos