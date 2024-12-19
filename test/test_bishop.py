from juego.bishop import Bishop
import unittest
from juego.board import Board


class TestBishop(unittest.TestCase):

    def test_diagonal_dec_rigt(self):
        board=Board(for_test=True)
        bishop= Bishop("White",board)
        possibles=bishop.possible_positions_diagonal(0,3,1,1)
        self.assertEqual(possibles, [(1,4),(2,5),(3,6),(4,7)])
    
    def test_diagonal_dec_left(self):
        board=Board(for_test=True)
        bishop= Bishop("White",board)
        possibles=bishop.possible_positions_diagonal(0,5,1,-1)
        self.assertEqual(possibles, [(1,4),(2,3),(3,2),(4,1),(5,0)])
    
    def test_diagonal_up_left(self):
        board=Board(for_test=True)
        bishop= Bishop("White",board)
        possibles=bishop.possible_positions_diagonal(7,7,-1,-1)
        self.assertEqual(possibles, [(6,6),(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)])
    
    def test_diagonal_up_right(self):
        board=Board(for_test=True)
        bishop= Bishop("White",board)
        possibles=bishop.possible_positions_diagonal(7,0,-1,1)
        self.assertEqual(possibles, [(6,1),(5,2),(4,3),(3,4),(2,5),(1,6),(0,7)])

    def test_diagonal_dec_rigt_2(self):
        board=Board(for_test=True)
        bishop= Bishop("White",board)
        possibles=bishop.possible_positions_diagonal(3,0,1,1)
        self.assertEqual(possibles, [(4,1),(5,2),(6,3),(7,4)])

if __name__ == '__main__':
    unittest.main()