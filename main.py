from board import *

print("TicTacToe Game\n")
print("Rules:\n"
"Select your desire number to play\n"
"|7|8|9|\n|4|5|6|\n|1|2|3|\n")

spots = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

player1 = input("Player1 choose X or O: ").upper()

if player1 == "X":
    player2 = "O"
else:
    player2 = "X"

current_player = player1

complete = False

playing = True

while playing:
    play = input(f"Player {current_player} choose number (1-9): ")

    if int(play):
        if not spots[int(play)] in {"X", "O"}:
            spots[int(play)] = current_player
            create_board(spots)

    if check_game(spots):
        print(f"Player {current_player} wins! ")
        complete = True
        playing = False

    if " " not in spots.values():
        print("It's a tie!")
        playing = False

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1


    