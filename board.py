from cell import Cell

class Board:
    def __init__(self):
        self.grid = []

    def create_board(self):

        '''
        00 10 20 
        01 11 21
        02 12 22
        '''

        for x in range(3):
            for y in range(3):
                self.grid.insert(Cell(x, y))

    def get_cell(self, x, y):
        for cell in self.grid:
            if cell.x == x and cell.y == y:
                return cell

    def game_logic(self):
        # vertical check
        for x in self.grid:
            if self.get_cell(x, 0).marker == self.get_cell(x, 1).marker == self.get_cell(x, 2).marker and self.get_cell(x, 0).marker != " ":
                return True

        # horizontal check
        for y in self.grid:
            if self.get_cell(0, y).marker == self.get_cell(1, y).marker == self.get_cell(2, y).marker and self.get_cell(0, y).marker != " ":
                return True

        # diagonal check
        if self.get_cell(0, 0).marker == self.get_cell(1, 1).marker == self.get_cell(2, 2).marker and self.get_cell(0, 0).marker != " ":
            return True
        if self.get_cell(2, 0).marker == self.get_cell(1, 1).marker == self.get_cell(0, 2).marker and self.get_cell(2, 0).marker != " ":
            return True

        return False

