"""
Unit tests for the Cell class in the TicTacToe game

This module contains tests for verifying the behavior and correctness of the
Cell class, including its initialization and handling of invalid inputs.
"""

import unittest
from tictactoe.cell import Cell

class TestCell(unittest.TestCase):
    """Tests for the Cell class in the TicTacToe game"""

    def test_initialize_valid(self):
        """Test that the Cell class initializes correctly with valid inputs"""
        cell = Cell(1, 2)
        self.assertEqual(cell.x, 1)
        self.assertEqual(cell.y, 2)
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
