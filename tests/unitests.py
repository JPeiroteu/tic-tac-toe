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
