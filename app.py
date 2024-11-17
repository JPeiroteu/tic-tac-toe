"""
Tic Tac Toe Flask Application

This module provides the routes and handlers for a Tic Tac Toe game using Flask.
"""

from datetime import datetime, timedelta
from flask import Flask, render_template, request
from tictactoe.board import Board
import random

app = Flask(__name__)

class Game:
    """Represents a Tic Tac Toe game with a board and the current player and IPs"""
    def __init__(self):
        self.board = Board()
        self.current_player = "X"
        self.allowed_ips = {}
        self.last_activity = datetime.now()
        self.inactivity_threshold = timedelta(minutes=2)

    def update_activity(self):
        """Update the last activity timestamp for the game"""
        self.last_activity = datetime.now()

    def is_inactive(self):
        """Check if the game has been inactive beyond the threshold"""
        return datetime.now() - self.last_activity > self.inactivity_threshold

games = {}

def get_game(game_id):
    """Retrieve the game with the specified ID and deleting if inactive"""
    game = games.get(game_id)
    if game and game.is_inactive():
        del games[game_id]
        return None
    return game

def generate_game_id():
    """Generate a unique game ID"""
    while True:
        game_id = random.randint(100, 999)
        if game_id not in games:
            return game_id

def get_client_ip():
    """Get the client's IP address"""
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.remote_addr
    return request.environ['HTTP_X_FORWARDED_FOR']

def is_ip_allowed(game, ip):
    """Check if an IP is allowed in the game, and add if within limit"""
    if ip not in game.allowed_ips:
        if len(game.allowed_ips) >= 2:
            return False
        game.allowed_ips[ip] = True
    return True

@app.after_request
def add_security_headers(response):
    """Add security headers to the App"""
    # Content Security Policy (CSP)
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "
        "img-src 'self' data:; "
        "font-src 'self';"
        "object-src 'none'; "
        "frame-ancestors 'none';"
        "base-uri 'self';"
        "form-action 'self';"
    )

    # Prevent Clickjacking
    response.headers["X-Frame-Options"] = "DENY"

    # Prevent content type sniffing
    response.headers["X-Content-Type-Options"] = "nosniff"

    # Basic XSS protection for older browsers
    response.headers["X-XSS-Protection"] = "1; mode=block"

    return response

@app.route("/")
def welcome():
    """Render the welcome page"""
    return render_template("index.html")

@app.route("/new_game", defaults={'game_id': None}, methods=["POST"])
@app.route("/new_game/<int:game_id>", methods=["POST"]) # Uses provided game ID from physical board
def new_game(game_id):
    """Creates new game with random ID or uses the provided ID for physical board (when online)"""
    if game_id is None:
        game_id = generate_game_id()

    if game_id in games:
        return {"error": "Game ID already exists."}, 400

    games[game_id] = Game()
    return {"game_id": game_id}

@app.route("/game/physical_board", methods=["GET"])
def get_physical_board():
    """Assign a game ID to the physical board and return the board state."""
    game_id = 99  
    game = get_game(game_id)
    if not game:
        return {"error": "Inactive game."}, 410

    client_ip = get_client_ip()
    if not is_ip_allowed(game, client_ip):
        return {"error": "Game full. Only 2 players allowed."}, 403

    return {"game_id": game_id, "grid": game.board.to_dict()}

@app.route("/game/<int:game_id>/board")
def get_board(game_id):
    """Get the current state of the board or deleting game if inactive"""
    game = get_game(game_id)
    if not game:
        return {"error": "Inactive game."}, 410

    client_ip = get_client_ip()
    if not is_ip_allowed(game, client_ip):
        return {"error": "Game full. Only 2 players allowed."}, 403

    return {"grid": game.board.to_dict()}

@app.route("/game/<int:game_id>/player/current", methods=['GET', 'POST'])
def current_player(game_id):
    """Get or set the current player"""
    game = get_game(game_id)
    if not game:
        return {"error": "Game deleted due to inactivity"}, 410

    client_ip = get_client_ip()
    if not is_ip_allowed(game, client_ip):
        return {"error": "Game full. Only 2 players allowed."}, 403

    if request.method == 'POST':
        game.current_player = request.form["currentPlayer"]
        game.update_activity()
        return {"success": True}
    return {"currentPlayer": game.current_player}

@app.route("/game/<int:game_id>/cell/mark", methods=["POST"])
def post_cell_mark(game_id):
    """Mark a cell on the board"""
    game = get_game(game_id)
    if not game:
        return {"error": "Game deleted due to inactivity"}, 410

    client_ip = get_client_ip()
    if not is_ip_allowed(game, client_ip):
        return {"error": "Game full. Only 2 players allowed."}, 403

    game.update_activity()

    try:
        x_coord = int(request.form["x_coord"])
        y_coord = int(request.form["y_coord"])
        mark = request.form["mark"]
        if not (0 <= x_coord <= 2 and 0 <= y_coord <= 2):
            raise ValueError("Invalid input. Please enter a valid number (0-2).")

        cell = game.board.get_cell(x_coord, y_coord)
        if cell.marker != " ":
            return {"error": "Choose another cell!"}

        cell.mark(mark)
        game.current_player = "O" if game.current_player == "X" else "X"
        return cell.to_dict()

    except ValueError:
        return {"error": "Invalid input. Please enter a number."}
    except Exception as error:
        return {"error": str(error)}

@app.route("/game/<int:game_id>/check_winner", methods=["GET"])
def check_winner(game_id):
    """Check if there is a winner on the board"""
    game = get_game(game_id)
    if not game:
        return {"error": "Game deleted due to inactivity"}, 410

    client_ip = get_client_ip()
    if not is_ip_allowed(game, client_ip):
        return {"error": "Game full. Only 2 players allowed."}, 403

    win_cell, win_cell2, win_cell3 = game.board.check_winner()
    if win_cell:
        return {"win_cell": win_cell, "win_cell2": win_cell2, "win_cell3": win_cell3}
    if game.board.is_board_full():
        return {"winner": "Tie"}
    return {"winner": None}

@app.route("/game/<int:game_id>/reset_board", methods=["POST"])
def reset_board(game_id):
    """Reset the board for the specified game"""
    game = get_game(game_id)
    if not game:
        return {"error": "Game deleted due to inactivity"}, 410

    client_ip = get_client_ip()
    if not is_ip_allowed(game, client_ip):
        return {"error": "Game full. Only 2 players allowed."}, 403

    game.update_activity()
    game.board.reset()

    return {"success": True}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)  # mac port 8000, server 5000
