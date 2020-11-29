def pawn():
    return 1

def king():
    if:
        current_pos == [i+1][j]
    elif:
        current_pos == [i][j+1]
    elif:
        current_pos == [i+1][j+1]
    elif:
        current_pos == [i-1][j+1]
    else:
        print("Invalid Move")

def queen(dice_param):
    if:
        current_pos == [i+dice_param][j]
    elif:
        current_pos == [i][j+dice_param]
    elif:
        current_pos == [i+dice_param][j+dice_param]
    elif:
        current_pos == [i-dice_param][j+dice_param]
    else:
        print("Invalid Move")

def knight(dice_param):
    if dice_param==3 or dice_param==6:
        return dice_param
    else:
        return 1

def bishop(dice_param):
    if:
        current_pos == [i+dice_param][j+dice_param]
    elif:
        current_pos == [i-dice_param][j+dice_param]
    else:
        print("Invalid Move")

def rook(dice_param):
    return dice_param

