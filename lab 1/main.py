from classes.Automata import Automata
from classes.Grammar import Grammar

user_choice = int(input("""Please choose the option:
1) Generate strings with progression
2) Check if string can be obtained
3) Check the type of Grammar\n>>>"""))

aut = Automata()
gr = Grammar()
match user_choice:
    case 1:
        aut.generating_strings()
    case 2:
        user_input = input("Insert the string: ")
        aut.check_string(user_input)
    case 3:
        grammar_choice = int(input("""
    1) Check current grammar
    2) Check grammar inserted by user
    >>>"""))
        match grammar_choice:
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
                print(f'{gr.VN}\n{gr.VT}\n{gr.P}')
                print(gr.chomsky_check())