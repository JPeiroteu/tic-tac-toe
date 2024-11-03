"""
Module represents a cell in Tic-Tac-Toe

Defines the Cell class used for each cell in the Tic-Tac-Toe game board.
"""

class Cell:
    """Represents a single cell in the Tic-Tac-Toe game board."""

    def __init__(self, x, y):
        """Initialize a Cell instance with coordinates (x, y) and an empty marker."""
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("x and y must be integers.")
        self.x = x
        self.y = y
        self.marker = " "
        
    def is_empty(self):
        """Check if the cell is empty."""
        return self.marker == " "

    def mark(self, marker):
        """Set the marker of the cell if it's valid and the cell is empty."""
        if marker.upper() not in ("X", "O"):
            raise Exception("Invalid marker!")
        elif self.marker != " ":
            raise Exception("Choose another cell!")
        self.marker = marker.upper()

    def to_dict(self):
        """Convert the cell's properties to a dictionary format."""
        return {
            "x": self.x,
            "y": self.y,
            "marker": self.marker
        }
