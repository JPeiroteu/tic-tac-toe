from cell import Cell

class Board:
    def __init__(self):
        self.grid = []
        self.create_board()

    def create_board(self):

        '''
        00 10 20 
        01 11 21
        02 12 22
        '''

        for x in range(3):
            for y in range(3):
                self.grid.append(Cell(x, y))
    
    def show_board(self):
        for y in range(3):
            print("|" + self.get_cell(0, y).marker + "|" + self.get_cell(1, y).marker + "|" + self.get_cell(2, y).marker + "|")
            
    def get_cell(self, x, y):
        for cell in self.grid:
            if cell.x == x and cell.y == y:
                return cell
        return None

    def get_mark(self, x, y):
        return self.get_cell(x, y).marker

    def play(self, x, y, marker):
        cell = self.get_cell(x, y)
        
        if cell is None: 
            print("Invalid coordinates!") 
        elif cell.marker != " ":
            print("Choose another cell!")
        elif marker == "X" or marker == "O":
            cell.mark(marker)
            return True
        else: 
            print("Invalid marker!")

        return False

    def check_winner(self):
        # vertical check
        for x in range(3):
            if self.get_mark(x, 0) == self.get_mark(x, 1) == self.get_mark(x, 2) != " ":
                print("Player " + self.get_mark(x, 0) + " is the winner!")
                return True

        # horizontal check
        for y in range(3):
            if self.get_mark(0, y) == self.get_mark(1, y) == self.get_mark(2, y) != " ":
                print("Player " + self.get_cell(0, y).marker + " is the winner!")
                return True

        # diagonal check
        if self.get_mark(0, 0) == self.get_mark(1, 1) == self.get_mark(2, 2) != " ":
            print("Player " + self.get_cell(0, 0).marker + " is the winner!")
            return True
        if self.get_mark(2, 0) == self.get_mark(1, 1) == self.get_mark(0, 2) != " ":
            print("Player " + self.get_cell(2, 0).marker + " is the winner!")
            return True

        return False

