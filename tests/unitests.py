"""
Unit tests for the Cell and Board classes in the TicTacToe game

This module contains tests for verifying the behavior and correctness of the
Cell class and it also contains tests for the Board class.
"""

import unittest
from unittest.mock import patch
from tictactoe.cell import Cell
from tictactoe.board import Board
from tictactoe.game import Game

class TestCell(unittest.TestCase):
    """Tests for the Cell class in the TicTacToe game"""

    def test_initialize_valid(self):
        """Test that the Cell class initializes correctly with valid inputs"""
        cell = Cell(1, 2)
        self.assertEqual(cell.x_coord, 1)
        self.assertEqual(cell.y_coord, 2)
        self.assertEqual(cell.marker, " ")

    def test_initialize_invalid(self):
        """Test that the Cell class raises TypeError with invalid inputs"""
        with self.assertRaises(TypeError):
            Cell("a", 2)
        with self.assertRaises(TypeError):
            Cell(1, "b")
        with self.assertRaises(TypeError):
            Cell(1, 2, 3)

    def test_is_empty_true(self):
        """Test that the is_empty method returns True for an unmarked cell"""
        cell = Cell(1, 2)
        self.assertTrue(cell.is_empty())

    def test_is_empty_false(self):
        """Test that the is_empty method returns False for a marked cell"""
        cell = Cell(1, 2)
        cell.marker = "X"
        self.assertFalse(cell.is_empty())

    def test_mark_valid(self):
        """Test that the mark method correctly sets a valid marker"""
        cell = Cell(1, 2)
        cell.mark("X")
        self.assertEqual(cell.marker, "X")

    def test_mark_invalid_marker(self):
        """Test that the mark method raises an exception for an invalid marker"""
        cell = Cell(1, 2)
        with self.assertRaises(Exception) as context:
            cell.mark("A")
        self.assertTrue("Invalid marker!" in str(context.exception))

    def test_mark_already_marked(self):
        """Test that the mark method raises an exception if the cell is already marked"""
        cell = Cell(1, 2)
        cell.mark("X")
        with self.assertRaises(Exception) as context:
            cell.mark("O")
        self.assertTrue("Choose another cell!" in str(context.exception))

    def test_mark_empty_marker(self):
        """Test that the mark method raises an exception for an empty marker"""
        cell = Cell(1, 2)
        with self.assertRaises(Exception) as context:
            cell.mark("")
        self.assertTrue("Invalid marker!" in str(context.exception))

    def test_to_dict(self):
        """Test that the to_dict method returns the correct dictionary representation of the cell"""
        cell = Cell(1, 2)
        self.assertEqual(cell.to_dict(), {"x_coord": 1, "y_coord": 2, "marker": " "})
        cell.mark("X")
        self.assertEqual(cell.to_dict(), {"x_coord": 1, "y_coord": 2, "marker": "X"})

