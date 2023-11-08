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
        print("|" + self.get_cell(0, 0).marker + "|" + self.get_cell(1, 0).marker + "|" + self.get_cell(2, 0).marker + "|")
        print("|" + self.get_cell(0, 1).marker + "|" + self.get_cell(1, 1).marker + "|" + self.get_cell(2, 1).marker + "|")
        print("|" + self.get_cell(0, 2).marker + "|" + self.get_cell(1, 2).marker + "|" + self.get_cell(2, 2).marker + "|")

    def get_cell(self, x, y):
        for cell in self.grid:
            if cell.x == x and cell.y == y:
                return cell
        return None

    def play(self, x, y, marker):
        cell = self.get_cell(x, y)
        
        if cell is None: 
            print("Invalid coordinates!") 
        elif cell.marker != " ":
            print("Choose another cell!")
        elif marker == "X" or marker == "O":
            cell.marker = marker
            return True
        else: 
            print("Invalid marker!")

        return False
            
    def game_logic(self):
        # vertical check
        for x in range(3):
            if self.get_cell(x, 0).marker == self.get_cell(x, 1).marker == self.get_cell(x, 2).marker and self.get_cell(x, 0).marker != " ":
                return True

        # horizontal check
        for y in range(3):
            if self.get_cell(0, y).marker == self.get_cell(1, y).marker == self.get_cell(2, y).marker and self.get_cell(0, y).marker != " ":
                return True

        # diagonal check
        if self.get_cell(0, 0).marker == self.get_cell(1, 1).marker == self.get_cell(2, 2).marker and self.get_cell(0, 0).marker != " ":
            return True
        if self.get_cell(2, 0).marker == self.get_cell(1, 1).marker == self.get_cell(0, 2).marker and self.get_cell(2, 0).marker != " ":
            return True

        return False

