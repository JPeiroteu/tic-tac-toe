from .board import Board

class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.current_player = None
        self.completed = False
        self.board = Board()

    def choose_marker(self):
        while True:
            self.player1 = input("Player1 choose X or O: ").upper()
            
            if self.player1 in ["X", "O"]:
                if self.player1 == "X":
                    self.player2 = "O"
                else:
                    self.player2 = "X"

                self.current_player = self.player1
                break
            else:
                print("Invalid input. Please enter X or O.")

    def input_coordinates(self):
        """Get valid coordinates from the current player"""
        while True:
            try:
                x_coord = int(input(f"Player {self.current_player} Coordinate x: "))
                y_coord = int(input(f"Player {self.current_player} Coordinate y: "))

                cell = self.board.get_cell(x_coord, y_coord)

                if cell is None:
                    print('Invalid input. Please enter a valid number (0-2).')
                elif cell.marker != " ":
                    print("Choose another cell!")
                elif 0 <= x_coord <= 2 and 0 <= y_coord <= 2:
                    return x_coord, y_coord
                else:
                    print('Invalid input. Please enter a valid number (0-2).')

            except ValueError:
                print('Invalid input. Please enter a valid number (0-2).')

    def playing(self):
        coord_x, coord_y = self.input_coordinates()

        if self.board.play(coord_x, coord_y, self.current_player):
            self.board.show_board()
            if self.board.check_winner(): 
                self.completed = True
            elif self.board.is_board_full():
                self.completed = True

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
