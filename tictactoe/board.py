"""
Module represents a Tic-Tac-Toe game board

Manages the grid of cells and game mechanics,
such as placing markers, checking for a winner, and resetting the board.
"""
    
from .cell import Cell

class Board:
    """Class representings the Tic-Tac-Toe game board"""
    def __init__(self):
        """Initialize the board and create the grid."""
        self.grid = []
        self.create_board()

    def create_board(self):
        """Create a 3x3 board by initializing Cell objects for each position."""
        for x in range(3):
            for y in range(3):
                self.grid.append(Cell(x, y))

    def show_board(self):
        """Display the current state of the board in the console."""
        for y in range(3):
            print("|" + self.get_cell(0, y).marker + "|" +
                  self.get_cell(1, y).marker + "|" +
                  self.get_cell(2, y).marker + "|")

    def get_cell(self, x, y):
        """Return the cell at the specified coordinates."""
        for cell in self.grid:
            if cell.x == x and cell.y == y:
                return cell
        return None

    def get_mark(self, x, y):
        """Return the marker of the cell at the specified coordinates."""
        return self.get_cell(x, y).marker

    def play(self, x, y, marker):
        """Place a marker on the board if it's a valid move."""
        cell = self.get_cell(x, y)

        if marker == "X" or marker == "O":
            cell.mark(marker)
            return True
        else:
            print("Invalid marker!")
            return False

    def check_winner(self):
        """Check for a winning combination on the board."""
        # Vertical check
        for x in range(3):
            if (self.get_mark(x, 0) == self.get_mark(x, 1) ==
                self.get_mark(x, 2) != " "):
                print("\nPlayer " + self.get_mark(x, 0) + " is the winner!")
                return (self.get_cell(x, 0).to_dict(),
                        self.get_cell(x, 1).to_dict(),
                        self.get_cell(x, 2).to_dict())

        # Horizontal check
        for y in range(3):
            if (self.get_mark(0, y) == self.get_mark(1, y) ==
                self.get_mark(2, y) != " "):
                print("\nPlayer " + self.get_mark(0, y) + " is the winner!")
                return (self.get_cell(0, y).to_dict(),
                        self.get_cell(1, y).to_dict(),
                        self.get_cell(2, y).to_dict())

        # Diagonal check
        if (self.get_mark(0, 0) == self.get_mark(1, 1) ==
            self.get_mark(2, 2) != " "):
            print("\nPlayer " + self.get_mark(0, 0) + " is the winner!")
            return (self.get_cell(0, 0).to_dict(),
                    self.get_cell(1, 1).to_dict(),
                    self.get_cell(2, 2).to_dict())

        if (self.get_mark(2, 0) == self.get_mark(1, 1) ==
            self.get_mark(0, 2) != " "):
            print("\nPlayer " + self.get_mark(2, 0) + " is the winner!")
            return (self.get_cell(2, 0).to_dict(),
                    self.get_cell(1, 1).to_dict(),
                    self.get_cell(0, 2).to_dict())

        return (None, None, None)

    def is_board_full(self):
        """Check if the board is full, indicating a draw."""
        for cell in self.grid:
            if cell.marker == " ":
                return False

        print("Draw")
        return True

    def reset(self):
        """Reset the board to its initial state."""
        self.grid = []
        self.create_board()

    def to_dict(self):
        """Return the board as a list of dictionaries representing each cell."""
        return [cell.to_dict() for cell in self.grid]
