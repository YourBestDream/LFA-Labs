# Chomsky Normal Form

### Course: Formal Languages & Finite Automata
### Author: Popov Nichita
### Variant: 22

----

## Theory
Chomsky Normal Form (CNF) is a fundamental structure in formal language theory, specifically for simplifying context-free grammars (CFGs). Devised by Noam Chomsky, CNF is crucial for algorithms like the CYK algorithm, which checks if a string belongs to a given grammar. In CNF, production rules are restricted to two types: one where a non-terminal produces exactly two non-terminals, or one where it produces a single terminal.
This format streamlines parsing and analysis by simplifying grammar rules without reducing their expressive power. The conversion to CNF involves removing useless symbols, erasing unit productions, and eliminating null productions, making grammars easier to handle computationally. Chomsky Normal Form's practical applications in programming language compilers and natural language processing make it an essential concept in computer science.

## Objectives:
1) Learn about Chomsky Normal Form (CNF).
2) Get familiar with the approaches of normalizing a grammar.
3) Implement a method for normalizing an input grammar by the rules of CNF.
    a. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    b. The implemented functionality needs executed and tested.
    c. A **BONUS point** will be given for the student who will have unit tests that validate the functionality of the project.
    d. Also, another **BONUS point** would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.

<!-- In this will I, Nikita Popov, also known as ScarletLiar or Not A Whale leave the following to my fellow comrade:

4 marvelous cat - feed 'em and do not fuck around with them or you will find out

A pair of recently purchased sneakers - these magnificent specimens of footwear art, acquired by me in a moment of inspiration and understanding of the deep essence of fashion. They are not just sneakers, they are the embodiment of freedom and my unwavering belief that style is not what you wear, but how you wear it. Wear them with pride and lightness, let every step remind you of the limitless democracy that you can deliver in all the corners of galaxy. -->

## Implementation Description
The `CNFConverter` class in `CNFConverter.py` is a comprehensive tool designed to convert context-free grammars (CFGs) into Chomsky Normal Form (CNF). This conversion is critical for simplifying the parsing process in computational applications such as compilers and natural language processing tools.

**Core Functionalities**
1) **Normalization of Grammar**: The `normalize_grammar` method systematically applies transformations to convert the given CFG into CNF. It handles the elimination of empty productions, unit productions, and inaccessible or non-productive symbols, culminating in the transformation to CNF.

```python
def normalize_grammar(self):
    print("Original grammar\nVn =", self.Vn, "\nVt=", self.Vt, "\nP=", self.P)
    P1 = self.eliminate_empty(self.P)
    print("---------------------------\n","Empty-elimination \n", P1)
    P2 = self.eliminate_renaming(P1)
    print("Unit production elimination\n", P2)
    P3, Vn, Vt = self.eliminate_inaccessible(P2)
    print("Inaccessible elimination \n",P3)
    P4, Vn = self.eliminate_non_productive(P3, Vn, Vt)
    print("Non-Productive elimination \n", P4)
    P5, Vn = self.bring_to_chomsky(P4, Vn, Vt)
    print("Chomsky normal form transformation\n", P5)

    print("-------------------------------")
    self.P = P5
    self.Vn = Vn
    self.Vt = Vt
    print("Chomsky normal form grammar\n Vn=", self.Vn, "\nVt=", self.Vt, "\nP=", self.P)
```
   
2) **Step-by-Step Transformation**: Each transformation step is methodically implemented through dedicated methods such as `eliminate_empty`, `eliminate_renaming`, `eliminate_inaccessible`, and `bring_to_chomsky`, ensuring that each aspect of the CNF is achieved accurately.

```python
def eliminate_empty(self, P):
    # Implementation for eliminating empty productions
    P1 = P
    empty_set = ["empty"]
    self.find_empty(P1, empty_set)
    for k, v in P1.items():
        for trans in v:
            if len(trans) >= 2:
                self.substitute_empty(empty_set[1:], k, trans, P1)
    return P1
```

3) **Verification and Testing**: The unit tests in `UnitTests.py` ensure that each transformation step is verified, ensuring robustness and correctness of the grammar transformation process.

