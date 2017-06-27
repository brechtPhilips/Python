import unittest

from rps import moves


class MoveTests(unittest.TestCase):

    def setUp(self):
        """Method that is run before each test.
         Use this to set up state for the tests"""

        self.rock = moves.Rock()
        self.paper = moves.Paper()
        self.scissors = moves.Scissors()

    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        assert not 1 + 1 == 3


    def test_equal(self):
        """Make sure x and y are equal"""
        self.assertEqual(self.rock, moves.Rock())

    def test_not_equal(self):
        """Make sure x and y are not equal"""
        self.assertNotEqual(self.rock,self.paper)

    def test_rock_better_than_sciccors(self):
        """Make sure x is greater than y"""
        self.assertGreater(self.rock,self.scissors)

    def test_paper_worse_than_sciccors(self):
        """Make sure x is less than y"""
        self.assertLess(self.paper,self.scissors)





#With this you can run it as an script
if __name__ == '__main__':
    unittest.main()