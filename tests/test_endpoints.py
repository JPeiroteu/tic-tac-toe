import unittest
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_check_x_o_mark_on_board(self):
        response = self.app.post('/cell/mark', data={'x': 0, 'y': 0, 'mark': 'X'})
        self.assertEqual(response.json, {'marker': 'X', 'x': 0, 'y': 0})
        
        response = self.app.post('/cell/mark', data={'x': 0, 'y': 1, 'mark': 'O'})
        self.assertEqual(response.json, {'marker': 'O', 'x': 0, 'y': 1})