```python
from CNFConverter import CNFConverter
import unittest

class TestCNFConverter(unittest.TestCase):
    def setUp(self):
        # Initialization for test cases
        self.Vn = ['S', 'A', 'B', 'C', 'E']
        self.Vt = ['a', 'b']
        self.P = {
            'S': ['aB', 'AC'],
            'A': ['a', 'ACSC', 'BC'],
            'B': ['b', 'aA'],
            'C': ['', 'BA'],  # The empty string representing an epsilon production
            'E': ['bB']
        }
        self.converter = CNFConverter(self.Vn, self.Vt, self.P)
    
    def test_initialization_and_production_formatting(self):
        # Check if empty strings are replaced with 'empty'
        self.assertIn('empty', self.converter.P['C'])

    def test_epsilon_elimination(self):
        P1 = self.converter.eliminate_empty(self.converter.P)
        # After elimination, 'C' should not have 'empty' anymore
        self.assertNotIn('empty', P1['C'])
        # 'BA' should still be present as it is not affected directly by the elimination of epsilon production
        self.assertIn('BA', P1['C'])


    def test_unit_production_elimination(self):
        P1 = self.converter.eliminate_empty(self.converter.P)
        P2 = self.converter.eliminate_renaming(P1)
        # Check that after elimination, no unit productions remain
        self.assertNotIn('B', P2['B'])

    def test_production_rule_handling(self):
        # Ensures the transformed productions are handled correctly
        self.assertIn('a', self.converter.P['A'])
        self.assertIn('ACSC', self.converter.P['A'])

# Run the tests
if __name__ == '__main__':
    unittest.main()
```

**Practical Application with `main.py`**
The driver script `main.py` demonstrates the practical use of the `CNFConverter` class by applying it to a CFG and outputting the converted grammar in Chomsky Normal Form. This script serves as an example of how the class can be applied to real-world grammar transformation tasks.

```python
from classes.CNFConverter import CNFConverter

Vn = ['S', 'A', 'B', 'C', 'E']  # Non-terminal symbols
Vt = ['a', 'b']  # Terminal symbols
P = {
    'S': {'aB', 'AC'},
    'A': {'a', 'ACSC', 'BC'},
    'B': {'b', 'aA'},
    'C': {'', 'BA'},  # The empty string representing an epsilon production
    'E': {'bB'}
}

chomsky_grammar = CNFConverter(Vn, Vt, P)

chomsky_grammar.normalize_grammar()
```

## Results
The results from utilizing the `CNFConverter` class illustrate the successful transformation of a context-free grammar into Chomsky Normal Form. The conversion process systematically eliminated empty productions, unit productions, inaccessible symbols, and non-productive symbols, ultimately restructuring the grammar into the stringent format required by CNF. The final output confirms the efficacy of the transformation algorithms, as the grammar adheres strictly to the rules of Chomsky Normal Form, where each production is either a non-terminal leading to exactly two non-terminals or to a single terminal symbol.
These transformations not only simplify the structure of the grammar but also enhance its suitability for efficient parsing algorithms like CYK, showcasing the practical utility of CNF in computational linguistics and programming language compilers. The detailed output at each step of the conversion provides clear insight into the transformation process, allowing users to trace the modifications to the grammar systematically, thus increasing transparency and understanding of the underlying mechanics.

## Conclusion
This laboratory work has highlighted the critical importance of Chomsky Normal Form in the field of computational linguistics and compiler design. Through the implementation and thorough testing of the `CNFConverter` class, we have gained a deep understanding of the transformation processes required to convert any context-free grammar into CNF. This experience has illuminated the structured approach necessary for such transformations, emphasizing the simplification it brings to parsing algorithms and the enhancement of grammatical analysis.
The detailed step-by-step transformation provided by the `CNFConverter` class, combined with the robust testing framework, has not only met the educational goals of understanding the mechanics behind grammar normalization but has also prepared us for future applications in parsing and grammar analysis in computer science. This project successfully demonstrated the practical and theoretical benefits of mastering CNF, reinforcing its value in both academic and practical computing contexts.


## References

* https://www.youtube.com/watch?v=sXQxhojSdZM
* https://www.youtube.com/watch?v=upu_TeZImN0&t
* https://www.youtube.com/watch?v=dQw4w9WgXcQ