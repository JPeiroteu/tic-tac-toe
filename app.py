from flask import Flask, render_template, request
from board import Board

app = Flask(__name__)

board = Board()


@app.route("/")
def welcome():
    return render_template("index.html")

    # return "<p>Welcome to Tic-Tac-Toe!</p>"


@app.route("/cell/<x>/<y>")
def get_cell(x, y):
    return board.get_cell(int(x), int(y)).to_dict()


@app.route("/board")
def get_board():
    return {"grid": board.to_dict()}


@app.route("/cell/mark", methods=["POST"])
def post_cell_mark():
    try:
        x = int(request.form["x"])
        y = int(request.form["y"])
        mark = request.form["mark"]

        cell = board.get_cell(x, y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            cell.mark(mark)
            return cell.to_dict()
        else:
            raise Exception("Invalid input. Please enter a valid number (0-2).")

    except ValueError:
        return {"error": "Invalid input. Please enter a number."}
    except Exception as e:
        return {"error": str(e)}


@app.route("/check_winner", methods=["GET"])
def check_winner():
    winner = board.check_winner()

    if winner:
        return {"winner": winner}
    elif board.is_board_full():
        return {"winner": "Tie"}

    else:
        return {"winner": None}

@app.route("/reset_board", methods=["GET"])
def reset_board():
    board.reset()
    return "Ok"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)