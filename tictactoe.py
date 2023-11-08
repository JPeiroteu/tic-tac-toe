from board import *

print("TicTacToe Game\n")
print("Rules:\n"
"Select your desire number to play\n"
"|7|8|9|\n|4|5|6|\n|1|2|3|\n")


player1 = input("Player1 choose X or O: ").upper()

if player1 == "X":
    player2 = "O"
else:
    player2 = "X"

current_player = player1

complete = False

playing = True

board = Board()

while playing:
    x = int(input(f"Player {current_player} Coordenate x: "))
    y = int(input(f"Player {current_player} Coordenate y: "))

    if board.play(x, y, current_player):
        if board.game_logic(): 
            playing = False
        
        board.show_board()
            
    else:
        print("Congrats!!!!")
        playing = False

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1