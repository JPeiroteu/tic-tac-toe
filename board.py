def create_board(spots):    
    board = (f"|{spots[7]}|{spots[8]}|{spots[9]}|\n"
    f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
    f"|{spots[1]}|{spots[2]}|{spots[3]}|\n")
    print(board)

def check_game(spots):
    # horizontal check
    if ((spots[7] == spots[8] == spots[8]) and (spots[7] != " ")) \
    or ((spots[4] == spots[5] == spots[6]) and (spots[4] != " ")) \
    or (spots[1] == spots[2] == spots[3]and (spots[1] != " ")):
        return True

    # vertical check
    if ((spots[7] == spots[4] == spots[1]) and (spots[7] != " ")) \
    or ((spots[8] == spots[5] == spots[2]) and (spots[7] != " ")) \
    or (spots[9] == spots[6] == spots[3] and (spots[9] != " ")):
        return True

    # diagonal check
    if ((spots[1] == spots[5] == spots[9]) and (spots[1] != " ")) \
    or ((spots[7] == spots[5] == spots[3]) and (spots[7] != " ")):
        return True

    return False

