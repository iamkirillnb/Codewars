def done_or_not(board):
    for x in range(9):
        if (
            len(set(board[x])) < 9 or
            len(set(board[a][x] for a in range(9))) < 9 or
            len(set(board[x//3*3+a//3][x//3*3+a%3] for a in range(9))) < 9
        ):
            return "Try again!"
    return "Finished!"