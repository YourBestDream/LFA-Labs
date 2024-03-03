from classes.Automata import Automata
from classes.Grammar import Grammar
from classes.FiniteAutomaton import FiniteAutomaton

aut = Automata()
gr = Grammar()
fa = FiniteAutomaton()

class Menu:
    def __init__(self):
        pass

    def main_menu(self):
        self.user_choice = int(input("""Please choose the option:
            1) Generate strings with progression
            2) Check if string can be obtained
            3) Check the type of Grammar
            4) FA choice menu
            5) Exit\n>>>"""))
        
        match self.user_choice:
            case 1:
                aut.generating_strings()
            case 2:
                user_input = input("Insert the string: ")
                aut.check_string(user_input)
            case 3:
                self.grammar_choice()
            case 4:
                self.fa_determination_menu()
            
            case 5:
                exit()
    
    def grammar_choice(self):
        gm_choice = int(input("""
            1) Check current grammar
            2) Check grammar inserted by user
            >>>"""))
        match gm_choice:
            case 1:
                print(gr.chomsky_check())
            case 2:
                VN = input("Insert Non-terminal symbols separated by commas:\n").split(',')
                VT = input("Insert Terminal symbols separated by commas:\n").split(',')
                P = {}
                for _ in VN:
                    transitions = input(f"Please insert all the transitions for {_} separated by commas:\n").split(',')
                    P[_] = transitions
                gr.set_grammar(VN, VT, P)
                print(gr.chomsky_check())
    
    def fa_determination_menu(self):
        self.fa_choice = int(input("""
        What FA use:
        1) Set the new FA
        2) Use already existing
        """))

        match self.fa_choice:
            case 1:
                Q = input("Insert states separated by commas:\n").split(",")
                E = input("Insert alphabet separated by commas:\n").split(",")
                F = input("Insert accept states separated by commas:\n").split(",")
                sigma={}
                for state in Q:
                    transitions_input = input(f"Insert all the transitions and states to which they lead for {state} in the format '[a,q0],[b,q2]':\n")
                    if transitions_input.lower() == 'none':
                        sigma[state] = []
                    else:
                        transitions_list = transitions_input.strip("[]").split("],[")
                        transitions = [transition.split(",") for transition in transitions_list]
                        sigma[state] = transitions
                sigma = {key: value for key, value in sigma.items() if len(value) > 0}
                fa.set_automaton(Q, E, F, sigma)
                self.fa_menu_choice()
            case 2:
                self.fa_menu_choice()

    def fa_menu_choice(self):
        user_choice = int(input("""Please choose the option:
1) Convert the FA to Grammar
2) Determine the type of FA
3) Convert NDFA to DFA\n>>>"""))

        match user_choice:
            case 1:
                print(fa.from_automaton_to_grammar())
            case 2:
                print(fa.is_dfa())
            case 3:
                print(fa.conversion_ndfa_to_dfa())