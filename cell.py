class Cell:
    def __init__(self, x, y):
        self.marker = " "
        self.x = x
        self.y = y
    
    def is_empty(self):
        return self.marker == " "
