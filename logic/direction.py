from move import *
from board import *


def king_direct(board,action):
    pass


def queen_direct(board,action):
    pass

def bishop_direct(board,action):
    pass

def knight_direct(board,action):
    """
    docstring
    """
    pass

def pawn_direct(board,action,current_pos=0):
    current_pos += pawn() 
    for i in range(10):
        for j in range(10):
            if board[i][j]==current_pos:
                board[i][j]='X'
    return board            

def rook_direct(board,action):

    pass