from tictactoe.game import Game

print("TicTacToe Game\n")
print("Rules:\n"
"Select your desire coordinate\n"
"xy xy xy\n"
"00 10 20\n"
"01 11 21\n"
"02 12 22\n")
print("| | | |\n| | | |\n| | | |\n")

game = Game()

game.choose_marker()

while not game.completed:
    game.playing()