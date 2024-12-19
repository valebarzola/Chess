import unittest
from juego.rook import Rook
from juego.board import Board
from juego.pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str1(self):
        board = Board()
        rook = Rook("White", board)
        self.assertEqual(
            str(rook),
            "♜",
        )
    def test_str2(self):
        board=Board()
        rook=Rook("Black",board)
        self.assertEqual(str(rook),"♖")

    def test_move_vertical_desc(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        possibles = rook.possible_positions_vertical(4, 1, 1, 8,1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1), (7, 1)]
        )

    def test_move_vertical_asc(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        possibles = rook.possible_positions_vertical(4, 1, -1, -1, -1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        board = Board(for_test=True)
        board.set_piece(6, 1, Pawn("White", board))
        rook = Rook("White", board)
        board.set_piece(2, 1, rook)
        possibles = rook.possible_positions_vertical(2, 1, 1, 8,1)
        self.assertEqual(
            possibles,
            [(3,1),(4,1),(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board(for_test=True)
        board.set_piece(6, 1, Pawn("Black", board))
        rook = Rook("White", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vertical(4, 1, 1, 8,1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )
    
    def test_move_vertical_asc_with_own_piece(self):
        board=Board(for_test=True)
        board.set_piece(2,4,Pawn("White",board))
        rook=Rook("White",board)
        board.set_piece(5,4,rook)
        possibles=rook.possible_positions_vertical(5,4,-1,-1,-1)
        self.assertEqual(possibles,[(4,4),(3,4)])
    
    def test_move_vertical_asc_with_not_own_piece(self):
        board=Board(for_test=True)
        board.set_piece(2,4,Pawn("Black",board))
        rook=Rook("White",board)
        board.set_piece(6,4,rook)
        possibles=rook.possible_positions_vertical(6,4,-1,-1,-1)
        self.assertEqual(possibles,[(5,4),(4,4),(3,4),(2,4)])

    def test_move_horizontal_right(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        possibles = rook.possible_positions_horizontal(4, 1, 1, 8, 1)
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]
        )
    def test_move_horizontal_left(self):
        board=Board(for_test=True)
        rook=Rook("White",board)
        possibles= rook.possible_positions_horizontal(4,7,-1,-1,-1)
        self.assertEqual(possibles,[(4,6),(4,5),(4,4),(4,3),(4,2),(4,1),(4,0)])

    def test_move_horizontal_right_with_own_piece(self):
        board = Board(for_test=True)
        board.set_piece(4, 5, Pawn("White", board))
        rook = Rook("White", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_horizontal(4, 1, 1, 8, 1)
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3), (4, 4)]
        )
    def test_move_horizontal_right_with_not_own_piece(self):
        board = Board(for_test=True)
        board.set_piece(4, 5, Pawn("Black", board))
        rook = Rook("White", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_horizontal(4, 1, 1, 8, 1)
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3), (4, 4), (4, 5)]
        )
    def test_move_horizontal_left_with_own_piece(self):
        board=Board(for_test=True)
        board.set_piece(4,3,Pawn("White",board))
        rook=Rook("White",board)
        board.set_piece(4,7,rook)
        possibles=rook.possible_positions_horizontal(4,7,-1,-1,-1)
        self.assertEqual(possibles,[(4,6),(4,5),(4,4)])

    def test_move_horizontal_left_with_not_own_piece(self):
        board=Board(for_test=True)
        board.set_piece(4,3,Pawn("Black",board))
        rook=Rook("White",board)
        board.set_piece(4,7,rook)
        possibles=rook.possible_positions_horizontal(4,7,-1,-1,-1)
        self.assertEqual(possibles,[(4,6),(4,5),(4,4),(4,3)])

    def test_move_diagonal_desc(self):
        board = Board(for_test=True)
        rook=Rook("White",board)
        is_possible=rook.valid_positions_rook(from_row=0,from_col=0,to_row=1,to_col=1)
        rook = board.get_piece(col=0, row=0)

        self.assertFalse(is_possible)
    
    def test_complete(self):
        board=Board()
        rook=Rook("White",board)
        board.set_piece(2,1,rook)
        possible=rook.valid_positions_rook(2,1,4,1)
        self.assertEqual(possible,True)

if __name__ == '__main__':
    unittest.main()