from juego.chess import Chess
from juego.board import Board
from juego.rook import Rook
from juego.bishop import Bishop
from juego.knight import Knight
from juego.pawn import Pawn
from juego.exceptions import *
import unittest

class TestChess(unittest.TestCase):

#testeamos que las piezas se muevan bien y que el espacio que queda es un espacio vacio
    def setUp(self):
        self.chess = Chess()

    def test_valid_move(self):
        self.chess.move(6, 0, 4, 0)  
        board = self.chess.__board__  # Acceder al tablero
        self.assertIsNone(board.__positions__[6][0])  
        self.assertIsNotNone(board.__positions__[4][0]) 
    def test_invalid_turn(self):
        self.chess.move(6, 0, 4, 0)  # Mover peón blanco de (6, 0) a (4, 0)
        with self.assertRaises(InvalidTurn):
            self.chess.move(6, 1, 4, 1) 

    def test_destination_invalid_move(self):
        with self.assertRaises(DestinationInvalidMove):
            self.chess.move(6, 0, 8, 0)  
    
    def test_invalid_move(self):
        with self.assertRaises(InvalidMove):
            self.chess.move(6, 0, 5, 1)  
    

if __name__== "__main__" :
    unittest.main()

