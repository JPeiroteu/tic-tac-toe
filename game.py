from board import Board

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.completed = False
        self.board = Board()

    def playing(self):
        x = int(input(f"Player {self.current_player} Coordenate x: "))
        y = int(input(f"Player {self.current_player} Coordenate y: "))

        if self.board.play(x, y, self.current_player):
            if self.board.check_winner(): 
                self.completed = True
            
            self.board.show_board()

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1