import itertools

class Regex:
    def __init__(self):
        pass

    def explain_process(self, steps):
        """
        Explain the sequence of processing the regular expression.
        
        Parameters:
        - steps: A list of strings, each describing a step in processing the regex.
        """
        print("\nProcessing Sequence:")
        for i, step in enumerate(steps, start=1):
            print(f"{i}. {step}")
        print("\n")

    def generate_combinations(self, parts, description, steps):
        """
        Generalized function to generate and print all combinations based on the given parts.
        
        Parameters:
        - parts: A list of lists, where each inner list represents possible variations of a regex part.
        - description: A string describing the regular expression being processed.
        - steps: A list of strings, each describing a step in processing the regex.
        """
        self.explain_process(steps)

        print(f"=========================================================\n")
        print(f"All possible combinations for {description}")
        print(f"\n=========================================================\n")
        for combination in itertools.product(*parts):
            print(f''.join(combination))

    def first_regex(self):
        parts = [
            ['', 'M'],  # M?
            ['NN'],  # N^2
            [''.join(x) for x in itertools.product('OP', repeat=3)],  # (O|P)^3
            [''.join(['Q']*i) for i in range(6)],  # Q^*
            [''.join(['R']*i) for i in range(1, 6)],  # R^+
        ]
        steps = [
            "Process 'M?' - M is optional",
            "Process 'N^2' - N appears exactly twice",
            "Process '(O|P)^3' - Either O or P appears exactly three times in any combination",
            "Process 'Q^*' - Q appears any number of times up to 5",
            "Process 'R^+' - R appears at least once and up to 5 times"
        ]
        self.generate_combinations(parts, "M? N^2 (O|P)^3 Q^* R^+", steps)

    def second_regex(self):
        parts = [
            [''.join(x) for x in itertools.product('XYZ', repeat=3)],  # (X|Y|Z)^3
            [''.join(['8']*i) for i in range(1, 6)],  # 8^+
            ['9', '0'],  # (9|0)
        ]
        steps = [
            "Process '(X|Y|Z)^3' - X, Y, or Z appears exactly three times in any combination",
            "Process '8^+' - 8 appears at least once and up to 5 times",
            "Process '(9|0)' - Either 9 or 0 appears exactly once"
        ]
        self.generate_combinations(parts, "(X|Y|Z)^3 8^+ (9|0)", steps)

    def third_regex(self):
        parts = [
            ['H', 'i'],  # (H|i)
            ['J', 'K'],  # (J|K)
            [''.join(['L']*i) for i in range(6)],  # L^*
            ['', 'N'],  # N?
        ]
        steps = [
            "Process '(H|i)' - Either H or i appears exactly once",
            "Process '(J|K)' - Either J or K appears exactly once",
            "Process 'L^*' - L appears any number of times up to 5",
            "Process 'N?' - N is optional"
        ]
        self.generate_combinations(parts, "(H|i) (J|K) L^* N?", steps)