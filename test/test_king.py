import unittest
from juego.board import Board
from juego.pawn import Pawn
from juego.king import King


class TestKing(unittest.TestCase):
    
    def test_possible_positions_vertical_down(self):
        board=Board(for_test=True)
        king=King("Black",board)
        possibles=king.possible_positions_one_move(4,1,1,0)
        self.assertEqual(possibles,[(5,1)])

    def test_possible_vertical_up(self):
        board=Board(for_test=True)
        king=King("White",board)
        possibles=king.possible_positions_one_move(4,1,-1,0)
        self.assertEqual(possibles,[(3,1)])

    def test_possible_positions_horizontal_right(self):
        board=Board(for_test=True)
        king=King("Black",board)
        possibles=king.possible_positions_one_move(1,4,0,1)
        self.assertEqual(possibles,[(1,5)])

    def test_possible_positions_horizontal_left(self):
        board=Board(for_test=True)
        king=King("White",board)
        possibles=king.possible_positions_one_move(1,4,0,-1)
        self.assertEqual(possibles,[(1,3)])

  


      