class TestBoard(unittest.TestCase):
    """Tests for the Board class in the TicTacToe game"""

    def setUp(self):
        """Set up a new board for each test"""
        self.board = Board()

    def test_create_board(self):
        """Test that the board initializes correctly with 9 cells"""
        self.assertEqual(len(self.board.grid), 9)
        for cell in self.board.grid:
            self.assertIsInstance(cell, Cell)
            self.assertEqual(cell.marker, " ")

    def test_get_cell(self):
        """Test that get_cell method returns the correct cell"""
        cell = self.board.get_cell(0, 0)
        self.assertEqual(cell.x_coord, 0)
        self.assertEqual(cell.y_coord, 0)
        self.assertEqual(cell.marker, " ")

    def test_get_cell_invalid(self):
        """Test that get_cell method returns None for invalid coordinates"""
        cell = self.board.get_cell(3, 3)
        self.assertIsNone(cell)

    def test_play_valid(self):
        """Test that the play method correctly marks a cell with a valid marker"""
        result = self.board.play(0, 0, "X")
        self.assertTrue(result)
        self.assertEqual(self.board.get_mark(0, 0), "X")

    def test_play_invalid_marker(self):
        """Test that the play method returns False and does not change the cell for an invalid marker"""
        result = self.board.play(0, 0, "A")
        self.assertFalse(result)
        self.assertEqual(self.board.get_mark(0, 0), " ")

    def test_play_occupied_cell(self):
        """Test that the play method raises an exception when trying to mark an already occupied cell"""
        self.board.play(0, 0, "X")
        with self.assertRaises(Exception) as context:
            self.board.play(0, 0, "O")
        self.assertTrue("Choose another cell!" in str(context.exception))

    def test_check_winner_vertical(self):
        """Test that the check_winner method correctly identifies a vertical win"""
        self.board.play(0, 0, "X")
        self.board.play(0, 1, "X")
        self.board.play(0, 2, "X")
        result = self.board.check_winner()
        self.assertIsNotNone(result)
        self.assertEqual(result[0]['marker'], "X")

    def test_check_winner_horizontal(self):
        """Test that the check_winner method correctly identifies a horizontal win"""
        self.board.play(0, 0, "X")
        self.board.play(1, 0, "X")
        self.board.play(2, 0, "X")
        result = self.board.check_winner()
        self.assertIsNotNone(result)
        self.assertEqual(result[0]['marker'], "X")

    def test_check_winner_diagonal(self):
        """Test that the check_winner method correctly identifies a diagonal win"""
        self.board.play(0, 0, "X")
        self.board.play(1, 1, "X")
        self.board.play(2, 2, "X")
        result = self.board.check_winner()
        self.assertIsNotNone(result)
        self.assertEqual(result[0]['marker'], "X")

    def test_check_no_winner(self):
        """Test that check_winner method returns no winner when there is no complete line"""
        self.board.play(0, 0, "X")
        self.board.play(1, 0, "O")
        self.board.play(2, 0, "X")
        result = self.board.check_winner()
        self.assertEqual(result, (None, None, None))

    def test_is_board_full(self):
        """Test that is_board_full method correctly identifies a fully occupied board"""
        for x_coord in range(3):
            for y_coord in range(3):
                self.board.play(x_coord, y_coord, "X")
        self.assertTrue(self.board.is_board_full())

    def test_reset(self):
        """Test that reset method clears the board and sets all cells to empty"""
        self.board.play(0, 0, "X")
        self.board.reset()
        self.assertEqual(self.board.get_mark(0, 0), " ")

    def test_to_dict(self):
        """Test that to_dict method returns the correct dictionary representation of the board"""
        self.board.play(0, 0, "X")
        result = self.board.to_dict()
        self.assertEqual(result[0]['marker'], "X")

class TestGame(unittest.TestCase):
    """Tests for the Game class in the TicTacToe game"""

    def setUp(self):
        """Set up a new game instance for each test"""
        self.game = Game()

    @patch('builtins.input', side_effect=['X'])
    def test_choose_marker_player1_X(self, mock_input):
        """Test that choosing X as player1's marker sets player1 to X and player2 to O"""
        self.game.choose_marker()
        self.assertEqual(self.game.player1, 'X')
        self.assertEqual(self.game.player2, 'O')
        self.assertEqual(self.game.current_player, 'X')

    @patch('builtins.input', side_effect=['O'])
    def test_choose_marker_player1_O(self, mock_input):
        """Test that choosing O as player1's marker sets player1 to O and player2 to X"""
        self.game.choose_marker()
        self.assertEqual(self.game.player1, 'O')
        self.assertEqual(self.game.player2, 'X')
        self.assertEqual(self.game.current_player, 'O')

    @patch('builtins.input', side_effect=['O'])
    def test_choose_marker_player1_O(self, mock_input):
        """Test that choosing O as player1's marker sets player1 to O and player2 to X"""
        self.game.choose_marker()
        self.assertEqual(self.game.player1, 'O')
        self.assertEqual(self.game.player2, 'X')
        self.assertEqual(self.game.current_player, 'O')

    @patch('builtins.input', side_effect=['A', 'X'])
    def test_choose_marker_invalid_then_valid(self, mock_input):
        """Test that choosing an invalid marker then a valid one sets the markers correctly"""
        self.game.choose_marker()
        self.assertEqual(self.game.player1, 'X')
        self.assertEqual(self.game.player2, 'O')
        self.assertEqual(self.game.current_player, 'X')

    @patch('builtins.input', side_effect=['0', '0'])
    def test_input_coordinates_valid(self, mock_input):
        """Test that input_coordinates correctly parses valid coordinates"""
        x, y = self.game.input_coordinates()
        self.assertEqual((x, y), (0, 0))

    @patch('builtins.input', side_effect=['3', '3', '0', '0'])
    def test_input_coordinates_invalid_then_valid(self, mock_input):
        """Test that input_coordinates handles invalid coordinates and then correctly parses valid ones"""
        x, y = self.game.input_coordinates()
        self.assertEqual((x, y), (0, 0))
    
    @patch('builtins.input', side_effect=['0', '0'])
    def test_playing(self, mock_input):
        """Test the playing mechanism for a valid move in the game"""
        self.game.player1 = 'X'
        self.game.player2 = 'O'
        self.game.current_player = self.game.player1
        self.game.board.play = lambda x, y, marker: True
        self.game.board.show_board = lambda: None
        self.game.board.check_winner = lambda: False
        self.game.board.is_board_full = lambda: False
        