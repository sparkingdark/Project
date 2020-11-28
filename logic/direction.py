from move import *
from board import *


'''
Pawn: Moves one step, same as the normal snakes and ladders movement. One step only, irrespective of number of dice roll.
Bishop: Moves steps of the dice diagonally, either left side up or right side up. If the move is not able to cover all the steps, that move is not allowed. eg: if player rolls 5, they have to move full 5 blocks upwards, not 3. If the diagonal ends at 3 towards the right, then they can't use that route. 
King: Can move one step forward only, in any direction.
Queen: Can move in any directions as long as there is space to finish the roll.
Knight: Can move only in L shape of 3 blocks, in any direction. This mean if the player rolls a 3, they can move one 'L'. If they roll < 3 they can't move. If they roll <6 they can move only one 'L'. If they roll 6 they can move 2 'L's.
Rook: Can move horizontal or vertical, as per the number of the dice roll. Will have the same movement as the normal snakes and ladders piece, basically, but can go straight upwards on the board

'''

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

def pawn_direct(current_pos=(0,0)):

    if current_pos[0]>10:
        current_pos[0]=1
        current_pos[1]+=1
        
    move_val = pawn()
    current_pos[0]+=move
    current_pos[1]+=move
    return current_pos         

def rook_direct(current_pos,dice_param):
    i = current_pos[0]
    j = current_pos[1]

    if current_pos[0]>10:
        current_pos[0]=1
        current_pos[1]+=1
        return current_pos
    move_val = rook(dice_param)

    return (i+move_val,j+move_val)



