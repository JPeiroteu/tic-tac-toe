"""
Tests for Tic Tac Toe Flask Application.

This module contains the tests for the routes and handlers
of the Tic Tac Toe game using Flask.
"""

import unittest
from app import app, games

class TestApp(unittest.TestCase):
    """Test suite for Tic Tac Toe Flask Application"""

    def setUp(self):
        """Set up the test client"""
        self.app = app.test_client()
        self.app.testing = True

        global games
        games = []

    def test_check_x_o_mark_on_board(self):
        """Test marking X and O on the board"""
        response = self.app.post('/new_game')
        game_id = response.json['game_id']

        response = self.app.post(f'/game/{game_id}/cell/mark', data={'x': 0, 'y': 0, 'mark': 'X'})
        self.assertEqual(response.json, {'marker': 'X', 'x': 0, 'y': 0})

        response = self.app.post(f'/game/{game_id}/cell/mark', data={'x': 0, 'y': 1, 'mark': 'O'})
        self.assertEqual(response.json, {'marker': 'O', 'x': 0, 'y': 1})

    def test_check_overlapping_marks(self):
        """Test marking an already marked cell"""
        response = self.app.post('/new_game')
        game_id = response.json['game_id']

        self.app.post(f'/game/{game_id}/cell/mark', data={'x': 1, 'y': 1, 'mark': 'X'})
        
        response = self.app.post(f'/game/{game_id}/cell/mark', data={'x': 1, 'y': 1, 'mark': 'O'})
        self.assertEqual(response.json['error'], 'Choose another cell!')

    def test_current_player(self):
        """Test getting the current player"""
        response = self.app.post('/new_game')
        game_id = response.json['game_id']

        response = self.app.get(f'/game/{game_id}/player/current')
        self.assertEqual(response.json, {'currentPlayer': 'X'})

    def test_check_winner(self):
        """Test checking for a winner"""
        response = self.app.post('/new_game')
        game_id = response.json['game_id']

        self.app.post(f'/game/{game_id}/cell/mark', data={'x': 2, 'y': 0, 'mark': 'X'})
        self.app.post(f'/game/{game_id}/cell/mark', data={'x': 2, 'y': 1, 'mark': 'X'})
        self.app.post(f'/game/{game_id}/cell/mark', data={'x': 2, 'y': 2, 'mark': 'X'})

        response = self.app.get(f'/game/{game_id}/check_winner')
        self.assertEqual(response.json, {
            "win_cell": {"marker": "X", "x": 2, "y": 0},
            "win_cell2": {"marker": "X", "x": 2, "y": 1},
            "win_cell3": {"marker": "X", "x": 2, "y": 2}
        })
