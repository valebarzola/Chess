import unittest
from juego.pawn import Pawn
from juego.board import Board
from juego.rook import Rook

class TestRook(unittest.TestCase):

    
    def test_str1(self):
        board=Board()
        pawn=Pawn("Black",board)
        self.assertEqual(str(pawn),"♙")
    
    def test_str2(self):
        board=Board()
        pawn=Pawn("White",board)
        self.assertEqual(str(pawn),"♟")

    def test_first_move_vertical_down(self):
        board=Board(for_test=True)
        pawn=Pawn("Black",board)
        possibles=pawn.first_move_vertical_down(1,1)
        self.assertEqual(possibles,[(2,1),(3,1)])
    
    def test_first_move_vertical_up(self):
        board=Board(for_test=True)
        pawn=Pawn("White",board)
        possibles=pawn.first_move_vertical_up(6,6)
        self.assertEqual(possibles,[(5,6),(4,6)])
    
    def test_possible_positions_vertical_down_no_piece(self):
        board=Board(for_test=True)
        pawn=Pawn("Black",board)
        possibles=pawn.possible_positions_vertical_down(4,1)
        self.assertEqual(possibles,[(5,1)])
    
    def test_possible_positions_vertical_up_no_piece(self):
        board=Board(for_test=True)
        pawn=Pawn("White",board)
        possibles=pawn.possible_positions_vertical_up(4,1)
        self.assertEqual(possibles,[(3,1)])
    
    def test_possible_positions_vertical_down_with_piece(self):
        board=Board(for_test=True)
        pawn=Pawn("Black",board)
        rook=Rook("Black",board)
        board.set_piece(2,1,rook)
        board.set_piece(1,1,pawn)
        possibles=pawn.possible_positions_vertical_down(1,1)
        self.assertEqual(possibles,[])
    
    def test_possible_positions_vertical_up_with_piece(self):
        board=Board(for_test=True)
        pawn=Pawn("White",board)
        rook=Rook("White",board)
        board.set_piece(5,1,rook)
        board.set_piece(6,1,pawn)
        possibles=pawn.possible_positions_vertical_up(6,1)
        self.assertEqual(possibles,[])
    
    def test_possible_capture_positions_down_right(self):
        board=Board(for_test=True)
        pawn=Pawn("Black",board)
        rook=Rook("White",board)
        board.set_piece(4,4,rook)
        possibles=pawn.possible_capture_positions_down_right(3,3)
        self.assertEqual(possibles,[(4,4)])
    
    def test_possible_capture_positions_down_left(self):
        board=Board(for_test=True)
        pawn=Pawn("Black",board)
        rook=Rook("White",board)
        board.set_piece(4,4,rook)
        possibles=pawn.possible_capture_positions_down_left(3,5)
        self.assertEqual(possibles,[(4,4)])
    
    def test_valid_positions_pawn(self):
        board=Board(for_test=True)
        pawn=Pawn("White",board)
        possibles=pawn.valid_positions_pawn(6,6,5,6)
        self.assertEqual(possibles,True)

    
  
if __name__ == "__main__":
    unittest.main()
