import unittest
import numpy as np
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sibling_dir = os.path.join(current_dir, '..', 'abstraction')
sys.path.append(sibling_dir)

from CardCentroid import CardCentroid
from treys import Card, Evaluator

notes = """
-  if the public board cards are 7dQh4h2s3c, then KcQc has an equity of 0.856 (prob winning + 0.5 * prob tying)
- makes number of abstractions equal to what was set
- makes correct histograms
- 50 regions of size 0.02
Clubs = 1, Diamonds = 2, Hearts = 3, Spades = 4
"""

class CardCentroidTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_data = np.zeros((50000, 50))
        cls.test_data[0:10000, :] = 0.0
        cls.test_data[10000:20000, :] = 0.3
        cls.test_data[20000:30000, :] = 0.6
        cls.test_data[30000:40000, :] = 0.9
        cls.test_data[40000:, :] = 1.0
        cls.cc = CardCentroid()

    def test_greatness(self):
        ref_array = np.full(50, 0.6)
        self.assertTrue(np.array_equal(self.test_data[20001], ref_array))
        pass

    def test_getEquity(self):
        board = ['7d', 'Qh', '4h','2s', '3c']
        hand = [ 'Kc', 'Qc']
        #Card.print_pretty_cards(board + hand)
        result = self.cc.getEquityAllCards(hand, tableCards=board)
        self.assertAlmostEqual(0.856, result, places=3)
        pass


if __name__ == "__main__":
    unittest.main()