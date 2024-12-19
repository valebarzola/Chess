import unittest
from juego.knight import Knight
from juego.board import Board

class TestHorse(unittest.TestCase):
    def test_possible_positions_down(self):
        board = Board(for_test=True)
        horse = Knight("White", board)
        possibles = horse.possible_positions_one_move(3, 3, 2, 1)
        expect=[(5, 4)]
        self.assertEqual(
            sorted(possibles),sorted(expect)
        )
    def test_possible_positions_up(self):
        board = Board(for_test=True)
        horse = Knight("White", board)
        possibles = horse.possible_positions_one_move(3, 3, -2, -1)
        expect=[(1, 2)]
        self.assertEqual(
            sorted(possibles),sorted(expect)
        )
    def test_possible_positions(self):
        board = Board(for_test=True)
        horse = Knight("White", board)
        possibles = horse.possible_positions_one_move(7, 7, -1, -2)
        expect=[(6, 5)]
        self.assertEqual(
            sorted(possibles),sorted(expect)
        )
    def test_possible_positions_2(self):
        board = Board(for_test=True)
        horse = Knight("White", board)
        possibles = horse.possible_positions_one_move(7, 7, -2, -1)
        expect=[(5, 6)]
        self.assertEqual(
            sorted(possibles),sorted(expect)
        )