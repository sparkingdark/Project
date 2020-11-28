import random
from move import *
from direction import *
from board import *
'''
Pawn: Moves one step, same as the normal snakes and ladders movement. One step only, irrespective of number of dice roll.
Bishop: Moves steps of the dice diagonally, either left side up or right side up. If the move is not able to cover all the steps, that move is not allowed. eg: if player rolls 5, they have to move full 5 blocks upwards, not 3. If the diagonal ends at 3 towards the right, then they can't use that route. 
King: Can move one step forward only, in any direction.
Queen: Can move in any directions as long as there is space to finish the roll.
Knight: Can move only in L shape of 3 blocks, in any direction. This mean if the player rolls a 3, they can move one 'L'. If they roll < 3 they can't move. If they roll <6 they can move only one 'L'. If they roll 6 they can move 2 'L's.
Rook: Can move horizontal or vertical, as per the number of the dice roll. Will have the same movement as the normal snakes and ladders piece, basically, but can go straight upwards on the board

'''





def randomizer(player):
    all_player={1:'king',2:'queen',3:'rook',4:'knight',5:'pawn',6:'rook'}
    return random.choice(all_player)



# is it optional???
def take_move(player_choice,dice_param=0):
    if player_choice=='pawn':
        return pawn()
    elif player_choice=='king':
        return king()    
    elif player_choice=='queen':
        return queen(dice_param)
    elif player_choice=='knight' and dice_param==3 or dice_param==6:
         return knight()
    elif player_choice=='bishop':
         return bishop(dice_param)
    else:
        return rook(dice_param)     


def dice_randomized():
    return random.choice([1,2,3,4,5,6])

def turn_player():
    return random.choice([1,2])

def fix_direction(board,action):
    if action=='pawn':
        return direct_pawn(board,action)
    elif action=='king':
        return direct_king(board,action)
    elif action=='queen':
        return direct_queen(board.action)
    elif action=='bishop':
        return direct_bishop(board,action)
    elif action=='knight':
        return direct_knight(board,action)
    else:
        return direct_rook(board,action)                    

  
