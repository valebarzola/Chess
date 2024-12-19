import unittest
from juego.board import Board
from juego.rook import Rook
from juego.pawn import Pawn
from juego.bishop import Bishop
from juego.queen import Queen
from juego.king import King
from juego.knight import Knight

class TestPiece(unittest.TestCase):
    def test_valid_move_rook(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.set_piece(0, 0, rook)
        self.assertTrue(rook.valid_move_2(0, 0, 0, 5))  # Movimiento horizontal válido
        self.assertTrue(rook.valid_move_2(0, 0, 5, 0))  # Movimiento vertical válido
        self.assertFalse(rook.valid_move_2(0, 0, 5, 5))  # Movimiento diagonal inválido

    def test_valid_move_pawn(self):
      board = Board(for_test=True)
      pawn = Pawn("White", board)
      board.set_piece(6, 6, pawn)
      self.assertTrue(pawn.valid_move_1(6, 6, 5, 6))  # Movimiento hacia adelante válido
      self.assertTrue(pawn.valid_move_1(6, 6, 4, 6))  # Movimiento hacia adelante válido (dos casillas en el primer movimiento)
      self.assertFalse(pawn.valid_move_1(6, 6, 5, 5))  # Movimiento diagonal inválido (sin captura)

    def test_valid_move_bishop(self):
        board = Board(for_test=True)
        bishop = Bishop("White", board)
        board.set_piece(2, 0, bishop)
        self.assertTrue(bishop.valid_move_2(2, 0, 4, 2))  # Movimiento diagonal válido
        self.assertFalse(bishop.valid_move_2(2, 0, 2, 2))  # Movimiento horizontal inválido

    def test_valid_move_queen(self):
        board = Board(for_test=True)
        queen = Queen("White", board)
        board.set_piece(3, 3, queen)
        self.assertTrue(queen.valid_move_2(3, 3, 3, 7))  # Movimiento horizontal válido
        self.assertTrue(queen.valid_move_2(3, 3, 7, 3))  # Movimiento vertical válido
        self.assertTrue(queen.valid_move_2(3, 3, 7, 7))  # Movimiento diagonal válido
        self.assertFalse(queen.valid_move_2(3, 3, 5, 6))  # Movimiento inválido

    def test_valid_move_king(self):
        board = Board(for_test=True)
        king = King("White", board)
        board.set_piece(4, 4, king)
        self.assertTrue(king.valid_move_1(4, 4, 4, 5))  # Movimiento horizontal válido
        self.assertTrue(king.valid_move_1(4, 4, 5, 5))  # Movimiento diagonal válido
        self.assertFalse(king.valid_move_1(4, 4, 6, 6))  # Movimiento inválido (demasiado lejos)

    def test_valid_move_horse(self):
        board = Board(for_test=True)
        knight = Knight("Black", board)
        board.set_piece(1, 1, knight)
        self.assertTrue(knight.valid_move_1(1,1,3,2))  # Movimiento en L válido
        self.assertTrue(knight.valid_move_1(1, 1, 3, 0))  # Movimiento en L válido
        self.assertFalse(knight.valid_move_1(1, 1, 3, 3))  # Movimiento inválido


if __name__ == '__main__':
    unittest.main()