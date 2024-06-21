class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.marker = " "
        # Tests if can initialize object with x and y.
        # Test if can initialize object with invalid x and y or marker. x3
    
    def is_empty(self):
        return self.marker == " "
        # Test if maker set returns False
        # Test if marker not set return True.
        # Test what happens if marker is invalid.

    def mark(self, marker):
        # Test if set marker works normally.
        # Test if set invalid marker throws exception.
        # Test if set marker to nothing throws exception.
        if (marker.upper() != "X" and marker.upper() != "O"):
            raise Exception("Invalid marker!")
        elif self.marker != " ":
            raise Exception("Choose another cell!")
    
        self.marker = marker.upper()

    def to_dict(self):
        # Test if initialized marker returns the correct dict.
        return {
            "x": self.x,
            "y": self.y,
            "marker": self.marker
        }
