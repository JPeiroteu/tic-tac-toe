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
        while True:
            try:
                x = int(input(f"Player {self.current_player} Coordenate x: "))
                y = int(input(f"Player {self.current_player} Coordenate y: "))

                cell = self.board.get_cell(x, y)

                if cell.marker != " ":
                    print("Choose another cell!")
                elif x <= 2 and x >= 0 and y >= 0 and y <= 2:
                    return x, y
                    '''
                    The tuple is accessed in order and immutable
                    The list is accessed in order and mutable
                    The dict is accessed by key
                    '''
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