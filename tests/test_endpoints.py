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

    def test_new_game_with_generated_id(self):
        """Test creating a new game without specifying an ID"""
        response = self.app.post('/new_game')
        game_id = response.json['game_id']
        self.assertIn(game_id, games)

    def test_new_game_with_specific_id(self):
        """Test creating a new game with a specific game ID"""
        response = self.app.post('/new_game/123')
        game_id = response.json['game_id']
        self.assertEqual(game_id, 123)
        self.assertIn(123, games)

    def test_check_x_o_mark_on_board(self):
        """Test marking X and O on the board"""
        response = self.app.post('/new_game')
        game_id = response.json['game_id']

        # Simulate IP Players
        with self.app as client:
            client.environ_base['REMOTE_ADDR'] = '192.168.1.1'
            response = client.post(f'/game/{game_id}/cell/mark', data={'x_coord': 0, 'y_coord': 0, 'mark': 'X'})
            self.assertEqual(response.json, {'marker': 'X', 'x_coord': 0, 'y_coord': 0})

            client.environ_base['REMOTE_ADDR'] = '192.168.1.2'
            response = client.post(f'/game/{game_id}/cell/mark', data={'x_coord': 0, 'y_coord': 1, 'mark': 'O'})
            self.assertEqual(response.json, {'marker': 'O', 'x_coord': 0, 'y_coord': 1})

    def test_ip_restriction(self):
        """Test IP restriction for more than two players"""
        response = self.app.post('/new_game')
        game_id = response.json['game_id']

        # Simulate IP 3 Players
        with self.app as client:
            client.environ_base['REMOTE_ADDR'] = '192.168.1.1'
            self.app.post(f'/game/{game_id}/cell/mark', data={'x_coord': 0, 'y_coord': 0, 'mark': 'X'})

            client.environ_base['REMOTE_ADDR'] = '192.168.1.2'
            self.app.post(f'/game/{game_id}/cell/mark', data={'x_coord': 0, 'y_coord': 1, 'mark': 'O'})

            client.environ_base['REMOTE_ADDR'] = '192.168.1.3'
            response = client.get(f'/game/{game_id}/board')
            self.assertEqual(response.json['error'], 'Game full. Only 2 players allowed.')

    def test_check_overlapping_marks(self):
        """Test marking an already marked cell"""
        response = self.app.post('/new_game')
        game_id = response.json['game_id']

        self.app.post(f'/game/{game_id}/cell/mark', data={'x_coord': 1, 'y_coord': 1, 'mark': 'X'})
        response = self.app.post(f'/game/{game_id}/cell/mark', data={'x_coord': 1, 'y_coord': 1, 'mark': 'O'})
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

        self.app.post(f'/game/{game_id}/cell/mark', data={'x_coord': 2, 'y_coord': 0, 'mark': 'X'})
        self.app.post(f'/game/{game_id}/cell/mark', data={'x_coord': 2, 'y_coord': 1, 'mark': 'X'})
        self.app.post(f'/game/{game_id}/cell/mark', data={'x_coord': 2, 'y_coord': 2, 'mark': 'X'})

        response = self.app.get(f'/game/{game_id}/check_winner')
        self.assertEqual(response.json, {
            "win_cell": {"marker": "X", "x_coord": 2, "y_coord": 0},
            "win_cell2": {"marker": "X", "x_coord": 2, "y_coord": 1},
            "win_cell3": {"marker": "X", "x_coord": 2, "y_coord": 2}
        })
