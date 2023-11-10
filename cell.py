class Cell:
    def __init__(self, x, y):
        self.marker = " "
        self.x = x
        self.y = y
    
    def is_empty(self):
        return self.marker == " "

    def mark(self, marker):
        self.marker = marker
