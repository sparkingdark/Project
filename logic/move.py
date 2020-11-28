def pawn():
    return 1

def king():
    return 1

def queen(dice_param):
    return dice_param

def knight(dice_param):
    if dice_param==3 or dice_param==6:
        return dice_param
    else:
        return 1

def bishop(dice_param):
    return dice_param

def rook(dice_param):
    return dice_param

