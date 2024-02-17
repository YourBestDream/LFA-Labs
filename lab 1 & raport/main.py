from classes.Automata import Automata

user_choice = int(input("""Please choose the option:
1) Generate strings with progression
2) Check if string can be obtained\n>>>"""))

aut = Automata()
match user_choice:
    case 1:
        aut.generating_strings()
    case 2:
        user_input = input("Insert the string: ")
        aut.check_string(user_input)