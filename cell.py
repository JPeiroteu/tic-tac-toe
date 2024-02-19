class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.marker = " "
    
    def is_empty(self):
        return self.marker == " "

    def mark(self, marker):
        if (marker.upper() != "X" and marker.upper() != "O"):
            raise Exception("Invalid marker!")
        elif self.marker != " ":
            raise Exception("Choose another cell!")
    
        self.marker = marker.upper()

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "marker": self.marker
        }
