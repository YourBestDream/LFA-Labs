import itertools

class Regex:
    def __init__(self):
        pass

    def first_regex(self):
        parts = []
        # M? - M is optional
        parts.append(['', 'M'])
        # N^2 - N appears exactly twice
        parts.append(['NN'])
        # (O|P)^3 - Either O or P appears exactly three times in any combination
        parts.append([''.join(x) for x in itertools.product('OP', repeat=3)])
        # Q^* - Q appears any number of times up to 5 (for the purpose of this example)
        parts.append([''.join(['Q']*i) for i in range(6)])
        # R^+ - R appears at least once and up to 5 times
        parts.append([''.join(['R']*i) for i in range(1, 6)])
        
        # Generate all combinations
        print("\n=========================================================\n")
        print("All possible combinations for M? N^2 (O|P)^3 Q^* R^+")
        print("\n=========================================================\n")
        for combination in itertools.product(*parts):
            print(f''.join(combination))
    
    def second_regex(self):
        parts = []
        # (X|Y|Z)^3 - X, Y, or Z appears exactly three times in any combination
        parts.append([''.join(x) for x in itertools.product('XYZ', repeat=3)])
        # 8^+ - 8 appears at least once and up to 5 times
        parts.append([''.join(['8']*i) for i in range(1, 6)])
        # (9|0) - Either 9 or 0 appears exactly once
        parts.append(['9', '0'])
        
        print("\n=========================================================\n")
        print("All possible combinations for (X|Y|Z)^3 8^+ (9|0)")
        print("\n=========================================================\n")
        # Generate all combinations
        for combination in itertools.product(*parts):
            print(f''.join(combination))
    
    def third_regex(self):
        parts = []
        # (H|i) - Either H or i appears exactly once
        parts.append(['H', 'i'])
        # (J|K) - Either J or K appears exactly once
        parts.append(['J', 'K'])
        # L^* - L appears any number of times up to 5 (for the purpose of this example)
        parts.append([''.join(['L']*i) for i in range(6)])
        # N? - N is optional
        parts.append(['', 'N'])
        
        print("\n=========================================================\n")
        print("\nAll possible combinations for (H|i) (J|K) L^* N?\n")
        print("\n=========================================================\n")
        # Generate all combinations
        for combination in itertools.product(*parts):
            print(''.join(combination))