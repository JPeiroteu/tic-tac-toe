"""
Tic Tac Toe Flask Application

This module provides the routes and handlers for a Tic Tac Toe game using Flask.
"""

from flask import Flask, render_template, request
from tictactoe.board import Board

app = Flask(__name__)

board = Board()
currentPlayer = "X"

@app.route("/")
def welcome():
    """Render the welcome page"""
    return render_template("index.html")

@app.route("/cell/<int:x_coord>/<int:y_coord>")
def get_cell(x_coord, y_coord):
    """Get the state of a specific cell"""
    return board.get_cell(x_coord, y_coord).to_dict()

@app.route("/board")
def get_board():
    """Get the current state of the board"""
    return {"grid": board.to_dict()}

@app.route('/player/current', methods=['GET', 'POST'])
def current_player():
    """Get or set the current player"""
    global currentPlayer
    if request.method == 'POST':
        currentPlayer = request.form['currentPlayer']
        return {"success": True}
    return {"currentPlayer": currentPlayer}

@app.route("/cell/mark", methods=["POST"])
def post_cell_mark():
    """Mark a cell on the board"""
    try:
        x_coord = int(request.form["x"])
        y_coord = int(request.form["y"])
        mark = request.form["mark"]

        if not (0 <= x_coord <= 2 and 0 <= y_coord <= 2):
            raise ValueError("Invalid input. Please enter a valid number (0-2).")

        cell = board.get_cell(x_coord, y_coord)
        cell.mark(mark)
        global current_player
        current_player = "O" if current_player == "X" else "X"
        return cell.to_dict()

    except ValueError:
        return {"error": "Invalid input. Please enter a number."}
    except Exception as error:
        return {"error": str(error)}

@app.route("/check_winner", methods=["GET"])
def check_winner():
    """Check if there is a winner on the board"""
    win_cell, win_cell2, win_cell3 = board.check_winner()

    if win_cell:
        return {"win_cell": win_cell, "win_cell2": win_cell2, "win_cell3": win_cell3}

    if board.is_board_full():
        return {"winner": "Tie"}

    return {"winner": None}

@app.route("/reset_board", methods=["GET"])
def reset_board():
    """Reset the board to its initial state"""
    board.reset()
    return "Ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)  # mac port 8000, server 5000
