def generate_board():
    board = [[0 for i in range(10)] for i in range(10)]
    k = 1
    for i in range(10):
        for j in range(10):
            board[i][j] = k
            k+=1 
    
    return board

def show_board(board):
    for i in board:
        for j in i:
            print(j,end=' ')
        print()