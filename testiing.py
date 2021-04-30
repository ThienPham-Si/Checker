board = []
for row in range(8):
    board.append([])
    for col in range(4):
        if row % 2 == 0: # even row
            board[row].append(0)
            board[row].append('x')
        else:
            board[row].append('x')
            board[row].append(0)
print(board)


[[0, P, 0, P, 0, P, 0, P], [P, 0, P, 0, P, 0, P, 0], [0, P, 0, P, 0, P, 0, P], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [P, 0, P, 0, P, 0, P, 0], [0, P, 0, P, 0, P, 0, P], [P, 0, P, 0, P, 0, P, 0]]
