"""
Tic Tac Toe Flask Application

This module provides the routes and handlers for a Tic Tac Toe game using Flask.
"""

from flask import Flask, render_template, request
from tictactoe.board import Board

app = Flask(__name__)

class Game:
    """Represents a Tic Tac Toe game with a board and the current player and IPs"""
    def __init__(self):
        self.board = Board()
        self.current_player = "X"
        self.allowed_ips = set()

games = []

def get_game(game_id):
    """Retrieve the game with the specified ID"""
    if 0 <= game_id < len(games):
        return games[game_id]
    return None

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
        game.allowed_ips.add(ip) 
    return True

@app.route("/")
def welcome():
    """Render the welcome page"""
    return render_template("index.html")

@app.route("/new_game", methods=["POST"])
def new_game():
    """Add new game to the pool and return its ID"""
    games.append(Game())
    return {"game_id": len(games) - 1}

@app.route("/game/<int:game_id>/board")
def get_board(game_id):
    """Get the current state of the board if the player's IP is allowed"""
    game = get_game(game_id)
    if not game:
        return {"error": "Game not found"}, 404

    client_ip = get_client_ip()
    if not is_ip_allowed(game, client_ip):
        return {"error": "Game full. Only 2 players allowed."}, 403

    return {"grid": game.board.to_dict()}

@app.route("/game/<int:game_id>/player/current", methods=['GET', 'POST'])
def current_player(game_id):
    """Get or set the current player if IP is allowed"""
    game = get_game(game_id)
    if not game:
        return {"error": "Game not found"}, 404

    client_ip = get_client_ip()
    if not is_ip_allowed(game, client_ip):
        return {"error": "Game full. Only 2 players allowed."}, 403

    if request.method == 'POST':
        game.current_player = request.form["currentPlayer"]
        return {"success": True}
    return {"currentPlayer": game.current_player}

@app.route("/game/<int:game_id>/cell/mark", methods=["POST"])
def post_cell_mark(game_id):
    """Mark a cell on the board"""
    game = get_game(game_id)
    if not game:
        return {"error": "Game not found"}, 404

    client_ip = get_client_ip()
    if not is_ip_allowed(game, client_ip):
        return {"error": "Game full. Only 2 players allowed."}, 403

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
        return {"error": "Game not found"}, 404

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
        return {"error": "Game not found"}, 404

    client_ip = get_client_ip()
    if not is_ip_allowed(game, client_ip):
        return {"error": "Game full. Only 2 players allowed."}, 403

    game.board.reset()
    return {"success": True}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True) # mac port 8000, server 5000
