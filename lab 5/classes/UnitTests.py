from CNFConverter import CNFConverter

import unittest

class TestCNFConverter(unittest.TestCase):
    def setUp(self):
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
