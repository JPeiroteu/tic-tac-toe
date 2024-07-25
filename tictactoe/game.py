"""
Game module for the TicTacToe game by terminal

This module contains the Game class, which manages the game flow, including
choosing markers, getting input coordinates, and handling game play.
"""

from .board import Board

class Game:
    """Class representing the TicTacToe game"""

    def __init__(self):
        """Initialize the game with two players and a board"""
        self.player1 = None
        self.player2 = None
        self.current_player = None
        self.completed = False
        self.board = Board()

    def choose_marker(self):
        """Allow player 1 to choose their marker and set player 2's marker accordingly"""
        while True:
            self.player1 = input("Player1 choose X or O: ").upper()

            if self.player1 in ["X", "O"]:
                if self.player1 == "X":
                    self.player2 = "O"
                else:
                    self.player2 = "X"

                self.current_player = self.player1
                break
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
        """Handle the main game playing loop, switching players and checking for winners"""
        coord_x, coord_y = self.input_coordinates()

        if self.board.play(coord_x, coord_y, self.current_player):
            self.board.show_board()
            if self.board.check_winner():
                self.completed = True
            elif self.board.is_board_full():
                self.completed = True

        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
