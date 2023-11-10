from game import Game

print("TicTacToe Game\n")
print("Rules:\n"
"Select your desire number to play\n"
"|7|8|9|\n|4|5|6|\n|1|2|3|\n")


player1 = input("Player1 choose X or O: ").upper()

if player1 == "X":
    player2 = "O"
else:
    player2 = "X"

game = Game(player1, player2)

while not game.completed:
    game.playing()