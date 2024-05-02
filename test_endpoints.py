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

    def test_check_overlapping_marks(self):
        self.app.post('/cell/mark', data={'x': 1, 'y': 1, 'mark': 'X'})
        response = self.app.post('/cell/mark', data={'x': 1, 'y': 1, 'mark': 'O'})
        self.assertEqual(response.json['error'], 'Choose another cell!')

    def test_current_player(self):
        response = self.app.get('/player/current')
        self.assertEqual(response.json, {'currentPlayer': 'X'})

    def test_check_winner(self):
        self.app.post('/cell/mark', data={'x': 2, 'y': 0, 'mark': 'X'})
        self.app.post('/cell/mark', data={'x': 2, 'y': 1, 'mark': 'X'})
        self.app.post('/cell/mark', data={'x': 2, 'y': 2, 'mark': 'X'})
        response = self.app.get('/check_winner')
        self.assertEqual(response.json, {
            "win_cell": {"marker": "X", "x": 2, "y": 0},
            "win_cell2": {"marker": "X", "x": 2, "y": 1},
            "win_cell3": {"marker": "X", "x": 2, "y": 2}
        })

if __name__ == '__main__':
    unittest.main()
