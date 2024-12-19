import unittest
from juego.queen import Queen
from juego.board import Board

class TestQueen(unittest.TestCase):
    def test_possible_positions_horizontal(self):
        board=Board(for_test=True)
        queen=Queen("White",board)
        possible=queen.possible_positions_horizontal(4,4)
        self.assertEqual(possible,[(4,5),(4,6),(4,7),(4,3),(4,2),(4,1),(4,0)])
    
    def test_possible_positions_queen(self):
        board=Board(for_test=True)
        queen=Queen("White",board)
        possible=queen.possible_positions_diagonal(4,4,1,1) + queen.possible_positions_diagonal(4,4,1,-1)
        self.assertEqual(possible,[(5,5),(6,6),(7,7),(5,3),(6,2),(7,1)])
    
    def test_possible_positions_diagonal_up(self):
        board=Board(for_test=True)
        queen=Queen("White",board)
        possible=queen.possible_positions_diagonal(7,4,-1,1) + queen.possible_positions_diagonal(7,4,-1,-1)
        self.assertEqual(possible,[(6,5),(5,6),(4,7),(6,3),(5,2),(4,1),(3,0)])

    def test_possible_positions_straight(self):
        board=Board(for_test=True)
        queen=Queen("White",board)
        possible=queen.possible_positions_vertical(4,4,1,1,8)+queen.possible_positions_vertical(4,4,-1,-1,-1)
        self.assertEqual(possible,[(5,4),(6,4),(7,4),(3,4),(2,4),(1,4),(0,4)])

    def test_possible_positions_horizontal(self):
        board=Board(for_test=True)
        queen=Queen("White",board)
        possible=queen.possible_positions_horizontal(4,4,1,8,1)+queen.possible_positions_horizontal(4,4,-1,-1,-1)
        self.assertEqual(possible,[(4,5),(4,6),(4,7),(4,3),(4,2),(4,1),(4,0)])
    
    # def test_valid_positions_queen(self):
    #     board=Board(for_test=True)
    #     queen=Queen("White",board)
    #     possible=queen.possible_positions_horizontal_total(4,4)+queen.possible_positions_straight_total(4,4)+queen.possible_positions_diagonal_dec(4,4)+queen.possible_positions_diagonal_up(4,4)
    #     expected_positions = [
    #         (5, 5), (6, 6), (7, 7), (3, 3), (2, 2), (1, 1), (0, 0), # Diagonal decreciente
    #         (3, 5), (2, 6), (1, 7), (5, 3), (6, 2), (7, 1), # Diagonal ascendente
    #         (5, 4), (6, 4), (7, 4), (3, 4), (2, 4), (1, 4), (0, 4), # Vertical
    #         (4, 5), (4, 6), (4, 7), (4, 3), (4, 2), (4, 1), (4, 0)  # Horizontal
    #     ]
    #     self.assertEqual(sorted(possible),sorted(expected_positions))

    if __name__ == '__main__':
        unittest.main()