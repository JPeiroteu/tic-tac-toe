from cell import Cell

class Board:
    def __init__(self):
        self.grid = []
        self.create_board()

    def create_board(self):
        for x in range(3):
            for y in range(3):
                self.grid.append(Cell(x, y)) 
                #porque nao faco cell(x, y)? => cell = Cell(x, y)
                # nao preciso fazer return?
    
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
        
        if marker == "X" or marker == "O":
            cell.mark(marker)
            return True
        else: 
            print("Invalid marker!")

        return False

    def check_winner(self):
        # vertical check
        for x in range(3):
            if self.get_mark(x, 0) == self.get_mark(x, 1) == self.get_mark(x, 2) != " ":
                print("\nPlayer " + self.get_mark(x, 0) + " is the winner!")
                return self.get_mark(x, 0)

        # horizontal check
        for y in range(3):
            if self.get_mark(0, y) == self.get_mark(1, y) == self.get_mark(2, y) != " ":
                print("\nPlayer " + self.get_cell(0, y).marker + " is the winner!")
                return self.get_mark(0, y)

        # diagonal check
        if self.get_mark(0, 0) == self.get_mark(1, 1) == self.get_mark(2, 2) != " ":
            print("\nPlayer " + self.get_cell(0, 0).marker + " is the winner!")
            return self.get_mark(0, 0)

        if self.get_mark(2, 0) == self.get_mark(1, 1) == self.get_mark(0, 2) != " ":
            print("\nPlayer " + self.get_cell(2, 0).marker + " is the winner!")
            return self.get_mark(2, 0)

        return False

    def is_board_full(self):
        for cell in self.grid:
            if cell.marker == " ":
                return False

        print("Draw")
        return True

    def to_dict(self):
        d = []

        for cell in self.grid:
            d.append(cell.to_dict())

        return d